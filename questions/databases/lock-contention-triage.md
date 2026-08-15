---
title: Triage PostgreSQL lock contention
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, monitoring, troubleshooting, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/explicit-locking.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-lock-modes
    source_type: official-docs
    verified_on: 2026-08-16
---

# Triage PostgreSQL lock contention

How do you investigate a request pile-up caused by PostgreSQL locks?

## Answer guide

- Identify blocked sessions, their wait events, the blocking session, lock modes, query text, transaction age, and application owner. PostgreSQL has several lock modes with differing conflict rules; the visible symptom is often many waiters, not the original blocker.
- Reduce impact by stopping or completing the safe blocker, pausing a conflicting deployment or batch job, and applying statement, lock, and idle-in-transaction timeouts where appropriate. Then fix transaction scope, access order, indexes, or migration method.
- Avoid a blanket kill of waiters: it can cause retry storms and hide the root cause. Some locks are expected, and DDL can request stronger locks than ordinary reads; rehearse migration locking behavior on representative data first.
- Blocking-chain triage transfers by name: MariaDB and MySQL expose wait-for graphs through InnoDB lock modes and the data dictionary, and SQL Server walks sys.dm_tran_locks blocking chains — find the head blocker, then fix transaction scope or access order applies in each.

## References

- [PostgreSQL documentation: explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- Further reading (blog): [pganalyze: lock monitoring](https://pganalyze.com/blog/postgres-lock-monitoring)
- [MariaDB — InnoDB lock modes](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-lock-modes)

## What to learn next

- Official documentation: [PostgreSQL: explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL lock monitoring](https://pganalyze.com/blog/postgres-lock-monitoring)
- Hands-on guide: [PostgreSQL lock monitoring views](https://www.postgresql.org/docs/current/view-pg-locks.html)
