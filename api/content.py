"""The real Content store, adapted to the API's `Store` seam.

`contentdb.store.Store` answers the reads the epic pins, but it is not quite the
`api.store.Store` protocol: its catalogue reads return bare tuples, its search
returns one row per hit rather than the whole item, and its query dataclasses
are its own. This module is the adapter that closes that gap, and it is the only
place in `api/` that knows `contentdb` exists.

The adaptation is deliberately one-directional. Plain mappings still cross the
seam — nothing here builds a Pydantic model, and `contentdb` still imports
nothing from `api/`. What crosses is exactly what `api/store.py` documents.

**How concurrent readers share the connection.** `contentdb.store.Store` opens
the database once, read-only (`file:…?mode=ro`) and with
`check_same_thread=False`, and this adapter holds that one `Store` for the
lifetime of the process. A request does not open its own connection; instead
**every read is taken under one re-entrant lock**, so the shared connection is
used by one thread at a time.

The lock is not defensive habit, and `sqlite3.threadsafety == 3` does not remove
the need for it. That constant describes SQLite's own mutexes, but CPython's
`sqlite3` module caches *prepared statements* per connection, and two threads
running the same SQL on one connection can hand the same `sqlite3_stmt` to
SQLite at once. The result is `sqlite3.InterfaceError: bad parameter or other
API misuse` — `SQLITE_MISUSE` — which this suite reproduced on a serialized
SQLite 3.50 before the lock existed, and which
`test_one_shared_store_answers_readers_on_many_threads` now guards.

Serializing reads is the right trade here, rather than opening a connection per
request:

- *Nothing writes.* A read-only handle cannot begin a write transaction, and
  Ingest publishes a new store by `os.replace`, so an open connection keeps
  reading the file it opened rather than a half-written one. There is no writer
  to contend with, no `SQLITE_BUSY` to retry, and therefore nothing held across
  a request boundary.
- *Every read is short.* A read is one or more indexed `SELECT`s against a file
  the operating system has cached, measured in microseconds. Opening a fresh
  connection per request would re-read the schema and re-prepare every
  statement, which for this workload costs more than the contention the lock
  introduces.
- *The lock is re-entrant.* `search()` resolves each hit through the same
  guarded helpers, so a non-re-entrant lock would deadlock on the first hit.

**Failing fast.** `content_store()` is the `CONTENT_API_STORE` target for a real
deployment. If the store file is missing or is not a database, it raises
:class:`ContentStoreUnavailable` naming the path it looked at and the Ingest
command that produces it. A service that started anyway would serve an empty,
perfectly valid-looking corpus, and no client could tell that apart from a
corpus that really is empty.
"""

from __future__ import annotations

import os
import sqlite3
import threading
from collections.abc import Mapping
from pathlib import Path
from typing import Any, ContextManager

from contentdb import models as content_models
from contentdb import store as content_store_module

from api.store import InvalidQuery, LabQuery, Page, QuestionQuery, Record, SearchQuery

#: Names the environment variable that points at the Content store file.
STORE_PATH_VARIABLE = "CONTENT_STORE_PATH"

#: Where Ingest writes the store by default, relative to the repository root.
DEFAULT_STORE_PATH = Path("build/content.db")

#: The command that produces the store, quoted in every failure message.
INGEST_COMMAND = "python -m contentdb.ingest --output build/content.db"


class ContentStoreUnavailable(RuntimeError):
    """Raised when the configured Content store cannot be opened and read."""


def read_guard() -> ContextManager[Any]:
    """The lock every read on the shared connection is taken under.

    Re-entrant, because `search()` resolves each hit through the same guarded
    helpers and a plain lock would deadlock on the first one.
    """
    return threading.RLock()


def _question_query(query: QuestionQuery) -> content_models.QuestionQuery:
    return content_models.QuestionQuery(
        theme=query.theme,
        difficulty=query.difficulty,
        type=query.type,
        tag=query.tag,
        q=query.q,
        sort=query.sort,
        limit=query.limit,
        offset=query.offset,
    )


def _lab_query(query: LabQuery) -> content_models.LabQuery:
    return content_models.LabQuery(
        theme=query.theme,
        difficulty=query.difficulty,
        tag=query.tag,
        question_ref=query.question_ref,
        q=query.q,
        sort=query.sort,
        limit=query.limit,
        offset=query.offset,
    )


class ContentStore:
    """The `api.store.Store` protocol, served by the SQLite Content store."""

    def __init__(self, store: Any):
        self._store = store
        self._guard = read_guard()

    @classmethod
    def open(cls, path: Path | str) -> "ContentStore":
        """Open the store at `path`, or say what is missing and how to build it."""
        path = Path(path)
        try:
            store = content_store_module.Store(path)
        except (FileNotFoundError, sqlite3.Error) as error:
            raise ContentStoreUnavailable(
                f"the Content store at {path} cannot be read ({error}). It is a derived "
                f"artifact, not something to hand-edit: build it with `{INGEST_COMMAND}`, "
                f"or point {STORE_PATH_VARIABLE} at an existing store. The Content API "
                "refuses to start without one rather than serve an empty corpus that no "
                "client could tell from a real one."
            ) from error
        return cls(store)

    def close(self) -> None:
        self._store.close()

    # -- Questions ---------------------------------------------------------

    def list_questions(self, query: QuestionQuery) -> Page:
        return self._page(self._read(self._store.list_questions, _question_query(query)))

    def get_question(self, question_id: str) -> Record | None:
        return self._read(self._store.get_question, question_id)

    # -- Labs --------------------------------------------------------------

    def list_labs(self, query: LabQuery) -> Page:
        return self._page(self._read(self._store.list_labs, _lab_query(query)))

    def get_lab(self, lab_id: str) -> Record | None:
        return self._read(self._store.get_lab, lab_id)

    # -- Catalogues --------------------------------------------------------

    def list_themes(self) -> Page:
        return self._catalogue(self._read(self._store.list_themes))

    def get_theme(self, name: str) -> Record | None:
        return self._read(self._store.get_theme, name)

    def list_tags(self) -> Page:
        return self._catalogue(self._read(self._store.list_tags))

    def list_learning_paths(self) -> Page:
        return self._catalogue(self._read(self._store.list_learning_paths))

    def get_learning_path(self, slug: str) -> Record | None:
        return self._read(self._store.get_learning_path, slug)

    # -- Search ------------------------------------------------------------

    def search(self, query: SearchQuery) -> Page:
        """Rank Questions and Labs together, each hit carrying its whole item.

        The store ranks with bm25 but does not hand the score across the seam,
        and this adapter will not invent a number that looks like one. What it
        reports instead is derived from the rank the store returned — strictly
        decreasing down the page — which is exactly what the contract promises:
        a relevance "comparable only within one response".

        Resolving each hit costs one indexed lookup by primary key. That is a
        query per hit, bounded by `limit` (at most 200), and it is what lets a
        client render a result list without a second round trip per item.
        """
        with self._guard:
            page = self._read(
                self._store.search,
                content_models.SearchQuery(
                    q=query.q, kind=query.kind, limit=query.limit, offset=query.offset
                ),
            )
            hits = []
            for position, hit in enumerate(page.items):
                item = (
                    self.get_question(hit["id"])
                    if hit["kind"] == "question"
                    else self.get_lab(hit["id"])
                )
                if item is None:  # pragma: no cover - the index cannot outlive its rows
                    continue
                hits.append(
                    {
                        "kind": hit["kind"],
                        "score": rank_score(query.offset + position),
                        "item": item,
                    }
                )
            return Page(items=hits, total=page.total)

    # -- Internals ---------------------------------------------------------

    def _read(self, call: Any, *arguments: Any) -> Any:
        """Run one read under the shared lock, in the API's error vocabulary.

        `q` reaches SQLite as an FTS5 expression, so a client can send text
        SQLite refuses to parse — an unbalanced quote is enough. That is a
        malformed request, not a fault, and the seam has a name for it.
        """
        with self._guard:
            try:
                return call(*arguments)
            except content_store_module.SearchError as error:
                raise InvalidQuery(str(error)) from error

    @staticmethod
    def _page(page: Any) -> Page:
        return Page(items=page.items, total=page.total)

    @staticmethod
    def _catalogue(records: tuple[Mapping[str, Any], ...]) -> Page:
        """Wrap a bounded catalogue in the envelope every list response shares."""
        return Page(items=records, total=len(records))


def rank_score(rank: int) -> float:
    """Turn a zero-based rank into the contract's descending relevance score."""
    return 1.0 / (1.0 + rank)


def store_path(environ: Mapping[str, str] | None = None) -> Path:
    """Where to look for the Content store, defaulting to Ingest's own output."""
    environ = os.environ if environ is None else environ
    configured = environ.get(STORE_PATH_VARIABLE, "").strip()
    return Path(configured) if configured else DEFAULT_STORE_PATH


def content_store() -> ContentStore:
    """The `CONTENT_API_STORE=api.content:content_store` entrypoint."""
    return ContentStore.open(store_path())
