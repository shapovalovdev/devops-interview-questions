---
title: Diagnose replication lag
theme: distributed-systems
difficulty: middle
type: troubleshooting
tags: [databases, latency, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/warm-standby.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose replication lag

What should an operator check when a read replica is behind its primary?

## Answer guide

- Measure lag as backlog and replay position, not only elapsed wall-clock time. Compare primary generation, transport, receive, durable write, and replay stages, then correlate with disk latency, network loss, CPU, locks, and maintenance activity.
- Determine the user guarantee before routing reads: an asynchronous replica can return older state, while a synchronous configuration changes write latency and availability. For read-your-writes, pin briefly to a primary or wait for a known replication position.
- Do not fix lag by blindly adding replicas or increasing timeout. A blocked apply worker, storage saturation, oversized transaction, missing retention, or replica rebuild can turn lag into data loss or a recovery event if the required log is no longer available.

## References

- [PostgreSQL: high availability and replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Further reading (personal blog): [Brandur Leach: Postgres replication](https://brandur.org/postgres-replication)

## What to learn next

- Official documentation: [PostgreSQL monitoring](https://www.postgresql.org/docs/current/monitoring.html)
- Manual or specification: [PostgreSQL warm standby](https://www.postgresql.org/docs/current/warm-standby.html)
- Maintainer or personal blog: [Brandur Leach's writing](https://brandur.org/)
- Technical blog: [Crunchy Data: replication](https://www.crunchydata.com/blog)
- Hands-on guide: [PostgreSQL streaming replication](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION)
