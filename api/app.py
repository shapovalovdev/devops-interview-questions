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

SERVICE_NAME = "content-api"
CONTRACT_VERSION = "v1"
PROBLEM_MEDIA_TYPE = "application/problem+json"
PROBLEM_SCHEMA_REF = "#/components/schemas/Problem"

#: The response header that names the corpus snapshot every answer came from.
#: It holds the snapshot's `content_digest` and is stamped by app-level
#: middleware on **every** response — success and error alike — so no route
#: can forget it and no client can mistake one snapshot for another.
SNAPSHOT_HEADER = "X-Content-Snapshot"

#: The license the corpus is published under, served at `GET /api/v1/meta`.
CORPUS_LICENSE = License(
    name="CC BY 4.0",
    spdx_id="CC-BY-4.0",
    url="https://creativecommons.org/licenses/by/4.0/",
)

#: Where attribution is owed: the repository the corpus lives in.
ATTRIBUTION_URL = "https://github.com/shapovalovdev/devops-interview-questions"

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


def only_documented_validation_errors(schema: dict[str, Any]) -> dict[str, Any]:
    """Drop the `422` FastAPI adds to every operation that parses a parameter.

    FastAPI documents a validation error on any operation with a parameter or a
    body, including `GET /api/v1/questions/{theme}/{slug}`, whose two path
    segments are strings that cannot fail validation. The contract documents
    `422` only where a client can actually provoke one, and the coverage census
    demands a real request per documented status — so an unprovokable `422` in
    the served schema is a promise no test could ever keep.

    The rule is mechanical: this service answers every error as
    `application/problem+json`, so a `422` that carries only the framework's own
    `application/json` validation model was added by the framework and is
    removed. Where the operation really does declare one, the problem document
    survives and the framework's model is dropped beside it, because two
    incompatible error shapes on one status is worse than either.
    """
    for item in schema.get("paths", {}).values():
        for operation in item.values():
            responses = operation.get("responses", {})
            content = responses.get("422", {}).get("content", {})
            content.pop("application/json", None)
            if "422" in responses and not content:
                del responses["422"]
    return schema


def problem_responses(*statuses: int) -> dict[int | str, dict[str, Any]]:
    """Declare, for the generated schema, that these statuses are problem docs."""
    return {
        status: {
            "description": HTTPStatus(status).phrase,
            "content": {PROBLEM_MEDIA_TYPE: {"schema": {"$ref": PROBLEM_SCHEMA_REF}}},
        }
        for status in statuses
    }


#: Every single-item read documents the same two things beyond its body: the
#: ETag it answers with, and the `304` a matching `If-None-Match` earns.
ETAG_DOCUMENTATION = {
    "headers": {
        "ETag": {
            "description": "The item's `content_hash`, quoted.",
            "schema": {"type": "string"},
        }
    }
}
NOT_MODIFIED_DOCUMENTATION = {
    "description": "The client's ETag still matches; no body is returned."
}

#: How many linked Labs a Question's `Link` header will name. A Question has a
#: handful of Labs at most, and a header is not a place to page.
LINKED_LABS_LIMIT = 50


def item_responses(*statuses: int) -> dict[int | str, dict[str, Any]]:
    """Declare the response set every single-item read shares."""
    return {
        200: dict(ETAG_DOCUMENTATION),
        304: dict(NOT_MODIFIED_DOCUMENTATION),
        **problem_responses(*statuses),
    }


def etag_for(record: Record, payload: BaseModel) -> str:
    """The ETag for one item, quoted as an HTTP entity tag.

    A Question and a Lab are files, and the contract publishes their
    `content_hash` — the sha256 of the source file — as the validator, so a
    client can compare what it holds against what git holds. A Theme, a tag, and
    a learning path have no file behind them: they are derived from the corpus.
    Rather than invent a hash the corpus does not have, their ETag is a digest of
    the representation the client is about to receive, which gives the same
    guarantee a validator has to give — it changes exactly when the body does.
    """
    content_hash = record.get("content_hash")
    if isinstance(content_hash, str) and content_hash:
        return f'"{content_hash}"'
    return f'"sha256:{hashlib.sha256(payload.model_dump_json().encode("utf-8")).hexdigest()}"'


def etag_matches(if_none_match: str | None, etag: str) -> bool:
    """Whether the client's `If-None-Match` already covers this ETag.

    RFC 9110 allows a list, the wildcard `*`, and weak tags; a client that sends
    back the `W/`-prefixed form of the tag it was given still holds the same
    representation, and answering it `200` would waste the round trip the header
    exists to save.
    """
    if not if_none_match:
        return False
    for candidate in if_none_match.split(","):
        candidate = candidate.strip()
        if candidate == "*" or candidate.removeprefix("W/") == etag:
            return True
    return False


def conditional(
    payload: BaseModel,
    record: Record,
    if_none_match: str | None,
    response: Response,
    links: Sequence[str] = (),
) -> Any:
    """Answer a single-item read, as `304` when the client is already current.

    The `304` carries the validator and the links but no body: that is the whole
    point of the exchange, and a body would make the saved bandwidth a lie.
    """
    headers = {"ETag": etag_for(record, payload)}
    if links:
        headers["Link"] = ", ".join(links)
    if etag_matches(if_none_match, headers["ETag"]):
        return Response(status_code=304, headers=headers)
    response.headers.update(headers)
    return payload


def catalogue(envelope: type[BaseModel], page: Any) -> Any:
    """Envelope a bounded catalogue: Themes, tags, and learning paths.

    These three are derived from the corpus and small enough to return whole,
    which the contract records by publishing no `limit` or `offset` parameter
    for them. The envelope is still the one every list shares — `limit` simply
    reports the size of the page returned, so a client parses one shape.
    """
    items = list(page.items)
    return envelope(items=items, total=page.total, limit=len(items), offset=0)


def missing(kind: str, identifier: str) -> NoReturn:
    """Answer for an id the corpus does not hold."""
    raise HTTPException(
        status_code=404,
        detail=f"No {kind} {identifier!r} exists in this Content store.",
    )


def lab_links(store: Store, question_id: str) -> list[str]:
    """The Labs that prepare a learner for this Question, as RFC 8288 links.

    The epic pins a Question's fields and none of them is a list of Labs, so the
    link lives in the header rather than in the body: `question_ref` points one
    way, and this points back, without either resource growing a field the
    contract does not describe. The collection link is always present — it is
    the query a client can re-run — and each Lab that exists today is named
    beside it.
    """
    page = store.list_labs(LabQuery(question_ref=question_id, limit=LINKED_LABS_LIMIT))
    collection = f"/api/v1/labs?question_ref={quote(question_id, safe='')}"
    links = [f'<{collection}>; rel="related"; title="Labs that prepare a learner for this Question"']
    links += [f'</api/v1/labs/{lab["id"]}>; rel="related"' for lab in page.items]
    return links


def question_link(store: Store, question_ref: str) -> list[str]:
    """The Question a Lab prepares a learner for, if the reference resolves.

    A `question_ref` that names nothing is a corpus defect the validators catch;
    the API neither hides it nor fails the read, it simply does not publish a
    link it cannot honour.
    """
    if store.get_question(question_ref) is None:
        return []
    return [f'</api/v1/questions/{question_ref}>; rel="related"; title="The Question this Lab prepares you for"']


def get_store(request: Request) -> Store:
    return request.app.state.store


# ------------------------------------------------------------- Writing

#: Every write documents the same validator it answers with. The status codes
#: differ per method and are listed at each route, because the contract lists
#: them there and the contract test compares the two sets exactly.
WRITTEN_DOCUMENTATION = {
    200: {
        "description": HTTPStatus.OK.phrase,
        "headers": {
            "ETag": {
                "description": "The item's new `content_hash`, quoted.",
                "schema": {"type": "string"},
            }
        },
    }
}


def write_responses(*statuses: int) -> dict[int | str, dict[str, Any]]:
    """The response set `PUT` and `PATCH` share: a new validator, then failures."""
    return {**WRITTEN_DOCUMENTATION, **problem_responses(*statuses)}


def require_write_access(request: Request, presented: str | None, store: Store) -> WritableStore:
    """Answer the three questions that come before any mutation is considered.

    In this order, and the order is the point:

    1. *Is this service allowed to write at all?* With no Write credential
       configured the answer is `503` and nothing else is examined. A deployment
       that forgot to set one is read-only, never open, and never quietly
       accepting a blank key.
    2. *Did the client bring a credential?* No header is `401` — "authenticate",
       not "you are wrong".
    3. *Is it the right one?* A wrong one is `403`, compared in constant time,
       and neither the presented value nor the expected one appears in the
       problem document, in a header, or in a log line. An error body that
       echoed the credential would put it in every client's console.

    A store that cannot write lands on `503` too: that is a fact about the
    deployment, exactly like a missing credential, and not the client's mistake.
    """
    expected = request.app.state.write_credential
    if expected is None:
        raise HTTPException(
            status_code=503,
            detail=(
                "This Content API is serving read-only: no Write credential is configured, so "
                f"every mutating request is refused. Set {writes.WRITE_CREDENTIAL_VARIABLE} in the "
                "service environment to enable writes."
            ),
        )
    if presented is None:
        raise HTTPException(
            status_code=401,
            detail="This request must carry the Write credential in the X-API-Key header.",
        )
    if not writes.credential_matches(expected, presented):
        raise HTTPException(
            status_code=403,
            detail="The X-API-Key header does not carry the Write credential this service accepts.",
        )
    return writable(store)


def precondition_matches(if_match: str, content_hash: str) -> bool:
    """Whether the client's `If-Match` names the version the store actually holds.

    RFC 9110 allows a list, the wildcard, and the weak form of a tag; a client
    that echoes back the `W/`-prefixed validator it was handed is still holding
    the same representation, and refusing it would fail a write for a syntax
    detail rather than for a conflict.
    """
    for candidate in if_match.split(","):
        candidate = candidate.strip()
        if candidate == "*":
            return True
        if candidate.removeprefix("W/").strip('"') == content_hash:
            return True
    return False


def require_precondition(if_match: str | None, record: Record) -> None:
    """Refuse a blind overwrite, and refuse one aimed at a version that has moved.

    A missing `If-Match` is `428`: the client never read the item, so it cannot
    know what it is about to destroy. A stale one is `412`: it read the item,
    somebody else has written since, and the write it is proposing was decided
    against content that no longer exists.
    """
    content_hash = str(record["content_hash"])
    if not if_match or not if_match.strip():
        raise HTTPException(
            status_code=428,
            detail=(
                "This request must carry If-Match with the item's current content_hash — the ETag "
                "a read hands over — so that concurrent writers cannot silently overwrite each other."
            ),
        )
    if not precondition_matches(if_match, content_hash):
        raise HTTPException(
            status_code=412,
            detail=(
                "If-Match names a version this item no longer has: it has been written since you "
                f'read it. Read it again, and retry against the ETag "{content_hash}".'
            ),
        )


def require_same_identity(payload: Mapping[str, Any], theme: str, slug: str, kind: str) -> None:
    """A body that renames the record it is replacing is refused, not obeyed.

    The URL identifies the record; the body repeats `theme` and `slug` because
    the same schema serves `POST`, where they are the only identity there is.
    When the two disagree the client is asking for a move, which is a create and
    a delete wearing one status code, and guessing which it meant is worse than
    saying so.
    """
    if str(payload.get("theme", "")) != theme:
        raise writes.WriteRejected(
            "theme",
            f"the body describes theme {payload.get('theme')!r} but the URL names {theme!r}; "
            f"a {kind} cannot be moved by replacing it.",
        )
    if str(payload.get("slug", "")) != slug:
        raise writes.WriteRejected(
            "slug",
            f"the body describes slug {payload.get('slug')!r} but the URL names {slug!r}; "
            f"a {kind} cannot be renamed by replacing it.",
        )


def resolvable(store: Store, question_ref: str) -> set[str]:
    """The Question ids a Lab's reference is allowed to name, drawn from the store.

    `contentdb.corpus` takes the set of every Question it just read; the API
    cannot afford to enumerate a corpus per request, so it asks the store about
    the one reference in hand. The rule being enforced is identical — the
    reference must resolve — and the answer comes from the same place a read
    would get it.
    """
    return {question_ref} if store.get_question(question_ref) is not None else set()


def written(response: Response, record: Record, model: type[BaseModel]) -> Any:
    """Answer a successful write with the stored record and its new validator."""
    response.headers["ETag"] = f'"{record["content_hash"]}"'
    return model.model_validate(record)


def _validation_errors(exception: RequestValidationError) -> list[dict[str, str]]:
    return [
        {
            "field": ".".join(str(part) for part in error.get("loc", ())),
            "message": str(error.get("msg", "invalid value")),
        }
        for error in exception.errors()
    ]


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

    def vocabulary() -> writes.Vocabulary:
        if app.state.vocabulary is None:
            try:
                app.state.vocabulary = writes.Vocabulary.load(environ=environ)
            except OSError as error:
                raise StoreIsReadOnly(
                    "This Content API cannot validate a write: the Theme and tag vocabularies are "
                    f"read from config/content-manifest.json and TAGS.md, and they are not readable "
                    f"({error}). Point {writes.CORPUS_ROOT_VARIABLE} at the corpus this store was "
                    "built from."
                ) from error
        return app.state.vocabulary

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

    @app.exception_handler(InvalidQuery)
    async def _on_invalid_query(request: Request, exception: InvalidQuery) -> JSONResponse:
        """Free text the store cannot parse is the client's fault, not a fault.

        The store raises this only for a query string it could not read — an
        unbalanced quote, a dangling operator — which the contract documents as
        `422`. Everything else a store raises stays a `500`.
        """
        return problem_response(
            status=422,
            detail="The free-text query could not be parsed; check quoting and operators.",
            instance=request.url.path,
            errors=[{"field": "q", "message": str(exception)}],
        )

    @app.exception_handler(writes.WriteRejected)
    async def _on_write_rejected(request: Request, exception: writes.WriteRejected) -> JSONResponse:
        """A write that breaks a corpus rule is the client's to fix, and it is told which.

        The contract promises a problem document naming the offending field, and
        this is the only place that promise is kept: the message comes from
        `contentdb`, which is what would have refused the same content at Ingest
        time, so a client is told the same thing a reviewer would be.
        """
        return problem_response(
            status=422,
            detail=(
                "The write would produce a record the Markdown corpus rules reject, so it was not "
                "stored."
            ),
            instance=request.url.path,
            errors=[{"field": exception.field, "message": exception.message}],
        )

    @app.exception_handler(RecordInUse)
    async def _on_record_in_use(request: Request, exception: RecordInUse) -> JSONResponse:
        """Deleting something the corpus still points at is a conflict, not a fault."""
        return problem_response(status=409, detail=str(exception), instance=request.url.path)

    @app.exception_handler(StoreIsReadOnly)
    async def _on_read_only_store(request: Request, exception: StoreIsReadOnly) -> JSONResponse:
        """This deployment cannot write, which the contract publishes as `503`."""
        return problem_response(status=503, detail=str(exception), instance=request.url.path)

    @app.exception_handler(StoreContractViolation)
    async def _on_store_contract_violation(
        request: Request, exception: StoreContractViolation
    ) -> JSONResponse:
        """A store that broke the seam is a fault, and it is ours, not the client's.

        The body stays the same `500` every other fault produces — a client can
        do nothing with the detail — but the exception has already said in the
        log which shape arrived and which was promised.
        """
        return problem_response(
            status=500,
            detail="The service failed to handle this request.",
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

    @app.get(
        "/api/v1/meta",
        operation_id="getMeta",
        tags=["Service"],
        summary="Identify the immutable corpus snapshot this service serves.",
        response_model=Meta,
    )
    def get_meta() -> Meta:
        # Serves the identity resolved at startup: the store state Ingest
        # recorded, plus the contract's own version and licensing, which are
        # facts about this service rather than about the store.
        return Meta(
            source_commit=str(app.state.content_meta["source_commit"]),
            content_digest=str(app.state.content_meta["content_digest"]),
            api_version=CONTRACT_VERSION,
            build_timestamp=str(app.state.content_meta["build_timestamp"]),
            license=CORPUS_LICENSE,
            attribution=ATTRIBUTION_URL,
        )

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
        responses={
            201: {
                "description": "The Question was created.",
                "headers": {
                    "ETag": {
                        "description": "The new Question's `content_hash`, quoted.",
                        "schema": {"type": "string"},
                    }
                },
            },
            **problem_responses(401, 403, 409, 422, 503),
        },
    )
    def create_question(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        question: QuestionWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        # Validation before the duplicate check: a body that could never be a
        # legal Question is malformed whatever else is in the store, and telling
        # a client "that id is taken" about content it would have had to fix
        # anyway sends it round the loop twice.
        record = writes.question_record(question.model_dump(mode="json"), vocabulary())
        if store.get_question(str(record["id"])) is not None:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"A Question {record['id']!r} already exists in this Content store. "
                    "Replace it with PUT, carrying its current ETag in If-Match."
                ),
            )
        return written(response, writer.write_question(record, "POST"), Question)

    @app.get(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="getQuestion",
        tags=["Questions"],
        summary="Read one Question by its id.",
        response_model=Question,
        responses=item_responses(404, 500),
    )
    def get_question(
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Any:
        identifier = f"{theme}/{slug}"
        record = store.get_question(identifier)
        if record is None:
            missing("Question", identifier)
        return conditional(
            Question.model_validate(record),
            record,
            if_none_match,
            response,
            lab_links(store, identifier),
        )

    @app.put(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="replaceQuestion",
        tags=["Questions"],
        summary="Replace a Question wholesale.",
        response_model=Question,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )
    def replace_question(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        question: QuestionWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_question(identifier)
        # Identity first, then the precondition, then the body. A client aiming
        # at something that is not there needs to hear `404` whatever else it
        # got wrong, and a body validated against a version that has already
        # moved is a body decided on the wrong facts.
        if existing is None:
            missing("Question", identifier)
        require_precondition(if_match, existing)
        payload = question.model_dump(mode="json")
        require_same_identity(payload, theme, slug, "Question")
        record = writes.question_record(payload, vocabulary())
        return written(response, writer.write_question(record, "PUT"), Question)

    @app.patch(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="patchQuestion",
        tags=["Questions"],
        summary="Change only the supplied fields of a Question.",
        response_model=Question,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )
    def patch_question(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        question: QuestionPatch,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_question(identifier)
        if existing is None:
            missing("Question", identifier)
        require_precondition(if_match, existing)
        # `exclude_unset` is what makes this a patch rather than a replace with
        # optional fields: a field the client did not mention keeps its stored
        # value, and `None` is never confused with "leave it alone".
        changes = question.model_dump(mode="json", exclude_unset=True)
        payload = writes.merge(existing, changes, writes.QUESTION_PATCH_FIELDS)
        record = writes.question_record(payload, vocabulary())
        return written(response, writer.write_question(record, "PATCH"), Question)

    @app.delete(
        "/api/v1/questions/{theme}/{slug}",
        operation_id="deleteQuestion",
        tags=["Questions"],
        summary="Delete a Question.",
        status_code=204,
        responses=problem_responses(401, 403, 404, 409, 412, 428, 503),
    )
    def delete_question(
        request: Request,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Response:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_question(identifier)
        if existing is None:
            missing("Question", identifier)
        require_precondition(if_match, existing)
        # A Question a Lab or a learning path still points at cannot go: the
        # store refuses and the handler above turns that into the `409` the
        # contract documents.
        writer.delete_question(identifier, "DELETE")
        return Response(status_code=204)

    # ------------------------------------------------------------------- Labs

    @app.get(
        "/api/v1/labs",
        operation_id="listLabs",
        tags=["Labs"],
        summary="List Labs, filtered, sorted, and paginated.",
        response_model=LabPage,
        responses=problem_responses(422, 500),
    )
    def list_labs(
        store: Annotated[Store, Depends(get_store)],
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
        page = store.list_labs(
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
        )
        return LabPage(items=page.items, total=page.total, limit=limit, offset=offset)

    @app.post(
        "/api/v1/labs",
        operation_id="createLab",
        tags=["Labs"],
        summary="Create a Lab.",
        status_code=201,
        response_model=Lab,
        responses={
            201: {
                "description": "The Lab was created.",
                "headers": {
                    "ETag": {
                        "description": "The new Lab's `content_hash`, quoted.",
                        "schema": {"type": "string"},
                    }
                },
            },
            **problem_responses(401, 403, 409, 422, 503),
        },
    )
    def create_lab(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        lab: LabWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        payload = lab.model_dump(mode="json")
        record = writes.lab_record(
            payload, vocabulary(), resolvable(store, str(payload.get("question_ref", "")))
        )
        if store.get_lab(str(record["id"])) is not None:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"A Lab {record['id']!r} already exists in this Content store. "
                    "Replace it with PUT, carrying its current ETag in If-Match."
                ),
            )
        return written(response, writer.write_lab(record, "POST"), Lab)

    @app.get(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="getLab",
        tags=["Labs"],
        summary="Read one Lab by its id.",
        response_model=Lab,
        responses=item_responses(404, 500),
    )
    def get_lab(
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Any:
        identifier = f"{theme}/{slug}"
        record = store.get_lab(identifier)
        if record is None:
            missing("Lab", identifier)
        return conditional(
            Lab.model_validate(record),
            record,
            if_none_match,
            response,
            question_link(store, str(record["question_ref"])),
        )

    @app.put(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="replaceLab",
        tags=["Labs"],
        summary="Replace a Lab wholesale.",
        response_model=Lab,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )
    def replace_lab(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        lab: LabWrite,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_lab(identifier)
        if existing is None:
            missing("Lab", identifier)
        require_precondition(if_match, existing)
        payload = lab.model_dump(mode="json")
        require_same_identity(payload, theme, slug, "Lab")
        record = writes.lab_record(
            payload, vocabulary(), resolvable(store, str(payload.get("question_ref", "")))
        )
        return written(response, writer.write_lab(record, "PUT"), Lab)

    @app.patch(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="patchLab",
        tags=["Labs"],
        summary="Change only the supplied fields of a Lab.",
        response_model=Lab,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )
    def patch_lab(
        request: Request,
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        lab: LabPatch,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_lab(identifier)
        if existing is None:
            missing("Lab", identifier)
        require_precondition(if_match, existing)
        changes = lab.model_dump(mode="json", exclude_unset=True)
        payload = writes.merge(existing, changes, writes.LAB_PATCH_FIELDS)
        record = writes.lab_record(
            payload, vocabulary(), resolvable(store, str(payload.get("question_ref", "")))
        )
        return written(response, writer.write_lab(record, "PATCH"), Lab)

    @app.delete(
        "/api/v1/labs/{theme}/{slug}",
        operation_id="deleteLab",
        tags=["Labs"],
        summary="Delete a Lab.",
        status_code=204,
        responses=problem_responses(401, 403, 404, 412, 428, 503),
    )
    def delete_lab(
        request: Request,
        store: Annotated[Store, Depends(get_store)],
        theme: str,
        slug: str,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Response:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = store.get_lab(identifier)
        if existing is None:
            missing("Lab", identifier)
        require_precondition(if_match, existing)
        # Nothing in the corpus refers to a Lab, so there is no `409` here and
        # the contract does not document one.
        writer.delete_lab(identifier, "DELETE")
        return Response(status_code=204)

    # --------------------------------------------------------------- Taxonomy

    @app.get(
        "/api/v1/themes",
        operation_id="listThemes",
        tags=["Taxonomy"],
        summary="List every canonical Theme with its counts.",
        response_model=ThemePage,
        responses=problem_responses(500),
    )
    def list_themes(store: Annotated[Store, Depends(get_store)]) -> ThemePage:
        return catalogue(ThemePage, store.list_themes())

    @app.get(
        "/api/v1/themes/{name}",
        operation_id="getTheme",
        tags=["Taxonomy"],
        summary="Read one Theme by its canonical name.",
        response_model=Theme,
        responses=item_responses(404, 500),
    )
    def get_theme(
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        name: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Any:
        record = store.get_theme(name)
        if record is None:
            missing("Theme", name)
        return conditional(Theme.model_validate(record), record, if_none_match, response)

    @app.get(
        "/api/v1/tags",
        operation_id="listTags",
        tags=["Taxonomy"],
        summary="List every tag with its counts.",
        response_model=TagPage,
        responses=problem_responses(500),
    )
    def list_tags(store: Annotated[Store, Depends(get_store)]) -> TagPage:
        return catalogue(TagPage, store.list_tags())

    # --------------------------------------------------------- Learning paths

    @app.get(
        "/api/v1/learning-paths",
        operation_id="listLearningPaths",
        tags=["Learning paths"],
        summary="List every learning path.",
        response_model=LearningPathPage,
        responses=problem_responses(500),
    )
    def list_learning_paths(store: Annotated[Store, Depends(get_store)]) -> LearningPathPage:
        return catalogue(LearningPathPage, store.list_learning_paths())

    @app.get(
        "/api/v1/learning-paths/{slug}",
        operation_id="getLearningPath",
        tags=["Learning paths"],
        summary="Read one learning path, with its ordered steps.",
        response_model=LearningPath,
        responses=item_responses(404, 500),
    )
    def get_learning_path(
        response: Response,
        store: Annotated[Store, Depends(get_store)],
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Any:
        record = store.get_learning_path(slug)
        if record is None:
            missing("learning path", slug)
        return conditional(LearningPath.model_validate(record), record, if_none_match, response)

    # ----------------------------------------------------------------- Search

    @app.get(
        "/api/v1/search",
        operation_id="search",
        tags=["Search"],
        summary="Search Questions and Labs together, ranked by relevance.",
        response_model=SearchPage,
        responses=problem_responses(422, 500),
    )
    def search(
        store: Annotated[Store, Depends(get_store)],
        q: Annotated[str, Query(min_length=1, description="The search text; it is required.")],
        kind: Annotated[
            ItemKind | None, Query(description="Restrict the result to one kind of item.")
        ] = None,
        limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
        offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
    ) -> SearchPage:
        page = store.search(
            SearchQuery(q=q, kind=kind.value if kind else None, limit=limit, offset=offset)
        )
        # One ranked list carries two kinds of item, so the hit says which it is
        # and the model is chosen from that rather than guessed from the fields:
        # a Question and a Lab overlap enough that a union would sometimes pick
        # the wrong one and silently drop what only the other has.
        items = []
        for hit in page.items:
            kind, score, item = search_hit(hit)
            model = Question if kind == ItemKind.question.value else Lab
            items.append(SearchHit(kind=kind, score=score, item=model.model_validate(item)))
        return SearchPage(items=items, total=page.total, limit=limit, offset=offset)

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
