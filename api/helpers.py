"""Response shapes every route in the contract shares.

These were module-level helpers in `api/app.py`.  They moved here when the
routes did, so that a router in `api/routes/` and `create_app()` itself use one
definition rather than each growing its own -- which is the defect this epic
exists to remove, and the one a "just import it from app.py" shortcut would have
recreated as an import cycle.

Nothing here touches application state.  Each function turns a record, a model,
or a set of status codes into the response or the schema fragment the contract
publishes for it, which is why it can sit below both callers.
"""

from __future__ import annotations

import hashlib
from collections.abc import Mapping, Sequence
from http import HTTPStatus
from typing import Any, NoReturn
from urllib.parse import quote

from fastapi import HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from api.models import Problem
from api.store import Record

PROBLEM_MEDIA_TYPE = "application/problem+json"
PROBLEM_SCHEMA_REF = "#/components/schemas/Problem"


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

