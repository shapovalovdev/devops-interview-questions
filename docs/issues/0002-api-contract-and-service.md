# API contract and tracer-bullet service

| | |
| --- | --- |
| **Status** | `ready-for-agent` |
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

- [ ] `uvicorn api.app:app` serves `GET /api/v1/health` returning `200` with a JSON body naming the service and contract version.
- [ ] `GET /api/v1/questions` returns the epic's envelope, applies every documented filter, respects `limit` (default 50, max 200) and `offset`, and rejects out-of-range or malformed parameters with `422` in problem+json.
- [ ] Errors are `application/problem+json` with the RFC 9457 members. A route raising an unexpected exception returns a `500` problem document with no stack trace in the body.
- [ ] The contract test passes and genuinely fails when a route is changed without the contract — prove it by describing the deliberate break you tried.
- [ ] The coverage census passes: every path, method, and status in `api/openapi.yaml` has a test.
- [ ] `pytest --cov=api --cov-branch --cov-fail-under=95` passes.
- [ ] The site build and `python tests/run_all_tests.py` still pass with no third-party package installed.

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
