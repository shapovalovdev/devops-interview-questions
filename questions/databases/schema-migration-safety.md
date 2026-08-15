---
title: Deploy a PostgreSQL schema migration safely
theme: databases
difficulty: middle
type: scenario
tags: [databases, postgresql, deployment, reliability, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/ddl-alter.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-online-ddl
    source_type: official-docs
    verified_on: 2026-08-16
---

# Deploy a PostgreSQL schema migration safely

What makes a production schema migration safe and reversible?

## Answer guide

- Classify the exact DDL and its lock, rewrite, validation, and duration behavior for the deployed PostgreSQL version. Prefer an expand–migrate–contract sequence: add compatible structures, backfill in bounded batches, switch readers and writers, verify, then remove old paths later.
- Rehearse against realistic volume and concurrent traffic, use lock and statement timeouts, observe blocking, and give the deployment a stop condition and rollback or forward-fix plan. Build indexes concurrently when the operation and version support it.
- A migration tool does not make DDL nonblocking. Long transactions can delay completion, a rollback can be impossible after data conversion, and application versions may race; coordinate compatibility windows and do not combine irreversible changes blindly.
- Expand–migrate–contract is not PostgreSQL-only: MySQL and MariaDB online DDL with ALGORITHM=INPLACE or INSTANT and LOCK=NONE, and SQL Server's ONLINE = ON option, are the equivalents of concurrent index builds — per-operation capability differs by engine and version, so verify the matrix for yours.

## References

- [PostgreSQL documentation: modifying tables](https://www.postgresql.org/docs/current/ddl-alter.html)
- Further reading (blog): [pganalyze: avoiding deadlocks in migrations](https://pganalyze.com/blog)
- [MariaDB — InnoDB online DDL](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-online-ddl)

## What to learn next

- Official documentation: [PostgreSQL: modifying tables](https://www.postgresql.org/docs/current/ddl-alter.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL migration articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL ALTER TABLE reference](https://www.postgresql.org/docs/current/sql-altertable.html)
