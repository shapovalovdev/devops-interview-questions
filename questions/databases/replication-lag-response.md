---
title: Respond to PostgreSQL replication lag
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, monitoring, troubleshooting, availability]
sources:
  - url: https://www.postgresql.org/docs/current/warm-standby.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to PostgreSQL replication lag

How would you investigate a PostgreSQL standby that is falling behind?

## Answer guide

- Determine whether lag is sending, writing, flushing, or replaying WAL, then compare primary WAL generation with standby CPU, disk, network, and replay capacity. PostgreSQL exposes replication status and supports several warm-standby configurations with different trade-offs.
- Protect correctness first: keep writes on the authoritative primary, remove or throttle a known expensive workload if safe, and verify the replica's storage and network health. Alert on lag relative to the service's stale-read and failover objectives.
- A replica is not automatically safe to promote while it is stale, and a low byte lag can still mean high time lag during bursts. Replication slots and feedback settings can retain WAL or delay cleanup, so include disk headroom and slot state in diagnosis.

## References

- [PostgreSQL documentation: warm standby and streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Further reading (blog): [pganalyze: Postgres replication topics](https://pganalyze.com/blog)

## What to learn next

- Official documentation: [PostgreSQL: warm standby and streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL replication articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL replication monitoring views](https://www.postgresql.org/docs/current/monitoring-stats.html)
