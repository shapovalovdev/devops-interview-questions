---
title: Roll out a backward-compatible database migration
theme: backend-architecture
difficulty: middle
type: scenario
tags: [databases, deployment, change-management]
sources:
  - url: https://www.postgresql.org/docs/current/ddl-alter.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Roll out a backward-compatible database migration

How do you change a database schema while old and new application versions coexist?

## Answer guide

- Use expand-contract: add compatible structures first, deploy readers and writers that tolerate both shapes, backfill in bounded batches, verify, then remove the old path only after all callers have moved. Version the migration and make it observable and reversible where feasible.
- Inspect database-specific locks, table rewrite behavior, replication lag, and query plans before production. Set a migration time budget, monitor errors and latency, and define a stop or rollback decision before starting.
- A destructive rename or non-null constraint may break an older binary even if the new binary works. Long locks and unthrottled backfills can cause an outage; rehearse on production-like data and test mixed-version deployment.

## References

- [PostgreSQL: ALTER TABLE](https://www.postgresql.org/docs/current/ddl-alter.html)
- Further reading (personal blog): [Brandur: Postgres migrations](https://brandur.org/fragments/postgres-zerodowntime-migrations)

## What to learn next

- Official documentation: [PostgreSQL concurrency control](https://www.postgresql.org/docs/current/mvcc.html)
- Manual or specification: [PostgreSQL SQL commands](https://www.postgresql.org/docs/current/sql-commands.html)
- Maintainer or personal blog: [Brandur Leach's blog](https://brandur.org/)
- Technical blog: [GitHub Engineering](https://github.blog/engineering/)
- Hands-on guide: [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
