"""The Content store's read interface — the seam the Content API sits on.

`Store` answers the questions the epic's read endpoints ask, and nothing else.
It opens the database **read-only**: writes arrive through the API and are
rendered back to Markdown by Export, so a component whose job is reading has no
business holding a writable handle on a derived artifact.

Everything it returns is a plain mapping keyed by the epic's field names, or a
:class:`~contentdb.models.Page` of them. Nothing in `api/` is imported here and
nothing from here needs to be imported there — slice 3 adapts dictionaries into
its own response models, and an API test can fake this class with a literal.

Three details a caller should know:

**Lists are paginated, catalogues are not.** `list_questions`, `list_labs`, and
`search` take a window and return a `Page`, because their results grow with the
corpus. Themes, Tags, and learning paths are bounded catalogues the API exposes
without `limit` or `offset`, so they return a tuple and no envelope is invented
for them.

**`sort` is validated, filters are not.** An unsupported sort key is a
programming or request error and raises; an unknown *value* — `theme=atlantis`
— is a legitimate query with an empty answer, and returns one. The API turns
the former into a `422` and serves the latter as an empty list.

**Search needs FTS5.** If the store was built by a SQLite without it, every
search path raises :class:`SearchUnavailable` naming the cause instead of
quietly degrading to a `LIKE` scan that would rank differently and mislead.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .models import MAXIMUM_LIMIT, LabQuery, Page, QuestionQuery, SearchQuery
from .schema import FTS_TABLE


#: Ordering by difficulty has to follow the ladder, or `junior` sorts above
#: `staff` and a "hardest first" listing is quietly wrong.
DIFFICULTY_RANK = "CASE difficulty WHEN 'junior' THEN 0 WHEN 'middle' THEN 1 WHEN 'senior' THEN 2 ELSE 3 END"
SORT_EXPRESSIONS = {"id": "id", "title": "title", "difficulty": DIFFICULTY_RANK, "updated_at": "updated_at"}

QUESTION_COLUMNS = (
    "id, theme, slug, title, difficulty, type, prompt, answer_guide, body_markdown,"
    " source_path, content_hash, updated_at"
)
LAB_COLUMNS = (
    "id, theme, slug, title, difficulty, question_ref, why, checklist, body_markdown,"
    " source_path, content_hash, updated_at"
)
#: `kind` and `ref_id` are UNINDEXED but still occupy a bm25 weight slot. A
#: title hit is the strongest signal a reader has, a `prompt`/`why` hit the next.
BM25_WEIGHTS = "0.0, 0.0, 10.0, 5.0, 1.0"


class SearchUnavailable(RuntimeError):
    """Raised when the store carries no full-text index to search."""


class SearchError(ValueError):
    """Raised when a search string is not valid FTS5 query syntax."""


class Store:
    """Read access to one Content store file."""

    def __init__(self, path: Path | str):
        path = Path(path)
        if not path.is_file():
            raise FileNotFoundError(f"no Content store at {path}; run `python -m contentdb.ingest` first")
        self.path = path
        self.connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.search_available = bool(
            self.connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?", (FTS_TABLE,)
            ).fetchone()
        )

    def __enter__(self) -> "Store":
        return self

    def __exit__(self, *_) -> None:
        self.close()

    def close(self) -> None:
        self.connection.close()

    # -- Questions ---------------------------------------------------------

    def get_question(self, question_id: str) -> dict | None:
        row = self.connection.execute(
            f"SELECT {QUESTION_COLUMNS} FROM questions WHERE id = ?", (question_id,)
        ).fetchone()
        return self._question(row) if row else None

    def list_questions(self, query: QuestionQuery | None = None) -> Page:
        query = query or QuestionQuery()
        where, parameters = self._filters(
            [
                ("theme = ?", query.theme),
                ("difficulty = ?", query.difficulty),
                ("type = ?", query.type),
                ("id IN (SELECT question_id FROM question_tags WHERE tag = ?)", query.tag),
                (self._matching("question"), query.q),
            ]
        )
        return self._page("questions", QUESTION_COLUMNS, where, parameters, query, self._question)

    # -- Labs --------------------------------------------------------------

    def get_lab(self, lab_id: str) -> dict | None:
        row = self.connection.execute(
            f"SELECT {LAB_COLUMNS} FROM labs WHERE id = ?", (lab_id,)
        ).fetchone()
        return self._lab(row) if row else None

    def list_labs(self, query: LabQuery | None = None) -> Page:
        query = query or LabQuery()
        where, parameters = self._filters(
            [
                ("theme = ?", query.theme),
                ("difficulty = ?", query.difficulty),
                ("question_ref = ?", query.question_ref),
                ("id IN (SELECT lab_id FROM lab_tags WHERE tag = ?)", query.tag),
                (self._matching("lab"), query.q),
            ]
        )
        return self._page("labs", LAB_COLUMNS, where, parameters, query, self._lab)

    # -- Catalogues --------------------------------------------------------

    def list_themes(self) -> tuple[dict, ...]:
        rows = self.connection.execute(
            "SELECT name, state, question_count, lab_count, difficulty_counts FROM themes ORDER BY name"
        ).fetchall()
        return tuple(self._theme(row) for row in rows)

    def get_theme(self, name: str) -> dict | None:
        row = self.connection.execute(
            "SELECT name, state, question_count, lab_count, difficulty_counts FROM themes WHERE name = ?",
            (name,),
        ).fetchone()
        return self._theme(row) if row else None

    def list_tags(self) -> tuple[dict, ...]:
        rows = self.connection.execute(
            "SELECT name, question_count, lab_count FROM tags ORDER BY name"
        ).fetchall()
        return tuple(dict(row) for row in rows)

    def list_learning_paths(self) -> tuple[dict, ...]:
        rows = self.connection.execute(
            "SELECT slug, title, description, prerequisites FROM learning_paths ORDER BY slug"
        ).fetchall()
        return tuple(self._learning_path(row) for row in rows)

    def get_learning_path(self, slug: str) -> dict | None:
        row = self.connection.execute(
            "SELECT slug, title, description, prerequisites FROM learning_paths WHERE slug = ?", (slug,)
        ).fetchone()
        return self._learning_path(row) if row else None

    # -- Search ------------------------------------------------------------

    def search(self, query: SearchQuery) -> Page:
        """Rank Questions and Labs together against one FTS5 query."""
        self._require_search()
        limit, offset = self._window(query.limit, query.offset)
        clauses = [f"{FTS_TABLE} MATCH ?"]
        parameters: list[object] = [query.q]
        if query.kind is not None:
            clauses.append("kind = ?")
            parameters.append(query.kind)
        where = " AND ".join(clauses)

        total = self._run(f"SELECT count(*) FROM {FTS_TABLE} WHERE {where}", parameters).fetchone()[0]
        rows = self._run(
            f"SELECT kind, ref_id, snippet({FTS_TABLE}, 4, '', '', '…', 24) AS snippet"
            f" FROM {FTS_TABLE} WHERE {where}"
            f" ORDER BY bm25({FTS_TABLE}, {BM25_WEIGHTS}), ref_id LIMIT ? OFFSET ?",
            [*parameters, limit, offset],
        ).fetchall()
        return Page(items=tuple(self._hit(row) for row in rows), total=total, limit=limit, offset=offset)

    # -- Internals ---------------------------------------------------------

    def _require_search(self) -> None:
        if not self.search_available:
            raise SearchUnavailable(
                f"this Content store carries no {FTS_TABLE} index: it was built by a sqlite3 "
                "without FTS5 support, so full-text search is unavailable"
            )

    def _matching(self, kind: str) -> str:
        return (
            f"id IN (SELECT ref_id FROM {FTS_TABLE} WHERE {FTS_TABLE} MATCH ? AND kind = '{kind}')"
        )

    def _filters(self, candidates: list[tuple[str, object]]) -> tuple[str, list[object]]:
        clauses, parameters = [], []
        for clause, value in candidates:
            if value is None:
                continue
            if FTS_TABLE in clause:
                self._require_search()
            clauses.append(clause)
            parameters.append(value)
        return (" AND ".join(clauses) or "1", parameters)

    def _window(self, limit: int, offset: int) -> tuple[int, int]:
        if limit < 0 or offset < 0:
            raise ValueError(f"limit and offset cannot be negative, got limit={limit}, offset={offset}")
        return min(limit, MAXIMUM_LIMIT), offset

    def _order(self, sort: str) -> str:
        descending = sort.startswith("-")
        field = sort[1:] if descending else sort
        if field not in SORT_EXPRESSIONS:
            raise ValueError(f"cannot sort by {sort!r}; supported keys are {sorted(SORT_EXPRESSIONS)}")
        direction = "DESC" if descending else "ASC"
        # `id` breaks every tie, so a window never skips or repeats a record.
        return f"{SORT_EXPRESSIONS[field]} {direction}, id {direction}"

    def _page(self, table, columns, where, parameters, query, adapt) -> Page:
        limit, offset = self._window(query.limit, query.offset)
        order = self._order(query.sort)
        total = self._run(f"SELECT count(*) FROM {table} WHERE {where}", parameters).fetchone()[0]
        rows = self._run(
            f"SELECT {columns} FROM {table} WHERE {where} ORDER BY {order} LIMIT ? OFFSET ?",
            [*parameters, limit, offset],
        ).fetchall()
        return Page(items=tuple(adapt(row) for row in rows), total=total, limit=limit, offset=offset)

    def _run(self, statement: str, parameters) -> sqlite3.Cursor:
        """Run a statement, turning FTS5 syntax complaints into a clear error.

        SQLite reports a malformed `MATCH` string as a generic `OperationalError`,
        which a caller would otherwise have to string-match to tell apart from a
        real database fault.
        """
        try:
            return self.connection.execute(statement, parameters)
        except sqlite3.OperationalError as error:
            if "fts5" in str(error).lower() or "MATCH" in statement:
                raise SearchError(f"invalid search query: {error}") from error
            raise

    def _tags(self, table: str, column: str, identifier: str) -> list[str]:
        """A record's Tags in the order its Markdown file lists them.

        Author order is not decoration: Export has to reproduce the source file
        byte for byte, so the store keeps the position rather than normalising
        to alphabetical."""
        return [
            row[0]
            for row in self.connection.execute(
                f"SELECT tag FROM {table} WHERE {column} = ? ORDER BY position", (identifier,)
            )
        ]

    def _question(self, row: sqlite3.Row) -> dict:
        record = dict(row)
        record["answer_guide"] = json.loads(record["answer_guide"])
        record["tags"] = self._tags("question_tags", "question_id", record["id"])
        record["sources"] = [
            dict(source)
            for source in self.connection.execute(
                "SELECT url, source_type, verified_on FROM question_sources"
                " WHERE question_id = ? ORDER BY position",
                (record["id"],),
            )
        ]
        return record

    def _lab(self, row: sqlite3.Row) -> dict:
        record = dict(row)
        record["checklist"] = json.loads(record["checklist"])
        record["tags"] = self._tags("lab_tags", "lab_id", record["id"])
        return record

    def _theme(self, row: sqlite3.Row) -> dict:
        record = dict(row)
        record["difficulty_counts"] = json.loads(record["difficulty_counts"])
        return record

    def _learning_path(self, row: sqlite3.Row) -> dict:
        record = dict(row)
        record["prerequisites"] = json.loads(record["prerequisites"])
        record["steps"] = [
            dict(step)
            for step in self.connection.execute(
                "SELECT question_id, why FROM learning_path_steps WHERE path_slug = ? ORDER BY position",
                (record["slug"],),
            )
        ]
        return record

    def _hit(self, row: sqlite3.Row) -> dict:
        """One search result: enough to render a hit list without a second call."""
        kind, identifier, snippet = row["kind"], row["ref_id"], row["snippet"]
        table = "questions" if kind == "question" else "labs"
        found = self.connection.execute(
            f"SELECT title, theme FROM {table} WHERE id = ?", (identifier,)
        ).fetchone()
        return {
            "kind": kind,
            "id": identifier,
            "theme": found["theme"] if found else "",
            "title": found["title"] if found else "",
            "snippet": snippet,
        }
