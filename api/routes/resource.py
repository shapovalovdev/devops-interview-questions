"""One implementation of the item operations, parameterised by resource kind.

Question and Lab publish the same five item operations -- create, read, replace,
patch, delete -- and the same ordered write check:

    503 -> 401 -> 403 -> 404 -> 428 -> 412 -> 422

`api/app.py` calls that order part of the contract.  It used to be written out
twice, once per kind, in two blocks that differed only in the kind label, the
store methods, the record builder, and the response models.  Nothing compared
them, so a correction to one could land nowhere near the other; `#182` filed
`tests/api/test_write_parity.py` first to make that visible, and this module is
what makes it impossible.

**The list operation is deliberately not here.**  It is the one operation whose
two versions genuinely differ: a Question is filtered by `type`, a Lab by
`question_ref`.  That is kind-specific query surface, not duplicated logic, and
folding it into a spec would mean describing each kind's filters in data instead
of in a signature -- more indirection to express a real difference.  The five
operations below are the ones where the two kinds said the same thing twice.

**Why the annotations are assigned rather than declared.**  FastAPI builds the
OpenAPI schema from a handler's type hints, and a generator cannot write
`body: QuestionWrite` when the model arrives as a parameter.  Each handler is
therefore defined with a placeholder and has `__annotations__` set from the spec
before the route decorator sees it, which is the same information reaching
FastAPI by a different road.  The proof that it is the same is
`tests/api/test_contract.py`: the served schema must stay byte-identical to
`api/openapi.yaml`, which is authored by hand and is the source of truth.

The write guards come from `api/guards.py`.  They were briefly passed in as
arguments instead, purely because they lived in `api/app.py`, which imports this
module -- an import-cycle workaround dressed as a design.  Moving them below
both callers removed the cycle and the ceremony with it.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Annotated, Any

from fastapi import APIRouter, Header, HTTPException, Request, Response
from pydantic import BaseModel

from api.guards import (
    require_precondition,
    require_same_identity,
    require_write_access,
    write_responses,
    written,
)
from api.helpers import conditional, item_responses, missing, problem_responses
from api.routes import StoreDep, VocabularyDep
from api.store import Record, Store, WritableStore


@dataclass(frozen=True)
class ResourceSpec:
    """Everything that differs between one resource kind and another.

    Each field names a difference the two hand-written blocks expressed by
    repeating themselves.  `resolve_references` is the one asymmetry that is
    real rather than incidental: a Lab points at the Question it prepares a
    learner for, and that reference is resolved against the store before the
    record is built.  A Question has nothing to resolve and leaves it unset --
    modelled as an option rather than flattened away, because pretending the two
    kinds are identical here would be a lie the store would eventually catch.
    """

    kind: str
    """The label a client sees in a problem document: "Question", "Lab"."""

    segment: str
    """The path segment: "questions", "labs"."""

    tag: str
    """The OpenAPI tag the operations are grouped under."""

    model: type[BaseModel]
    write_model: type[BaseModel]
    patch_model: type[BaseModel]

    read: Callable[[Store, str], Record | None]
    write: Callable[[WritableStore, Record, str], Record]
    remove: Callable[[WritableStore, str, str], None]

    build: Callable[[Mapping[str, Any], Any], Record]
    """Turn a validated payload into a store record, applying the corpus rules."""

    patch_fields: Sequence[str]
    links: Callable[[Store, str], list[str]]
    summaries: Mapping[str, str]

    delete_statuses: Sequence[int] = (401, 403, 404, 409, 412, 428, 503)
    """The problem statuses DELETE publishes.

    Not the same for both kinds, and the difference is the contract's rather
    than the implementation's: a Question can be referred to by a Lab or a
    learning path, so deleting one can conflict and the contract documents
    `409`. Nothing in the corpus refers to a Lab, so its DELETE has no `409` to
    document and must not grow one. Hardcoding the Question set here would have
    added a status to the Lab contract that no request can produce.
    """

    resolve_references: Callable[[Store, Mapping[str, Any]], Any] | None = None


def resource_routes(spec: ResourceSpec) -> APIRouter:
    """Build the five item operations for one resource kind."""
    router = APIRouter()
    collection = f"/api/v1/{spec.segment}"
    item = f"{collection}/{{theme}}/{{slug}}"
    Model, Write, Patch = spec.model, spec.write_model, spec.patch_model

    def record_for(store: Store, payload: Mapping[str, Any], vocabulary: Any) -> Record:
        """Build the record, resolving references first where the kind has them."""
        if spec.resolve_references is None:
            return spec.build(payload, vocabulary)
        return spec.build(payload, vocabulary, spec.resolve_references(store, payload))

    # ------------------------------------------------------------------ create

    def create(
        request: Request,
        response: Response,
        store: StoreDep,
        vocabulary: VocabularyDep,
        body: Any,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        # Validation before the duplicate check: a body that could never be a
        # legal record is malformed whatever else is in the store, and telling a
        # client "that id is taken" about content it would have had to fix
        # anyway sends it round the loop twice.
        record = record_for(store, body.model_dump(mode="json"), vocabulary())
        if spec.read(store, str(record["id"])) is not None:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"A {spec.kind} {record['id']!r} already exists in this Content store. "
                    "Replace it with PUT, carrying its current ETag in If-Match."
                ),
            )
        return written(response, spec.write(writer, record, "POST"), Model)

    create.__annotations__["body"] = Write
    create.__name__ = f"create_{spec.segment[:-1]}"

    # -------------------------------------------------------------------- read

    def read_one(
        response: Response,
        store: StoreDep,
        theme: str,
        slug: str,
        if_none_match: Annotated[str | None, Header(alias="If-None-Match")] = None,
    ) -> Any:
        identifier = f"{theme}/{slug}"
        record = spec.read(store, identifier)
        if record is None:
            missing(spec.kind, identifier)
        return conditional(
            Model.model_validate(record),
            record,
            if_none_match,
            response,
            spec.links(store, identifier),
        )

    read_one.__name__ = f"get_{spec.segment[:-1]}"

    # ----------------------------------------------------------------- replace

    def replace(
        request: Request,
        response: Response,
        store: StoreDep,
        vocabulary: VocabularyDep,
        theme: str,
        slug: str,
        body: Any,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = spec.read(store, identifier)
        # Identity first, then the precondition, then the body. A client aiming
        # at something that is not there needs to hear `404` whatever else it
        # got wrong, and a body validated against a version that has already
        # moved is a body decided on the wrong facts.
        if existing is None:
            missing(spec.kind, identifier)
        require_precondition(if_match, existing)
        payload = body.model_dump(mode="json")
        require_same_identity(payload, theme, slug, spec.kind)
        record = record_for(store, payload, vocabulary())
        return written(response, spec.write(writer, record, "PUT"), Model)

    replace.__annotations__["body"] = Write
    replace.__name__ = f"replace_{spec.segment[:-1]}"

    # ------------------------------------------------------------------- patch

    def patch(
        request: Request,
        response: Response,
        store: StoreDep,
        vocabulary: VocabularyDep,
        theme: str,
        slug: str,
        body: Any,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Any:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = spec.read(store, identifier)
        if existing is None:
            missing(spec.kind, identifier)
        require_precondition(if_match, existing)
        # `exclude_unset` is what makes this a patch rather than a replace with
        # optional fields: a field the client did not mention keeps its stored
        # value, and `None` is never confused with "leave it alone".
        from api import writes

        changes = body.model_dump(mode="json", exclude_unset=True)
        payload = writes.merge(existing, changes, spec.patch_fields)
        record = record_for(store, payload, vocabulary())
        return written(response, spec.write(writer, record, "PATCH"), Model)

    patch.__annotations__["body"] = Patch
    patch.__name__ = f"patch_{spec.segment[:-1]}"

    # ------------------------------------------------------------------ delete

    def remove(
        request: Request,
        store: StoreDep,
        theme: str,
        slug: str,
        x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
        if_match: Annotated[str | None, Header(alias="If-Match")] = None,
    ) -> Response:
        writer = require_write_access(request, x_api_key, store)
        identifier = f"{theme}/{slug}"
        existing = spec.read(store, identifier)
        if existing is None:
            missing(spec.kind, identifier)
        require_precondition(if_match, existing)
        # A record something else still points at cannot go: the store refuses
        # and the handler above turns that into the `409` the contract documents.
        spec.remove(writer, identifier, "DELETE")
        return Response(status_code=204)

    remove.__name__ = f"delete_{spec.segment[:-1]}"

    # ------------------------------------------------------------------- mount

    router.post(
        collection,
        operation_id=f"create{spec.kind}",
        tags=[spec.tag],
        summary=spec.summaries["create"],
        status_code=201,
        response_model=Model,
        responses={
            201: {
                "description": f"The {spec.kind} was created.",
                "headers": {
                    "ETag": {
                        "description": f"The new {spec.kind}'s `content_hash`, quoted.",
                        "schema": {"type": "string"},
                    }
                },
            },
            **problem_responses(401, 403, 409, 422, 503),
        },
    )(create)

    router.get(
        item,
        operation_id=f"get{spec.kind}",
        tags=[spec.tag],
        summary=spec.summaries["get"],
        response_model=Model,
        responses=item_responses(404, 500),
    )(read_one)

    router.put(
        item,
        operation_id=f"replace{spec.kind}",
        tags=[spec.tag],
        summary=spec.summaries["replace"],
        response_model=Model,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )(replace)

    router.patch(
        item,
        operation_id=f"patch{spec.kind}",
        tags=[spec.tag],
        summary=spec.summaries["patch"],
        response_model=Model,
        responses=write_responses(401, 403, 404, 412, 422, 428, 503),
    )(patch)

    router.delete(
        item,
        operation_id=f"delete{spec.kind}",
        tags=[spec.tag],
        summary=spec.summaries["delete"],
        status_code=204,
        responses=problem_responses(*spec.delete_statuses),
    )(remove)

    return router
