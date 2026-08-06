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
---

# Design PostgreSQL high availability and failover

What must a PostgreSQL failover design decide before an outage occurs?

## Answer guide

- Define the authoritative primary, replica topology, acceptable data loss, failover trigger and authority, client routing, fencing of the former primary, and rejoin process. Streaming replication provides standby capability, but its synchrony and promotion choices determine availability and durability trade-offs.
- Automate health observation but make promotion safeguards explicit; test detection, promotion, DNS or proxy convergence, application retry behavior, data reconciliation, and rebuilding the old primary. Monitor WAL, replica lag, quorum assumptions, and backup health continuously.
- Automatic promotion without fencing risks split brain and divergent writes. Synchronous replication can increase write latency or reduce availability when a required standby disappears; asynchronous replication can lose acknowledged recent writes during promotion.

## References

- [PostgreSQL documentation: warm standby and streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Further reading (blog): [pganalyze: Postgres replication topics](https://pganalyze.com/blog)
