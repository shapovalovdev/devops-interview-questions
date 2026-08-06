# Databases: related materials

The Databases Theme uses PostgreSQL as its concrete operational model. Treat
the upstream manual as authority for PostgreSQL behaviour; database products
vary in locking, recovery, replication, and privilege semantics.

## What to learn next

- Official documentation: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Manual or specification: [PostgreSQL SQL command reference](https://www.postgresql.org/docs/current/sql-commands.html)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL performance and operations](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)

## Legal free books

- [The Internals of PostgreSQL](https://www.interdb.jp/pg/) is a free online
  book published by its author, Hironobu Suzuki. It is especially useful for
  MVCC, locking, WAL, recovery, and replication mechanics.
- [The PostgreSQL manual](https://www.postgresql.org/docs/current/) is freely
  published by the PostgreSQL Global Development Group. Read its tutorial and
  administration chapters alongside experiments on a disposable instance.

## Suggested study order

Begin with relational constraints, transactions, roles, and connection
authentication. Then learn query plans, indexes, locking, and MVCC. Finish
with backups, point-in-time recovery, replication, failover, capacity, and
safe version upgrades.
