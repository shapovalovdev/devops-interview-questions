---
title: Define SLOs for a shared database service
theme: databases
difficulty: staff
type: scenario
tags: [databases, postgresql, reliability, monitoring, governance]
sources:
  - url: https://www.postgresql.org/docs/current/monitoring.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define SLOs for a shared database service

How would you define service objectives for a shared PostgreSQL platform?

## Answer guide

- Set user-centered availability and latency indicators for connection, read, write, backup recoverability, and failover outcomes, then state which client populations and maintenance windows they cover. Use PostgreSQL statistics alongside host, storage, and application telemetry to link symptoms to capacity and workload.
- Establish error budgets, ownership, alert thresholds, and escalation paths, and review objectives with product teams. Segment tenants and workloads so a quiet aggregate does not hide one customer's data loss, saturation, or sustained tail latency.
- Do not promise zero downtime or measure only process uptime. Replica lag, backup age, connection exhaustion, and a successful-but-slow failover can violate customer outcomes even if the primary process is running.

## References

- [PostgreSQL documentation: monitoring database activity](https://www.postgresql.org/docs/current/monitoring.html)
- Further reading (blog): [pganalyze: Postgres monitoring improvements](https://pganalyze.com/blog/postgres13-better-performance-monitoring-usability)
