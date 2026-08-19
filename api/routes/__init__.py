"""Routers that implement the contract, one module per area of it.

`create_app()` in `api/app.py` used to define every route inside its own body,
which made 721 of that module's 1,392 lines one function and left nothing inside
it importable: the smallest unit a test could reach was the whole application.

A router here is an ordinary module-level object.  It can be imported, mounted
onto a bare `FastAPI()` with a store of the test's choosing, and exercised
without `create_app()` ever running -- which is what `tests/api/test_routes.py`
does.

**Dependencies arrive through `Depends`, never through a closure.**  Both
resolvers read `request.app.state`, so a router is bound to whichever
application mounts it rather than to the scope that built it.  `get_store` was
already written this way; `get_vocabulary` replaces the one genuine closure the
service had left -- the `vocabulary()` function the six write routes called.

`api/openapi.yaml` remains the source of truth.  Moving a route here must not
change the served schema by one byte, and `tests/api/test_contract.py` is what
proves it.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Annotated, Any

from fastapi import Depends, Request

if TYPE_CHECKING:  # pragma: no cover - import cycle only matters to type checkers
    from api.store import Store


def get_store(request: Request) -> "Store":
    """The Content store this application was built over."""
    return request.app.state.store


def get_vocabulary(request: Request) -> Callable[[], Any]:
    """A **loader** for the Theme and tag vocabularies a write is validated against.

    Note what this returns: a zero-argument callable, not the vocabularies.  The
    distinction is the contract's, not a style choice.

    `api/app.py` documents the order a write is checked in -- can this service
    write at all (`503`), did the client authenticate (`401`), is the credential
    right (`403`), does the record exist (`404`), which version (`428`), is it
    current (`412`), and only then is the content legal (`422`) -- and calls that
    order part of the contract.  Loading the vocabularies can itself raise
    `StoreIsReadOnly`, which is the `503`.  Resolved eagerly as a dependency, it
    would run *before* the route body and so before `require_write_access`,
    turning an unauthenticated request into a `503` where the contract promises
    a `401`.

    Returning the loader keeps the call at the point in the body where it always
    was, so the order is preserved by construction rather than by remembering.

    Loading is still lazy and cached on `app.state`: a read-only deployment has
    no use for the vocabularies, and refusing to start without `TAGS.md` beside
    the store would break every deployment that ships only the store.
    """

    def load() -> Any:
        from api import writes
        from api.store import StoreIsReadOnly

        if request.app.state.vocabulary is None:
            try:
                request.app.state.vocabulary = writes.Vocabulary.load(
                    environ=request.app.state.environ
                )
            except OSError as error:
                raise StoreIsReadOnly(
                    "This Content API cannot validate a write: the Theme and tag vocabularies "
                    "are read from config/content-manifest.json and TAGS.md, and they are not "
                    f"readable ({error}). Point {writes.CORPUS_ROOT_VARIABLE} at the corpus this "
                    "store was built from."
                ) from error
        return request.app.state.vocabulary

    return load


#: The two seams a router may depend on, named so route signatures stay short.
StoreDep = Annotated["Store", Depends(get_store)]
VocabularyDep = Annotated[Callable[[], Any], Depends(get_vocabulary)]

__all__ = ["StoreDep", "VocabularyDep", "get_store", "get_vocabulary"]
