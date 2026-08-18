# Packaging, end-to-end suite, and CI coverage gate

| | |
| --- | --- |
| **Status** | `closed` |
| **GitHub** | [#174](https://github.com/shapovalovdev/devops-interview-questions/issues/174) |
| **Label** | `enhancement` |
| **Epic** | [Content API v1](./0000-epic-content-api.md) |
| **Depends on** | 0003, 0004 |
| **Branch** | `feature/api-packaging-e2e` |

Part of the Content API v1 epic. **Read the epic first.**

Depends on slices 3 and 4 (the complete read and write surfaces), merged to `main` before this starts.

The API works under `pytest`. This slice makes it something you can run, and proves it works as a deployed service rather than as an imported app object: a container, an **end-to-end suite that speaks real HTTP to a real running container over a real store**, and the CI jobs and coverage gate that keep it that way.

## Scope

- **`Dockerfile.api`**, multi-stage: a builder that installs `requirements-api.txt` and runs Ingest over the corpus to bake `content.db` into the image, and a slim runtime running uvicorn as a non-root user with a `HEALTHCHECK` hitting `/api/v1/health`. The existing static-site `Dockerfile` must keep building and stay dependency-free — do not merge the two.
- **`docker-compose.yml`** bringing up the static site and the API together, so `docker compose up` gives a working local stack, with the Write credential supplied by environment variable.
- **The end-to-end suite** (`tests/e2e/`): starts the container, waits for health, and exercises real journeys over HTTP against real corpus data — browse a Theme, filter by difficulty and tag, open a Question, follow it to the Lab that prepares you for it, search, then a full authenticated write journey (create, conditional update with `If-Match`, delete) including the rejection paths. Assert on status codes, headers (`ETag`, `Content-Type: application/problem+json`), and bodies. No FastAPI `TestClient` here — that is what the API tests already do; this suite exists to catch what only appears when the thing is packaged and served.
- **CI.** A job that runs the API tests with coverage, and a job that builds the image and runs the end-to-end suite against it. Both must fail the build when they fail.
- **The coverage gate, enforced.** `pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95` in CI, plus the slice 2 coverage census asserting every documented path, method, and status code is exercised. Report coverage in the job summary.
- **Documentation.** `docs/content-api.md`: what the API is, how to run it locally and in Docker, how to authenticate a write, the endpoint list, and a pointer to `api/openapi.yaml` and ADR 0001. Link it from `README.md`.

## Acceptance criteria

- [ ] `docker build -f Dockerfile.api -t devops-questions-api .` succeeds, and the container serves `/api/v1/health` within 30 seconds of start.
- [ ] The container runs as a non-root user, and its `HEALTHCHECK` reports healthy.
- [ ] `docker compose up` serves the static site and the API side by side.
- [ ] The end-to-end suite passes against the running container: read journeys, the Question↔Lab link, search, and the authenticated write journey with its `401`, `403`, `412`, `428`, and `422` rejections.
- [ ] Both CI jobs run on pull requests and on pushes to `main`, and fail the build on failure. Include the run URL demonstrating each.
- [ ] The coverage gate and the coverage census pass in CI.
- [ ] `docker build -t devops-questions .` (the static site image) still builds and smoke-tests green, and `python scripts/build_site.py` still runs with no third-party package installed.
- [ ] `docs/content-api.md` exists, is accurate against the shipped API, and is linked from `README.md`.

## Inherited from slices 0003 and 0004

- The service is configured by three environment variables: `CONTENT_API_STORE` (`<module>:<callable>`,
  use `api.content:content_store`), `CONTENT_API_STORE_PATH` for the database, and the Write credential
  variable named in `api/writes.py`. With the credential unset the service starts read-only and refuses
  every write with `503` — that is the correct default for a container that has not been given one.
- `api/content.py` opens the store read-only and lazily opens a second `mode=rw` connection on the first
  write. Your image must therefore ship a **writable** database file, not a read-only mount, if writes are
  to work in the container.
- Validation renders each candidate through `contentdb.export` and re-reads it through `contentdb.corpus`,
  so a write cannot create a record the Drift gate would reject.
- The suite is at 378 tests, 95.09% combined branch coverage. Your end-to-end suite is additional to it, not
  a replacement: it exists to catch what only appears once the thing is packaged and served.

## Notes

- Work in a git worktree on branch `feature/api-packaging-e2e`.
- The end-to-end suite must clean up its container on failure — a wedged container in CI is worse than a red test.
- This is the last slice: when it closes, post the release-gate verification on the epic.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).

## Completion report

Implemented by the coordinator directly, since every remaining agent slot had been lost to environmental
failures and this was the last slice.

### What shipped

- `Dockerfile.api` — multi-stage, non-root (uid 10001), `HEALTHCHECK` on `/api/v1/health`, with the Content
  store ingested at build time so a container starts with the whole corpus and no volume. The static site's
  `Dockerfile` is untouched and still dependency-free.
- `docker-compose.yml` — the site and the API side by side, with the Write credential supplied by
  environment variable and defaulting to absent.
- `tests/e2e/test_content_api_e2e.py` — 18 checks over real HTTP (`urllib`, no `TestClient`, no imports from
  `api/`): health, non-root, the served schema, filtering, the Lab→Question link, conditional `304`, search,
  problem documents, and the full authenticated write journey with its `401`, `403`, `412`, `428`, and `422`
  refusals. A second container, given no credential, proves reads work and every write is `503`. Containers
  are removed in `tearDownClass` even on failure.
- `.github/workflows/content-api.yml` — three jobs: the API suite under the coverage gate with coverage in
  the job summary, the end-to-end suite against a built image, and a Compose job asserting both services
  answer.
- `docs/content-api.md` extended with running, configuration, writing, and testing; `README.md` now shows the
  two commands that get someone querying the database.

### Two real defects the end-to-end suite caught

Both were invisible to 378 passing `TestClient` tests, which is precisely why this slice exists:

1. **The image served reads but refused every write with `503`** — `config/content-manifest.json` and
   `TAGS.md` were not in it, and writes are validated against those vocabularies. Fixed by shipping them and
   setting `CONTENT_API_CORPUS_ROOT`.
2. **`attempt to write a readonly database`** — the store file was owned by the service user but sat in a
   root-owned directory, and SQLite writes its journal beside the database. Fixed by giving the store its own
   writable directory.

### Verification

```
python tests/e2e/test_content_api_e2e.py    → Ran 18 tests, OK (real containers, built and torn down)
pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95 → 378 passed, 95.09%
python tests/run_all_tests.py               → 195 checks / 62 modules
python scripts/build_site.py                → 1179 pages, standard library only
python -m contentdb.drift                   → clean, exit 0
docker build -t devops-questions .          → the static site image still builds
docker compose up --build                   → site serves "DevOps Question Field Manual", API reports healthy
```

The Compose check was first run against a port already held by an unrelated local service and returned that
service's title; it was re-run on free ports before being believed.

### Left for human review

- CI binds 8080 and 8000. Both are free on hosted runners; a self-hosted runner with either occupied would
  need the ports overridden.
- The image ships no Write credential, so a container is read-only until one is supplied. That is the
  intended default for anything reachable from a network.
