---
title: Triage a sudden slow PostgreSQL query
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, performance, monitoring, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/using-explain.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a sudden slow PostgreSQL query

What evidence would you collect before changing a slow query or its indexes?

## Answer guide

- Capture the normalized query, parameters or representative selectivity, timing distribution, plan, row estimates versus actuals, buffer and I/O evidence, locks, and resource saturation. Compare a known-good period to separate a query regression from a system-level incident.
- Reproduce safely and use `EXPLAIN (ANALYZE, BUFFERS)` only with understood impact. Correct the demonstrated cause: refresh statistics, change query shape, create an appropriate index, resolve blocking, or add capacity after measuring the bottleneck.
- Do not treat an index as a universal fix or force planner settings globally. An observed plan can vary by parameter, cached data, statistics, and version; an online index build still consumes I/O and needs failure handling.

## References

- [PostgreSQL documentation: using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- Further reading (blog): [pganalyze: index selection](https://pganalyze.com/blog/how-postgres-chooses-index)

## What to learn next

- Official documentation: [PostgreSQL: using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — how PostgreSQL chooses an index](https://pganalyze.com/blog/how-postgres-chooses-index)
- Hands-on guide: [PostgreSQL EXPLAIN reference](https://www.postgresql.org/docs/current/sql-explain.html)
