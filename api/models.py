"""Pydantic models mirroring the schemas in `api/openapi.yaml`.

The contract is the source of truth for the wire format; these models exist so
FastAPI can validate and serialize it, and their class names are deliberately
the contract's `components/schemas` names — FastAPI derives the generated
schema's component names from them, and `tests/api/test_contract.py` compares
the `$ref` of every request body against the hand-written file.

These models live on the *outside* of the service. They are never handed to the
Store: plain mappings cross that seam (see `api/store.py`), so the Content store
never has to import Pydantic.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Literal

from pydantic import BaseModel


class Difficulty(str, Enum):
    junior = "junior"
    middle = "middle"
    senior = "senior"
    staff = "staff"


class QuestionType(str, Enum):
    theory = "theory"
    scenario = "scenario"
    troubleshooting = "troubleshooting"


class ItemKind(str, Enum):
    question = "question"
    lab = "lab"


class SortKey(str, Enum):
    """The sort vocabulary the epic pins, ascending and descending.

    Member names cannot be `-id`, so the descending members carry a `_desc`
    suffix; only the *values* reach the wire, and those are what the contract
    enumerates.
    """

    id = "id"
    id_desc = "-id"
    title = "title"
    title_desc = "-title"
    difficulty = "difficulty"
    difficulty_desc = "-difficulty"
    updated_at = "updated_at"
    updated_at_desc = "-updated_at"


class HealthReport(BaseModel):
    status: Literal["ok"]
    service: str
    contract_version: str


class Source(BaseModel):
    url: str
    source_type: str
    verified_on: date


class Question(BaseModel):
    id: str
    theme: str
    slug: str
    title: str
    difficulty: Difficulty
    type: QuestionType
    tags: list[str]
    sources: list[Source]
    prompt: str
    answer_guide: list[str]
    body_markdown: str
    source_path: str
    content_hash: str
    updated_at: datetime


class QuestionWrite(BaseModel):
    theme: str
    slug: str
    title: str
    difficulty: Difficulty
    type: QuestionType
    tags: list[str]
    sources: list[Source]
    prompt: str
    answer_guide: list[str]
    body_markdown: str


class QuestionPatch(BaseModel):
    title: str | None = None
    difficulty: Difficulty | None = None
    type: QuestionType | None = None
    tags: list[str] | None = None
    sources: list[Source] | None = None
    prompt: str | None = None
    answer_guide: list[str] | None = None
    body_markdown: str | None = None


class Lab(BaseModel):
    id: str
    theme: str
    slug: str
    title: str
    difficulty: Difficulty
    tags: list[str]
    question_ref: str
    why: str
    checklist: list[str]
    body_markdown: str
    source_path: str
    content_hash: str
    updated_at: datetime


class LabWrite(BaseModel):
    theme: str
    slug: str
    title: str
    difficulty: Difficulty
    tags: list[str]
    question_ref: str
    why: str
    checklist: list[str]
    body_markdown: str


class LabPatch(BaseModel):
    title: str | None = None
    difficulty: Difficulty | None = None
    tags: list[str] | None = None
    question_ref: str | None = None
    why: str | None = None
    checklist: list[str] | None = None
    body_markdown: str | None = None


class Theme(BaseModel):
    name: str
    state: str
    question_count: int
    lab_count: int
    difficulty_counts: dict[str, int]


class Tag(BaseModel):
    name: str
    question_count: int
    lab_count: int


class LearningPathStep(BaseModel):
    question_id: str
    why: str


class LearningPath(BaseModel):
    slug: str
    title: str
    description: str
    steps: list[LearningPathStep]


class SearchHit(BaseModel):
    kind: ItemKind
    score: float
    item: Question | Lab


class Page(BaseModel):
    """The envelope every list response shares."""

    total: int
    limit: int
    offset: int


class QuestionPage(Page):
    items: list[Question]


class LabPage(Page):
    items: list[Lab]


class ThemePage(Page):
    items: list[Theme]


class TagPage(Page):
    items: list[Tag]


class LearningPathPage(Page):
    items: list[LearningPath]


class SearchPage(Page):
    items: list[SearchHit]


class ProblemDetail(BaseModel):
    field: str
    message: str


class Problem(BaseModel):
    """An RFC 9457 problem document. It never carries a stack trace."""

    type: str
    title: str
    status: int
    detail: str
    instance: str
    errors: list[ProblemDetail] | None = None
