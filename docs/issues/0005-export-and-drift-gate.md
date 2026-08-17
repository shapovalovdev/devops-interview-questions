# Export to Markdown and the CI Drift gate

| | |
| --- | --- |
| **Status** | `blocked` |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | 0001 |
| **Branch** | `feature/content-export-drift` |

Part of the Content API v1 epic. **Read the epic first.**

Depends on slice 1 (Content store and Ingest), merged to `main` before this starts.

Ingest is one-way: Markdown becomes a Content store. This slice builds the return path — **Export**, which renders store records back to Markdown files — and the **Drift** gate that keeps the two honest. Without it, a write through the API is invisible to git, to review, and to the content validators, and ADR 0001's promise that Markdown stays the durable record is just a sentence.

## Scope

- **Export.** `python -m contentdb.export --database build/content.db --output .` writes every stored Question and Lab back to its `source_path` as Markdown, in the exact format the corpus already uses: front matter field order, quoting style, list style, body layout. Standard library only.
- **Round-trip fidelity.** Ingest → Export over an unmodified corpus must reproduce every file byte-for-byte. Any file that does not round-trip is a bug in this slice — either the parser lost something or the renderer guesses. Do not "fix" it by rewriting the corpus to match the renderer; the corpus is the specification.
- **Drift detection.** `python -m contentdb.drift` builds a store from the committed corpus, exports it to a temporary tree, and diffs. Clean → exit 0. Any difference → exit non-zero with a readable per-file diff naming the field that differs.
- **The CI gate.** Wire the drift check into `.github/workflows/validate-questions.yml` so a corpus that cannot round-trip fails the build.
- **Document the workflow** in `docs/publishing.md` or a new `docs/content-api.md`: how a change authored through the API becomes a reviewed commit — Export, inspect the diff, commit, PR, existing validators run. Be explicit that a write is not landed until it is Markdown in `main`.

## Acceptance criteria

- [ ] Ingest → Export over the committed corpus reproduces every `questions/**/*.md` and `labs/**/*.md` byte-for-byte, asserted per file with the first differing file named on failure.
- [ ] `python -m contentdb.drift` exits 0 on the committed corpus and non-zero on a deliberately perturbed store, with a diff identifying the changed file and field.
- [ ] Export refuses to write outside the repository tree or to a path that is not `questions/<theme>/<slug>.md` or `labs/<theme>/<slug>.md` — a store row with a hostile `source_path` must not become a path traversal.
- [ ] Export is idempotent: running it twice changes nothing the second time.
- [ ] The drift check runs in CI and fails the workflow when it fails.
- [ ] Tests are picked up by `python tests/run_all_tests.py`, run without network access, and cover round-trip fidelity, drift detection both ways, path-traversal refusal, and idempotence.
- [ ] `python tests/run_all_tests.py` and `python scripts/build_site.py` still pass.

## Inherited from slice 0001

- `contentdb` is built and merged. Ingest reads the corpus; you are writing the reverse. Read
  `contentdb/corpus.py` and `contentdb/frontmatter.py` first — they define what a record holds and how the
  corpus's YAML subset is parsed, and your renderer must be their exact inverse.
- Records cross the `Store` seam as **plain mappings** keyed by the epic's field names. `contentdb/models.py`
  holds query and page types only, not record dataclasses.
- `updated_at` is the file's git commit time in UTC, falling back to `1970-01-01T00:00:00Z` when git cannot
  answer. **CI checks out shallow** (`actions/checkout@v4` with no `fetch-depth`), so every file would take
  the fallback there. Nothing depends on it today, but your Drift gate might: if it does, set
  `fetch-depth: 0` on the checkout in the workflow you touch, and say in the issue report that you did.

## Notes

- Work in a git worktree on branch `feature/content-export-drift`.
- Use the `tdd` skill.
- Round-trip fidelity across a corpus this size is the hard part. Start by exporting one file and diffing, then widen — and when a file will not round-trip, report what the corpus does that the model does not capture instead of trimming the corpus to fit.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).
