"""The guards a write passes, and the links a read answers with.

These were module-level helpers in `api/app.py`.  They moved here so the
routers in `api/routes/` can import them directly: `api/routes/resource.py`
previously took them as arguments purely to avoid importing `api.app`, which
imports it back.  That injection was an import-cycle workaround wearing the
costume of a design, and it is gone now that the helpers sit below both.

`require_write_access`, `require_precondition` and `require_same_identity`
between them implement the ordered write check the contract publishes -- 503,
401, 403, then 404, 428, 412, and only then 422 -- once, for every resource
kind.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

from fastapi import HTTPException, Request, Response
from pydantic import BaseModel

from api import writes
from api.helpers import LINKED_LABS_LIMIT, etag_for, problem_responses
from api.store import LabQuery, Record, Store, WritableStore, writable


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


