---
title: Plan a near-zero-downtime PostgreSQL major upgrade
theme: databases
difficulty: senior
type: scenario
tags: [databases, postgresql, deployment, reliability, governance]
sources:
  - url: https://www.postgresql.org/docs/current/upgrading.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/sql/database-engine/install-windows/upgrade-sql-server
    source_type: official-docs
    verified_on: 2026-08-16
---

# Plan a near-zero-downtime PostgreSQL major upgrade

How would you plan a PostgreSQL major-version upgrade for a critical service?

## Answer guide

- Choose an upgrade method based on compatibility, size, outage budget, and rollback needs: dump/restore, `pg_upgrade`, or a carefully designed replication-based migration. Inventory extensions, collations, client drivers, configuration, schema changes, and operational tooling before selecting the path.
- Rehearse with production-like data, measure cutover and rollback timing, validate query and application behavior, freeze conflicting changes, and communicate ownership and decision gates. Take known-good backups and retain the old system until reconciliation completes.
- Major upgrades are not only binary swaps: extension and OS dependencies, planner changes, authentication defaults, and logical-replication limitations can affect behavior. A no-downtime target may add data consistency and operational complexity that must be justified.
- The method menu mirrors other engines: SQL Server offers in-place upgrades or a rolling replica upgrade through availability groups, and MySQL supports replication-based cross-version cut-over much like logical replication here — inventorying extensions and rehearsing timing is method-independent work.

## References

- [PostgreSQL documentation: upgrading](https://www.postgresql.org/docs/current/upgrading.html)
- Further reading (blog): [pganalyze: zero-downtime Postgres upgrades](https://pganalyze.com/blog)
- [SQL Server — upgrade SQL Server](https://learn.microsoft.com/sql/database-engine/install-windows/upgrade-sql-server)

## What to learn next

- Official documentation: [PostgreSQL: upgrading a cluster](https://www.postgresql.org/docs/current/upgrading.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL upgrade articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL pg_upgrade reference](https://www.postgresql.org/docs/current/pgupgrade.html)
