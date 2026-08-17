# SQLite Content store behind a FastAPI Content API

---
Status: accepted
---

Questions and Labs have only ever been Markdown files rendered to a static site, which cannot answer a query like "senior Kubernetes Questions tagged `cks`" without shipping the entire corpus to the browser. We are adding a SQLite Content store, built from the Markdown corpus by an Ingest step, and a FastAPI Content API that serves it with filtering, search, and pagination, so that other tools — a mobile client, a spaced-repetition trainer, an interview bot — can consume the database without parsing Markdown.

## Considered options

**FastAPI over a stdlib `http.server` app.** The repository is otherwise strictly zero-dependency and standard-library only, and a hand-rolled server would have preserved that. We took the dependency anyway: request validation, typed models, and a generated, always-accurate OpenAPI document are the bulk of the work in a CRUD API, and re-implementing them by hand is the kind of code that rots silently. The cost is a `requirements.txt` that CI must install and a Docker image that is no longer just nginx and static files. The static site build stays stdlib-only and keeps working with no Python runtime at all — the dependency is confined to the API service.

**SQLite over Postgres.** The corpus is a few thousand small documents that change only when someone commits, and read traffic is trivially cacheable. SQLite makes the store a single file that the build can produce deterministically and the Docker image can ship, with no service to operate. If the API ever needs concurrent multi-writer traffic, this is the decision to revisit.

**Read-write over read-only.** A read-only API would have kept Markdown-in-git as the unambiguous single source of truth. We chose full CRUD so that content can be authored through the API, accepting that writes make the store diverge from the corpus.

## Consequences

Git remains the durable record of content. Writes land in the Content store, and an Export step renders store records back to Markdown files; CI runs Ingest against the committed corpus and fails on Drift, so a change made through the API is not considered landed until it exists as reviewed Markdown. Content policy, source verification, and the coverage target continue to be enforced against Markdown by the existing validators — the API cannot be used to bypass them.

The Content store is a derived, disposable artifact: it is rebuilt from Markdown by Ingest on every build, and nothing may be stored in it that does not survive a rebuild.
