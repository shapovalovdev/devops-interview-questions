# Databases: related materials

Vendor scope, stated plainly: this Theme teaches database operations through
PostgreSQL. Every Question's primary source is the PostgreSQL manual, so
PostgreSQL is the concrete engine in every scenario — that is a deliberate
default, not a claim that the behaviour shown is universal. The concepts,
however, are engine-portable, and each answer guide names how its construct
maps onto another engine — InnoDB history-list growth and purge threads where
PostgreSQL shows dead tuples and autovacuum, binary-log replay or a SQL Server
log-chain restore for point-in-time recovery, online DDL options where
PostgreSQL offers concurrent index builds. Where that other implementation's
documentation is the authority for the equivalent construct, it is cited as an
additional primary source (SQL Server and MariaDB documentation, and NIST
standards where one applies). Treat the upstream PostgreSQL manual as the
authority for PostgreSQL behaviour; database products vary in locking,
recovery, replication, and privilege semantics, and the mapped equivalents are
orientation rather than a promise of identical semantics.

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
