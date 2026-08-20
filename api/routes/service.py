"""The two operations that describe the service rather than the corpus.

`getHealth` says the service is up and which contract it serves.  `getMeta`
names the immutable corpus snapshot behind it -- the commit Ingest read, the
content digest, and the licence the corpus is published under.

Both were defined inside `create_app()`.  `get_meta` was the last route handler
in the service that closed over it, reading the enclosing `app` for its state;
it reads `request.app.state` now, like every other handler.
"""

from __future__ import annotations

from fastapi import APIRouter, Request

from api.constants import ATTRIBUTION_URL, CONTRACT_VERSION, CORPUS_LICENSE, SERVICE_NAME
from api.models import HealthReport, Meta

router = APIRouter()


@router.get(
    "/api/v1/health",
    operation_id="getHealth",
    tags=["Service"],
    summary="Report that the service is up and which contract it serves.",
    response_model=HealthReport,
)
def get_health() -> HealthReport:
    return HealthReport(status="ok", service=SERVICE_NAME, contract_version=CONTRACT_VERSION)

@router.get(
    "/api/v1/meta",
    operation_id="getMeta",
    tags=["Service"],
    summary="Identify the immutable corpus snapshot this service serves.",
    response_model=Meta,
)
def get_meta(request: Request) -> Meta:
    # Serves the identity resolved at startup: the store state Ingest
    # recorded, plus the contract's own version and licensing, which are
    # facts about this service rather than about the store.
    #
    # Reads `request.app.state` rather than the enclosing `app`, so this is
    # the last route handler in the module that closed over create_app().
    meta = request.app.state.content_meta
    return Meta(
        source_commit=str(meta["source_commit"]),
        content_digest=str(meta["content_digest"]),
        api_version=CONTRACT_VERSION,
        build_timestamp=str(meta["build_timestamp"]),
        license=CORPUS_LICENSE,
        attribution=ATTRIBUTION_URL,
    )

# -------------------------------------------------------------- Questions

