# Epic: serve Questions and Labs from a Content store through a Content API

| | |
| --- | --- |
| **Status** | `open` |
| **Label** | `epic` |
| **Release** | Content API v1 |

Questions and Labs are Markdown files rendered into a static site. Nothing can ask the corpus a question — "senior Kubernetes Questions tagged `cks`", "every Lab that prepares me for this Question" — without downloading and parsing the whole corpus in a browser. This epic puts the corpus in a **Content store** and serves it through a versioned **Content API**, so other tools (a trainer, a mobile client, an interview bot, the site itself) can consume it.

Vocabulary is defined in the repository's root `CONTEXT.md`; the architectural decision and its trade-offs are recorded in [ADR 0001](../adr/0001-sqlite-content-store-behind-a-fastapi-content-api.md).

## Shape

```
questions/**.md   ──Ingest──▶   Content store (SQLite)   ──▶   Content API (FastAPI)
labs/**.md        ◀──Export──                                   GET/POST/PUT/PATCH/DELETE
      ▲                                                                │
      └──────────── CI Drift gate ────────────────────────────────────┘
```

- **Markdown stays the durable, reviewable record.** The Content store is a derived artifact, rebuilt by Ingest from the corpus on every build. Writes through the API are rendered back to Markdown by Export; CI fails on Drift. Content policy, source verification, and the coverage target keep being enforced against Markdown by the existing validators — the API must not become a way around them.
- **The API contract is authored first.** `api/openapi.yaml` is the source of truth for the wire format; the implementation is tested against it, not derived from it by accident.
- **The static site build stays standard-library only.** FastAPI, Pydantic, and uvicorn are confined to the API service and its tests. `scripts/build_site.py` must keep working with no third-party package installed.

## The contract, pinned

Every slice below implements against these shapes. Do not renegotiate them inside a slice; if a shape is wrong, say so on this epic first.

**Identity.** A Question and a Lab are both identified by `"<theme>/<slug>"` — e.g. `kubernetes/admission-policy-and-guardrails` — matching their path under `questions/` or `labs/` without the `.md`.

**Question**

| field | type | notes |
| --- | --- | --- |
| `id` | string | `<theme>/<slug>` |
| `theme` | string | canonical Theme, must exist in `config/content-manifest.json` |
| `slug` | string | |
| `title` | string | |
| `difficulty` | enum | `junior` \| `middle` \| `senior` \| `staff` |
| `type` | enum | `theory` \| `scenario` \| `troubleshooting` |
| `tags` | string[] | every tag must exist in `TAGS.md` |
| `sources` | Source[] | `{url, source_type, verified_on}` |
| `prompt` | string | the question itself |
| `answer_guide` | string[] | the expected points |
| `body_markdown` | string | full Markdown body below the front matter |
| `source_path` | string | `questions/<theme>/<slug>.md` |
| `content_hash` | string | sha256 of the source file; serves as the ETag |
| `updated_at` | date-time | |

**Lab** — `id`, `theme`, `slug`, `title`, `difficulty`, `tags`, `body_markdown`, `source_path`, `content_hash`, `updated_at` as above, plus `question_ref` (the `id` of the Question it prepares you for), `why` (string), and `checklist` (string[]).

**Theme** — `name`, `state`, `question_count`, `lab_count`, `difficulty_counts` (object keyed by difficulty).
**Tag** — `name`, `question_count`, `lab_count`.
**LearningPath** — `slug`, `title`, `description`, `steps[]` (each `{question_id, why}`), sourced from `config/learning-paths.json`.

**Endpoints (v1)**

```
GET    /api/v1/health
GET    /api/v1/questions?theme=&difficulty=&type=&tag=&q=&limit=&offset=&sort=
GET    /api/v1/questions/{theme}/{slug}
POST   /api/v1/questions
PUT    /api/v1/questions/{theme}/{slug}
PATCH  /api/v1/questions/{theme}/{slug}
DELETE /api/v1/questions/{theme}/{slug}
GET    /api/v1/labs?theme=&difficulty=&tag=&question_ref=&q=&limit=&offset=
GET    /api/v1/labs/{theme}/{slug}
POST   /api/v1/labs
PUT    /api/v1/labs/{theme}/{slug}
PATCH  /api/v1/labs/{theme}/{slug}
DELETE /api/v1/labs/{theme}/{slug}
GET    /api/v1/themes
GET    /api/v1/themes/{name}
GET    /api/v1/tags
GET    /api/v1/learning-paths
GET    /api/v1/learning-paths/{slug}
GET    /api/v1/search?q=&kind=            # questions and labs together
```

**Conventions**

- List responses are enveloped: `{"items": [...], "total": int, "limit": int, "offset": int}`. Default `limit` 50, maximum 200.
- Errors are `application/problem+json` per RFC 9457: `{type, title, status, detail, instance}`. Never leak a stack trace.
- Reads are anonymous. Every mutating request must carry a **Write credential** in the `X-API-Key` header: missing → `401`, wrong → `403`.
- `PUT`, `PATCH`, and `DELETE` require `If-Match` carrying the item's `content_hash`: missing → `428`, stale → `412`.
- `POST` on an existing `id` → `409`. Unknown `id` → `404`. Body that violates the Theme or Tag vocabulary → `422`.
- A write must be rejected if it would break a rule the Markdown validators enforce, with the same reason.

**Sort and search parameters**

`sort` on list endpoints accepts `id`, `title`, `difficulty`, `updated_at`, each optionally prefixed `-` for
descending. The default is `id`, so pagination is deterministic. `q` on `/api/v1/search` is required — a
search with no query is meaningless, and its absence is a documented `422`.

**How the service finds its store**

The environment variable `CONTENT_API_STORE` names the store factory as `<module>:<callable>`. With it
unset and no `store=` passed, `create_app()` raises rather than serving anything — a service that
silently invents content is worse than one that refuses to start. `api.demo:app` is the explicit,
clearly named entrypoint for the in-memory fake. Slice 6's container configures the real store this way.

**A complete contract, with stubs marked**

The contract describes the whole v1 surface from the day it is written — every path, method, parameter,
request body, header, and status code, including `X-API-Key`, `If-Match`, and their `401`, `403`, `409`,
`412`, and `428` responses. It is the published API scheme, not a log of what happens to be built.

An operation that is not yet implemented carries `x-implementation: stub` in the contract; an implemented
one carries `x-implementation: implemented`. The two tests read that marker:

- The **contract test** compares paths, methods, parameters, and request bodies for every operation, and
  compares response status codes for implemented operations only.
- The **coverage census** requires every documented status code of an implemented operation to be exercised
  by a test, and requires each stub operation to have a test asserting its `501`.

Flipping an operation to `implemented` is therefore what makes the census demand its full set of status
codes — a slice cannot claim an endpoint without also testing every response the contract promises for it.
By the end of slice 4 no `x-implementation: stub` may remain, and the release gate checks this.

## Slices

| # | Slice | Depends on |
| --- | --- | --- |
| [0001](./0001-content-store-and-ingest.md) | Content store schema and Ingest | — |
| [0002](./0002-api-contract-and-service.md) | API contract and tracer-bullet service | — |
| [0003](./0003-api-read-surface.md) | Complete read surface over the real store | 0001, 0002 |
| [0004](./0004-api-write-surface.md) | Write surface: CRUD, Write credential, optimistic concurrency | 0003 |
| [0005](./0005-export-and-drift-gate.md) | Export to Markdown and the CI Drift gate | 0001 |
| [0006](./0006-packaging-and-e2e.md) | Packaging, end-to-end suite, and CI coverage gate | 0003, 0004 |

## Release gate

The release **Content API v1** closes when:

- every slice above is closed and verified;
- `api/openapi.yaml` describes the served API exactly, proven by a contract test, carries no remaining
  `x-implementation: stub` operation, and has every documented path, method, and status code exercised by at
  least one test;
- API tests and end-to-end tests against a running container both pass in GitHub Actions, with the coverage gate green;
- `python tests/run_all_tests.py`, the existing content validators, and the static site build all still pass with no third-party package installed;
- a Drift check proves the committed Markdown corpus and the Content store agree.
