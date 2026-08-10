---
title: Design cache coherence across regions
theme: caching
difficulty: staff
type: scenario
tags: [caching, distributed-systems, architecture, reliability, latency]
sources:
  - url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/develop/use/keyspace-notifications/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design cache coherence across regions

A product runs in three regions, each with a local cache in front of a database that is written in one region. How do you keep the caches coherent enough?

## Answer guide

- State the goal as a bound, not as coherence. A globally synchronous cache invalidation would make every write pay a cross-region round trip and would make a regional partition into a write outage. The realistic design defines a convergence bound: after a write, how long may a remote region serve the old value, and what is the worst case during a partition.
- Make invalidation a replicated event rather than a synchronous call. Publish an invalidation or an updated value onto a durable, ordered stream that each region consumes, using the same log that already replicates the database if one exists. Redis keyspace notifications and change-data-capture feeds are both ways to derive the event from the write rather than from remembering to call a purge in application code — the code path everybody forgets to update.
- Handle ordering and idempotency at the consumer. Events arrive out of order and more than once, so carry a version or timestamp with each entry and refuse to overwrite a newer cached value with an older event. Deleting the entry instead of updating it is usually safer, because the next read repopulates from the local replica and cannot resurrect a stale write.
- Accept that some layers cannot be invalidated quickly. A CDN purge is an asynchronous operation across every point of presence, and browsers cannot be purged at all, so version the URL for content that must change atomically. Reserve purge for correcting mistakes and use short TTLs with stale-while-revalidate for routine freshness, because a purge-per-write design collapses under real write rates and API limits.
- Failure modes and operations: an invalidation stream that lags silently, so add an alert on consumer lag and expose the age of served entries; a replay after an outage that re-invalidates the whole keyspace and produces a global stampede, so rate-limit replay; a region reading its local database replica and caching a value that is behind its own invalidation event; and a follow-the-write pattern where users who move regions lose read-your-writes. Add a periodic low-rate reconciliation sweep so a lost event self-heals rather than persisting until someone notices.

## References

- [Amazon CloudFront invalidation documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
- [Redis keyspace notifications documentation](https://redis.io/docs/latest/develop/use/keyspace-notifications/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Amazon CloudFront invalidation documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
- Manual or specification: [Redis Cluster specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
- Maintainer or personal blog: [Martin Kleppmann — using logs to build a solid data infrastructure](https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html)
- Technical blog: [Scaling Memcache at Facebook, NSDI 2013](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala)
- Hands-on guide: [Redis keyspace notifications guide](https://redis.io/docs/latest/develop/use/keyspace-notifications/)
