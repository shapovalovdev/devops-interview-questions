"""The FastAPI application that serves the contract in `api/openapi.yaml`.

This slice is the tracer bullet: `GET /api/v1/health` and `GET /api/v1/questions`
are implemented end to end against the `Store` seam, and every other operation
the contract publishes is present as a route that answers `501`. Slices 3 and 4
therefore find a scaffold with the right address, parameters, and request body
already agreed, instead of a blank file.

Two invariants are worth stating here because they are easy to lose:

**The contract is the source of truth.** Nothing in this module is generated
from `api/openapi.yaml`, and the file is never generated from these routes.
`tests/api/test_contract.py` compares the two and fails on any divergence.

**The service never invents a corpus.** `create_app()` with no store configured
raises `StoreNotConfigured` naming what to set, rather than quietly serving
fabricated Questions that a client cannot distinguish from the real ones. The
in-memory fake lives in `api/testing.py` and is reachable only from the tests and
from the explicitly named demo entrypoint, `api.demo:app`.
"""

from __future__ import annotations

import importlib
import os
from collections.abc import Mapping
from http import HTTPStatus
from typing import Annotated, Any, NoReturn

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.models import (
    Difficulty,
    HealthReport,
    ItemKind,
    Lab,
    LabPage,
    LabPatch,
    LabWrite,
    LearningPath,
    LearningPathPage,
    Problem,
    Question,
    QuestionPage,
    QuestionPatch,
    QuestionType,
    QuestionWrite,
    SearchPage,
    SortKey,
    TagPage,
    Theme,
    ThemePage,
)
from api.store import LabQuery, QuestionQuery, SearchQuery, Store

SERVICE_NAME = "content-api"
CONTRACT_VERSION = "v1"
PROBLEM_MEDIA_TYPE = "application/problem+json"
PROBLEM_SCHEMA_REF = "#/components/schemas/Problem"

#: Names the environment variable that points the service at a Content store.
#: Its value is `<module>:<callable>`, a zero-argument callable returning a
#: `Store`. Slice 3 points it at the SQLite Content store in `contentdb/`.
STORE_ENVIRONMENT_VARIABLE = "CONTENT_API_STORE"

CONTRACT_TAGS = [
    {"name": "Service", "description": "Liveness and contract identification."},
    {"name": "Questions", "description": "The interview prompts that make up the corpus."},
    {"name": "Labs", "description": "Hands-on exercises, each preparing a learner for one Question."},
    {"name": "Taxonomy", "description": "Themes and tags, derived from the corpus rather than authored."},
    {"name": "Learning paths", "description": "Deliberate sequences through the corpus."},
    {"name": "Search", "description": "Free-text search across Questions and Labs together."},
]


class StoreNotConfigured(RuntimeError):
    """Raised when the service is asked to start without a Content store."""


def store_from_environment(environ: Mapping[str, str] | None = None) -> Store:
    """Load the configured Content store, or explain exactly what is missing."""
    environ = os.environ if environ is None else environ
    target = environ.get(STORE_ENVIRONMENT_VARIABLE, "").strip()
    if not target:
        raise StoreNotConfigured(
            "No Content store is configured, and the Content API will not invent one: "
            "serving fabricated Questions from a production entrypoint is a correctness "
            f"bug, because no client can tell them from the corpus. Set {STORE_ENVIRONMENT_VARIABLE} "
            "to '<module>:<callable>' naming a zero-argument callable that returns a Store "
            "(slice 3 points it at the SQLite Content store), pass one to create_app(store=...), "
            "or run the demo service 'uvicorn api.demo:app', which says in its name that its "
            "corpus is fake."
        )
    module_name, separator, attribute = target.partition(":")
    if not separator or not module_name or not attribute:
        raise StoreNotConfigured(
            f"{STORE_ENVIRONMENT_VARIABLE} must look like '<module>:<callable>', "
            f"for example 'api.testing:demo_store'; got {target!r}."
        )
    try:
        module = importlib.import_module(module_name)
    except ImportError as error:
        raise StoreNotConfigured(
            f"{STORE_ENVIRONMENT_VARIABLE} names the module {module_name!r}, which cannot be "
            f"imported: {error}."
        ) from error
    factory = getattr(module, attribute, None)
    if factory is None:
        raise StoreNotConfigured(
            f"{STORE_ENVIRONMENT_VARIABLE} names {attribute!r} in {module_name!r}, "
            "which does not define it."
        )
    return factory()


def problem_response(
    status: int,
    detail: str,
    instance: str,
    errors: list[dict[str, str]] | None = None,
) -> JSONResponse:
    """Build an RFC 9457 problem document. It never carries a stack trace."""
    body: dict[str, Any] = {
        # `about:blank` is RFC 9457's own marker for "the status code is the
        # whole story"; a made-up URI would promise documentation that does not
        # exist yet. Slice 4 introduces real type URIs alongside real failures.
        "type": "about:blank",
        "title": HTTPStatus(status).phrase,
        "status": status,
        "detail": detail,
        "instance": instance,
    }
    if errors:
        body["errors"] = errors
    return JSONResponse(status_code=status, media_type=PROBLEM_MEDIA_TYPE, content=body)


def problem_responses(*statuses: int) -> dict[int | str, dict[str, Any]]:
    """Declare, for the generated schema, that these statuses are problem docs."""
    return {
        status: {
            "description": HTTPStatus(status).phrase,
            "content": {PROBLEM_MEDIA_TYPE: {"schema": {"$ref": PROBLEM_SCHEMA_REF}}},
        }
        for status in statuses
    }


def not_implemented(operation_id: str) -> NoReturn:
    """Answer for an operation the contract publishes but this build stubs."""
    raise HTTPException(
        status_code=501,
        detail=(
            f"{operation_id} is part of the published v1 contract but carries "
            "x-implementation: stub in api/openapi.yaml; it is not implemented in this build."
        ),
    )


def get_store(request: Request) -> Store:
    return request.app.state.store


def _validation_errors(exception: RequestValidationError) -> list[dict[str, str]]:
    return [
        {
            "field": ".".join(str(part) for part in error.get("loc", ())),
            "message": str(error.get("msg", "invalid value")),
        }
        for error in exception.errors()
    ]


def create_app(store: Store | None = None) -> FastAPI:
    """Build the Content API over `store`, or over the configured Content store.

    Passing a store explicitly is how the tests and the demo entrypoint inject
    one. Passing nothing falls through to `store_from_environment()`, which
    raises rather than fabricating a corpus.
    """
    if store is None:
        store = store_from_environment()

    app = FastAPI(
        title="Content API",
        version="1.0.0",
        summary="Query and maintain the Question and Lab corpus in the Content store.",
        description=(
            "The Content API serves the Questions and Labs that live as Markdown under "
            "`questions/` and `labs/` and are loaded into the Content store by Ingest. "
            "Markdown in git stays the durable, reviewable record."
        ),
        license_info={"name": "CC BY 4.0", "url": "https://creativecommons.org/licenses/by/4.0/"},
        openapi_tags=CONTRACT_TAGS,
    )
    app.state.store = store

    generated_openapi = app.openapi

    def openapi_with_problem_schema() -> dict[str, Any]:
        """Keep `#/components/schemas/Problem` resolvable in the served schema.

        Problem documents are produced by exception handlers rather than by a
        route's `response_model`, so FastAPI never learns the model and would
        leave every error response pointing at a component it did not emit.
        """
        schema = generated_openapi()
        problem = Problem.model_json_schema(ref_template="#/components/schemas/{model}")
        nested = problem.pop("$defs", {})
        schema.setdefault("components", {}).setdefault("schemas", {}).update(
            {"Problem": problem, **nested}
        )
        return schema

    app.openapi = openapi_with_problem_schema  # type: ignore[method-assign]

    @app.exception_handler(RequestValidationError)
    async def _on_validation_error(request: Request, exception: RequestValidationError) -> JSONResponse:
        return problem_response(
            status=422,
            detail="The request parameters or body do not satisfy the contract.",
            instance=request.url.path,
            errors=_validation_errors(exception),
        )

    @app.exception_handler(StarletteHTTPException)
    async def _on_http_error(request: Request, exception: StarletteHTTPException) -> JSONResponse:
        return problem_response(
            status=exception.status_code,
            detail=str(exception.detail),
            instance=request.url.path,
        )

    @app.exception_handler(Exception)
    async def _on_unhandled_error(request: Request, exception: Exception) -> JSONResponse:
        # The exception itself is deliberately not echoed: a stack trace or an
        # internal message in the body is how a service leaks its innards.
        return problem_response(
            status=500,
            detail="The service failed to handle this request.",
            instance=request.url.path,
        )

    # ---------------------------------------------------------------- Service

    @app.get(
        "/api/v1/health",
        operation_id="getHealth",
        tags=["Service"],
        summary="Report that the service is up and which contract it serves.",
        response_model=HealthReport,
    )
    def get_health() -> HealthReport:
        return HealthReport(status="ok", service=SERVICE_NAME, contract_version=CONTRACT_VERSION)

    # -------------------------------------------------------------- Questions

    @app.get(
        "/api/v1/questions",
        operation_id="listQuestions",
        tags=["Questions"],
        summary="List Questions, filtered, sorted, and paginated.",
        response_model=QuestionPage,
        responses=problem_responses(422, 500),
    )
    def list_questions(
        store: Annotated[Store, Depends(get_store)],
        theme: Annotated[str | None, Query(description="Canonical Theme that owns the Question.")] = None,
        difficulty: Difficulty | None = None,
        type_: Annotated[
            QuestionType | None, Query(alias="type", description="The interview format of the Question.")
        ] = None,
        tag: Annotated[
            str | None, Query(description="A single tag; a Question matches when it carries the tag.")
        ] = None,
        q: Annotated[str | None, Query(description="Free-text filter over title, prompt, and body.")] = None,
        limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
        offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
        sort: SortKey = SortKey.id,
    ) -> QuestionPage:
        page = store.list_questions(
            QuestionQuery(
                theme=theme,
                difficulty=difficulty.value if difficulty else None,
                type=type_.value if type_ else None,
                tag=tag,
                q=q,
                sort=sort.value,
                limit=limit,
                offset=offset,
            )
        )
        # This is the seam: plain mappings go in, typed models come out. If the
        # store hands back something the contract cannot describe, the
        # validation failure surfaces as a 500 rather than as a malformed body.
        return QuestionPage(items=page.items, total=page.total, limit=limit, offset=offset)

    @app.post(
        "/api/v1/questions",
        operation_id="createQuestion",
        tags=["Questions"],
        summary="Create a Question.",
        status_code=201,
        response_model=Question,
        responses=problem_responses(422, 501),
    )
    def create_question(
        question: QuestionWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
    ) -> Question:
        not_implemented("createQuestion")

    @app.get(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="getQuestion",
        tags=["Questions"],
        summary="Read one Question by its id.",
        response_model=Question,
        responses=problem_responses(501),
    )
    def get_question(
        theme: str,
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Question:
        not_implemented("getQuestion")

    @app.put(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="replaceQuestion",
        tags=["Questions"],
        summary="Replace a Question wholesale.",
        response_model=Question,
        responses=problem_responses(422, 501),
    )
    def replace_question(
        theme: str,
        slug: str,
        question: QuestionWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Question:
        not_implemented("replaceQuestion")

    @app.patch(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="patchQuestion",
        tags=["Questions"],
        summary="Change only the supplied fields of a Question.",
        response_model=Question,
        responses=problem_responses(422, 501),
    )
    def patch_question(
        theme: str,
        slug: str,
        question: QuestionPatch,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Question:
        not_implemented("patchQuestion")

    @app.delete(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="deleteQuestion",
        tags=["Questions"],
        summary="Delete a Question.",
        status_code=204,
        responses=problem_responses(501),
    )
    def delete_question(
        theme: str,
        slug: str,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> None:
        not_implemented("deleteQuestion")

    # ------------------------------------------------------------------- Labs

    @app.get(
        "/api/v1/labs",
        operation_id="listLabs",
        tags=["Labs"],
        summary="List Labs, filtered, sorted, and paginated.",
        response_model=LabPage,
        responses=problem_responses(422, 501),
    )
    def list_labs(
        theme: str | None = None,
        difficulty: Difficulty | None = None,
        tag: str | None = None,
        question_ref: Annotated[
            str | None, Query(description="The id of the Question a Lab prepares a learner for.")
        ] = None,
        q: Annotated[str | None, Query(description="Free-text filter over title, prompt, and body.")] = None,
        limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
        offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
        sort: SortKey = SortKey.id,
    ) -> LabPage:
        # The query is built even though the operation is a stub, so that slice 3
        # inherits a route whose parameters already reach the seam intact.
        LabQuery(
            theme=theme,
            difficulty=difficulty.value if difficulty else None,
            tag=tag,
            question_ref=question_ref,
            q=q,
            sort=sort.value,
            limit=limit,
            offset=offset,
        )
        not_implemented("listLabs")

    @app.post(
        "/api/v1/labs",
        operation_id="createLab",
        tags=["Labs"],
        summary="Create a Lab.",
        status_code=201,
        response_model=Lab,
        responses=problem_responses(422, 501),
    )
    def create_lab(
        lab: LabWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
    ) -> Lab:
        not_implemented("createLab")

    @app.get(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="getLab",
        tags=["Labs"],
        summary="Read one Lab by its id.",
        response_model=Lab,
        responses=problem_responses(501),
    )
    def get_lab(
        theme: str,
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Lab:
        not_implemented("getLab")

    @app.put(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="replaceLab",
        tags=["Labs"],
        summary="Replace a Lab wholesale.",
        response_model=Lab,
        responses=problem_responses(422, 501),
    )
    def replace_lab(
        theme: str,
        slug: str,
        lab: LabWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Lab:
        not_implemented("replaceLab")

    @app.patch(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="patchLab",
        tags=["Labs"],
        summary="Change only the supplied fields of a Lab.",
        response_model=Lab,
        responses=problem_responses(422, 501),
    )
    def patch_lab(
        theme: str,
        slug: str,
        lab: LabPatch,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Lab:
        not_implemented("patchLab")

    @app.delete(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="deleteLab",
        tags=["Labs"],
        summary="Delete a Lab.",
        status_code=204,
        responses=problem_responses(501),
    )
    def delete_lab(
        theme: str,
        slug: str,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> None:
        not_implemented("deleteLab")

    # --------------------------------------------------------------- Taxonomy

    @app.get(
        "/api/v1/themes",
        operation_id="listThemes",
        tags=["Taxonomy"],
        summary="List every canonical Theme with its counts.",
        response_model=ThemePage,
        responses=problem_responses(501),
    )
    def list_themes() -> ThemePage:
        not_implemented("listThemes")

    @app.get(
        "/api/v1/themes/{name}",
        operation_id="getTheme",
        tags=["Taxonomy"],
        summary="Read one Theme by its canonical name.",
        response_model=Theme,
        responses=problem_responses(501),
    )
    def get_theme(
        name: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Theme:
        not_implemented("getTheme")

    @app.get(
        "/api/v1/tags",
        operation_id="listTags",
        tags=["Taxonomy"],
        summary="List every tag with its counts.",
        response_model=TagPage,
        responses=problem_responses(501),
    )
    def list_tags() -> TagPage:
        not_implemented("listTags")

    # --------------------------------------------------------- Learning paths

    @app.get(
        "/api/v1/learning-paths",
        operation_id="listLearningPaths",
        tags=["Learning paths"],
        summary="List every learning path.",
        response_model=LearningPathPage,
        responses=problem_responses(501),
    )
    def list_learning_paths() -> LearningPathPage:
        not_implemented("listLearningPaths")

    @app.get(
        "/api/v1/learning-paths/{slug}",
        operation_id="getLearningPath",
        tags=["Learning paths"],
        summary="Read one learning path, with its ordered steps.",
        response_model=LearningPath,
        responses=problem_responses(501),
    )
    def get_learning_path(
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> LearningPath:
        not_implemented("getLearningPath")

    # ----------------------------------------------------------------- Search

    @app.get(
        "/api/v1/search",
        operation_id="search",
        tags=["Search"],
        summary="Search Questions and Labs together, ranked by relevance.",
        response_model=SearchPage,
        responses=problem_responses(422, 501),
    )
    def search(
        q: Annotated[str, Query(min_length=1, description="The search text; it is required.")],
        kind: Annotated[
            ItemKind | None, Query(description="Restrict the result to one kind of item.")
        ] = None,
        limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
        offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
    ) -> SearchPage:
        SearchQuery(q=q, kind=kind.value if kind else None, limit=limit, offset=offset)
        not_implemented("search")

    return app


def __getattr__(name: str) -> Any:
    """Resolve `api.app:app` lazily, so importing this module never starts a service.

    `uvicorn api.app:app` reads this attribute once at startup and gets an
    application bound to the configured Content store — or a `StoreNotConfigured`
    naming what to set. Building it eagerly at import time would make every
    import of this module, including the test suite's, depend on a configured
    store.
    """
    if name == "app":
        return create_app()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
