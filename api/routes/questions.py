"""Questions: the five item operations, plus the one that is not shared.

`list` stays hand-written here rather than joining the ResourceSpec. A Question
is filtered by `type` and a Lab by `question_ref`, so the two list operations
say genuinely different things; folding them into a spec would mean describing
each kind's query surface in data instead of in a signature, which is more
indirection to express a real difference rather than a shared one.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Query

from api import writes
from api.guards import lab_links
from api.models import Difficulty, Question, QuestionPage, QuestionPatch, QuestionType, QuestionWrite, SortKey
from api.helpers import problem_responses
from api.routes import StoreDep
from api.routes.resource import ResourceSpec, resource_routes
from api.store import QuestionQuery

#: Question, expressed as the differences from any other resource kind.
#: `resolve_references` is unset: a Question points at nothing that has to be
#: resolved before its record is built. A Lab does, which is why the spec models
#: that as an option rather than pretending the two kinds are identical.
RESOURCE = ResourceSpec(
    kind="Question",
    segment="questions",
    tag="Questions",
    model=Question,
    write_model=QuestionWrite,
    patch_model=QuestionPatch,
    read=lambda store, identifier: store.get_question(identifier),
    write=lambda writer, record, method: writer.write_question(record, method),
    remove=lambda writer, identifier, method: writer.delete_question(identifier, method),
    build=lambda payload, vocabulary: writes.question_record(payload, vocabulary),
    patch_fields=writes.QUESTION_PATCH_FIELDS,
    links=lambda store, identifier: lab_links(store, identifier),
    summaries={
        "create": "Create a Question.",
        "get": "Read one Question by its id.",
        "replace": "Replace a Question wholesale.",
        "patch": "Change only the supplied fields of a Question.",
        "delete": "Delete a Question.",
    },
)

router = APIRouter()
router.include_router(resource_routes(RESOURCE))


@router.get(
    "/api/v1/questions",
    operation_id="listQuestions",
    tags=["Questions"],
    summary="List Questions, filtered, sorted, and paginated.",
    response_model=QuestionPage,
    responses=problem_responses(422, 500),
)
def list_questions(
    store: StoreDep,
    theme: Annotated[str | None, Query(description="Canonical Theme that owns the Question.")] = None,
    difficulty: Difficulty | None = None,
    type_: Annotated[
        QuestionType | None, Query(alias="type", description="The interview format of the Question.")
    ] = None,
    tag: Annotated[
        str | None, Query(description="A single tag; a Question matches when it carries the tag.")
    ] = None,
    q: Annotated[str | None, Query(description="Free-text filter over title, prompt, and body.")] = None,
    limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
    offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
    sort: SortKey = SortKey.id,
) -> QuestionPage:
    page = store.list_questions(
        QuestionQuery(
            theme=theme,
            difficulty=difficulty.value if difficulty else None,
            type=type_.value if type_ else None,
            tag=tag,
            q=q,
            sort=sort.value,
            limit=limit,
            offset=offset,
        )
    )
    # This is the seam: plain mappings go in, typed models come out. If the
    # store hands back something the contract cannot describe, the
    # validation failure surfaces as a 500 rather than as a malformed body.
    return QuestionPage(items=page.items, total=page.total, limit=limit, offset=offset)

# The five item operations -- create, read, replace, patch, delete -- are
# generated from a ResourceSpec in api/routes/resource.py, so the ordered
# write check (503, 401, 403, 404, 428, 412, 422) has one implementation.
# `list` stays here: a Question is filtered by `type` and a Lab by
# `question_ref`, which is real kind-specific query surface rather than
# duplicated logic. tests/api/test_write_parity.py holds both kinds to the
# same answers, and tests/api/test_contract.py holds the served schema
# byte-identical to api/openapi.yaml.
