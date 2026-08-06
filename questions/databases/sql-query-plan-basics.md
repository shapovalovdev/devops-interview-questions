---
title: Read a basic PostgreSQL query plan
theme: databases
difficulty: junior
type: theory
tags: [databases, postgresql, performance, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/using-explain.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Read a basic PostgreSQL query plan

What should you look for first in an `EXPLAIN` plan for a slow query?

## Answer guide

- Start with the plan tree, estimated versus actual row counts, scan and join nodes, and the node with the largest actual time when using `EXPLAIN (ANALYZE, BUFFERS)`. A sequential scan is not inherently wrong; it can be cheapest for a large fraction of a table.
- Compare the plan under representative parameters and data, then address a proven cause: stale statistics, an unsuitable index, an inefficient query shape, or missing memory and I/O capacity. Measure before and after rather than forcing a plan.
- `ANALYZE` executes the statement and can take locks or mutate data for write statements. Never run an unfamiliar production query blindly, and remember estimates and plans change with statistics, data distribution, and PostgreSQL version.

## References

- [PostgreSQL documentation: using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- Further reading (blog): [pganalyze: how Postgres chooses an index](https://pganalyze.com/blog/how-postgres-chooses-index)
