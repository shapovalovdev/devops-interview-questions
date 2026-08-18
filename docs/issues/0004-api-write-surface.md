# Write surface: CRUD, Write credential, optimistic concurrency

| | |
| --- | --- |
| **Status** | `closed` |
| **GitHub** | [#172](https://github.com/shapovalovdev/devops-interview-questions/issues/172) |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | 0003 |
| **Branch** | `feature/api-write-surface` |

Part of the Content API v1 epic. **Read the epic first** — it pins the auth, concurrency, and error rules this slice implements.

Depends on slice 3 (complete read surface), merged to `main` before this starts.

This slice makes the Content API writable: create, replace, patch, and delete Questions and Labs, guarded by a **Write credential** and optimistic concurrency. It is the slice where the API can do damage, so its failure paths matter more than its happy paths.

## Scope

- `POST`, `PUT`, `PATCH`, `DELETE` for both `/api/v1/questions` and `/api/v1/labs`, per the contract.
- **Write credential.** Every mutating request must carry `X-API-Key`. Missing → `401`; present but wrong → `403`. The expected value comes from an environment variable; **if it is unset, the service must start read-only and reject every write with `503`** rather than defaulting to an empty or well-known key. Never log the credential, and never echo it in an error body.
- **Optimistic concurrency.** `PUT`, `PATCH`, `DELETE` require `If-Match` carrying the current `content_hash`: missing → `428`, stale → `412`. A successful write returns the new `ETag`.
- **Validation is the Markdown rules, enforced at the edge.** A write is rejected with `422` and a problem document naming the offending field when it uses a Theme absent from `config/content-manifest.json`, a tag absent from `TAGS.md`, a difficulty or type outside the allowed set, a Lab `question_ref` that resolves to nothing, or a malformed `id`. The existing validators define these rules — call into shared logic rather than restating the rules in a second place where they can drift.
- `POST` on an existing `id` → `409`. Any mutation of a missing `id` → `404`. `PATCH` applies only the supplied fields and leaves the rest untouched.
- **Writes update `content_hash` and `updated_at`** so a subsequent read returns the new ETag, and so slice 5's Export sees a coherent record.
- Every write is recorded in an append-only audit table — `id`, method, timestamp, resulting `content_hash` — so Export and Drift investigation have a trail. Reads never touch it.

## Acceptance criteria

- [ ] Every write path in `api/openapi.yaml` is implemented; none returns `501`.
- [ ] Round trip: `POST` a Question, read it back and get identical field values, `PATCH` one field and see only that field change, `DELETE` it and get `404` afterwards.
- [ ] Auth: no header → `401`; wrong key → `403`; correct key → success. With the environment variable unset, every write returns `503` and no data changes.
- [ ] Concurrency: no `If-Match` → `428`; stale `If-Match` → `412`; a concurrent-update scenario (read hash, someone else writes, you write with the old hash) is covered by a test and returns `412`.
- [ ] Validation: a test per rejected rule — unknown Theme, unknown tag, bad difficulty, bad type, dangling `question_ref`, malformed `id` — each returning `422` with the offending field named in the problem document.
- [ ] `409` on duplicate `POST`; `404` on mutating an unknown `id`.
- [ ] No test, log line, or error body contains the Write credential.
- [ ] The coverage census passes with every write status code covered: 200, 201, 204, 401, 403, 404, 409, 412, 422, 428, 503.
- [ ] `pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95` passes.
- [ ] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

## Inherited from slice 0003

- `api/content.py` is the adapter between the API and `contentdb`; `CONTENT_API_STORE=api.content:content_store`
  is the documented wiring. Do not hand `create_app` a raw `contentdb.store.Store` — it satisfies the
  protocol structurally but not the seam, and startup now refuses it with `StoreDoesNotConform`.
- Reads share one read-only SQLite connection serialized under a re-entrant lock, because CPython caches
  prepared statements per connection and two threads reusing one raised `InterfaceError`. Your writer must
  respect that lock rather than opening a second path to the file without thought.
- Every read endpoint is swept against a store built from the committed corpus. Extend that sweep to writes;
  it is the test class that catches an in-memory fake diverging from the real store, and it has already
  earned its place twice.
- Flipping the last eight `x-implementation: stub` markers is your slice's job. When they are gone the
  release gate's "no stub remains" condition is met.

## Notes

- Flip every write operation from `x-implementation: stub` to `x-implementation: implemented` in `api/openapi.yaml`. No stub may remain after this slice — the release gate checks. See the epic's **A complete contract, with stubs marked** section.
- Work in a git worktree on branch `feature/api-write-surface`.
- Use the `tdd` skill, and write the failure-path tests first — they are the point of this slice.
- The store is opened writable here; keep the read path's connection handling coherent with slice 3's, and say in the docstring how concurrent readers and a writer coexist under SQLite's locking.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).

## Completion report

The dispatched agent implemented the service and was killed by a session limit while building the test
helpers; the coordinator finished the suite, closed two gaps, and verified everything.

### What the agent built

`api/writes.py` (the Write credential, corpus-rule validation, the audit trail), the write half of
`api/content.py` against the real store, the routes in `api/app.py`, and a refactor of `contentdb/corpus.py`
so its rules can read a document in memory rather than only a file on disk. **No `x-implementation: stub`
remains** in the contract.

The validation design is worth recording: a candidate write is rendered through `contentdb.export` and then
re-read through `contentdb.corpus`, so the only records the store can hold are ones Export can reproduce.
That makes "the API cannot create a record that breaks the Drift gate" a structural property rather than a
promise.

### What the coordinator added

- `tests/api/test_writes.py` — 69 checks, failure paths first: every write refused without a credential,
  with the wrong credential, and with the credential unconfigured (`503`); `428` and `412` across all six
  mutations; the concurrent-writer race; `409` on duplicate create and on deleting a Question a Lab points
  at; `422` per corpus rule with the offending field named; and an assertion that no refusal body ever
  contains a credential.
- `tests/api/test_write_corpus.py` — the write surface against a **real Ingest-built store**, not the fake:
  create/read/replace/delete, persistence across reopening the database, the audit trail, and the loop that
  matters — API write → Export → Ingest, proving a written record comes back through Markdown.
- Rewrote the coverage census: with no stubs left, it now produces every documented status of all eight
  write operations itself, and its meta-test proves the marker is load-bearing against a synthetic contract
  rather than a real stub.

### A defect found while writing the census

`PATCH` accepted a field the contract does not publish — patching `theme` returned `200` and silently
changed nothing, so a client would believe it had moved the Question. Identity is deliberately not patchable.
The four write schemas now set `additionalProperties: false`, the Pydantic models `extra="forbid"`, and an
unpublished field is a `422`.

### Verification

```
pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95  → 378 passed, 95.09%
python tests/run_all_tests.py                                      → 195 checks / 62 modules
python scripts/build_site.py                                       → 1179 pages, stdlib only
python -m contentdb.drift                                          → clean, exit 0
grep -c "x-implementation: stub" api/openapi.yaml                  → 0
```

Two sabotage checks, applied and reverted: making the credential check accept anything fails **12** tests;
disabling the `If-Match` precondition fails **19**. (A third attempt was a no-op — inserting `pass` before a
`raise` — and its green run proved nothing; it was redone properly.)

### Left for human review

- The Write credential is read from the environment and never logged or echoed; a test asserts it appears in
  no refusal body. Choosing and distributing the real value is an operational decision for slice 0006.
- `DELETE` on a Question a Lab references answers `409`. That is referential integrity, not a limitation:
  the alternative is a `question_ref` that cannot be exported.
