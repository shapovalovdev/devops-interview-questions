"""The Content API: a versioned HTTP interface over the Content store.

Importing this package pulls in nothing third-party. `api.store` is
standard-library only on purpose, so the Content store in `contentdb/` can
satisfy the `Store` protocol without ever importing FastAPI or Pydantic.
"""
