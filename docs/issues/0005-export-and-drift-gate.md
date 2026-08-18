# Export to Markdown and the CI Drift gate

| | |
| --- | --- |
| **Status** | `needs-review` |
| **GitHub** | [#173](https://github.com/shapovalovdev/devops-interview-questions/issues/173) |
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

## Completion report

Implemented by the coordinator directly, after three dispatched agents died to environmental failures
(a stall, the machine sleeping, a session limit) without writing a line between them.

Commits on `feature/content-export-drift`: `35547ef`, `e7aedaa`, `5c44568`.

### Round-trip result

**1111 of 1111 files round-trip byte for byte — 1100 Questions and 11 Labs — read back out of a built
store, not merely out of freshly parsed records.** No file needed a special case, and no corpus file was
edited to make the renderer pass.

That was only possible after fixing a real defect in the merged Ingest, which the round trip exposed:

- `contentdb/corpus.py` sorted and de-duplicated each record's tags;
- `contentdb/ingest.py` sorted them again into `question_tags` / `lab_tags`;
- `contentdb/store.py` sorted them a third time on read.

1025 of the 1111 corpus files list their tags non-alphabetically, so author order — information the corpus
carries — was being discarded three times over. Both tag tables now carry an explicit `position`, following
the precedent `question_sources` already set, and the store returns tags in file order. One merged test
asserted the sorted behavior and was updated, with a comment explaining why.

Fidelity was tractable because Ingest already keeps `body_markdown` verbatim, so only front matter is
re-rendered. The corpus's uniformity was measured, not assumed: one field order per kind, plain scalars for
Questions and double-quoted for Labs, every file newline-terminated, no CRLF, no title containing `:`, no
quoted value containing an embedded quote. The renderer asserts those invariants and raises rather than
approximating when one does not hold.

### Commands run, real output

```
$ python tests/run_all_tests.py
Ran 192 checks across 62 test modules.                         exit 0   (baseline 188 / 61)

$ python tests/test_contentdb_export.py
Ran 16 tests in 2.117s   OK

$ python -m contentdb.drift
No drift: every Question and Lab round-trips through the Content store unchanged.   exit 0

$ python -m contentdb.export --database build/content.db --output .   # twice
Exported 1111 files: 0 written, 1111 already current.
Exported 1111 files: 0 written, 1111 already current.
   → git status clean both times: Export reproduces the corpus and is idempotent

$ python -m contentdb.ingest --output a.db && python -m contentdb.ingest --output b.db
   → identical sha256; the position column did not cost determinism

$ python scripts/build_site.py
Rendered 1178 Markdown pages                                   exit 0, standard library only
```

### The gate was proved to bite

A store row was tampered with directly (`UPDATE questions SET title = 'Tampered title'`), exported, and
compared. `drift.compare` returned exactly one difference, a unified diff naming the file and both titles.
Covered as a test, alongside a store that has lost a record entirely.

### Left for human review

- CI now checks out with `fetch-depth: 0`. `updated_at` is each file's git commit time, so a shallow clone
  pins every record to the epoch. This makes the content job clone the full history — a cost worth knowing
  about, though the alternative is a Drift check comparing against a store CI cannot reproduce.
- `docs/content-api.md` documents the Export → review → commit workflow. Slice 0006 is expected to extend
  the same file with how to run and package the service; it should add sections rather than rewrite it.
