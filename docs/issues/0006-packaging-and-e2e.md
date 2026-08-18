# Packaging, end-to-end suite, and CI coverage gate

| | |
| --- | --- |
| **Status** | `blocked` |
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

## Notes

- Work in a git worktree on branch `feature/api-packaging-e2e`.
- The end-to-end suite must clean up its container on failure — a wedged container in CI is worse than a red test.
- This is the last slice: when it closes, post the release-gate verification on the epic.
- When you finish, append a **Completion report** section to this file: branch and commit SHA, the
  commands you ran with their results, test and coverage numbers, and anything left for human review.
  GitHub Issues are unavailable, so this file is the tracker — update its **Status** row as you go
  (`ready-for-agent` → `in-progress` → `needs-review`).
