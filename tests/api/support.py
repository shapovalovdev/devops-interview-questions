"""Shared scaffolding for the API test suite.

Everything here builds an application explicitly, from an explicitly supplied
store. Nothing in the suite reaches for `api.app:app`, because that entrypoint
resolves the Content store from the environment, and a test that depended on
the environment would be testing the machine it runs on.
"""

from __future__ import annotations

import secrets
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from api.app import create_app  # noqa: E402
from api import writes  # noqa: E402
from api.store import LabQuery, Page, QuestionQuery, SearchQuery  # noqa: E402
from api.testing import InMemoryStore, demo_corpus  # noqa: E402

CONTRACT_PATH = ROOT / "api" / "openapi.yaml"

#: The Write credential the suite configures a service with.
#:
#: Generated per session rather than written down, for two reasons. A literal
#: in this file would be a credential committed to the repository, which is the
#: habit this slice exists to refuse; and a value nobody can predict is what
#: lets `test_writes.py` assert that no response body, header, or problem
#: document ever contains it — an assertion that would be vacuous against a
#: string that happened to appear in the source anyway.
TEST_WRITE_CREDENTIAL = secrets.token_urlsafe(24)

#: A credential that is well-formed and wrong, for the `403` path.
WRONG_WRITE_CREDENTIAL = secrets.token_urlsafe(24)


def question_body(**overrides: Any) -> dict[str, Any]:
    """A `QuestionWrite` body that the Markdown corpus rules accept.

    Corpus-legal is the whole point: `prompt` and `answer_guide` are read out of
    `body_markdown` by `contentdb.corpus`, so a body that merely satisfied the
    JSON schema would be rejected at the edge and every test built on it would
    be testing the rejection. `overrides` is how a failure-path test breaks
    exactly one rule and leaves the rest valid.
    """
    fields: dict[str, Any] = {
        "theme": "kubernetes",
        "slug": "demo-write",
        "title": "Write a Question through the API",
        "difficulty": "middle",
        "type": "theory",
        "tags": ["kubernetes"],
        "sources": [
            {
                "url": "https://kubernetes.io/docs/home/",
                "source_type": "official-docs",
                "verified_on": "2026-08-01",
            }
        ],
        "prompt": "What does the Content API do with a write?",
        "answer_guide": ["Export renders it back to Markdown."],
    }
    fields.update(overrides)
    fields.setdefault(
        "body_markdown",
        f"\n# {fields['title']}\n\n{fields['prompt']}\n\n## Answer guide\n\n"
        + "\n".join(f"- {point}" for point in fields["answer_guide"]),
    )
    return fields


def lab_body(**overrides: Any) -> dict[str, Any]:
    """A `LabWrite` body the corpus rules accept. Every Lab field is front matter."""
    fields: dict[str, Any] = {
        "theme": "kubernetes",
        "slug": "demo-write",
        "title": "Write a Lab through the API",
        "difficulty": "middle",
        "tags": ["kubernetes"],
        "question_ref": "kubernetes/demo-admission-guardrails",
        "why": "Because a Lab prepares a learner for exactly one Question.",
        "checklist": ["Send the request."],
    }
    fields.update(overrides)
    fields.setdefault(
        "body_markdown",
        f"\n# {fields['title']}\n\n{fields['why']}\n\n## Steps\n\n"
        + "\n".join(f"- {step}" for step in fields["checklist"]),
    )
    return fields


#: The canonical bodies, for tests that only need "a valid one".
QUESTION_WRITE = question_body()
LAB_WRITE = lab_body()

#: A Question the demo corpus holds and that nothing points at, so it can be
#: replaced, patched, and deleted without tripping the referential `409`.
DEMO_SPARE_QUESTION = "kubernetes/demo-pod-disruption"

#: A Question the demo corpus holds that a Lab *and* a learning path point at.
DEMO_REFERENCED_QUESTION = "kubernetes/demo-admission-guardrails"

#: The demo Lab, which nothing points at.
DEMO_WRITABLE_LAB = "kubernetes/demo-admission-guardrails"


#: One request per write operation the contract publishes, keyed by the
#: contract's `(path, method)`. Every body is valid and every precondition is
#: satisfied, so each of these is the *success* path: the census pairs them with
#: the failure requests it builds itself.
WRITE_REQUESTS: dict[tuple[str, str], dict[str, Any]] = {
    ("/api/v1/questions", "post"): {"url": "/api/v1/questions", "json": QUESTION_WRITE},
    ("/api/v1/questions/{theme}/{slug}", "put"): {
        "url": f"/api/v1/questions/{DEMO_SPARE_QUESTION}",
        "json": question_body(slug="demo-pod-disruption"),
    },
    ("/api/v1/questions/{theme}/{slug}", "patch"): {
        "url": f"/api/v1/questions/{DEMO_SPARE_QUESTION}",
        "json": {"difficulty": "senior"},
    },
    ("/api/v1/questions/{theme}/{slug}", "delete"): {
        "url": f"/api/v1/questions/{DEMO_SPARE_QUESTION}"
    },
    ("/api/v1/labs", "post"): {"url": "/api/v1/labs", "json": LAB_WRITE},
    ("/api/v1/labs/{theme}/{slug}", "put"): {
        "url": f"/api/v1/labs/{DEMO_WRITABLE_LAB}",
        "json": lab_body(slug="demo-admission-guardrails"),
    },
    ("/api/v1/labs/{theme}/{slug}", "patch"): {
        "url": f"/api/v1/labs/{DEMO_WRITABLE_LAB}",
        "json": {"title": "A new title"},
    },
    ("/api/v1/labs/{theme}/{slug}", "delete"): {"url": f"/api/v1/labs/{DEMO_WRITABLE_LAB}"},
}

#: Which write operations need a precondition, so a caller can build the right
#: headers without restating the contract's table of methods.
NEEDS_IF_MATCH = ("put", "patch", "delete")


def send(
    client: TestClient,
    path: str,
    method: str,
    credential: str | None = TEST_WRITE_CREDENTIAL,
    if_match: str | None = None,
    **overrides: Any,
) -> Any:
    """Send the canonical write for one operation, with the headers it needs.

    `if_match` defaults to the item's current ETag, read back from the service
    just before the write, because that is what a client does and because a
    hard-coded validator would make every concurrency test a test of the
    fixture. Passing one explicitly is how a test produces a `412`; passing the
    empty string is how it produces a `428`.
    """
    specification = dict(WRITE_REQUESTS[(path, method)])
    specification.update(overrides)
    url = specification.pop("url")
    headers = {}
    if credential is not None:
        headers["X-API-Key"] = credential
    if method in NEEDS_IF_MATCH:
        headers["If-Match"] = current_etag(client, url) if if_match is None else if_match
    headers = {name: value for name, value in headers.items() if value != ""}
    return client.request(method.upper(), url, headers=headers, **specification)



def problem(response: Any) -> dict[str, Any]:
    """The RFC 9457 document a refusal answered with.

    Two test modules had grown their own copy of this; a refusal's shape is a
    contract detail, so it belongs beside the other shared fixtures.
    """
    assert response.headers["content-type"].startswith("application/problem+json"), (
        f"{response.request.method} {response.request.url} answered "
        f"{response.headers.get('content-type')!r}, not a problem document"
    )
    return response.json()

def current_etag(client: TestClient, url: str) -> str:
    """The validator the service hands over for `url` right now."""
    response = client.get(url)
    return response.headers.get("ETag", '"no-such-item"')


class ExplodingStore(InMemoryStore):
    """A store that fails the way a real one eventually will: unexpectedly.

    Every read raises, not only the first one that was implemented: the contract
    documents a `500` on each read operation, and the census can only prove one
    is really produced if the failure is available to every route.
    """

    def _fail(self, *_arguments: Any, **_keywords: Any) -> Page:
        raise RuntimeError("the Content store is unreachable: sqlite3.OperationalError")

    list_questions = _fail
    get_question = _fail
    list_labs = _fail
    get_lab = _fail
    list_themes = _fail
    get_theme = _fail
    list_tags = _fail
    list_learning_paths = _fail
    get_learning_path = _fail
    search = _fail


#: The ids the demo corpus holds, and one it deliberately does not, so a test
#: naming a `404` cannot accidentally name something real.
DEMO_QUESTION = "/api/v1/questions/kubernetes/demo-admission-guardrails"
DEMO_LAB = "/api/v1/labs/kubernetes/demo-admission-guardrails"
DEMO_THEME = "/api/v1/themes/kubernetes"
DEMO_LEARNING_PATH = "/api/v1/learning-paths/demo-kubernetes-basics"
UNKNOWN_QUESTION = "/api/v1/questions/kubernetes/nothing-here"
UNKNOWN_LAB = "/api/v1/labs/kubernetes/nothing-here"
UNKNOWN_THEME = "/api/v1/themes/nothing-here"
UNKNOWN_LEARNING_PATH = "/api/v1/learning-paths/nothing-here"


def revalidate(client: TestClient, url: str) -> Any:
    """Read an item, then ask for it again with the ETag it just handed over."""
    first = client.get(url)
    assert first.status_code == 200, f"{url} answered {first.status_code}, so it has no ETag"
    etag = first.headers["ETag"]
    return client.get(url, headers={"If-None-Match": etag})


class RawHitStore(InMemoryStore):
    """A store whose search answers the way `contentdb.store.Store` does.

    Bare rows keyed `{kind, id, theme, title, snippet}` — no `score`, no nested
    `item`. This is exactly what reached the service when the real store was
    wired in without `api/content.py`, and it is why the seam now says what a
    hit is instead of trusting whoever implements it.
    """

    def search(self, query: SearchQuery) -> Page:
        return Page(
            items=[
                {
                    "kind": "question",
                    "id": "kubernetes/demo-admission-guardrails",
                    "theme": "kubernetes",
                    "title": "Design admission guardrails",
                    "snippet": "…admission…",
                }
            ],
            total=1,
        )


class MalformedStore(InMemoryStore):
    """A store that answers with a record the contract cannot describe."""

    def list_questions(self, query: QuestionQuery) -> Page:
        return Page(items=[{"id": "kubernetes/broken"}], total=1)


def environment(
    credential: str | None = TEST_WRITE_CREDENTIAL, corpus_root: Any = None
) -> dict[str, str]:
    """The environment a test service reads its write configuration from.

    Built as a mapping rather than exported into the process: `create_app` takes
    one, so a suite can run a service that accepts writes without putting a
    credential into the environment of the interpreter running the tests, where
    every other test and every subprocess would inherit it.
    """
    environ: dict[str, str] = {}
    if credential is not None:
        environ[writes.WRITE_CREDENTIAL_VARIABLE] = credential
    if corpus_root is not None:
        environ[writes.CORPUS_ROOT_VARIABLE] = str(corpus_root)
    return environ


def demo_app(credential: str | None = TEST_WRITE_CREDENTIAL) -> FastAPI:
    return create_app(store=demo_corpus(), environ=environment(credential))


def demo_client(credential: str | None = TEST_WRITE_CREDENTIAL) -> TestClient:
    """A client over the demo corpus, returning server errors as responses.

    `raise_server_exceptions=False` is what lets a test observe the `500`
    problem document instead of the exception the handler already answered.

    Each call builds a fresh store, so a test that writes cannot leak into the
    next one. `credential=None` builds the read-only service the contract
    answers `503` from.
    """
    return TestClient(demo_app(credential), raise_server_exceptions=False)


def client_for(
    store: Any, credential: str | None = TEST_WRITE_CREDENTIAL, corpus_root: Any = None
) -> TestClient:
    return TestClient(
        create_app(store=store, environ=environment(credential, corpus_root)),
        raise_server_exceptions=False,
    )


__all__ = [
    "CONTRACT_PATH",
    "DEMO_LAB",
    "DEMO_LEARNING_PATH",
    "DEMO_QUESTION",
    "DEMO_THEME",
    "ExplodingStore",
    "InMemoryStore",
    "LAB_WRITE",
    "LabQuery",
    "MalformedStore",
    "Page",
    "QUESTION_WRITE",
    "QuestionQuery",
    "ROOT",
    "RawHitStore",
    "TEST_WRITE_CREDENTIAL",
    "WRITE_REQUESTS",
    "WRONG_WRITE_CREDENTIAL",
    "DEMO_REFERENCED_QUESTION",
    "DEMO_SPARE_QUESTION",
    "DEMO_WRITABLE_LAB",
    "NEEDS_IF_MATCH",
    "current_etag",
    "environment",
    "lab_body",
    "question_body",
    "writes",
    "UNKNOWN_LAB",
    "UNKNOWN_LEARNING_PATH",
    "UNKNOWN_QUESTION",
    "UNKNOWN_THEME",
    "SearchQuery",
    "client_for",
    "create_app",
    "demo_app",
    "demo_client",
    "demo_corpus",
    "revalidate",
    "send",
]
