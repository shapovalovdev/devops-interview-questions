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

Constraints and transactions before query plans, query plans before recovery —
the order runs from the relational basics to keeping a production PostgreSQL
alive.

1. [Explain relational tables, keys, and constraints](../../questions/databases/relational-data-model-basics.html)
    — Tables, keys, and constraints are the contract every later query, lock,
    and recovery presumes.
2. [Explain database transaction boundaries](../../questions/databases/transaction-basics.html)
    — Transactions define the unit of atomicity before concurrency arrives to
    complicate it.
3. [Design least-privilege PostgreSQL roles](../../questions/databases/role-privilege-design.html)
    — Least-privilege roles decide who may hold the power the transaction gives.
4. [Explain PostgreSQL connection authentication](../../questions/databases/connection-authentication-basics.html)
    — Connection authentication is the door the roles and transactions sit
    behind.
5. [Read a basic PostgreSQL query plan](../../questions/databases/sql-query-plan-basics.html)
    — Reading a query plan turns slow performance into evidence instead of
    folklore.
6. [Explain database index trade-offs](../../questions/databases/index-tradeoffs.html)
    — Indexes are the plan's main lever, with write costs that must be priced
    rather than ignored.
7. [Triage PostgreSQL lock contention](../../questions/databases/lock-contention-triage.html)
    — Lock contention is the concurrency face of the plans and indexes above.
8. [Diagnose long transactions in an MVCC database](../../questions/databases/mvcc-and-long-transactions.html)
    — MVCC explains why long transactions poison even correctly indexed tables.
9. [Explain database backup and restore validation](../../questions/databases/backup-restore-basics.html)
    — Backups open the durability tier, and only a validated restore makes them
    real.
10. [Design PostgreSQL point-in-time recovery](../../questions/databases/point-in-time-recovery-design.html)
    — Point-in-time recovery bounds how much a restore can lose, the arithmetic
    the backup proved.
11. [Respond to PostgreSQL replication lag](../../questions/databases/replication-lag-response.html)
    — Replication adds the read copies the failover tier will depend on.
12. [Design PostgreSQL high availability and failover](../../questions/databases/high-availability-failover.html)
    — Failover spends the replication design on the day the primary dies.
13. [Govern capacity for a multi-team database platform](../../questions/databases/database-capacity-governance.html)
    — Capacity governance prices a database platform shared by many teams.
14. [Plan a near-zero-downtime PostgreSQL major upgrade](../../questions/databases/zero-downtime-major-upgrade.html)
    — The near-zero-downtime major upgrade is the durability tier's capstone,
    consuming replication, failover, and capacity at once.
