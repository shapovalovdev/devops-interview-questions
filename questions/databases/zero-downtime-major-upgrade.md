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
---

# Plan a near-zero-downtime PostgreSQL major upgrade

How would you plan a PostgreSQL major-version upgrade for a critical service?

## Answer guide

- Choose an upgrade method based on compatibility, size, outage budget, and rollback needs: dump/restore, `pg_upgrade`, or a carefully designed replication-based migration. Inventory extensions, collations, client drivers, configuration, schema changes, and operational tooling before selecting the path.
- Rehearse with production-like data, measure cutover and rollback timing, validate query and application behavior, freeze conflicting changes, and communicate ownership and decision gates. Take known-good backups and retain the old system until reconciliation completes.
- Major upgrades are not only binary swaps: extension and OS dependencies, planner changes, authentication defaults, and logical-replication limitations can affect behavior. A no-downtime target may add data consistency and operational complexity that must be justified.

## References

- [PostgreSQL documentation: upgrading](https://www.postgresql.org/docs/current/upgrading.html)
- Further reading (blog): [pganalyze: zero-downtime Postgres upgrades](https://pganalyze.com/blog)
