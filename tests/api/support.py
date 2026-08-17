"""Shared scaffolding for the API test suite.

Everything here builds an application explicitly, from an explicitly supplied
store. Nothing in the suite reaches for `api.app:app`, because that entrypoint
resolves the Content store from the environment, and a test that depended on
the environment would be testing the machine it runs on.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from api.app import create_app  # noqa: E402
from api.store import LabQuery, Page, QuestionQuery, SearchQuery  # noqa: E402
from api.testing import InMemoryStore, demo_corpus  # noqa: E402

CONTRACT_PATH = ROOT / "api" / "openapi.yaml"

#: A body that satisfies `QuestionWrite`, so a stubbed write route is reached
#: rather than rejected by schema validation before it can answer `501`.
QUESTION_WRITE = {
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
    "body_markdown": "# Write\n",
}

#: The same, for `LabWrite`.
LAB_WRITE = {
    "theme": "kubernetes",
    "slug": "demo-write",
    "title": "Write a Lab through the API",
    "difficulty": "middle",
    "tags": ["kubernetes"],
    "question_ref": "kubernetes/demo-write",
    "why": "Because a Lab prepares a learner for exactly one Question.",
    "checklist": ["Send the request."],
    "body_markdown": "# Write\n",
}


#: One request per stubbed operation, chosen so the request reaches the route
#: rather than being rejected by schema validation first — a `422` from a
#: malformed body would prove nothing about the stub. Keyed by the contract's
#: `(path, method)`, so the coverage census can check this table against
#: `api/openapi.yaml` and fail when an operation is published without one.
STUB_REQUESTS: dict[tuple[str, str], dict[str, Any]] = {
    ("/api/v1/questions", "post"): {
        "url": "/api/v1/questions",
        "json": QUESTION_WRITE,
    },
    ("/api/v1/questions/{theme}/{slug}", "get"): {
        "url": "/api/v1/questions/kubernetes/demo-admission-guardrails",
    },
    ("/api/v1/questions/{theme}/{slug}", "put"): {
        "url": "/api/v1/questions/kubernetes/demo-admission-guardrails",
        "json": QUESTION_WRITE,
    },
    ("/api/v1/questions/{theme}/{slug}", "patch"): {
        "url": "/api/v1/questions/kubernetes/demo-admission-guardrails",
        "json": {"title": "A new title"},
    },
    ("/api/v1/questions/{theme}/{slug}", "delete"): {
        "url": "/api/v1/questions/kubernetes/demo-admission-guardrails",
    },
    ("/api/v1/labs", "get"): {"url": "/api/v1/labs"},
    ("/api/v1/labs", "post"): {"url": "/api/v1/labs", "json": LAB_WRITE},
    ("/api/v1/labs/{theme}/{slug}", "get"): {
        "url": "/api/v1/labs/kubernetes/demo-admission-guardrails",
    },
    ("/api/v1/labs/{theme}/{slug}", "put"): {
        "url": "/api/v1/labs/kubernetes/demo-admission-guardrails",
        "json": LAB_WRITE,
    },
    ("/api/v1/labs/{theme}/{slug}", "patch"): {
        "url": "/api/v1/labs/kubernetes/demo-admission-guardrails",
        "json": {"title": "A new title"},
    },
    ("/api/v1/labs/{theme}/{slug}", "delete"): {
        "url": "/api/v1/labs/kubernetes/demo-admission-guardrails",
    },
    ("/api/v1/themes", "get"): {"url": "/api/v1/themes"},
    ("/api/v1/themes/{name}", "get"): {"url": "/api/v1/themes/kubernetes"},
    ("/api/v1/tags", "get"): {"url": "/api/v1/tags"},
    ("/api/v1/learning-paths", "get"): {"url": "/api/v1/learning-paths"},
    ("/api/v1/learning-paths/{slug}", "get"): {
        "url": "/api/v1/learning-paths/demo-kubernetes-basics",
    },
    ("/api/v1/search", "get"): {"url": "/api/v1/search?q=admission"},
}


def send(client: TestClient, path: str, method: str) -> Any:
    """Send the canonical request for a stubbed operation."""
    specification = dict(STUB_REQUESTS[(path, method)])
    url = specification.pop("url")
    return client.request(method.upper(), url, **specification)


class ExplodingStore(InMemoryStore):
    """A store that fails the way a real one eventually will: unexpectedly."""

    def list_questions(self, query: QuestionQuery) -> Page:
        raise RuntimeError("the Content store is unreachable: sqlite3.OperationalError")


class MalformedStore(InMemoryStore):
    """A store that answers with a record the contract cannot describe."""

    def list_questions(self, query: QuestionQuery) -> Page:
        return Page(items=[{"id": "kubernetes/broken"}], total=1)


def demo_app() -> FastAPI:
    return create_app(store=demo_corpus())


def demo_client() -> TestClient:
    """A client over the demo corpus, returning server errors as responses.

    `raise_server_exceptions=False` is what lets a test observe the `500`
    problem document instead of the exception the handler already answered.
    """
    return TestClient(demo_app(), raise_server_exceptions=False)


def client_for(store: Any) -> TestClient:
    return TestClient(create_app(store=store), raise_server_exceptions=False)


__all__ = [
    "CONTRACT_PATH",
    "ExplodingStore",
    "InMemoryStore",
    "LAB_WRITE",
    "LabQuery",
    "MalformedStore",
    "Page",
    "QUESTION_WRITE",
    "QuestionQuery",
    "ROOT",
    "STUB_REQUESTS",
    "SearchQuery",
    "client_for",
    "create_app",
    "demo_app",
    "demo_client",
    "demo_corpus",
    "send",
]
