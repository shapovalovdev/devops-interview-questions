---
title: Explain MongoDB replica set fundamentals
theme: databases
difficulty: junior
type: theory
tags: [databases, mongodb, availability, monitoring]
sources:
  - url: https://www.mongodb.com/docs/manual/replication/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.mongodb.com/docs/manual/core/read-preference/
    source_type: official-docs
    verified_on: 2026-08-17
---

# Explain MongoDB replica set fundamentals

How do a primary, secondaries, and elections combine into the MongoDB availability model?

## Answer guide

- A replica set is one primary plus secondaries replicating the primary's operations via an oplog (an ordered log of writes each member applies idempotently). All writes go to the primary; secondaries stay read-only copies that can also serve reads when a client asks. The conceptual mapping to PostgreSQL is streaming replication, and the oplog is the analogue of WAL replay.
- Elections use a majority: members heartbeat each other, and when the primary is unreachable a majority of voting members elects an eligible secondary, deliberately preferring the most up-to-date member. A set of three voting members tolerates one failure; with an even count, an arbiter or priorities tune quorum. Lose the majority and the set goes read-only rather than risking two primaries — the same quorum instinct as Patroni's DCS leader key, and the same most-advanced-wins preference MySQL encodes through GTID sets when picking a replica to promote.
- Read preference is the client-side lever: `primary` by default, but `secondaryPreferred` and friends route reads to replicas, accepting eventual consistency and the staleness window it implies; write concern is the matching lever for how many members must acknowledge a write before it counts. Tuning the two together is the durability/latency dial of the engine.
- Operationally, monitor replication lag (oplog apply position versus primary), oplog window size — a secondary down longer than the window needs an initial sync, not a catch-up — and election health, because those three signals predict almost every replica-set incident.

## References

- [MongoDB documentation: replication](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB documentation: read preference](https://www.mongodb.com/docs/manual/core/read-preference/)
- Further reading (blog): [MongoDB blog: replica set and availability articles](https://www.mongodb.com/blog)

## What to learn next

- Official documentation: [MongoDB manual: replication](https://www.mongodb.com/docs/manual/replication/)
- Manual or specification: [MongoDB manual: read preference reference](https://www.mongodb.com/docs/manual/core/read-preference/)
- Maintainer or personal blog: [MongoDB engineering blog](https://www.mongodb.com/blog)
- Technical blog: [Percona engineering blog: MongoDB operations](https://www.percona.com/blog/)
- Hands-on guide: [MongoDB manual: deploy a replica set](https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set/)
