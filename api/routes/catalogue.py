"""The derived catalogues, and search across both kinds of item.

Themes, tags, and learning paths are derived from the corpus rather than
authored, and are small enough to return whole -- which the contract records by
publishing no `limit` or `offset` for them.  Search is here rather than beside
Questions or Labs because one ranked list carries both kinds.

These six operations were the first moved out of `create_app()`, because the
compiled code objects showed they close over nothing: every one takes its store
through `Depends`, so the move is verbatim and the served schema is unchanged.
`tests/api/test_contract.py` is what proves that claim rather than asserting it.
"""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Header, Query, Response

from api.helpers import catalogue, conditional, item_responses, missing, problem_responses
from api.models import (
    ItemKind,
    Lab,
    LearningPath,
    LearningPathPage,
    Question,
    SearchHit,
    SearchPage,
    TagPage,
    Theme,
    ThemePage,
)
from api.routes import StoreDep
from api.store import SearchQuery, search_hit

router = APIRouter()


@router.get(
    "/api/v1/themes",
    operation_id="listThemes",
    tags=["Taxonomy"],
    summary="List every canonical Theme with its counts.",
    response_model=ThemePage,
    responses=problem_responses(500),
)
def list_themes(store: StoreDep) -> ThemePage:
    return catalogue(ThemePage, store.list_themes())


@router.get(
    "/api/v1/themes/{name}",
    operation_id="getTheme",
    tags=["Taxonomy"],
    summary="Read one Theme by its canonical name.",
    response_model=Theme,
    responses=item_responses(404, 500),
)
def get_theme(
    response: Response,
    store: StoreDep,
    name: str,
    if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
) -> Any:
    record = store.get_theme(name)
    if record is None:
        missing("Theme", name)
    return conditional(Theme.model_validate(record), record, if_none_match, response)


@router.get(
    "/api/v1/tags",
    operation_id="listTags",
    tags=["Taxonomy"],
    summary="List every tag with its counts.",
    response_model=TagPage,
    responses=problem_responses(500),
)
def list_tags(store: StoreDep) -> TagPage:
    return catalogue(TagPage, store.list_tags())


@router.get(
    "/api/v1/learning-paths",
    operation_id="listLearningPaths",
    tags=["Learning paths"],
    summary="List every learning path.",
    response_model=LearningPathPage,
    responses=problem_responses(500),
)
def list_learning_paths(store: StoreDep) -> LearningPathPage:
    return catalogue(LearningPathPage, store.list_learning_paths())


@router.get(
    "/api/v1/learning-paths/{slug}",
    operation_id="getLearningPath",
    tags=["Learning paths"],
    summary="Read one learning path, with its ordered steps.",
    response_model=LearningPath,
    responses=item_responses(404, 500),
)
def get_learning_path(
    response: Response,
    store: StoreDep,
    slug: str,
    if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
) -> Any:
    record = store.get_learning_path(slug)
    if record is None:
        missing("learning path", slug)
    return conditional(LearningPath.model_validate(record), record, if_none_match, response)


@router.get(
    "/api/v1/search",
    operation_id="search",
    tags=["Search"],
    summary="Search Questions and Labs together, ranked by relevance.",
    response_model=SearchPage,
    responses=problem_responses(422, 500),
)
def search(
    store: StoreDep,
    q: Annotated[str, Query(min_length=1, description="The search text; it is required.")],
    kind: Annotated[
        ItemKind | None, Query(description="Restrict the result to one kind of item.")
    ] = None,
    limit: Annotated[int, Query(ge=1, le=200, description="Maximum number of items in the page.")] = 50,
    offset: Annotated[int, Query(ge=0, description="Number of items to skip before the page starts.")] = 0,
) -> SearchPage:
    page = store.search(
        SearchQuery(q=q, kind=kind.value if kind else None, limit=limit, offset=offset)
    )
    # One ranked list carries two kinds of item, so the hit says which it is
    # and the model is chosen from that rather than guessed from the fields:
    # a Question and a Lab overlap enough that a union would sometimes pick
    # the wrong one and silently drop what only the other has.
    items = []
    for hit in page.items:
        kind, score, item = search_hit(hit)
        model = Question if kind == ItemKind.question.value else Lab
        items.append(SearchHit(kind=kind, score=score, item=model.model_validate(item)))
    return SearchPage(items=items, total=page.total, limit=limit, offset=offset)
