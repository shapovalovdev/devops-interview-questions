# Complete read surface over the real store

| | |
| --- | --- |
| **Status** | `needs-review` |
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

- [x] Every read path in `api/openapi.yaml` is implemented; none returns `501`.
- [x] Responses match the contract exactly — the slice 2 contract test still passes, unchanged in strictness.
- [x] A real corpus check: with a store built by Ingest from the committed corpus, `GET /api/v1/questions?theme=kubernetes&difficulty=senior` returns only senior Kubernetes Questions, and the count matches what a direct filesystem scan of the front matter reports. Assert against the corpus, not a hard-coded number.
- [x] `GET /api/v1/search?q=` returns Questions and Labs together, ranked, with `kind` distinguishing them, and honours `kind=` to restrict.
- [x] Unknown `id`, unknown theme, unknown tag, unknown path slug each return `404` in problem+json.
- [x] ETag and `If-None-Match` behave as specified, including a `304` carrying no body.
- [x] The coverage census passes with every read status code covered, including `304` and `404`.
- [x] `pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95` passes.
- [x] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

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

## Completion report

**Branch** `feature/api-read-surface` (worktree `.claude/worktrees/capi-0003`), five commits on top of
`main`, newest last:

| Commit | What it does |
| --- | --- |
| `ce9468d` | Wire `contentdb.store.Store` in through `CONTENT_API_STORE`; `GET /api/v1/questions/{theme}/{slug}`, ETags, conditional reads |
| `d679c35` | `GET /api/v1/labs` and `GET /api/v1/labs/{theme}/{slug}`, with the Question↔Lab link resolved in both directions |
| `f893672` | `GET /api/v1/themes`, `/themes/{name}`, `/tags`, `/learning-paths`, `/learning-paths/{slug}` |
| `598edd5` | `GET /api/v1/search`, ranked across both kinds, with `kind=` restricting |
| `fdc8f2a` | Every single-item read held to one conditional contract; 404-versus-empty pinned |

A sixth commit refreshes the two module docstrings that still described the tracer bullet.

### What was built

- **`api/content.py`** is new: the adapter from `contentdb.store.Store` to the `api.store.Store`
  protocol, and the only module in `api/` that names `contentdb`. It wraps the bounded catalogues in
  the seam's `Page`, resolves each search hit into a whole item, and translates an unparseable
  free-text query into `api.store.InvalidQuery`.
- **`CONTENT_API_STORE=api.content:content_store`** is the one door. It reads `CONTENT_STORE_PATH`
  (default `build/content.db`) and raises `ContentStoreUnavailable` naming that path and
  `python -m contentdb.ingest --output build/content.db` when the file is missing or is not a
  database. No second mechanism was added.
- **Every read operation is `x-implementation: implemented`.** The eight remaining `stub` markers are
  all writes (`createQuestion`, `replaceQuestion`, `patchQuestion`, `deleteQuestion`, and the four Lab
  equivalents), which slice 4 owns. No read answers `501`.

### Decisions worth a reviewer's attention

1. **The shared read-only connection is taken under a re-entrant lock.** The issue asked which sharing
   model was chosen and why; the answer is one process-wide connection, serialized. This was not a
   precaution: with `sqlite3.threadsafety == 3` and four threads reading one connection, the suite
   reproduced `sqlite3.InterfaceError: bad parameter or other API misuse` (SQLITE_MISUSE), because
   CPython's `sqlite3` caches prepared statements per connection and two threads can hand SQLite the
   same statement. `tests/api/test_content_store.py::test_one_shared_store_answers_readers_on_many_threads`
   guards it, and `api/content.py`'s module docstring records the reasoning.
2. **The Question↔Lab link is served as an RFC 8288 `Link` header, not as a new body field.** The epic
   pins a Question's fields and none of them is a list of Labs, and the contract's `Question` schema has
   no place to put one, so a Question's response carries `Link: </api/v1/labs?question_ref=…>` plus one
   link per Lab that exists today, and a Lab's response carries a link back to its Question when the
   reference resolves. The queryable direction — `GET /api/v1/labs?question_ref=<id>` — is contract
   surface and is tested. **If the coordinator wants the link in the body instead, that is a contract
   change to `Question` and should be decided on the epic, not here.**
3. **A search hit crosses the seam as `{"kind", "score", "item"}`.** Slice 2 left `search` unimplemented
   and its result shape unpinned; the fake returned bare items, which cannot express two kinds in one
   ranked list. `api/testing.py` and the one assertion in `tests/api/test_store.py` that read the old
   shape were updated. `score` is derived from rank, because SQLite's bm25 score does not cross the
   seam and the contract defines the score as comparable only within one response.
4. **The served schema now drops the `422` FastAPI adds by reflex.** FastAPI documents a validation
   error on every operation that parses a parameter, including `GET /api/v1/questions/{theme}/{slug}`,
   whose only parameters are two path strings. The contract documents `422` only where a client can
   provoke one, and the census demands a real request per documented status, so
   `only_documented_validation_errors()` removes a `422` that carries nothing but the framework's own
   model. Where the contract does document one, the problem document survives. Neither the contract
   test nor the census was weakened; both still compare exactly what they compared before.
5. **"Unknown tag returns 404" could not be implemented as written.** The contract publishes no
   operation that reads a single tag — `GET /api/v1/tags` is the whole tag surface — so an unknown tag
   can only reach the service as a filter value, where it is a legitimate query with an empty answer.
   Unknown *ids* (Question, Lab, Theme, learning path) are all `404` in problem+json;
   `test_a_filter_that_matches_nothing_is_an_empty_page_not_a_404` pins the other half. Flagged rather
   than resolved by inventing an endpoint the contract does not describe.
6. **`pytest.ini` now collects the Content store's own checks too.** The gate is
   `--cov=api --cov=contentdb`, and `testpaths = tests/api` alone measured `contentdb` only through
   whatever the API tests happened to touch (93%, below the gate). The three `tests/test_contentdb_*.py`
   modules are plain `unittest` and still run under `tests/run_all_tests.py` with nothing installed;
   listing them here changes only what the coverage number describes. `tests/run_all_tests.py`'s
   non-recursive `tests/test_*.py` glob is untouched.

### Commands run, with their real output

```
$ .venv/bin/python -m pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95 -q
Name                       Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
api/__init__.py                0      0      0      0   100%
api/app.py                   206      0     40      0   100%
api/content.py                80      0      2      0   100%
api/demo.py                    4      0      0      0   100%
api/models.py                149      0      0      0   100%
api/store.py                  40      0      0      0   100%
api/testing.py                95      0     28      0   100%
contentdb/__init__.py          2      0      0      0   100%
contentdb/corpus.py          185     12     64     11    91%
contentdb/frontmatter.py      61      2     28      2    96%
contentdb/ingest.py           79     17      4      2    77%
contentdb/models.py           37      0      0      0   100%
contentdb/schema.py            4      0      0      0   100%
contentdb/store.py           135      1     18      1    99%
------------------------------------------------------------
TOTAL                       1077     32    184     16    96%
Required test coverage of 95% reached. Total coverage: 96.19%
273 passed, 3 warnings in 6.12s
```

```
$ .venv/bin/python tests/run_all_tests.py
...
Validated vendor-honesty mappings across cloud, databases, and infrastructure-as-code.
Ran 188 checks across 61 test modules.          # exit status 0
```

```
$ .venv/bin/python scripts/build_site.py --output <tmp>
Rendered 1178 Markdown pages into <tmp>          # exit status 0
```

```
$ python -m contentdb.ingest --root . --output <tmp>/content.db
Ingested 1100 Questions and 11 Labs across 40 Themes, 219 Tags, and 3 learning paths,
with full-text search.
```

`scripts/build_site.py` also runs clean under the system `python3` (3.9.6, no third-party package
installed); `tests/run_all_tests.py` needs a newer interpreter for the repository's own syntax, so it
was run with the virtualenv's Python 3.13 — the no-third-party guarantee itself is asserted by
`tests/test_api_dependency_separation.py`, which blocks every third-party import in a subprocess and
passed.

### Guard tests, deliberately sabotaged and confirmed to fail

- Making `conditional()` ignore `If-None-Match`: **10 failures**, including every
  `test_every_single_item_read_answers_304_with_no_body` case and the census's `304` producers.
- Flipping `getLab` back to `x-implementation: stub` while the route stays implemented:
  `test_the_census_covers_every_response_the_contract_promises` **fails**, reporting the `501` the
  contract now promises and nothing produces.

Both files were restored and the suite re-run green before committing.

### Tests added

- `tests/api/test_content_store.py` — the adapter: protocol conformance, the seam's shapes, hit
  ranking across a page boundary, concurrency on the shared connection, failing fast on a missing or
  corrupt store, and reaching the service through `CONTENT_API_STORE`.
- `tests/api/test_reads.py` — every read endpoint against a store Ingest built, plus four tests against
  the **committed corpus**: the epic's `theme=kubernetes&difficulty=senior` filter counted by scanning
  front matter (not `contentdb.frontmatter`, so the expectation cannot agree with a bug), Theme counts
  against a filesystem scan, every Lab's `question_ref` read back as a Question, and every
  learning-path step read back as a Question.
- `tests/api/test_coverage_census.py` — a producer per documented status of all eleven implemented
  operations, `304`s produced the way a client produces them.

### Left for human review

- Decision 2 (the Question↔Lab link as a header rather than a body field) and decision 5 (no
  single-tag endpoint exists to return `404` from) are the two places where the issue text and the
  published contract disagree. Both were resolved in favour of the contract.
- `contentdb/ingest.py` sits at 77% branch coverage: its `main()` argument parsing and the
  FTS5-unavailable fallback are exercised by `tests/test_contentdb_ingest.py` only in part. Nothing in
  this slice touched `contentdb/`, and the total is above the gate, so it was left alone.
- **On merge with `main`:** this branch was cut before slice 0005 landed, and `main` has since added
  Export and the Drift gate, including `tests/test_contentdb_export.py`. The coverage gate now measures
  all of `contentdb`, so that file needs adding to `testpaths` in `pytest.ini` beside the three
  `tests/test_contentdb_*.py` modules already listed, or `contentdb/export.py` will be counted without
  its own tests and the 95% gate may fail for reasons that have nothing to do with this slice.
- Slice 6 owns packaging; nothing here sets `CONTENT_API_STORE` in the image. A deployment runs
  `python -m contentdb.ingest --output build/content.db` and then
  `CONTENT_API_STORE=api.content:content_store uvicorn api.app:app`.
