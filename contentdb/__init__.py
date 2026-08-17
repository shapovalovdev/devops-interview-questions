"""The Content store: the Markdown corpus, made queryable.

`contentdb` is standard library only — `sqlite3`, `pathlib`, `hashlib`, `json`,
`re` — because Ingest runs inside the static site build, where nothing is
installed and nothing may be.  FastAPI and Pydantic live on the other side of
this package's seam, in `api/`, and adapt to it there.  See
`docs/adr/0001-sqlite-content-store-behind-a-fastapi-content-api.md`.

The package is three layers, each usable without the one above it:

- :mod:`contentdb.frontmatter` reads the YAML subset the corpus is written in;
- :mod:`contentdb.corpus` turns the Markdown files into validated records;
- :mod:`contentdb.ingest` writes those records into a SQLite file, and
  :mod:`contentdb.store` reads them back.

Records cross the read seam as plain mappings keyed by the field names the epic
pins (`docs/issues/0000-epic-content-api.md`), never as ORM rows or Pydantic
models, so a fake `Store` is a dictionary and the API layer owns its own types.
"""

from __future__ import annotations

__all__ = ["corpus", "frontmatter", "ingest", "models", "schema", "store"]
