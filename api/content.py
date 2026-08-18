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

- *Every read is short.* A read is one or more indexed `SELECT`s against a file
  the operating system has cached, measured in microseconds. Opening a fresh
  connection per request would re-read the schema and re-prepare every
  statement, which for this workload costs more than the contention the lock
  introduces.
- *The lock is re-entrant.* `search()` resolves each hit through the same
  guarded helpers, so a non-re-entrant lock would deadlock on the first hit.

**How a writer coexists with those readers.** Slice 4 made this store writable,
and a write cannot go down the read path: the shared connection is opened
`mode=ro`, and it stays that way. Instead the writer opens **a second
connection**, `mode=rw`, lazily on the first write and kept for the life of the
process — and it takes **the same re-entrant lock every read takes**. That one
sentence is what makes the arrangement safe, in two different ways at once:

- *Inside this process*, the lock means a write and a read are never in flight
  together, so the writer never has to contend with a reader it could have
  simply waited for. It also keeps the two connections' statement caches
  strictly apart, which is the failure the lock was introduced for: prepared
  statements are cached per connection, so nothing is shared across the two
  handles and no thread can hand SQLite a statement another thread is running.
- *Between processes* — a second replica, or `contentdb.ingest` running beside
  the service — the lock is worth nothing and SQLite's own file locking does
  the work. The store keeps the rollback journal Ingest gave it, so a write
  takes a `RESERVED` lock, upgrades to `EXCLUSIVE` only at commit, and readers
  see either the whole transaction or none of it. A reader that arrives during
  that instant gets `SQLITE_BUSY`, which is why the writer sets a
  `busy_timeout`: the alternative is failing a request over a lock that clears
  in microseconds. WAL is deliberately *not* enabled — it would leave `-wal`
  and `-shm` files beside a store that Ingest publishes by `os.replace`, and a
  read-only handle cannot create the shared-memory file it would then need.

Because the read connection is only ever in autocommit, every `SELECT` starts a
fresh read transaction and therefore sees a write the moment it commits. That is
what lets a write answer with the record read back through the read path rather
than with an echo of the request body: the response and the next `GET` cannot
disagree.

The store the writer touches is still a derived artifact. Ingest rebuilds it
from the Markdown corpus, so a write that never becomes a committed file is
lost on the next build — which is the point of ADR 0001 and of the Drift gate,
not a defect in this module. The append-only audit table this writer creates
(`content_writes`) is derived in the same sense, and disappears with it.

**Failing fast.** `content_store()` is the `CONTENT_API_STORE` target for a real
deployment. If the store file is missing or is not a database, it raises
:class:`ContentStoreUnavailable` naming the path it looked at and the Ingest
command that produces it. A service that started anyway would serve an empty,
perfectly valid-looking corpus, and no client could tell that apart from a
corpus that really is empty.
"""

from __future__ import annotations

import json
import os
import sqlite3
import threading
from collections.abc import Mapping, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any, ContextManager, Iterator

from contentdb import models as content_models
from contentdb import store as content_store_module
from contentdb.corpus import DIFFICULTIES
from contentdb.schema import FTS_TABLE

from api.store import (
    InvalidQuery,
    LabQuery,
    Page,
    QuestionQuery,
    Record,
    RecordInUse,
    SearchQuery,
    StoreIsReadOnly,
)
from api.writes import timestamp

#: Names the environment variable that points at the Content store file.
STORE_PATH_VARIABLE = "CONTENT_STORE_PATH"

#: How long a write waits for another process to finish before giving up. A
#: commit on this store holds the exclusive lock for microseconds, so anything
#: at this scale is "wait for it" rather than "queue behind a long job".
BUSY_TIMEOUT_MILLISECONDS = 5000

#: The append-only trail every write leaves. It is created by the writer rather
#: than by `contentdb.schema`, because Ingest has no business emitting a table
#: that only the API writes: a store built for a read-only deployment should not
#: carry one. The triggers are what make "append-only" a property of the
#: database instead of a promise about this module's SQL.
AUDIT_DDL = """
CREATE TABLE IF NOT EXISTS content_writes (
    sequence     INTEGER PRIMARY KEY,
    kind         TEXT NOT NULL,
    id           TEXT NOT NULL,
    method       TEXT NOT NULL,
    written_at   TEXT NOT NULL,
    content_hash TEXT
);
CREATE INDEX IF NOT EXISTS idx_content_writes_id ON content_writes(id);
CREATE TRIGGER IF NOT EXISTS content_writes_refuse_update
BEFORE UPDATE ON content_writes
BEGIN
    SELECT RAISE(ABORT, 'the Content API write trail is append-only');
END;
CREATE TRIGGER IF NOT EXISTS content_writes_refuse_delete
BEFORE DELETE ON content_writes
BEGIN
    SELECT RAISE(ABORT, 'the Content API write trail is append-only');
END;
"""

AUDIT_TABLE = "content_writes"

QUESTION_UPSERT = """
INSERT INTO questions (id, theme, slug, title, difficulty, type, prompt, answer_guide,
                       body_markdown, source_path, content_hash, updated_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    theme = excluded.theme, slug = excluded.slug, title = excluded.title,
    difficulty = excluded.difficulty, type = excluded.type, prompt = excluded.prompt,
    answer_guide = excluded.answer_guide, body_markdown = excluded.body_markdown,
    source_path = excluded.source_path, content_hash = excluded.content_hash,
    updated_at = excluded.updated_at
"""

LAB_UPSERT = """
INSERT INTO labs (id, theme, slug, title, difficulty, question_ref, why, checklist,
                  body_markdown, source_path, content_hash, updated_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    theme = excluded.theme, slug = excluded.slug, title = excluded.title,
    difficulty = excluded.difficulty, question_ref = excluded.question_ref,
    why = excluded.why, checklist = excluded.checklist,
    body_markdown = excluded.body_markdown, source_path = excluded.source_path,
    content_hash = excluded.content_hash, updated_at = excluded.updated_at
"""

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
        #: Opened on the first write and kept afterwards. A deployment with no
        #: Write credential configured never opens it at all, which is what
        #: keeps a read-only service from touching the file it serves.
        self._writer: sqlite3.Connection | None = None

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
        with self._guard:
            if self._writer is not None:
                self._writer.close()
                self._writer = None
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

    # -- Writes ------------------------------------------------------------

    def write_question(self, record: Record, method: str) -> Record:
        """Create or replace one Question, and read it back through the read path."""
        with self._writing() as connection:
            self._ensure_tags(connection, record["tags"])
            connection.execute(
                QUESTION_UPSERT,
                (
                    record["id"],
                    record["theme"],
                    record["slug"],
                    record["title"],
                    record["difficulty"],
                    record["type"],
                    record["prompt"],
                    json.dumps(list(record["answer_guide"]), ensure_ascii=False),
                    record["body_markdown"],
                    record["source_path"],
                    record["content_hash"],
                    record["updated_at"],
                ),
            )
            previous = self._replace_children(
                connection,
                "question_tags",
                "question_id",
                record["id"],
                record["tags"],
            )
            connection.execute("DELETE FROM question_sources WHERE question_id = ?", (record["id"],))
            connection.executemany(
                "INSERT INTO question_sources (question_id, position, url, source_type, verified_on)"
                " VALUES (?, ?, ?, ?, ?)",
                [
                    (record["id"], position, source["url"], source["source_type"], str(source["verified_on"]))
                    for position, source in enumerate(record["sources"])
                ],
            )
            self._index(connection, "question", record["id"], record["title"], record["prompt"], record["body_markdown"])
            self._refresh_theme(connection, str(record["theme"]))
            self._refresh_tags(connection, previous | set(record["tags"]))
            self._record_write(connection, "question", str(record["id"]), method, str(record["content_hash"]))
        return self._read_back(self.get_question, str(record["id"]))

    def delete_question(self, question_id: str, method: str) -> None:
        """Remove one Question, unless the corpus would be left inconsistent."""
        with self._writing() as connection:
            row = connection.execute(
                "SELECT theme FROM questions WHERE id = ?", (question_id,)
            ).fetchone()
            if row is None:  # pragma: no cover - the API answers 404 before calling
                return
            self._refuse_if_referenced(connection, question_id)
            tags = self._child_values(connection, "question_tags", "question_id", question_id)
            connection.execute("DELETE FROM questions WHERE id = ?", (question_id,))
            self._unindex(connection, "question", question_id)
            self._refresh_theme(connection, str(row["theme"]))
            self._refresh_tags(connection, tags)
            self._record_write(connection, "question", question_id, method, None)

    def write_lab(self, record: Record, method: str) -> Record:
        """Create or replace one Lab, and read it back through the read path."""
        with self._writing() as connection:
            self._ensure_tags(connection, record["tags"])
            connection.execute(
                LAB_UPSERT,
                (
                    record["id"],
                    record["theme"],
                    record["slug"],
                    record["title"],
                    record["difficulty"],
                    record["question_ref"],
                    record["why"],
                    json.dumps(list(record["checklist"]), ensure_ascii=False),
                    record["body_markdown"],
                    record["source_path"],
                    record["content_hash"],
                    record["updated_at"],
                ),
            )
            previous = self._replace_children(
                connection, "lab_tags", "lab_id", record["id"], record["tags"]
            )
            self._index(connection, "lab", record["id"], record["title"], record["why"], record["body_markdown"])
            self._refresh_theme(connection, str(record["theme"]))
            self._refresh_tags(connection, previous | set(record["tags"]))
            self._record_write(connection, "lab", str(record["id"]), method, str(record["content_hash"]))
        return self._read_back(self.get_lab, str(record["id"]))

    def delete_lab(self, lab_id: str, method: str) -> None:
        """Remove one Lab. Nothing in the corpus points at a Lab, so nothing blocks it."""
        with self._writing() as connection:
            row = connection.execute("SELECT theme FROM labs WHERE id = ?", (lab_id,)).fetchone()
            if row is None:  # pragma: no cover - the API answers 404 before calling
                return
            tags = self._child_values(connection, "lab_tags", "lab_id", lab_id)
            connection.execute("DELETE FROM labs WHERE id = ?", (lab_id,))
            self._unindex(connection, "lab", lab_id)
            self._refresh_theme(connection, str(row["theme"]))
            self._refresh_tags(connection, tags)
            self._record_write(connection, "lab", lab_id, method, None)

    def audit_trail(self, identifier: str | None = None) -> Sequence[Record]:
        """Every write this store has seen, oldest first.

        Read through the **read-only** connection, so asking for the trail can
        never create the table it reads: a store nobody has written to has no
        trail, and answering an empty one is the truth rather than a side effect.
        """
        with self._guard:
            connection = self._store.connection
            present = connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?", (AUDIT_TABLE,)
            ).fetchone()
            if not present:
                return ()
            statement = f"SELECT sequence, kind, id, method, written_at, content_hash FROM {AUDIT_TABLE}"
            parameters: list[Any] = []
            if identifier is not None:
                statement += " WHERE id = ?"
                parameters.append(identifier)
            statement += " ORDER BY sequence"
            return tuple(dict(row) for row in connection.execute(statement, parameters))

    # -- Writer internals --------------------------------------------------

    @contextmanager
    def _writing(self) -> Iterator[sqlite3.Connection]:
        """One write, as one transaction, under the lock every read is taken under.

        The lock is held for the whole transaction rather than per statement:
        half of an upsert is not a state any reader should be able to observe,
        and the transaction is a handful of indexed statements long.
        """
        with self._guard:
            connection = self._writable_connection()
            try:
                yield connection
            except BaseException:
                connection.rollback()
                raise
            connection.commit()

    def _writable_connection(self) -> sqlite3.Connection:
        """The second, writable handle on the store file, opened on first use."""
        if self._writer is not None:
            return self._writer
        path = self._store.path
        try:
            connection = sqlite3.connect(f"file:{path}?mode=rw", uri=True, check_same_thread=False)
        except sqlite3.Error as error:
            raise StoreIsReadOnly(
                f"the Content store at {path} cannot be opened for writing ({error})."
            ) from error
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(f"PRAGMA busy_timeout = {BUSY_TIMEOUT_MILLISECONDS}")
        try:
            # The audit table is created here rather than on demand because it
            # doubles as the writability probe: a store on a read-only mount
            # opens fine and only refuses when something tries to write it, and
            # finding that out on the first `CREATE TABLE` is better than
            # finding it out half way through a client's `PUT`.
            connection.executescript(AUDIT_DDL)
        except sqlite3.Error as error:
            connection.close()
            raise StoreIsReadOnly(
                f"the Content store at {path} opened but refuses to be written ({error}); "
                "this deployment serves the corpus read-only."
            ) from error
        self._writer = connection
        return connection

    def _read_back(self, read: Any, identifier: str) -> Record:
        """The record as the read path now sees it, never an echo of the request."""
        record = read(identifier)
        if record is None:  # pragma: no cover - a committed row that cannot be read
            raise RuntimeError(f"{identifier} was written but cannot be read back")
        return record

    def _ensure_tags(self, connection: sqlite3.Connection, tags: Any) -> None:
        """Give every tag a row before anything references it.

        `question_tags.tag` and `lab_tags.tag` are foreign keys into `tags`, and
        Ingest only lists the tags the corpus *uses* — so the first Question to
        carry a permitted but so-far-unused tag has to create its row, or the
        insert fails on a constraint the client did nothing wrong to hit.
        """
        connection.executemany(
            "INSERT OR IGNORE INTO tags (name, question_count, lab_count) VALUES (?, 0, 0)",
            [(tag,) for tag in tags],
        )

    def _replace_children(
        self, connection: sqlite3.Connection, table: str, column: str, identifier: str, values: Any
    ) -> set[str]:
        """Rewrite a record's ordered tag rows, returning the ones it had before.

        The previous set is what tells `_refresh_tags` which counts moved: a tag
        dropped by a `PUT` still needs its count corrected, and it is no longer
        reachable from the record.
        """
        previous = self._child_values(connection, table, column, identifier)
        connection.execute(f"DELETE FROM {table} WHERE {column} = ?", (identifier,))
        connection.executemany(
            f"INSERT INTO {table} ({column}, position, tag) VALUES (?, ?, ?)",
            [(identifier, position, tag) for position, tag in enumerate(values)],
        )
        return previous

    def _child_values(
        self, connection: sqlite3.Connection, table: str, column: str, identifier: str
    ) -> set[str]:
        return {
            row[0] for row in connection.execute(f"SELECT tag FROM {table} WHERE {column} = ?", (identifier,))
        }

    def _refuse_if_referenced(self, connection: sqlite3.Connection, question_id: str) -> None:
        """Refuse to delete a Question the corpus still points at.

        A Lab whose `question_ref` dangles and a learning-path step that names
        nothing are both corpus errors that Ingest refuses to build, so allowing
        the delete would produce a store that cannot be rebuilt from its own
        Markdown. Naming what points at it is the difference between a `409` a
        client can act on and one it can only retry.
        """
        labs = [
            row[0]
            for row in connection.execute(
                "SELECT id FROM labs WHERE question_ref = ? ORDER BY id", (question_id,)
            )
        ]
        paths = [
            row[0]
            for row in connection.execute(
                "SELECT DISTINCT path_slug FROM learning_path_steps WHERE question_id = ? ORDER BY path_slug",
                (question_id,),
            )
        ]
        if not labs and not paths:
            return
        references = [f"lab {identifier}" for identifier in labs] + [f"learning path {slug}" for slug in paths]
        raise RecordInUse(
            f"{question_id} cannot be deleted while the corpus still points at it: "
            f"{', '.join(references)}. Remove or repoint those first.",
            references,
        )

    def _index(
        self, connection: sqlite3.Connection, kind: str, identifier: str, title: Any, prompt: Any, body: Any
    ) -> None:
        """Keep the full-text index in step with the row it describes.

        A store built by a `sqlite3` without FTS5 carries no index at all, and
        the read path already answers search with a clear failure there; writing
        into a table that does not exist would turn that into an opaque one.
        """
        if not self._store.search_available:
            return
        self._unindex(connection, kind, identifier)
        connection.execute(
            f"INSERT INTO {FTS_TABLE} (kind, ref_id, title, prompt, body) VALUES (?, ?, ?, ?, ?)",
            (kind, identifier, title, prompt, body),
        )

    def _unindex(self, connection: sqlite3.Connection, kind: str, identifier: str) -> None:
        if not self._store.search_available:
            return
        connection.execute(
            f"DELETE FROM {FTS_TABLE} WHERE kind = ? AND ref_id = ?", (kind, identifier)
        )

    def _refresh_theme(self, connection: sqlite3.Connection, theme: str) -> None:
        """Recount one Theme from the rows, rather than adjusting a number by one.

        Ingest derives these counts from the corpus; a writer that incremented
        and decremented them would drift the first time a write failed half way,
        and the drift would be invisible until somebody compared a Theme page
        with a filtered list.
        """
        counts = {
            difficulty: connection.execute(
                "SELECT count(*) FROM questions WHERE theme = ? AND difficulty = ?", (theme, difficulty)
            ).fetchone()[0]
            for difficulty in DIFFICULTIES
        }
        labs = connection.execute(
            "SELECT count(*) FROM labs WHERE theme = ?", (theme,)
        ).fetchone()[0]
        connection.execute(
            "UPDATE themes SET question_count = ?, lab_count = ?, difficulty_counts = ? WHERE name = ?",
            (sum(counts.values()), labs, json.dumps(counts, sort_keys=True), theme),
        )

    def _refresh_tags(self, connection: sqlite3.Connection, tags: Any) -> None:
        """Recount the tags a write touched, and drop the ones nothing uses.

        `TAGS.md` is the permitted vocabulary and the `tags` table is the used
        one — Ingest publishes only tags the corpus actually carries, so that a
        client filtering by one gets something back. A tag whose last Question
        was just deleted goes back to being merely permitted.
        """
        for tag in sorted(tags):
            questions = connection.execute(
                "SELECT count(*) FROM question_tags WHERE tag = ?", (tag,)
            ).fetchone()[0]
            labs = connection.execute(
                "SELECT count(*) FROM lab_tags WHERE tag = ?", (tag,)
            ).fetchone()[0]
            if questions or labs:
                connection.execute(
                    "UPDATE tags SET question_count = ?, lab_count = ? WHERE name = ?",
                    (questions, labs, tag),
                )
            else:
                connection.execute("DELETE FROM tags WHERE name = ?", (tag,))

    def _record_write(
        self,
        connection: sqlite3.Connection,
        kind: str,
        identifier: str,
        method: str,
        content_hash: str | None,
    ) -> None:
        """Append one line to the write trail, inside the write's own transaction.

        Inside, not after: a trail that could record a write which then rolled
        back would send a Drift investigation looking for a change that never
        happened. A delete has no resulting hash, and says so with `NULL` rather
        than with the hash it used to have.
        """
        connection.execute(
            f"INSERT INTO {AUDIT_TABLE} (kind, id, method, written_at, content_hash)"
            " VALUES (?, ?, ?, ?, ?)",
            (kind, identifier, method, timestamp(), content_hash),
        )

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
