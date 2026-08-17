# Content store schema and Ingest

| | |
| --- | --- |
| **Status** | `in-progress` |
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

- [ ] `python -m contentdb.ingest --output build/content.db` builds the store from a clean checkout with no third-party package installed.
- [ ] Every active Question and every Lab in the corpus appears in the store, with the field values its Markdown file declares. Ingest fails loudly — non-zero exit, named file, named field — on a file it cannot parse; it never silently skips one.
- [ ] Counts in the store match the corpus: assert against a fresh `find questions -name '*.md' | wc -l` and the Lab equivalent, not against a hard-coded number.
- [ ] Running Ingest twice produces identical bytes (test asserts sha256 equality of the two files).
- [ ] Every Theme referenced by a Question or Lab exists in `config/content-manifest.json`; every tag exists in `TAGS.md`; every Lab's `question_ref` resolves to a stored Question. Ingest fails if not.
- [ ] `Store` answers each documented query correctly, including filter combinations, pagination boundaries (`offset` past the end returns an empty page with the true `total`), and search.
- [ ] `build/` stays git-ignored; the store is never committed.
- [ ] Tests live in `tests/` and are picked up by `python tests/run_all_tests.py`. They must run without network access. Cover: parsing (including a malformed fixture), determinism, every `Store` query method, filter combinations, pagination edges, search ranking, and the failure paths above.
- [ ] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

## Notes

- Work in a git worktree on branch `feature/content-store-ingest`.
- Do not modify `assets/questions.js` or the site build in this slice.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).
