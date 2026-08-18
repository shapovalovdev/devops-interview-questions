# The Content API and the Markdown corpus

The Content store is a SQLite database holding every Question and Lab, built from the Markdown corpus by
Ingest. The Content API serves and modifies it. This page explains the rule that keeps those two honest.

## Markdown is still the record

The store is a derived, disposable artifact: it is rebuilt from `questions/` and `labs/` on every build, and
nothing may live in it that does not survive a rebuild. That matters because the API can write, and a write
that only ever lived in a database would bypass the things this repository exists to guarantee — the content
policy, source verification, the coverage target, and human review.

So a write is not landed when the API returns `200`. It is landed when it is Markdown in `main`.

```text
questions/**.md   ──Ingest──▶   Content store   ──▶   Content API
labs/**.md        ◀──Export──                          writes
      ▲                                                  │
      └──────────────── Drift gate in CI ────────────────┘
```

## Turning an API write into a reviewed commit

1. **Export.** `python -m contentdb.export --database build/content.db` renders every store record back to
   its source file. Unchanged files are left alone, so the diff shows only what actually changed.
2. **Read the diff.** `git diff` is the review surface. An unexpected file in it means the store and the
   corpus disagreed about something other than your edit — investigate before committing.
3. **Commit and open a pull request.** From here it is an ordinary content change.
4. **CI validates it.** The existing validators check the front matter, the Tag vocabulary, the Theme
   manifest, source liveness, and the coverage target. None of them can be satisfied from the database.

## The Drift gate

`python -m contentdb.drift` builds a store from the committed corpus, exports it into a throwaway tree, and
diffs the result against the corpus. Clean means every file the store holds is exactly the file on disk.

It runs in CI on every pull request and push to `main`. When it fails it prints a unified diff naming the
file and the lines that differ, because "something drifted" is not actionable.

Drift failing means one of three things:

- an API write has not been exported and committed yet;
- Export has a bug and cannot reproduce some shape the corpus uses;
- a corpus file uses a shape Ingest silently loses.

The third is the dangerous one, and it has happened: Ingest sorted each record's tags, which discarded the
author order that 1025 of the 1111 corpus files rely on. The corpus is the specification — when a file will
not round-trip, the renderer or the parser is what is wrong, never the file.

## Commands

| Command | What it does |
| --- | --- |
| `python -m contentdb.ingest --output build/content.db` | Build the Content store from the corpus |
| `python -m contentdb.export --database build/content.db` | Render store records back to Markdown |
| `python -m contentdb.drift` | Fail if the corpus and a store built from it disagree |

All three are standard-library only and run with nothing installed, because they run inside the site build.

The decision behind this design, and the alternatives rejected, are recorded in
[ADR 0001](./adr/0001-sqlite-content-store-behind-a-fastapi-content-api.md).
