"""The Store seam: how the Content API asks the Content store for records.

The service codes against the `Store` protocol below and never against a
particular store. Two implementations satisfy it: `api/content.py` adapts the
SQLite Content store in `contentdb/`, which is what a deployment serves, and
`api/testing.py` holds an in-memory fake for the tests and the demo entrypoint.
Neither is named anywhere in `api/app.py`.

Two rules make that swap possible, and they are the reason this module looks the
way it does.

**Only plain data crosses the seam.** A query dataclass goes in; a `Page` of
plain mappings comes out. The mappings are keyed by the field names the epic
pins for a Question and a Lab, and their values are JSON-shaped — dates and
timestamps are ISO 8601 strings, exactly as SQLite will hand them over. No
Pydantic model appears anywhere below, so a store implementation never has to
learn the API's serialization layer.

**This module imports nothing outside the standard library.** `contentdb` is
standard-library only — it runs inside the static site build, where nothing is
installed — so an implementation that had to import `api/` to satisfy the
protocol could not exist. Because the protocol is structural, `contentdb`
does not have to import this module either: it can mirror `QuestionQuery` and
`Page` with its own dataclasses, or return any object carrying the same fields.
A test in `tests/api/test_store.py` imports this module in a clean interpreter
and asserts that Pydantic never gets pulled in, so the rule cannot rot.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable

#: One Question, Lab, Theme, tag, or learning path as the store hands it over:
#: a plain mapping keyed by the epic's field names.
Record = Mapping[str, Any]

#: The sort keys the contract accepts, without the optional `-` prefix.
SORT_KEYS = ("id", "title", "difficulty", "updated_at")

#: The default sort. `id` is unique across the corpus, so paging through a list
#: with a stable `limit`/`offset` visits every item exactly once. A default of
#: `-updated_at` would not: two Questions updated in the same second may swap
#: places between two requests and a client would skip one and see another
#: twice.
DEFAULT_SORT = "id"


@dataclass(frozen=True)
class QuestionQuery:
    """Everything `GET /api/v1/questions` asks the store for, in one value."""

    theme: str | None = None
    difficulty: str | None = None
    type: str | None = None
    tag: str | None = None
    q: str | None = None
    sort: str = DEFAULT_SORT
    limit: int = 50
    offset: int = 0


@dataclass(frozen=True)
class LabQuery:
    """Everything `GET /api/v1/labs` asks the store for. Slice 3 implements it."""

    theme: str | None = None
    difficulty: str | None = None
    tag: str | None = None
    question_ref: str | None = None
    q: str | None = None
    sort: str = DEFAULT_SORT
    limit: int = 50
    offset: int = 0


@dataclass(frozen=True)
class SearchQuery:
    """Everything `GET /api/v1/search` asks the store for.

    A store answers it with `Page` of *hit* mappings rather than of items:
    `{"kind": "question" | "lab", "score": float, "item": Record}`, mirroring the
    contract's `SearchHit`. The nesting is what lets one ranked list carry two
    kinds of item without the API guessing which it is holding, and `score` is
    the store's own relevance — the contract defines it as comparable only
    within one response, so a store may derive it from rank.
    """

    q: str
    kind: str | None = None
    limit: int = 50
    offset: int = 0


#: The keys a search hit carries across the seam, mirroring `SearchHit` in the
#: contract. They are named here, not in `api/app.py`, because this module is
#: what a store implementation reads to learn what it owes.
SEARCH_HIT_FIELDS = ("kind", "score", "item")


class StoreContractViolation(RuntimeError):
    """Raised when a store answers in a shape this seam does not describe.

    The `Store` protocol is `runtime_checkable`, which means `isinstance` checks
    that the methods *exist* and nothing about what they return. An object can
    therefore pass the check and still hand back a tuple where a `Page` was
    promised, or a bare record where a hit was. That gap is not hypothetical: it
    shipped, as a `KeyError: 'score'` on every search, when a store was wired in
    without the adapter that reshapes it. This exception exists so the next
    occurrence names the seam and the fix instead of a missing dictionary key.
    """


def is_page(value: object) -> bool:
    """Whether a store's answer is a `Page` — anything carrying items and a total."""
    return hasattr(value, "items") and hasattr(value, "total")


def search_hit(record: Record) -> tuple[str, float, Record]:
    """Unpack one search hit, or say precisely how the store broke the seam."""
    absent = [field for field in SEARCH_HIT_FIELDS if field not in record]
    if absent:
        raise StoreContractViolation(
            f"a search hit is missing {absent}: the seam carries "
            f"{{'kind': 'question' | 'lab', 'score': float, 'item': record}}, and this store "
            f"answered with keys {sorted(record)}. A store whose search returns bare records "
            "has to be adapted before it reaches the service — see api/content.py."
        )
    return str(record["kind"]), float(record["score"]), record["item"]


class InvalidQuery(ValueError):
    """Raised when free text is not something the store can parse as a query.

    It is the store's way of saying "this is the client's fault, not mine": the
    API answers it with the contract's `422` rather than the `500` a generic
    failure earns. Everything else a store raises is a fault, and stays one.
    """


@dataclass(frozen=True)
class Page:
    """A window onto a result set, plus how large the whole result set is.

    `total` counts the matches *before* `limit` and `offset` are applied, which
    is what the list envelope reports and what lets a client know there is more
    to fetch.
    """

    items: Sequence[Record]
    total: int


class RecordInUse(RuntimeError):
    """Raised when a record cannot be deleted because something still points at it.

    Deleting a Question that a Lab prepares a learner for, or that a learning
    path walks through, would leave the corpus in a state the validators reject
    — a dangling `question_ref` is a build failure, not a tidy-up job for later.
    The store refuses, names what is pointing, and the API answers `409`.
    """

    def __init__(self, message: str, references: Sequence[str] = ()):
        super().__init__(message)
        self.references = tuple(references)


class StoreIsReadOnly(RuntimeError):
    """Raised when a store that can only read is asked to write.

    It is not a fault and not the client's mistake: it is a fact about how this
    deployment was configured, which the contract publishes as `503`. A store
    that does not implement the write seam at all lands here too, rather than as
    an `AttributeError` a client would see as `500`.
    """


@runtime_checkable
class Store(Protocol):
    """Every read the Content API performs goes through this protocol.

    Writes are a separate protocol, `WritableStore`, because a store that only
    reads is a legitimate deployment: with no Write credential configured the
    service serves the corpus and refuses every mutation, and nothing in the
    read surface should have to grow a method it never calls to say so.
    """

    def list_questions(self, query: QuestionQuery) -> Page: ...

    def get_question(self, question_id: str) -> Record | None: ...

    def list_labs(self, query: LabQuery) -> Page: ...

    def get_lab(self, lab_id: str) -> Record | None: ...

    def list_themes(self) -> Page: ...

    def get_theme(self, name: str) -> Record | None: ...

    def list_tags(self) -> Page: ...

    def list_learning_paths(self) -> Page: ...

    def get_learning_path(self, slug: str) -> Record | None: ...

    def search(self, query: SearchQuery) -> Page: ...


@runtime_checkable
class WritableStore(Protocol):
    """Every write the Content API performs goes through this protocol.

    Two verbs cover the four HTTP methods, because at the level of the store
    there are only two things that can happen to a record: it is written, or it
    is gone. `POST`, `PUT`, and `PATCH` differ in what the API checks *before*
    it calls — a duplicate id, a missing id, a stale precondition — and by the
    time a record reaches here those questions have been answered and it is one
    complete, validated record either way.

    `method` is the HTTP method the write arrived as. It is carried down rather
    than inferred because it is what the audit trail records: "this id changed"
    is much less useful to a Drift investigation than "this id was replaced by a
    `PUT` at this time and ended at this hash".

    A write returns the record as the store now holds it, read back rather than
    echoed, so the response a client gets and the answer a later `GET` gives
    cannot disagree.
    """

    def write_question(self, record: Record, method: str) -> Record: ...

    def delete_question(self, question_id: str, method: str) -> None: ...

    def write_lab(self, record: Record, method: str) -> Record: ...

    def delete_lab(self, lab_id: str, method: str) -> None: ...

    def audit_trail(self, identifier: str | None = None) -> Sequence[Record]: ...


def writable(store: object) -> "WritableStore":
    """The store as a writer, or the reason this deployment cannot write.

    `isinstance` against a `runtime_checkable` protocol only proves the methods
    exist, which is exactly the guarantee needed here: the alternative is an
    `AttributeError` in the middle of a request, reported to the client as a
    `500` that blames the service for a deployment choice.
    """
    if not isinstance(store, WritableStore):
        raise StoreIsReadOnly(
            f"{type(store).__module__}.{type(store).__qualname__} implements the read seam but not "
            "the write seam in api/store.py, so this deployment serves the corpus read-only."
        )
    return store
