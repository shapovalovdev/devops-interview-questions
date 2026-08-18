# Issue board

GitHub Issues was unavailable when this epic was charted, so the queue was written here as
version-controlled Markdown. The API recovered on 2026-08-18 and every file below is now also a GitHub
issue, listed in the table. **GitHub is the tracker of record**; these files stay as the long-form
specification each issue links to, and carry the completion reports.

Statuses: `ready-for-agent` → `in-progress` → `needs-review` → `closed`. `blocked` means an unfinished
dependency, not a problem.

## Content API v1

Epic: [serve Questions and Labs from a Content store through a Content API](./0000-epic-content-api.md)

| # | Issue | GitHub | Status | Depends on | Branch |
| --- | --- | --- | --- | --- | --- |
| 0001 | [Content store schema and Ingest](./0001-content-store-and-ingest.md) | [#169](https://github.com/shapovalovdev/devops-interview-questions/issues/169) | `closed` | — | `feature/content-store-ingest` |
| 0002 | [API contract and tracer-bullet service](./0002-api-contract-and-service.md) | [#170](https://github.com/shapovalovdev/devops-interview-questions/issues/170) | `closed` | — | `feature/api-contract` |
| 0003 | [Complete read surface over the real store](./0003-api-read-surface.md) | [#171](https://github.com/shapovalovdev/devops-interview-questions/issues/171) | `ready-for-agent` | 0001, 0002 | `feature/api-read-surface` |
| 0004 | [Write surface: CRUD, Write credential, optimistic concurrency](./0004-api-write-surface.md) | [#172](https://github.com/shapovalovdev/devops-interview-questions/issues/172) | `ready-for-agent` | 0003 | `feature/api-write-surface` |
| 0005 | [Export to Markdown and the CI Drift gate](./0005-export-and-drift-gate.md) | [#173](https://github.com/shapovalovdev/devops-interview-questions/issues/173) | `closed` | 0001 | `feature/content-export-drift` |
| 0006 | [Packaging, end-to-end suite, and CI coverage gate](./0006-packaging-and-e2e.md) | [#174](https://github.com/shapovalovdev/devops-interview-questions/issues/174) | `blocked` | 0003, 0004 | `feature/api-packaging-e2e` |

## Dispatch order

```
0001 ─┬─▶ 0003 ─▶ 0004 ─┬─▶ 0006
0002 ─┘                 │
0001 ─────▶ 0005 ───────┘
```

Wave 1 runs 0001 and 0002 in parallel — 0002 is contract-first and codes against a `Store` protocol with an
in-memory fake, so it does not wait for the real store. Wave 2 runs 0003 and 0005. Wave 3 runs 0004, then
0006 last. At most three implementation agents are active at once, each in its own git worktree.

## Epic

[#168](https://github.com/shapovalovdev/devops-interview-questions/issues/168) — release [Content API v1](https://github.com/shapovalovdev/devops-interview-questions/milestone/10).
