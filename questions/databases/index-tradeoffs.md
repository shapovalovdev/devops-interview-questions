---
title: Explain database index trade-offs
theme: databases
difficulty: middle
type: theory
tags: [databases, postgresql, reliability, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/indexes-intro.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain database index trade-offs

Why can an index speed up a query yet still make an application slower overall?

## Answer guide

- An index can let the planner find qualifying rows without scanning a whole table, but only when its access method and column order fit the predicate, join, or ordering of the actual query.
- Every index consumes disk and cache memory, and writes must update each affected index. Extra indexes can therefore increase write latency, vacuum/maintenance work, and recovery time even if one read query gets faster.
- Start with observed production query shapes and data distribution; use `EXPLAIN (ANALYZE, BUFFERS)` in a safe environment to compare plans and then measure the write and storage cost under representative load.
- A plan is data- and PostgreSQL-version-dependent. Stale statistics, low selectivity, parameter values, and an index that cannot support the required ordering can make a sequential scan the right plan rather than an incident to override.
- The write-amplification argument shifts with storage layout: InnoDB and SQL Server tables are clustered indexes (the primary key is the row's physical order) where PostgreSQL keeps a heap with separate indexes, so secondary-index count weighs differently — the measured cost-benefit discipline is the portable part.

## References

- [PostgreSQL documentation: introduction to indexes](https://www.postgresql.org/docs/current/indexes-intro.html)
- Further reading (blog): [pganalyze: Postgres index selection](https://pganalyze.com/blog/how-postgres-chooses-index)
- [SQL Server — clustered and nonclustered indexes](https://learn.microsoft.com/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)

## What to learn next

- Official documentation: [PostgreSQL: introduction to indexes](https://www.postgresql.org/docs/current/indexes-intro.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — how PostgreSQL chooses an index](https://pganalyze.com/blog/how-postgres-chooses-index)
- Hands-on guide: [PostgreSQL index types](https://www.postgresql.org/docs/current/indexes-types.html)
