"""The FastAPI application that serves the contract in `api/openapi.yaml`.

Every operation the contract publishes is implemented here against the `Store`
seam. The **reads**: Questions and Labs, one by one and as filtered pages; the
derived Theme, tag, and learning-path catalogues; and search across both kinds
together. The **writes**: create, replace, patch, and delete for Questions and
Labs, each guarded by the Write credential and by optimistic concurrency. No
operation carries `x-implementation: stub` any more, and nothing here answers
`501`.

Single-item reads are conditional. Each answers an `ETag` — the item's
`content_hash` where a file backs it — and a matching `If-None-Match` earns a
`304` with no body. The write surface is built on that same validator: `If-Match`
carries the `content_hash` a read handed over, so "the version I read" and "the
version I am replacing" are the same string, and a successful write answers with
the new one.

**A write is checked in a fixed order, and the order is part of the contract.**
Can this service write at all (`503`), did the client authenticate (`401`), is
the credential right (`403`), does the record exist (`404`), did the client say
which version it is replacing (`428`), is that still the current version
(`412`), and only then: is the content legal (`422`). Each answer is the most
useful thing that can be said at that point, and none of them is reachable by a
request that should have been stopped earlier.

Two invariants are worth stating here because they are easy to lose:

**The contract is the source of truth.** Nothing in this module is generated
from `api/openapi.yaml`, and the file is never generated from these routes.
`tests/api/test_contract.py` compares the two and fails on any divergence.

**The service never invents a corpus.** `create_app()` with no store configured
raises `StoreNotConfigured` naming what to set, rather than quietly serving
fabricated Questions that a client cannot distinguish from the real ones. The
in-memory fake lives in `api/testing.py` and is reachable only from the tests and
from the explicitly named demo entrypoint, `api.demo:app`. A real deployment
points `CONTENT_API_STORE` at `api.content:content_store`, which opens the
SQLite Content store read-only or refuses to start.

**Every answer names its snapshot.** The store records which corpus commit it
was built from and a corpus-wide content digest; `GET /api/v1/meta` publishes
them and `SnapshotHeaderMiddleware` stamps the digest on every response header,
error responses included, so a downstream consumer can tell which immutable
snapshot any answer — or any refusal — came from.
"""

from __future__ import annotations

import hashlib
import importlib
import os
from collections.abc import Mapping, Sequence
from http import HTTPStatus
from typing import Annotated, Any, NoReturn
from urllib.parse import quote

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
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
    License,
    Meta,
    Problem,
    Question,
    QuestionPage,
    QuestionPatch,
    QuestionType,
    QuestionWrite,
    SearchHit,
    SearchPage,
    SortKey,
    TagPage,
    Theme,
    ThemePage,
)
from api import writes
from api.helpers import (
    ETAG_DOCUMENTATION,
    LINKED_LABS_LIMIT,
    NOT_MODIFIED_DOCUMENTATION,
    PROBLEM_MEDIA_TYPE,
    PROBLEM_SCHEMA_REF,
    catalogue,
    conditional,
    etag_for,
    etag_matches,
    item_responses,
    missing,
    only_documented_validation_errors,
    problem_response,
    problem_responses,
)
from api.routes import catalogue as catalogue_routes
from api.routes import labs as lab_routes
from api.routes import questions as question_routes
from api.routes import service as service_routes
from api.routes.resource import ResourceSpec, resource_routes
from api.routes import StoreDep, VocabularyDep, get_store, get_vocabulary
from api import problems
from api.constants import (
    ATTRIBUTION_URL,
    CONTRACT_TAGS,
    CONTRACT_VERSION,
    CORPUS_LICENSE,
    SERVICE_NAME,
    SNAPSHOT_HEADER,
    STORE_ENVIRONMENT_VARIABLE,
)
from api.guards import (
    lab_links,
    question_link,
    require_precondition,
    require_same_identity,
    require_write_access,
    resolvable,
    write_responses,
    written,
)
from api.store import (
    InvalidQuery,
    LabQuery,
    QuestionQuery,
    Record,
    RecordInUse,
    SearchQuery,
    SNAPSHOT_FIELDS,
    Store,
    StoreContractViolation,
    StoreIsReadOnly,
    WritableStore,
    is_page,
    search_hit,
    writable,
)



class StoreNotConfigured(RuntimeError):
    """Raised when the service is asked to start without a Content store."""


class StoreDoesNotConform(StoreNotConfigured):
    """Raised when the configured store answers in a shape the seam forbids.

    It is a `StoreNotConfigured`, because from the operator's side it is the same
    mistake — the service was pointed at something that cannot serve the
    contract — and every caller that already refuses to start on one refuses on
    the other.
    """


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


#: One cheap call per list read whose answer must be a `Page`. `list_questions`
#: is windowed to a single row so the probe costs nothing on a large corpus.
def store_probes(store: Store) -> tuple[tuple[str, Any], ...]:
    return (
        ("list_questions", lambda: store.list_questions(QuestionQuery(limit=1))),
        ("list_themes", store.list_themes),
        ("list_tags", store.list_tags),
        ("list_learning_paths", store.list_learning_paths),
    )


def check_store_conforms(store: Store) -> None:
    """Refuse at startup a store that answers in the wrong shape.

    `isinstance(store, Store)` only checks that the methods exist, so an object
    can satisfy the protocol and still return `contentdb`'s own tuples and bare
    search rows. That is how a build shipped where every search answered `500`
    with `KeyError: 'score'` while the whole test suite was green: the fake
    conformed and the real store, wired in without its adapter, did not.

    A store whose reads *raise* is left alone. Being unreachable is a runtime
    failure the contract already describes as `500`, and refusing to start over
    it would turn a transient outage into an unbootable service. Only an answer
    that arrives in the wrong shape is a wiring mistake, and only that is fatal.
    """
    for name, call in store_probes(store):
        try:
            answer = call()
        except Exception:  # noqa: BLE001 - see the docstring: this is not our failure
            continue
        if not is_page(answer):
            raise StoreDoesNotConform(
                f"{type(store).__module__}.{type(store).__qualname__}.{name}() answered with "
                f"{type(answer).__name__}, but the Store seam promises a Page of plain mappings "
                "(see api/store.py). The Content store in contentdb/ answers its catalogues as "
                "tuples and its search as bare rows on purpose, and api/content.py is the adapter "
                "that reshapes them: set CONTENT_API_STORE=api.content:content_store, or pass "
                "api.content.ContentStore.open(path) to create_app(), rather than the contentdb "
                "store itself."
            )


def snapshot_metadata(store: Store) -> Record:
    """The snapshot identity this service will announce, resolved once.

    Every response this service sends carries the snapshot header, so the
    snapshot's identity is configuration, not a per-request read: a store that
    cannot name its snapshot cannot be served at all, and this refuses at
    startup rather than letting a service answer a client's every question
    except "who are you". This is deliberately stricter than
    `check_store_conforms`, which leaves a store whose reads merely raise
    alone: those failures are runtime `500`s, while a missing identity is a
    wiring mistake that could never self-heal.
    """
    try:
        meta = store.get_meta()
    except Exception as error:  # noqa: BLE001 - any failure is the same refusal
        raise StoreDoesNotConform(
            f"{type(store).__module__}.{type(store).__qualname__}.get_meta() failed ({error}), but the "
            "snapshot identity is stamped on every response this service sends: set "
            "CONTENT_API_STORE=api.content:content_store over a store built by "
            "`python -m contentdb.ingest`, which records source_commit, content_digest, and "
            "build_timestamp."
        ) from error
    if not isinstance(meta, Mapping) or any(
        not isinstance(meta.get(field), str) or not meta.get(field) for field in SNAPSHOT_FIELDS
    ):
        raise StoreDoesNotConform(
            f"{type(store).__module__}.{type(store).__qualname__}.get_meta() answered with "
            f"{meta!r}, but the snapshot identity needs a non-empty string for each of "
            f"{list(SNAPSHOT_FIELDS)}. See api/store.py for what the seam owes."
        )
    return dict(meta)


class SnapshotHeaderMiddleware:
    """Stamp `X-Content-Snapshot` on every HTTP response, errors included.

    A pure ASGI wrapper rather than a route decorator, for two reasons. First,
    no route can opt out or forget: the header is added where the response
    bytes leave the service, not where each handler happens to remember it.
    Second, it is installed **outside** the whole middleware stack — wrapped
    around what `build_middleware_stack()` returns — so even the outermost
    500 renderer, which sits above every user middleware and answers when a
    handler raises past them all, sends its problem document through this
    wrapper and carries the header too.

    The digest is read from `app.state` (resolved once at startup by
    `snapshot_metadata`) rather than from the store per request: a store that
    fails mid-flight still produces responses, and every one of them still
    names the snapshot it came from.
    """

    def __init__(self, app: Any) -> None:
        self.app = app

    async def __call__(self, scope: Any, receive: Any, send: Any) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        digest = scope["app"].state.content_digest

        async def send_with_snapshot(message: Any) -> None:
            if message["type"] == "http.response.start":
                headers = list(message.get("headers") or [])
                headers.append((SNAPSHOT_HEADER.lower().encode("ascii"), digest.encode("ascii")))
                message = {**message, "headers": headers}
            await send(message)

        await self.app(scope, receive, send_with_snapshot)









def create_app(store: Store | None = None, environ: Mapping[str, str] | None = None) -> FastAPI:
    """Build the Content API over `store`, or over the configured Content store.

    Passing a store explicitly is how the tests and the demo entrypoint inject
    one. Passing nothing falls through to `store_from_environment()`, which
    raises rather than fabricating a corpus.

    `environ` is the environment this application reads its configuration from,
    and it is a parameter rather than a global read so that a test can build a
    service with a Write credential without exporting one into the process that
    is running the suite. It defaults to the real environment, which is what a
    deployment gets.

    **The Write credential is resolved once, here.** A service either starts
    able to write or starts read-only, and which one it is does not change under
    it between two requests. Rotating the credential is a restart.
    """
    environ = os.environ if environ is None else environ
    if store is None:
        store = store_from_environment(environ)
    check_store_conforms(store)
    content_meta = snapshot_metadata(store)

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
    app.state.environ = environ
    app.state.write_credential = writes.write_credential(environ)
    #: The snapshot identity, resolved once: the header on every response and
    #: `GET /api/v1/meta` serve this, never a per-request store read.
    app.state.content_meta = content_meta
    app.state.content_digest = str(content_meta["content_digest"])
    #: Loaded on the first write rather than at startup: a read-only deployment
    #: has no use for the Theme and tag vocabularies, and making the service
    #: refuse to start without `TAGS.md` beside it would break every deployment
    #: that ships only the store.
    app.state.vocabulary = None


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
        return only_documented_validation_errors(schema)

    app.openapi = openapi_with_problem_schema  # type: ignore[method-assign]

    problems.install(app)



    # The catalogue reads -- Themes, tags, learning paths, and search -- live in
    # `api/routes/catalogue.py`. They close over nothing, so they moved verbatim;
    # `tests/api/test_contract.py` proves the served schema is unchanged.
    app.include_router(service_routes.router)
    app.include_router(question_routes.router)
    app.include_router(lab_routes.router)
    app.include_router(catalogue_routes.router)

    # The snapshot header goes on outside everything, including the outermost
    # 500 renderer no user middleware sits above: wrapping the built stack
    # puts this around `ServerErrorMiddleware` itself. See the class for why
    # that placement is the whole point.
    stack_factory = app.build_middleware_stack

    def stack_that_stamps_the_snapshot() -> Any:
        return SnapshotHeaderMiddleware(stack_factory())

    app.build_middleware_stack = stack_that_stamps_the_snapshot  # type: ignore[method-assign]

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
