"""Prove the router seam is real: a route works without `create_app()`.

The point of moving routes into `api/routes/` is not tidiness. It is that the
smallest unit a test can reach stops being the whole application. Every test in
this module mounts a router onto a bare `FastAPI()` with a store of its own
choosing, and never calls `create_app()`.

The closure measurements below are the other half of the claim, taken from the
compiled code objects rather than by reading. Before this change, ten of
`create_app()`'s thirty-one nested functions closed over it; six of those were
write routes capturing `vocabulary`, and `get_meta` captured `app`. Now no route
handler captures anything, so a route is bound to whichever application mounts
it. That is what makes the mounting below possible, and what #182 and #183 need
in order to generate routes from a spec.
"""

from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from api.routes import get_store, get_vocabulary  # noqa: E402
from api.routes.catalogue import router as catalogue_router  # noqa: E402
from api.testing import demo_corpus  # noqa: E402


def mounted(router, store) -> TestClient:
    """A bare application carrying one router and one store. No create_app()."""
    app = FastAPI()
    app.state.store = store
    app.state.vocabulary = None
    app.state.environ = {}
    app.include_router(router)
    return TestClient(app)


@pytest.fixture
def catalogue() -> TestClient:
    return mounted(catalogue_router, demo_corpus())


def test_a_router_answers_without_the_application_being_built(catalogue: TestClient) -> None:
    """The seam: six operations, served from a FastAPI() the test made itself."""
    answer = catalogue.get("/api/v1/themes")
    assert answer.status_code == 200
    body = answer.json()
    assert body["total"] == len(body["items"]) > 0
    assert body["offset"] == 0


def test_every_catalogue_operation_is_reachable(catalogue: TestClient) -> None:
    assert {route.operation_id for route in catalogue_router.routes} == {
        "listThemes",
        "getTheme",
        "listTags",
        "listLearningPaths",
        "getLearningPath",
        "search",
    }


def test_a_single_item_read_still_answers_its_validator(catalogue: TestClient) -> None:
    """Conditional reads are a helper, not application state, so they move too."""
    name = catalogue.get("/api/v1/themes").json()["items"][0]["name"]
    first = catalogue.get(f"/api/v1/themes/{name}")
    assert first.status_code == 200 and first.headers["ETag"]

    again = catalogue.get(
        f"/api/v1/themes/{name}", headers={"If-None-Match": first.headers["ETag"]}
    )
    assert again.status_code == 304
    assert not again.content


def test_a_missing_item_is_a_404_from_the_router_alone(catalogue: TestClient) -> None:
    assert catalogue.get("/api/v1/themes/not-a-theme").status_code == 404


def test_search_ranks_both_kinds(catalogue: TestClient) -> None:
    answer = catalogue.get("/api/v1/search", params={"q": "the", "limit": 5})
    assert answer.status_code == 200
    assert {hit["kind"] for hit in answer.json()["items"]} <= {"question", "lab"}


def test_the_store_dependency_reads_the_mounting_application(catalogue: TestClient) -> None:
    """Two applications, two stores, one router object shared between them."""
    other = mounted(catalogue_router, demo_corpus())
    assert other.get("/api/v1/themes").status_code == 200
    assert catalogue.get("/api/v1/themes").status_code == 200


def test_the_vocabulary_dependency_hands_back_a_loader_not_a_value() -> None:
    """The lazy form is what preserves the contract's write-check order.

    `api/app.py` documents 503 -> 401 -> 403 -> 404 -> 428 -> 412 -> 422 and
    calls the order part of the contract. Loading the vocabularies can raise
    `StoreIsReadOnly`, which is the 503. Resolved eagerly as a dependency it
    would run before the route body, and so before `require_write_access`,
    turning an unauthenticated write into a 503 where the contract promises a
    401. Returning a loader keeps the call where it was.
    """
    request = types.SimpleNamespace(
        app=types.SimpleNamespace(state=types.SimpleNamespace(vocabulary=object(), environ={}))
    )
    loader = get_vocabulary(request)  # type: ignore[arg-type]
    assert callable(loader), "get_vocabulary must return a loader, not the vocabularies"
    assert loader() is request.app.state.vocabulary


def test_the_store_dependency_is_a_plain_read_of_application_state() -> None:
    store = object()
    request = types.SimpleNamespace(app=types.SimpleNamespace(state=types.SimpleNamespace(store=store)))
    assert get_store(request) is store  # type: ignore[arg-type]


def test_no_route_handler_closes_over_create_app() -> None:
    """Measured from the code objects, because reading the source got it wrong.

    The audit claimed every handler closed over `store`, `vocabulary()` and
    `environ`. It did not: `store` has always arrived through `Depends`. What
    was true is that six write routes captured `vocabulary` and `get_meta`
    captured `app`. Neither does now, and this check is what keeps it that way --
    a route that captures the enclosing scope cannot be moved to a router or
    generated from a spec.
    """
    import api.app as app_module

    source = Path(app_module.__file__).read_text(encoding="utf-8")
    code = compile(source, app_module.__file__, "exec")

    def find(container, name):
        for const in container.co_consts:
            if isinstance(const, types.CodeType):
                if const.co_name == name:
                    return const
                found = find(const, name)
                if found:
                    return found
        return None

    create_app = find(code, "create_app")
    assert create_app, "api/app.py no longer defines create_app"

    handler_prefixes = ("get_", "list_", "create_", "replace_", "patch_", "delete_", "search")
    offenders = {
        const.co_name: list(const.co_freevars)
        for const in create_app.co_consts
        if isinstance(const, types.CodeType)
        and const.co_freevars
        and const.co_name.startswith(handler_prefixes)
    }
    assert not offenders, (
        f"these route handlers close over create_app(): {offenders}. Dependencies must arrive "
        "through Depends so the handler can be mounted anywhere."
    )


def test_an_unreadable_vocabulary_is_a_read_only_service(monkeypatch: pytest.MonkeyPatch) -> None:
    """The 503 the contract publishes, raised where the route body asks for it.

    A deployment that ships only the store has no `TAGS.md` beside it. That is a
    legitimate read-only deployment, so it must start and serve reads; only a
    write discovers the missing vocabularies, and only when it reaches the point
    of validating content.
    """
    from api import writes
    from api.store import StoreIsReadOnly

    def unreadable(*_: object, **__: object) -> None:
        raise OSError("TAGS.md: No such file or directory")

    monkeypatch.setattr(writes.Vocabulary, "load", staticmethod(unreadable))

    request = types.SimpleNamespace(
        app=types.SimpleNamespace(state=types.SimpleNamespace(vocabulary=None, environ={}))
    )
    loader = get_vocabulary(request)  # type: ignore[arg-type]

    with pytest.raises(StoreIsReadOnly) as raised:
        loader()
    assert "TAGS.md" in str(raised.value)
    assert writes.CORPUS_ROOT_VARIABLE in str(raised.value)
