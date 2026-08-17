# Content store schema and Ingest

| | |
| --- | --- |
| **Status** | `closed` |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | — |
| **Branch** | `feature/content-store-ingest` |

Part of the Content API v1 epic. **Read the epic first** — it pins the Question, Lab, Theme, Tag, and LearningPath shapes this slice must produce. Do not renegotiate them here.

This slice builds the **Content store**: the SQLite database that holds every Question and Lab, and the **Ingest** step that fills it from the Markdown corpus. It has no HTTP surface — the API arrives in slice 2 and is wired to this store in slice 3.

## Scope

Deliver a `contentdb` package (standard library only — `sqlite3`, no ORM, no third-party dependency, because Ingest runs in the site build where nothing is installed) exposing:

- **A schema.** Tables for questions, labs, themes, tags, question↔tag and lab↔tag relations, sources, and learning paths, with the columns the epic's shapes require. Foreign keys on. Indexes on the columns the API filters by: `theme`, `difficulty`, `type`, and tag joins.
- **Ingest.** `python -m contentdb.ingest --output build/content.db` parses every file under `questions/**/*.md` and `labs/**/*.md`, plus `config/content-manifest.json`, `config/learning-paths.json`, and `TAGS.md`, and writes the store. Reuse the front-matter parsing already proven in `tests/validate_labs.py` and `scripts/generate_question_catalog.py` rather than inventing a third parser — factor out one parser they can all agree on if that is cleaner, but do not break the existing callers.
- **Full-text search.** An FTS5 table over title, prompt, and body so slice 3's `q=` parameter is a store capability, not a `LIKE` scan. Fall back gracefully with a clear error if the runtime `sqlite3` lacks FTS5.
- **A read interface.** A `Store` class with the query methods the API will need — list/get questions and labs with filters and pagination, themes, tags, learning paths, search. Slice 2 codes against this interface; keep the method signatures obvious and the return types plain dataclasses so a fake is trivial to write.
- **Determinism.** Two Ingest runs over an unchanged corpus produce byte-identical database files. Sort every insert; do not store wall-clock time. `updated_at` comes from the source file's git commit time or a fixed value — pick one, document it, and make it reproducible.
- **`content_hash`.** sha256 of the source file's bytes, stored per row. The API uses it as an ETag.

## Acceptance criteria

- [x] `python -m contentdb.ingest --output build/content.db` builds the store from a clean checkout with no third-party package installed.
- [x] Every active Question and every Lab in the corpus appears in the store, with the field values its Markdown file declares. Ingest fails loudly — non-zero exit, named file, named field — on a file it cannot parse; it never silently skips one.
- [x] Counts in the store match the corpus: assert against a fresh `find questions -name '*.md' | wc -l` and the Lab equivalent, not against a hard-coded number.
- [x] Running Ingest twice produces identical bytes (test asserts sha256 equality of the two files).
- [x] Every Theme referenced by a Question or Lab exists in `config/content-manifest.json`; every tag exists in `TAGS.md`; every Lab's `question_ref` resolves to a stored Question. Ingest fails if not.
- [x] `Store` answers each documented query correctly, including filter combinations, pagination boundaries (`offset` past the end returns an empty page with the true `total`), and search.
- [x] `build/` stays git-ignored; the store is never committed.
- [x] Tests live in `tests/` and are picked up by `python tests/run_all_tests.py`. They must run without network access. Cover: parsing (including a malformed fixture), determinism, every `Store` query method, filter combinations, pagination edges, search ranking, and the failure paths above.
- [x] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

## Notes

- Work in a git worktree on branch `feature/content-store-ingest`.
- Do not modify `assets/questions.js` or the site build in this slice.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).

## Completion report

**Branch** `feature/content-store-ingest` — implementation commit `a5d7526`; this report is the commit that follows it on the branch.

### What was built

`contentdb`, standard library only, in three layers so each is usable and testable without the one above it:

| module | responsibility |
| --- | --- |
| `contentdb/frontmatter.py` | the one front-matter parser; the YAML subset proven in `tests/validate_labs.py` and `scripts/generate_question_catalog.py`, extended with the block-list-of-mappings shape Question `sources` uses |
| `contentdb/corpus.py` | Markdown → validated records: vocabularies, enums, referential integrity, `prompt`/`answer_guide` extraction, `content_hash`, `updated_at` |
| `contentdb/schema.py` | the DDL: nine tables, foreign keys on, indexes on `theme`, `difficulty`, `type`, `question_ref`, and both tag joins, plus the FTS5 index created separately |
| `contentdb/ingest.py` | writes the store and owns the CLI |
| `contentdb/store.py` | the read seam the Content API sits on |
| `contentdb/models.py` | the query dataclasses and the `Page` envelope that cross that seam |

The existing callers were not modified: the parser was extracted alongside them, and a test re-parses the whole live corpus with both the old parsers and the new one and demands identical results, so a third dialect cannot appear unnoticed.

### Commands run, with their real output

```
$ python tests/run_all_tests.py
Ran 187 checks across 60 test modules.            # exit 0 (baseline before this slice: 172 checks / 57 modules)

$ python scripts/build_site.py
Rendered 1178 Markdown pages into .../build/site  # exit 0, no third-party package installed

$ python -m contentdb.ingest --output build/content.db
Ingested 1100 Questions and 11 Labs across 40 Themes, 219 Tags, and 3 learning paths,
with full-text search. Wrote build/content.db.    # exit 0

$ find questions -name '*.md' | wc -l  ->  1100   # matches the store
$ find labs -name '*.md' | wc -l       ->    11   # matches the store

$ python -m contentdb.ingest --output build/second.db   # a second, separate process
$ shasum -a 256 build/content.db build/second.db
4f01fdfb37db7951abe6f0d753dfe1cc58ed90b49da3f4573206d8a32c7c8507  build/content.db
4f01fdfb37db7951abe6f0d753dfe1cc58ed90b49da3f4573206d8a32c7c8507  build/second.db
```

**Ingested:** 1100 Questions, 11 Labs, 40 Themes, 219 Tags, 3 learning paths — an 11 MB store.

### Tests

72 test methods in three new modules, which `tests/run_all_tests.py` counts as 15 checks:

| module | methods | covers |
| --- | --- | --- |
| `tests/test_contentdb_frontmatter.py` | 11 | supported shapes, six malformed-front-matter refusals, and full-corpus agreement with both existing parsers |
| `tests/test_contentdb_ingest.py` | 28 | field-level storage, corpus counts against a fresh walk, determinism, `content_hash`, foreign keys, and twelve loud-failure paths |
| `tests/test_contentdb_store.py` | 33 | every query method, filter combinations, sort keys, pagination edges, search ranking, the FTS5-absent fallback, and read-only enforcement |

`tests/contentdb_fixtures.py` builds a small corpus — eight Questions, three Labs, three Themes — so query answers are known by counting the fixture. It is deliberately not named `test_*.py`, which is what `run_all_tests.py` discovers. No test touches the network.

Two checks were mutation-tested rather than merely observed to pass: injecting wall-clock time into `updated_at` makes the determinism check fail, and the search-ranking check asserts an order that is *not* the alphabetical one, so it is testing bm25 and not the tiebreak.

### Decisions taken inside the slice

- **`updated_at` is the source file's git commit time in UTC**, read in one batched `git log` pass and formatted from a Unix timestamp so the running machine's timezone cannot leak in. The issue allowed a fixed value; a constant was rejected because the Content API publishes this field. Where git cannot answer — no repository, as in a Docker build, or an uncommitted file — it falls back to `1970-01-01T00:00:00Z`, which keeps that environment deterministic too.
- **Determinism** comes from a fresh file per run, a pinned `page_size`, ordered inserts throughout, nothing derived from wall-clock time, and a closing `VACUUM`. The store is written to a sibling `.building` file and renamed into place, so a failed run leaves nothing behind.
- **`prompt` falls back to the `#` heading.** 75 of the 1100 Questions ask their question in the heading and go straight to the answer guide. They are not malformed, so the heading becomes the prompt rather than Ingest failing or storing an empty string.
- **`question_ref` is stored as a Question `id`.** The corpus writes it as `<theme>/<slug>.md`; the epic pins it as an `id`. The `.md` is dropped on the way in, and Export (slice 5) puts it back.
- **`description` comes from the learning path's `audience` field.** `config/learning-paths.json` has no `description`; `audience` is the reader-facing blurb the epic's field describes. `prerequisites` is carried through as well, since the site already publishes it.
- **`tags` holds only Tags the corpus uses.** `TAGS.md` is the permitted vocabulary, not an inventory; publishing its unused entries would tell an API client that filtering by them returns something.
- **Themes publish all four difficulty bands, zeros included**, so a client charting a Theme's mix never has to guess whether a missing key means "none" or "not counted".

### Left for human review

1. **`models.py` no longer defines record dataclasses.** The previous agent's draft had `Question`, `Lab`, `Theme`, `Tag`, and `LearningPath` frozen dataclasses. The coordinator pinned plain mappings as the read seam, so they were removed rather than left as an unused second representation of the same records. `models.py` now holds `QuestionQuery`, `LabQuery`, `SearchQuery`, and `Page`. **Slice 2 should code against mappings.**
2. **One line of `docs/issues/0000-epic-content-api.md` was changed** — a pre-existing failure, not caused by this slice. `[`CONTEXT.md`](../../CONTEXT.md)` cannot resolve inside the built site, because `scripts/build_site.py` renders only `questions/` and `docs/` and never the repository root, so `test_build_site.py::OwnSiteBuildParity` failed on the branch HEAD before any work here (verified against a pristine `git archive HEAD`). It is now an unlinked `` `CONTEXT.md` `` reference, matching `docs/agents/domain.md`. **This file is shared with slice 2 — the coordinator may want to resolve it centrally.**
3. **CI checks out shallow.** `.github/workflows/` uses `actions/checkout@v4` with no `fetch-depth`, so `git log` sees one commit and most `updated_at` values would degrade to the `1970-01-01T00:00:00Z` fallback. Nothing breaks and no test depends on it, but whoever wires Ingest into CI (slice 5's Drift gate) should add `fetch-depth: 0`.
4. **Ingest is not yet wired into any workflow or the site build.** That is slice 5's Drift gate; this slice only guarantees the store can be built and read.
5. **An unquoted list item reading `- Key: value` parses as a mapping** in this YAML subset, so a Lab checklist step written that way would change type. Ingest refuses it loudly, naming the file and the field and saying to quote it, rather than storing it — but the underlying dialect limitation is inherited from the existing validators and is worth knowing about.
