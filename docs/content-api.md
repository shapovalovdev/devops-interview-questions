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

## Running the service

The API is a separate image from the static site, and the site does not depend on it. Both come up together
with Compose:

```bash
docker compose up --build          # site on :8080, API on :8000
```

Or the API alone:

```bash
docker build -f Dockerfile.api -t devops-questions-api .
docker run -p 8000:8000 devops-questions-api
curl http://127.0.0.1:8000/api/v1/health
```

The Content store is built into the image at build time, so a container starts with the whole corpus and no
volume to mount. `openapi.json` is served at the root; the hand-written contract it is checked against is
`api/openapi.yaml` in the repository.

Locally, without Docker:

```bash
pip install -r requirements-api.txt
python -m contentdb.ingest --output build/content.db
CONTENT_API_STORE=api.content:content_store CONTENT_STORE_PATH=build/content.db \
  uvicorn api.app:app --reload
```

## Configuration

| Variable | Meaning |
| --- | --- |
| `CONTENT_API_STORE` | The store factory, as `<module>:<callable>`. Use `api.content:content_store`. |
| `CONTENT_STORE_PATH` | The Content store file the factory opens. |
| `CONTENT_API_CORPUS_ROOT` | Where `config/content-manifest.json` and `TAGS.md` live. Writes are validated against them. |
| `CONTENT_API_WRITE_KEY` | The Write credential. **Unset means the service serves read-only** and refuses every write with `503`. |

With no store configured the service refuses to start rather than serving invented content, and a store that
satisfies the `Store` protocol structurally but not its contract is refused at start-up with a message naming
the method that disagreed.

## Writing through the API

Reads are anonymous. Every mutating request carries `X-API-Key`, and every `PUT`, `PATCH`, and `DELETE`
carries `If-Match` with the item's current `ETag`:

```bash
KEY=$(openssl rand -base64 24)
docker run -p 8000:8000 -e CONTENT_API_WRITE_KEY="$KEY" devops-questions-api

ETAG=$(curl -sS -D- -o/dev/null http://127.0.0.1:8000/api/v1/questions/kubernetes/some-slug \
       | awk '/^etag:/ {print $2}' | tr -d '\r')
curl -X PATCH http://127.0.0.1:8000/api/v1/questions/kubernetes/some-slug \
     -H "X-API-Key: $KEY" -H "If-Match: $ETAG" -H 'Content-Type: application/json' \
     -d '{"difficulty": "senior"}'
```

Refusals are RFC 9457 problem documents: `401` without a credential, `403` with the wrong one, `503` when
none is configured, `428` without a validator, `412` with a stale one, `409` on a duplicate create or on
deleting a Question a Lab still points at, and `422` when the write would break a corpus rule — with the
offending field named.

A write is still not landed until it is Markdown in `main`: Export it, review the diff, and commit.

## Tests

| Command | What it covers |
| --- | --- |
| `pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95` | The API suite and the coverage gate |
| `python tests/e2e/test_content_api_e2e.py` | The packaged service, over real HTTP, in a container |
| `python tests/run_all_tests.py` | The standard-library corpus suite, which never imports FastAPI |

Two guards keep the contract honest, and both are meant to fail loudly. The **contract test** compares the
served schema against `api/openapi.yaml`; the **coverage census** requires every status code the contract
documents to be produced by a real request. Neither may be weakened to make a change pass.

The end-to-end suite exists because `TestClient` cannot see packaging. It has already earned that: it caught
an image that served reads but refused every write, because the Theme and Tag vocabularies were not in it,
and a store file that was writable in a directory the service user could not write to.
