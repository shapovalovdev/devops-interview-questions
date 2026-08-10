---
title: Operate Redis replication and failover for a cache tier
theme: caching
difficulty: senior
type: scenario
tags: [caching, redis, reliability, availability, incident-response]
sources:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/replication/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Operate Redis replication and failover for a cache tier

How do you make a Redis cache tier survive the loss of a primary, and what should the service do while that is happening?

## Answer guide

- Decide first what failover is actually protecting. For a pure cache the dataset is reconstructible, so the goal is to shorten the window in which the service runs without a cache, not to guarantee that no entry is lost. That reframing usually simplifies the design: an automatic failover to a warm replica is worth having, and heroic durability engineering on cache data is not.
- Know the mechanics. Redis replication is asynchronous: a primary acknowledges a write before replicas have it, so a promoted replica can legitimately be missing recent writes. Sentinel monitors primaries and replicas, agrees on failure through a quorum, elects a replica, and reconfigures the remaining replicas and the clients that subscribe to its notifications. Redis Cluster performs the equivalent per shard. Neither makes replication synchronous, and `WAIT` only bounds the acknowledgement, it does not make the system linearizable.
- Choose persistence for restart behaviour, not for correctness. RDB snapshots restore a point in time cheaply; AOF replays a command log with a configurable fsync policy and restores far more. For a cache, persistence mostly determines whether a restarted node comes back warm or cold, and a cold restart of the whole tier is the scenario worth rehearsing. Note that both add fork and disk cost to a memory-bound process.
- Make the client's behaviour explicit for the failover window. Connections break, and the client must reconnect, discover the new topology, cap its retries, and fall back to the origin rather than blocking. Timeouts must be short enough that a stalled cache does not consume the whole request budget, and the origin must have enough capacity, or a circuit breaker, to absorb the resulting miss burst.
- Failure modes to name: a Sentinel quorum sharing a failure domain with the primary; a network partition where clients still reach the demoted primary and write to it; a promoted replica that was cold and immediately produces a full-tier miss storm; and DNS or discovery caching that keeps clients pointed at the old address long after promotion.

## References

- [Redis replication documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
- [Redis Sentinel documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
- [Redis persistence documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- Further reading (blog): [Redis blog](https://redis.io/blog/)

## What to learn next

- Official documentation: [Redis replication documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
- Manual or specification: [Redis Sentinel reference manual](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
- Maintainer or personal blog: [Martin Kleppmann — how to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- Technical blog: [Jepsen — distributed systems safety analyses](https://jepsen.io/)
- Hands-on guide: [Redis persistence guide](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
