---
title: Size a PostgreSQL connection pool
theme: databases
difficulty: middle
type: scenario
tags: [databases, postgresql, capacity-planning, performance, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/runtime-config-connection.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/dotnet/framework/data/adonet/sql-server-connection-pooling
    source_type: official-docs
    verified_on: 2026-08-16
---

# Size a PostgreSQL connection pool

Why can adding more application connections make a PostgreSQL service slower?

## Answer guide

- Each PostgreSQL connection is a server process with memory and scheduling cost; `max_connections` is a hard admission limit, not a throughput target. Excess concurrent work can increase CPU contention, cache pressure, lock waits, and tail latency.
- Pool close to the application, set bounded acquisition and query timeouts, reserve administrative capacity, and size concurrency from measured query cost and database resources. Monitor active, idle, waiting, rejected, and long-running connections alongside request latency.
- A pool can conceal leaks or hold transactions open. Do not simply raise `max_connections` after errors: first find leak paths, retry storms, slow queries, and per-tenant unfairness; ensure failover and credential rotation behavior is tested.
- Connection-cost reasoning generalizes with engine shape in mind: MySQL and MariaDB also bind a thread to each connection with a max_connections ceiling, while SQL Server multiplexes work over a scheduler pool — in all cases concurrency is a resource to budget, not a number to raise reflexively.

## References

- [PostgreSQL documentation: connection settings](https://www.postgresql.org/docs/current/runtime-config-connection.html)
- Further reading (blog): [pganalyze: connection tracing](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)
- [SQL Server — connection pooling (ADO.NET)](https://learn.microsoft.com/dotnet/framework/data/adonet/sql-server-connection-pooling)

## What to learn next

- Official documentation: [PostgreSQL: connection settings](https://www.postgresql.org/docs/current/runtime-config-connection.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — connection tracing and idle transactions](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)
- Hands-on guide: [PostgreSQL server configuration](https://www.postgresql.org/docs/current/config-setting.html)
