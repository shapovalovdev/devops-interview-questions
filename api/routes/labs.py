"""Labs: the five item operations, plus the list operation they do not share.

The spec below carries the two places a Lab genuinely differs from a Question.
`resolve_references` resolves the Question a Lab prepares a learner for, so a
Lab naming one that does not exist is refused rather than stored.
`delete_statuses` omits `409`: nothing in the corpus refers to a Lab, so its
DELETE cannot conflict and the contract documents no conflict for it.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Query

from api import writes
from api.guards import question_link, resolvable
from api.models import Difficulty, Lab, LabPage, LabPatch, LabWrite, SortKey
from api.helpers import problem_responses
from api.routes import StoreDep
from api.routes.resource import ResourceSpec, resource_routes
from api.store import LabQuery

#: Lab, and the two places it genuinely differs from a Question.
#:
#: `resolve_references` resolves the Question a Lab prepares a learner for, so
#: a Lab naming a Question that does not exist is refused rather than stored.
#: `delete_statuses` omits `409`: nothing in the corpus refers to a Lab, so its
#: DELETE cannot conflict and the contract documents no conflict for it.
RESOURCE = ResourceSpec(
    kind="Lab",
    segment="labs",
    tag="Labs",
    model=Lab,
    write_model=LabWrite,
    patch_model=LabPatch,
    read=lambda store, identifier: store.get_lab(identifier),
    write=lambda writer, record, method: writer.write_lab(record, method),
    remove=lambda writer, identifier, method: writer.delete_lab(identifier, method),
    build=lambda payload, vocabulary, resolved: writes.lab_record(payload, vocabulary, resolved),
    patch_fields=writes.LAB_PATCH_FIELDS,
    links=lambda store, identifier: question_link(
        store, str((store.get_lab(identifier) or {}).get("question_ref", ""))
    ),
    summaries={
        "create": "Create a Lab.",
        "get": "Read one Lab by its id.",
        "replace": "Replace a Lab wholesale.",
        "patch": "Change only the supplied fields of a Lab.",
        "delete": "Delete a Lab.",
    },
    delete_statuses=(401, 403, 404, 412, 428, 503),
    resolve_references=lambda store, payload: resolvable(
        store, str(payload.get("question_ref", ""))
    ),
)

router = APIRouter()
router.include_router(resource_routes(RESOURCE))


@router.get(
    "/api/v1/labs",
    operation_id="listLabs",
    tags=["Labs"],
    summary="List Labs, filtered, sorted, and paginated.",
    response_model=LabPage,
    responses=problem_responses(422, 500),
)
def list_labs(
    store: StoreDep,
    theme: str | None = None,
    difficulty: Difficulty | None = None,
    tag: str | None = None,
    question_ref: Annotated[
        str | None, Query(description="The id of the Question a Lab prepares a learner for.")
    ] = None,
    q: Annotated[str | None, Query(description="Free-text filter over title, prompt, and body.")] = None,
    limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
    offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
    sort: SortKey = SortKey.id,
) -> LabPage:
    page = store.list_labs(
        LabQuery(
            theme=theme,
            difficulty=difficulty.value if difficulty else None,
            tag=tag,
            question_ref=question_ref,
            q=q,
            sort=sort.value,
            limit=limit,
            offset=offset,
        )
    )
    return LabPage(items=page.items, total=page.total, limit=limit, offset=offset)

