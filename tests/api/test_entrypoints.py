"""How the service starts, and what it refuses to do when it cannot.

The coordinator ruled that `create_app()` must never fall back to a fabricated
corpus. Serving invented Questions from the production entrypoint is not a
convenience, it is a correctness bug: a client has no way to tell them from the
corpus, and a demo that looks like production is how invented content reaches a
learner. So the failure has to be loud, and it has to say what to configure.
"""

from __future__ import annotations

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import api.app
from api.app import STORE_ENVIRONMENT_VARIABLE, StoreNotConfigured, create_app
from api.testing import InMemoryStore


@pytest.fixture(autouse=True)
def _no_store_configured(monkeypatch):
    """Every test here decides for itself what the environment says."""
    monkeypatch.delenv(STORE_ENVIRONMENT_VARIABLE, raising=False)


def test_creating_the_app_without_a_store_fails_fast_and_says_what_to_set():
    with pytest.raises(StoreNotConfigured) as raised:
        create_app()
    message = str(raised.value)
    assert STORE_ENVIRONMENT_VARIABLE in message
    assert "api.demo" in message, "the message should point at the demo entrypoint"
    assert "create_app(store=" in message


def test_the_failure_names_the_reason_rather_than_inventing_a_corpus():
    with pytest.raises(StoreNotConfigured, match="will not invent one"):
        create_app()


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("api.testing", "must look like"),
        (":demo_store", "must look like"),
        ("api.testing:", "must look like"),
        ("   ", STORE_ENVIRONMENT_VARIABLE),
        ("no.such.module:factory", "cannot be imported"),
        ("api.testing:no_such_factory", "does not define it"),
    ],
)
def test_a_misconfigured_store_target_is_refused_with_a_reason(monkeypatch, value, expected):
    monkeypatch.setenv(STORE_ENVIRONMENT_VARIABLE, value)
    with pytest.raises(StoreNotConfigured, match=expected):
        create_app()


def test_a_configured_store_is_what_the_service_serves(monkeypatch):
    monkeypatch.setenv(STORE_ENVIRONMENT_VARIABLE, "api.testing:demo_store")
    with TestClient(create_app()) as client:
        assert client.get("/api/v1/health").status_code == 200
        assert client.get("/api/v1/questions").json()["total"] == 4


def test_uvicorn_can_resolve_api_app_app(monkeypatch):
    """`uvicorn api.app:app` is exactly this attribute lookup."""
    monkeypatch.setenv(STORE_ENVIRONMENT_VARIABLE, "api.testing:demo_store")
    application = getattr(api.app, "app")
    assert isinstance(application, FastAPI)
    with TestClient(application) as client:
        response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "content-api", "contract_version": "v1"}


def test_resolving_api_app_app_without_a_store_fails_the_same_way():
    with pytest.raises(StoreNotConfigured):
        getattr(api.app, "app")


def test_importing_the_module_does_not_build_an_application():
    """The import itself must not need a store, or the tests could not import it."""
    assert "app" not in vars(api.app)


def test_an_unknown_attribute_is_still_an_attribute_error():
    with pytest.raises(AttributeError, match="has no attribute 'nope'"):
        api.app.nope


def test_an_explicit_store_bypasses_the_environment_entirely():
    application = create_app(store=InMemoryStore())
    with TestClient(application) as client:
        assert client.get("/api/v1/questions").json() == {
            "items": [], "total": 0, "limit": 50, "offset": 0,
        }


def test_the_demo_entrypoint_serves_a_corpus_that_announces_it_is_fake():
    import api.demo

    with TestClient(api.demo.app) as client:
        assert client.get("/api/v1/health").status_code == 200
        body = client.get("/api/v1/questions").json()
    assert body["total"] == 4
    for item in body["items"]:
        assert item["slug"].startswith("demo-")
