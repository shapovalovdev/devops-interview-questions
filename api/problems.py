"""Every refusal this service can make, as the problem documents it publishes.

These eight handlers were defined inside `create_app()`.  None of them closed
over it -- measured from the code objects, all eight had empty `co_freevars` --
so they were nested for no reason beyond where the file grew.

They are the other half of the contract's error surface: the routes decide
*which* refusal applies, and these decide what a refusal looks like on the wire.
Keeping them together means the RFC 9457 shape is stated once.
"""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api import writes
from api.helpers import problem_response
from api.store import InvalidQuery, RecordInUse, StoreContractViolation, StoreIsReadOnly


def _validation_errors(exception: RequestValidationError) -> list[dict[str, str]]:
    return [
        {
            "field": ".".join(str(part) for part in error.get("loc", ())),
            "message": str(error.get("msg", "")),
        }
        for error in exception.errors()
    ]


def install(app: FastAPI) -> None:
    """Register every exception handler on `app`."""
    @app.exception_handler(RequestValidationError)
    async def _on_validation_error(request: Request, exception: RequestValidationError) -> JSONResponse:
        return problem_response(
            status=422,
            detail="The request parameters or body do not satisfy the contract.",
            instance=request.url.path,
            errors=_validation_errors(exception),
        )

    @app.exception_handler(StarletteHTTPException)
    async def _on_http_error(request: Request, exception: StarletteHTTPException) -> JSONResponse:
        return problem_response(
            status=exception.status_code,
            detail=str(exception.detail),
            instance=request.url.path,
        )

    @app.exception_handler(InvalidQuery)
    async def _on_invalid_query(request: Request, exception: InvalidQuery) -> JSONResponse:
        """Free text the store cannot parse is the client's fault, not a fault.

        The store raises this only for a query string it could not read — an
        unbalanced quote, a dangling operator — which the contract documents as
        `422`. Everything else a store raises stays a `500`.
        """
        return problem_response(
            status=422,
            detail="The free-text query could not be parsed; check quoting and operators.",
            instance=request.url.path,
            errors=[{"field": "q", "message": str(exception)}],
        )

    @app.exception_handler(writes.WriteRejected)
    async def _on_write_rejected(request: Request, exception: writes.WriteRejected) -> JSONResponse:
        """A write that breaks a corpus rule is the client's to fix, and it is told which.

        The contract promises a problem document naming the offending field, and
        this is the only place that promise is kept: the message comes from
        `contentdb`, which is what would have refused the same content at Ingest
        time, so a client is told the same thing a reviewer would be.
        """
        return problem_response(
            status=422,
            detail=(
                "The write would produce a record the Markdown corpus rules reject, so it was not "
                "stored."
            ),
            instance=request.url.path,
            errors=[{"field": exception.field, "message": exception.message}],
        )

    @app.exception_handler(RecordInUse)
    async def _on_record_in_use(request: Request, exception: RecordInUse) -> JSONResponse:
        """Deleting something the corpus still points at is a conflict, not a fault."""
        return problem_response(status=409, detail=str(exception), instance=request.url.path)

    @app.exception_handler(StoreIsReadOnly)
    async def _on_read_only_store(request: Request, exception: StoreIsReadOnly) -> JSONResponse:
        """This deployment cannot write, which the contract publishes as `503`."""
        return problem_response(status=503, detail=str(exception), instance=request.url.path)

    @app.exception_handler(StoreContractViolation)
    async def _on_store_contract_violation(
        request: Request, exception: StoreContractViolation
    ) -> JSONResponse:
        """A store that broke the seam is a fault, and it is ours, not the client's.

        The body stays the same `500` every other fault produces — a client can
        do nothing with the detail — but the exception has already said in the
        log which shape arrived and which was promised.
        """
        return problem_response(
            status=500,
            detail="The service failed to handle this request.",
            instance=request.url.path,
        )

    @app.exception_handler(Exception)
    async def _on_unhandled_error(request: Request, exception: Exception) -> JSONResponse:
        # The exception itself is deliberately not echoed: a stack trace or an
        # internal message in the body is how a service leaks its innards.
        return problem_response(
            status=500,
            detail="The service failed to handle this request.",
            instance=request.url.path,
        )

    # ---------------------------------------------------------------- Service

