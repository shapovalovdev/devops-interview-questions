---
title: Diagnose long transactions in an MVCC database
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, monitoring, troubleshooting, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/mvcc.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose long transactions in an MVCC database

Why can an idle or long-running transaction become a production problem in PostgreSQL?

## Answer guide

- PostgreSQL uses multiversion concurrency control (MVCC), so a transaction can retain an old snapshot while other sessions create new row versions. A long-running transaction can delay removal of versions it might still need and contribute to bloat or maintenance pressure.
- Find the session and state in PostgreSQL activity views, identify its application owner and transaction age, then correct the code path, timeout, pooling configuration, or operational runbook. Alert on long active and idle-in-transaction sessions with contextual thresholds.
- Do not terminate a session without assessing work and locks; cancellation or termination rolls back uncommitted work and may trigger retries. Treat a growing table as a system signal: autovacuum settings, replica feedback, and replication slots can also retain cleanup horizons.

## References

- [PostgreSQL documentation: concurrency control](https://www.postgresql.org/docs/current/mvcc.html)
- Further reading (blog): [pganalyze: idle transaction monitoring](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)

## What to learn next

- Official documentation: [PostgreSQL: concurrency control](https://www.postgresql.org/docs/current/mvcc.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — connection tracing and idle transactions](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)
- Hands-on guide: [PostgreSQL transaction isolation guide](https://www.postgresql.org/docs/current/transaction-iso.html)
