# API contract and tracer-bullet service

| | |
| --- | --- |
| **Status** | `closed` |
| **GitHub** | [#170](https://github.com/shapovalovdev/devops-interview-questions/issues/170) |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | — |
| **Branch** | `feature/api-contract` |

Part of the Content API v1 epic. **Read the epic first** — it pins the resource shapes, the endpoint list, the envelope, the error format, and the auth and concurrency rules. Do not renegotiate them here.

This slice authors the **API contract** and stands up the FastAPI service behind one real endpoint end to end. It runs in parallel with slice 1, so it must **not** depend on the real Content store: code against a `Store` protocol and test with an in-memory fake. Slice 3 swaps the real store in.

## Scope

- **`api/openapi.yaml`, written by hand, first.** The complete v1 contract from the epic: every path, method, parameter, request body, response, and status code, with `components/schemas` for Question, Lab, Theme, Tag, LearningPath, the list envelope, and the RFC 9457 problem document. This file is the source of truth for the wire format.
- **The FastAPI app.** `api/app.py` with Pydantic models mirroring those schemas, a `Store` protocol (matching what slice 1 is building — the epic's shapes are the agreement), dependency-injected so tests substitute a fake, and RFC 9457 problem responses wired to a global exception handler so no route hand-rolls an error body.
- **Two endpoints implemented for real**, as the tracer bullet: `GET /api/v1/health` and `GET /api/v1/questions` with `theme`, `difficulty`, `type`, `tag`, `q`, `limit`, `offset`, and `sort`, fully enveloped and paginated. Every other path in the contract may return `501` for now — but it must be *in the contract* and its stub must be covered by a test asserting the `501`, so slice 3 and 4 find a scaffold, not a blank file.
- **A contract test.** Assert that FastAPI's generated schema and the hand-written `api/openapi.yaml` agree on paths, methods, parameters, and request bodies for every operation, and on response status codes for operations marked `x-implementation: implemented`. A route that drifts from the contract must fail the build. This test is the backbone of the whole epic — make it strict and make its failure message name the exact divergence.
- **A coverage census test.** Walk `api/openapi.yaml` and assert every documented status code of an implemented operation is exercised by at least one test, and that each `x-implementation: stub` operation has a test asserting its `501`. This is how "full coverage" is enforced mechanically rather than by eyeball.

See the epic's **A complete contract, with stubs marked** section for the rule these two tests implement: the contract covers the whole v1 surface immediately — including `X-API-Key`, `If-Match`, and their `401`, `403`, `409`, `412`, `428` responses — and the `x-implementation` marker is what lets slices 3 and 4 turn those promises into tested behavior.

**Tests live in `tests/api/`.** `tests/run_all_tests.py` globs `tests/test_*.py` non-recursively, so a subdirectory keeps the stdlib-only suite from ever importing FastAPI. Do not change that glob.
- **Dependencies, declared and pinned.** `requirements-api.txt` (fastapi, uvicorn, pydantic) and `requirements-dev.txt` (pytest, pytest-cov, httpx). The static site build must keep working with none of them installed — add a test that imports `scripts/build_site.py` in a subprocess with third-party imports blocked, or otherwise prove the separation.

## Acceptance criteria

- [x] `uvicorn api.app:app` serves `GET /api/v1/health` returning `200` with a JSON body naming the service and contract version.
- [x] `GET /api/v1/questions` returns the epic's envelope, applies every documented filter, respects `limit` (default 50, max 200) and `offset`, and rejects out-of-range or malformed parameters with `422` in problem+json.
- [x] Errors are `application/problem+json` with the RFC 9457 members. A route raising an unexpected exception returns a `500` problem document with no stack trace in the body.
- [x] The contract test passes and genuinely fails when a route is changed without the contract — prove it by describing the deliberate break you tried.
- [x] The coverage census passes: every path, method, and status in `api/openapi.yaml` has a test.
- [x] `pytest --cov=api --cov-branch --cov-fail-under=95` passes.
- [x] The site build and `python tests/run_all_tests.py` still pass with no third-party package installed.

## Notes

- Work in a git worktree on branch `feature/api-contract`.
- Use the `tdd` skill: write the failing test, then the code. The contract test and census test are the ones that make the rest of the epic safe — write them first.
- Do not touch `contentdb/` — slice 1 owns it. Your `Store` protocol lives in `api/`.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).

## Coordinator rulings, 2026-08-17

Two agents worked this slice concurrently by coordinator error, leaving the worktree with two partial
implementations. These rulings settle every conflict between them. They are decisions, not suggestions.

1. **Tests live in `tests/api/`.** Delete `api/tests/`, carrying across any test worth keeping. One suite,
   one `conftest.py`. `pytest.ini` sets `testpaths = tests/api`.
2. **Keep the committed `api/openapi.yaml`.** It matches the epic: the whole v1 surface, `501` deliberately
   absent from documented responses, `x-implementation` carrying that fact instead.
3. **Sort obeys the epic**: `id`, `title`, `difficulty`, `updated_at`, each optionally `-`-prefixed, default
   `id`. A `-updated_at` default is a defect — pagination must be deterministic.
4. **Plain mappings cross the `Store` seam**, keyed by the epic's field names, with a query dataclass in and
   a page result out. No Pydantic model may cross it: `contentdb` is standard-library only and must be able
   to implement this protocol in slice 3 without importing `api/`.
5. **The census must not depend on test ordering or on a global mutated by middleware.** A partial run
   (`-k`, `-x`, `-n`) must fail or skip loudly, never pass silently. A census that quietly reports success
   because no test ran is worse than no census.
6. **`create_app()` must not fall back to a fabricated corpus.** Serving invented Questions under a
   production entrypoint is a correctness bug. With no store configured, fail fast with a message naming
   what to configure. The in-memory fake belongs in tests and in an explicit, clearly named demo entrypoint.

## Completion report, 2026-08-17

**Branch** `feature/api-contract` · **Implementation commit** `0bef7dd` ·
**Worktree** `.claude/worktrees/capi-0002` · not pushed, not merged — the coordinator integrates.

### What was reconciled

The worktree held two partial implementations of this slice. Each ruling above was applied:

1. **One suite, in `tests/api/`.** `api/tests/` is gone. What was worth keeping came across: the
   store-behaviour cases now live in `tests/api/test_store.py`, the app cases in
   `tests/api/test_service.py`. There is one `conftest.py`, and it holds no state. `pytest.ini` sets
   `testpaths = tests/api`.
2. **`api/openapi.yaml` kept unchanged as the source of truth**, byte for byte as committed. The service
   was rewritten to match it — operation ids, tags, parameter names and required flags, request-body
   schemas, and the enumerated vocabularies — rather than the file being edited to match the service.
3. **Sort corrected.** `SortKey` is `id|title|difficulty|updated_at`, each optionally `-`-prefixed,
   default `id`, in the contract, the models, the query dataclass, and the store. The demo corpus is
   deliberately arranged so `id` order and `-updated_at` order disagree, which is what makes
   `test_the_default_sort_is_id_so_paging_is_deterministic` catch the old defect instead of passing by
   coincidence. `id` also breaks every tie, so `limit`/`offset` paging cannot skip or repeat an item.
4. **Pydantic no longer crosses the seam.** `api/store.py` defines `QuestionQuery`, `LabQuery`,
   `SearchQuery`, and a `Page` result over `Mapping[str, Any]` records keyed by the epic's field names,
   with timestamps as ISO 8601 strings the way SQLite will store them. The module imports nothing outside
   the standard library, and two tests hold that line: one imports `api.store` in a clean subprocess and
   fails if `pydantic`, `fastapi`, `starlette`, or `yaml` appears in `sys.modules`; the other
   (`tests/test_api_dependency_separation.py`, run by the stdlib-only suite) imports it with every
   third-party package blocked by a meta-path finder. A standard-library-only class satisfying the
   protocol is asserted with `isinstance`, so slice 1 can implement it without importing `api/`.
5. **The census no longer has state to be wrong about.** The middleware recorder, the module-level `SEEN`
   set, and the `pytest_collection_modifyitems` hook that shoved the census to the end of the session are
   all deleted. `tests/api/test_coverage_census.py` derives what each operation owes from
   `x-implementation`, builds its own clients, issues every request itself in a single test, and compares
   what it got with what the contract promises. It cannot pass because nothing ran, it cannot be
   half-run, and it is indifferent to ordering, `-k`, `-x`, and `-n`.
6. **`create_app()` fails fast.** With no store it raises `StoreNotConfigured` naming
   `CONTENT_API_STORE`, the `create_app(store=...)` argument, and the demo entrypoint. `api.app:app` is
   resolved lazily through a module `__getattr__`, so `uvicorn api.app:app` gets a configured application
   or that error, while importing the module never needs a store. The fake corpus lives in
   `api/testing.py` and is reachable only from the tests and from `api.demo:app`; every demo id carries a
   `demo-` prefix, and a test asserts it.

### What was built

| file | role |
| --- | --- |
| `api/openapi.yaml` | the hand-written v1 contract (unchanged) |
| `api/app.py` | the application: 2 implemented operations, 17 stubs, RFC 9457 handlers |
| `api/models.py` | Pydantic models named for the contract's `components/schemas` |
| `api/store.py` | the `Store` protocol and its query and page types — standard library only |
| `api/testing.py` | the in-memory fake and the demo corpus |
| `api/demo.py` | `uvicorn api.demo:app`, the explicitly fake service |
| `tests/api/` | `test_contract.py`, `test_coverage_census.py`, `test_service.py`, `test_store.py`, `test_entrypoints.py`, `support.py`, `conftest.py` |
| `tests/test_api_dependency_separation.py` | the standard-library boundary, run by the stdlib-only suite |
| `pytest.ini`, `.coveragerc`, `requirements-api.txt`, `requirements-dev.txt` | tooling and pinned dependencies |

### Commands run, with their output

```
$ pytest --cov=api --cov-branch --cov-fail-under=95 -q
Name              Stmts   Miss Branch BrPart  Cover
---------------------------------------------------
api/__init__.py       0      0      0      0   100%
api/app.py          135      0     12      0   100%
api/demo.py           4      0      0      0   100%
api/models.py       149      0      0      0   100%
api/store.py         39      0      0      0   100%
api/testing.py       93      0     28      0   100%
---------------------------------------------------
TOTAL               420      0     40      0   100%
Required test coverage of 95% reached. Total coverage: 100.00%
118 passed, 1 warning in 2.50s
```

**118 tests, 100.00% statement and branch coverage of `api/`** (gate is 95%). Python 3.13.7,
`fastapi==0.141.1`, `pydantic==2.13.4`, `uvicorn[standard]==0.52.3`, `pytest==9.1.1`,
`pytest-cov==7.1.0`, `httpx==0.28.1`, `PyYAML==6.0.3`. `.coveragerc` excludes the `Protocol` bodies
(`def …: ...`), which are documentation with nothing to execute.

```
$ python3 scripts/build_site.py --output <tmp>          # no third-party package installed
Rendered 1178 Markdown pages into <tmp>

$ python3 -c "import api.store"                          # same interpreter, no fastapi/pydantic
ok []

$ python3 tests/run_all_tests.py
Ran 173 checks across 58 test modules.
FAILED 1: test_build_site.py::OwnSiteBuildParity        # pre-existing, see below
```

Live service, not a test client:

```
$ CONTENT_API_STORE=api.testing:demo_store uvicorn api.app:app --port 8731
$ curl -si /api/v1/health          → HTTP/1.1 200 OK, {"status":"ok","service":"content-api","contract_version":"v1"}
$ curl -s  '/api/v1/questions?limit=1&theme=linux'
                                   → {"total":1,"limit":1,"offset":0,"items":[{"id":"linux/demo-exit-codes",…}]}
$ curl -si '/api/v1/questions?limit=0'  → HTTP/1.1 422 Unprocessable Content   (application/problem+json)
$ curl -si /api/v1/tags                 → HTTP/1.1 501 Not Implemented          (application/problem+json)

$ uvicorn api.app:app          # with CONTENT_API_STORE unset
api.app.StoreNotConfigured: No Content store is configured, and the Content API will not invent one:
serving fabricated Questions from a production entrypoint is a correctness bug, because no client can
tell them from the corpus. Set CONTENT_API_STORE to '<module>:<callable>' naming a zero-argument
callable that returns a Store (slice 3 points it at the SQLite Content store), pass one to
create_app(store=...), or run the demo service 'uvicorn api.demo:app', which says in its name that its
corpus is fake.
```

### The deliberate breaks, and how each was caught

Six changes were made one at a time, the suite run, and each reverted. Every one failed, and every
failure names the exact divergence rather than reporting that two dictionaries differ.

| # | the break | what failed, and what it said |
| --- | --- | --- |
| 1 | `listQuestions` query parameter `tag` renamed to `tags` | `test_parameters_match` — *contract declares `('tag', 'query')` but the route does not; route declares `('tags', 'query')` but the contract does not* |
| 2 | `listQuestions` moved to `/api/v1/question` | `test_paths_and_methods_match` — *served but not in the contract: `['GET /api/v1/question']`; in the contract but not served: `['GET /api/v1/questions']`* |
| 3 | the documented `500` dropped from the `listQuestions` route | `test_response_statuses_match_for_implemented_operations` — *the route can answer `['200','422']` but the contract documents `['200','422','500']`* |
| 4 | `createQuestion` body changed from `QuestionWrite` to `QuestionPatch` | `test_request_bodies_match` — *request body is `…/QuestionPatch` but the contract says `…/QuestionWrite`* |
| 5 | `difficulty` removed from the served `SortKey` vocabulary | `test_parameters_match` — *`('sort','query')` accepts `['-id','-title','-updated_at','id','title','updated_at']` but the contract pins `['-difficulty','-id','-title','-updated_at','difficulty','id','title','updated_at']`*, on both `GET /api/v1/questions` and `GET /api/v1/labs` |
| 6 | the `listThemes` stub quietly made to return a page | census — *`GET /api/v1/themes` was exercised for 501 but answered 200*, plus `test_no_stub_operation_secretly_works` |

Break 5 is the one that made the contract test stricter than it started. FastAPI writes an optional
enum parameter as `anyOf: [{$ref: …}, {type: null}]` while the contract writes a bare `$ref`, so the
original comparison walked for a literal `enum` key, found none on either side, and compared nothing.
`enums()` now dereferences local `$ref`s, and both documents are additionally checked for dangling
references.

A seventh change flipped `listTags` to `x-implementation: implemented` in the contract without
implementing it. The census refused it — *promised by the contract but never exercised:
`[('/api/v1/tags','get','200'), ('/api/v1/tags','get','500')]`* — and the contract test refused it
independently — *the route can answer `['200','501']` but the contract documents `['200','500']`*.
That is the epic's rule working: flipping a marker immediately obliges the slice that flipped it to
produce every response the contract promises.

### For the coordinator

1. **`tests/run_all_tests.py` has one failure, and it predates this branch.**
   `test_build_site.py::OwnSiteBuildParity::test_every_generated_docs_link_resolves_within_the_build`
   reports `docs/issues/0000-epic-content-api.html: ../../CONTEXT.md`. The epic links
   `[CONTEXT.md](../../CONTEXT.md)`, and the site build renders `docs/issues/` but not the repository
   root, so the relative link does not resolve inside the built tree. Reproduced on a pristine export of
   `main` at `1387982` (`Ran 172 checks across 57 test modules. FAILED 1:
   test_build_site.py::OwnSiteBuildParity`), i.e. before any file in this branch existed. It is a
   one-line fix in `docs/issues/0000-epic-content-api.md`, but that file is the epic and slice 1 may be
   editing `docs/issues/` in parallel, so it is left for central resolution rather than fixed here. Every
   other check passes: 173 checks across 58 modules, the one new module being
   `test_api_dependency_separation.py`.
2. **`api.app:app` is a lazy attribute, not a module-level object.** `uvicorn api.app:app` works
   unchanged, but anything that does `from api.app import app` at import time now needs
   `CONTENT_API_STORE` set. Slice 6's packaging should set it in the image rather than reintroducing an
   eager `app`.
3. **`CONTENT_API_STORE` is this slice's invention**, not something the epic pins. It takes
   `<module>:<callable>`. If slice 3 or 6 would rather configure a database path directly, this is the
   place to change it, and the name should be settled before the Dockerfile depends on it.
4. **The `Store` protocol covers reads only.** Writes are slice 4's, together with the `content_hash`
   and Export semantics that give them meaning; declaring those methods now would have been guessing at
   an agreement nobody has made. Slice 4 extends the protocol.
5. **Slice 3 must flip markers, not add routes.** Every stub is already at its contracted address with
   its contracted parameters and request body. Implementing one means replacing the `not_implemented`
   call and flipping `x-implementation`, at which point the census demands that operation's full set of
   documented responses — including the `503` the contract reserves for a service with no Write
   credential configured.
6. **Not pushed, no pull request, no merge.** Two commits on `feature/api-contract`: the implementation
   and this report.
