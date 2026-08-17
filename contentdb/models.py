"""The shapes that cross the Content store's read seam.

Only two kinds of thing cross it: a frozen query dataclass going in, and plain
mappings coming out, wrapped in :class:`Page` when the result is a list.

That asymmetry is deliberate, and it is the seam's whole point. A *query* is a
closed set of named options, so a dataclass documents it, defaults it, and lets
a caller build one field at a time. A *record* is an open bag of content fields
that the Content API will re-shape into its own Pydantic models anyway; handing
it over as a mapping keyed by the epic's field names
(`docs/issues/0000-epic-content-api.md`) means slice 3 adapts one dictionary
instead of unwrapping an object it cannot import, and a fake `Store` used in an
API test is a literal `{"id": "kubernetes/...", ...}` written inline.

`contentdb` therefore never imports from `api/`, and `api/` never needs a
`contentdb` type in a response model.

An earlier draft of this module also defined `Question`, `Lab`, `Theme`, `Tag`,
and `LearningPath` record dataclasses. They were removed once the coordinator
pinned mappings as the seam: two representations of the same record, one of
them unused, is how a contract starts drifting.
"""

from __future__ import annotations

from dataclasses import dataclass, field


DEFAULT_LIMIT = 50
MAXIMUM_LIMIT = 200

#: `sort` values the list queries accept, each optionally prefixed `-`.
SORT_FIELDS = ("id", "title", "difficulty", "updated_at")


@dataclass(frozen=True)
class QuestionQuery:
    """Filters, ordering, and a window over the Questions in the store.

    Every field is optional and independent; a filter left `None` is not
    applied, and combinations are conjunctive. `q` runs the full-text index
    rather than a `LIKE` scan, so it needs the FTS5 table Ingest builds.
    """

    theme: str | None = None
    difficulty: str | None = None
    type: str | None = None
    tag: str | None = None
    q: str | None = None
    sort: str = "id"
    limit: int = DEFAULT_LIMIT
    offset: int = 0


@dataclass(frozen=True)
class LabQuery:
    """The same window over Labs, which filter by `question_ref` instead of `type`."""

    theme: str | None = None
    difficulty: str | None = None
    tag: str | None = None
    question_ref: str | None = None
    q: str | None = None
    sort: str = "id"
    limit: int = DEFAULT_LIMIT
    offset: int = 0


@dataclass(frozen=True)
class SearchQuery:
    """A full-text search across Questions and Labs together.

    `q` has no default because a search without one is meaningless — the epic
    documents its absence as a `422`, which is the API's job to raise, not the
    store's to invent an answer for.
    """

    q: str
    kind: str | None = None
    limit: int = DEFAULT_LIMIT
    offset: int = 0


@dataclass(frozen=True)
class Page:
    """The list envelope: this window's records, and the size of the whole result.

    `total` counts every record the filters match, not the ones in `items`, so
    a caller can page without asking twice. An `offset` past the end is a valid
    request with an empty answer: `items` is empty and `total` still reports the
    truth.
    """

    items: tuple[dict, ...] = field(default_factory=tuple)
    total: int = 0
    limit: int = DEFAULT_LIMIT
    offset: int = 0
