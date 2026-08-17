---
title: Diagnose a failed Patroni switchover
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, patroni, monitoring, troubleshooting]
sources:
  - url: https://patroni.readthedocs.io/en/latest/rest_api.html
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.postgresql.org/docs/current/hot-standby.html
    source_type: official-docs
    verified_on: 2026-08-17
---

# Diagnose a failed Patroni switchover

A planned Patroni switchover finishes without promoting the candidate replica. Where do you look and in what order?

## Answer guide

- Start from the cluster state machine, not from the logs of a single node: `patronictl list` (or the Patroni REST API `/cluster` endpoint) shows whether the cluster sees a leader, whether the candidate is a running replica, and whether any node reports "not allowed to promote". A switchover that silently no-ops usually means the candidate never became eligible, and everything after that observation narrows the cause.
- Check replica lag first: Patroni refuses to promote a replica whose replay lag exceeds `maximum_lag_on_failover`, so compare received versus replayed WAL positions and recent write volume on the primary; a laggy replica is the most common reason a switchover stalls. A MySQL replica stuck replaying its binlog fails promotion candidacy the same way, so the diagnosis is engine-portable: find the apply position, then find what holds it back. Look for a saturated network link, a replay paused by `recovery_min_apply_delay` or hot-standby feedback pressure, and long-running queries on the candidate pinning replay.
- Check DCS reachability second: if the node cannot reach etcd/Consul, it cannot take the leader key, and Patroni reports DCS connection errors in its log. A frozen cluster after DCS loss is intentional behavior, so verify DCS quorum health before blaming Patroni, and remember the REST API must be reachable from your monitoring and HAProxy health checks.
- Only then read the Patroni and PostgreSQL logs on the candidate for promotion-time failures (stale replication slot, missing `pg_ctl promote` permissions, timeline history divergence), and re-run the switchover during a low-write window once the underlying cause — lag, DCS, or eligibility — is fixed rather than retrying blindly.

## References

- [Patroni REST API: health and cluster state endpoints](https://patroni.readthedocs.io/en/latest/rest_api.html)
- [PostgreSQL documentation: hot standby and replay lag](https://www.postgresql.org/docs/current/hot-standby.html)
- Further reading (blog): [Percona database engineering blog: PostgreSQL HA troubleshooting topics](https://www.percona.com/blog/)

## What to learn next

- Official documentation: [Patroni documentation](https://patroni.readthedocs.io/en/latest/)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Percona engineering blog: Patroni operations](https://www.percona.com/blog/)
- Technical blog: [pganalyze — PostgreSQL replication articles](https://pganalyze.com/blog)
- Hands-on guide: [Patroni source repository with sample configurations](https://github.com/patroni/patroni)
