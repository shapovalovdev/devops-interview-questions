---
title: Provide read-your-writes consistency
theme: distributed-systems
difficulty: senior
type: scenario
tags: [databases, reliability, latency]
sources:
  - url: https://www.postgresql.org/docs/current/warm-standby.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Provide read-your-writes consistency

How can an application ensure a user sees a just-completed update when reads normally use replicas?

## Answer guide

- Return a commit or replication position with the write and route the following read to a replica known to have applied at least that position, or temporarily route that user to the primary. The contract must identify the session, object scope, and maximum wait.
- Make freshness visible in telemetry and response behavior. A caller may choose a bounded wait, primary fallback, or explicit stale result; the system should not silently return older data after claiming a successful update is immediately visible.
- Replica lag, failover, and a lost session token break naive affinity. Pinning every read to the primary harms scale, while waiting forever harms availability; use an expiry and test the primary-unavailable path and user-visible reconciliation.

## References

- [PostgreSQL: high availability and replication](https://www.postgresql.org/docs/current/warm-standby.html)
- Further reading (personal blog): [Martin Kleppmann: consistency](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html)

## What to learn next

- Official documentation: [PostgreSQL hot standby](https://www.postgresql.org/docs/current/hot-standby.html)
- Manual or specification: [PostgreSQL warm standby](https://www.postgresql.org/docs/current/warm-standby.html)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [CockroachDB: follower reads](https://www.cockroachlabs.com/docs/stable/follower-reads)
- Hands-on guide: [PostgreSQL replication monitoring](https://www.postgresql.org/docs/current/monitoring-stats.html)
