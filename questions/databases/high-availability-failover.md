---
title: Design PostgreSQL high availability and failover
theme: databases
difficulty: senior
type: scenario
tags: [databases, postgresql, availability, reliability, incident-response]
sources:
  - url: https://www.postgresql.org/docs/current/warm-standby.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design PostgreSQL high availability and failover

What must a PostgreSQL failover design decide before an outage occurs?

## Answer guide

- Define the authoritative primary, replica topology, acceptable data loss, failover trigger and authority, client routing, fencing of the former primary, and rejoin process. Streaming replication provides standby capability, but its synchrony and promotion choices determine availability and durability trade-offs.
- Automate health observation but make promotion safeguards explicit; test detection, promotion, DNS or proxy convergence, application retry behavior, data reconciliation, and rebuilding the old primary. Monitor WAL, replica lag, quorum assumptions, and backup health continuously.
- Automatic promotion without fencing risks split brain and divergent writes. Synchronous replication can increase write latency or reduce availability when a required standby disappears; asynchronous replication can lose acknowledged recent writes during promotion.
- The same decisions recur in other engines' failover designs: SQL Server Always On availability groups add a cluster-quorum and fencing story, and MySQL Group Replication provides quorum-based promotion — topology, data-loss tolerance, client rerouting, and old-primary fencing must be settled in each.

## References

- [PostgreSQL documentation: warm standby and streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Further reading (blog): [pganalyze: Postgres replication topics](https://pganalyze.com/blog)
- [SQL Server — Always On availability groups](https://learn.microsoft.com/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server)

## What to learn next

- Official documentation: [PostgreSQL: warm standby and streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL replication articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL synchronous replication configuration](https://www.postgresql.org/docs/current/runtime-config-replication.html)
