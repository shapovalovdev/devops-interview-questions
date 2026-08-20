"""Names the whole service agrees on.

These sat at the top of `api/app.py` and were imported from there, which meant
any module wanting the contract version or the snapshot header name had to
import the application module to get it.  They sit below everything now.
"""

from __future__ import annotations

from api.models import License

SERVICE_NAME = "content-api"
CONTRACT_VERSION = "v1"

#: The response header that names the corpus snapshot every answer came from.
#: It holds the snapshot's `content_digest` and is stamped by app-level
#: middleware on **every** response — success and error alike — so no route
#: can forget it and no client can mistake one snapshot for another.
SNAPSHOT_HEADER = "X-Content-Snapshot"

#: The license the corpus is published under, served at `GET /api/v1/meta`.
CORPUS_LICENSE = License(
    name="CC BY 4.0",
    spdx_id="CC-BY-4.0",
    url="https://creativecommons.org/licenses/by/4.0/",
)

#: Where attribution is owed: the repository the corpus lives in.
ATTRIBUTION_URL = "https://github.com/shapovalovdev/devops-interview-questions"

#: Names the environment variable that points the service at a Content store.
#: Its value is `<module>:<callable>`, a zero-argument callable returning a
#: `Store`. Slice 3 points it at the SQLite Content store in `contentdb/`.
STORE_ENVIRONMENT_VARIABLE = "CONTENT_API_STORE"

CONTRACT_TAGS = [
    {"name": "Service", "description": "Liveness and contract identification."},
    {"name": "Questions", "description": "The interview prompts that make up the corpus."},
    {"name": "Labs", "description": "Hands-on exercises, each preparing a learner for one Question."},
    {"name": "Taxonomy", "description": "Themes and tags, derived from the corpus rather than authored."},
    {"name": "Learning paths", "description": "Deliberate sequences through the corpus."},
    {"name": "Search", "description": "Free-text search across Questions and Labs together."},
]
