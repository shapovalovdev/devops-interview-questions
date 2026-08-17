"""A demo Content API over a small, obviously fake corpus.

Run it with `uvicorn api.demo:app` to click around the contract without a
Content store. Every record it serves is invented and every id carries a
`demo-` prefix, which is why this lives behind its own entrypoint: the
production entrypoint, `api.app:app`, refuses to start without a real store
rather than quietly serving these.
"""

from __future__ import annotations

from api.app import create_app
from api.testing import demo_store

app = create_app(store=demo_store())
