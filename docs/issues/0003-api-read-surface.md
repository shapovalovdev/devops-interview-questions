# Complete read surface over the real store

| | |
| --- | --- |
| **Status** | `ready-for-agent` |
| **GitHub** | [#171](https://github.com/shapovalovdev/devops-interview-questions/issues/171) |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | 0001, 0002 |
| **Branch** | `feature/api-read-surface` |

Part of the Content API v1 epic. **Read the epic first** — it pins the resource shapes, endpoints, envelope, and error format.

Depends on slice 1 (Content store and Ingest) and slice 2 (API contract and service skeleton), both merged to `main` before this starts.

This slice replaces slice 2's in-memory fake with the real Content store and implements every remaining **read** endpoint. After it, the whole read surface of the contract is live against real corpus data. Writes stay `501` — slice 4 owns them.

## Scope

- Wire `contentdb.Store` into the app as the `Store` dependency, opened read-only, one connection per request or a safely shared read-only connection — say which and why in the module docstring.
- Implement, per the contract: `GET /api/v1/questions/{theme}/{slug}`, `GET /api/v1/labs`, `GET /api/v1/labs/{theme}/{slug}`, `GET /api/v1/themes`, `GET /api/v1/themes/{name}`, `GET /api/v1/tags`, `GET /api/v1/learning-paths`, `GET /api/v1/learning-paths/{slug}`, `GET /api/v1/search`.
- **ETags.** Every single-item read returns `ETag: "<content_hash>"`. A request with a matching `If-None-Match` gets `304`. This is what slice 4's `If-Match` concurrency will build on.
- **A Lab knows its Question.** `GET /api/v1/labs/{theme}/{slug}` resolves `question_ref` to a real Question id, and `GET /api/v1/questions/{theme}/{slug}` reports the Labs that prepare a learner for it. This link is the reason Labs are in the API at all — do not ship it as a dangling string.
- Where the store is missing or unreadable at startup, fail fast with a clear message naming the expected path and the Ingest command that produces it. A silently empty API is worse than one that refuses to start.

## Acceptance criteria

- [ ] Every read path in `api/openapi.yaml` is implemented; none returns `501`.
- [ ] Responses match the contract exactly — the slice 2 contract test still passes, unchanged in strictness.
- [ ] A real corpus check: with a store built by Ingest from the committed corpus, `GET /api/v1/questions?theme=kubernetes&difficulty=senior` returns only senior Kubernetes Questions, and the count matches what a direct filesystem scan of the front matter reports. Assert against the corpus, not a hard-coded number.
- [ ] `GET /api/v1/search?q=` returns Questions and Labs together, ranked, with `kind` distinguishing them, and honours `kind=` to restrict.
- [ ] Unknown `id`, unknown theme, unknown tag, unknown path slug each return `404` in problem+json.
- [ ] ETag and `If-None-Match` behave as specified, including a `304` carrying no body.
- [ ] The coverage census passes with every read status code covered, including `304` and `404`.
- [ ] `pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95` passes.
- [ ] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

## Inherited from slices 0001 and 0002

- `contentdb.Store` (merged) opens the store **read-only** with `check_same_thread=False`. Your module
  docstring must say how concurrent readers share it, as the issue requires.
- Records cross the seam as **plain mappings** keyed by the epic's field names. `api/store.py` is
  deliberately stdlib-only and two tests enforce that it never imports pydantic, fastapi, starlette, or
  yaml. Adapt to Pydantic on the `api/` side of the seam, never inside it.
- The service finds its store through `CONTENT_API_STORE` (`<module>:<callable>`); `create_app()` raises
  `StoreNotConfigured` when it is absent. Wire the real `contentdb.Store` in through that same door.
- Flipping an operation to `x-implementation: implemented` makes the census demand a test for every status
  code the contract documents for it. That is deliberate: it is what stops an endpoint being claimed
  without being covered.
- `api/testing.py` holds the in-memory fake; keep it working, since the contract and census tests use it.

## Notes

- Flip every read operation you implement from `x-implementation: stub` to `x-implementation: implemented` in `api/openapi.yaml`, which makes the coverage census demand a test for each of its documented status codes. See the epic's **A complete contract, with stubs marked** section.
- Work in a git worktree on branch `feature/api-read-surface`.
- Use the `tdd` skill.
- Tests must build their fixture store by running Ingest over a small fixture corpus, plus at least one test against the real committed corpus so schema drift in real content is caught.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).
