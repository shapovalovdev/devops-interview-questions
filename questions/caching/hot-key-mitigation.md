---
title: Mitigate a hot key in a sharded cache
theme: caching
difficulty: middle
type: troubleshooting
tags: [caching, redis, performance, troubleshooting, latency]
sources:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Mitigate a hot key in a sharded cache

One node in a sharded cache is saturated while the rest are idle. How do you confirm a hot key and what can you actually do about it?

## Answer guide

- Confirm the shape first. Sharding distributes keys, not traffic: a single key that every request reads lands on exactly one node no matter how many nodes exist. Look for one node with high CPU or network utilisation and normal key counts, and identify the offending key with per-command sampling, the slow log, key-space statistics, or a short `MONITOR` capture taken with care because it is itself expensive.
- Understand why adding shards will not help. In Redis Cluster the key maps to one of the fixed hash slots and the slot maps to one primary; more shards moves other slots away but leaves the hot slot exactly as loaded. Resharding is the right answer for an unbalanced key distribution, not for a single hot key.
- The effective mitigations all add copies. Add a near cache in the application process so most reads never leave the host; replicate the value under several suffixed keys and have clients pick one at random; or serve the value from read replicas where the client library supports it and the staleness is acceptable. Each trades memory and consistency for spread.
- Reduce the request rate rather than only spreading it. Coalesce concurrent refreshes so one origin fetch serves many waiters, batch reads into pipelines, and check whether the key is hot because of a retry loop or a polling client that could use a longer interval or a subscription instead.
- Failure modes to name: a near cache with no TTL discipline making every replica disagree; random-suffix replication multiplying the invalidation problem by the replica count; `MONITOR` left running and becoming the new bottleneck; and treating a hot key as a capacity problem, adding nodes, and paying for hardware that cannot receive the traffic.

## References

- [Redis scaling and cluster management documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)
- [Redis Cluster specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Redis scaling and cluster management documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)
- Manual or specification: [Redis Cluster specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
- Maintainer or personal blog: [Salvatore Sanfilippo — Redis Cluster, no longer vaporware](https://antirez.com/news/79)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Redis client-side caching guide](https://redis.io/docs/latest/develop/reference/client-side-caching/)
