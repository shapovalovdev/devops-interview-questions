---
title: Tune Redis maxmemory and eviction behaviour
theme: caching
difficulty: middle
type: scenario
tags: [caching, redis, memory, capacity, reliability]
sources:
  - url: https://redis.io/docs/latest/develop/reference/eviction/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Tune Redis maxmemory and eviction behaviour

A Redis instance used purely as a cache is approaching its memory limit. How do you configure `maxmemory` and the eviction policy so the failure mode is predictable?

## Answer guide

- Set `maxmemory` explicitly. With no limit, Redis grows until the operating system or the container's cgroup kills it, which turns a gradual capacity problem into an instant total loss of the dataset. Set it below the container limit, leaving headroom for replication buffers, client output buffers, and copy-on-write during a background save.
- Choose the policy from `maxmemory-policy` deliberately. The default `noeviction` returns errors on writes once the limit is reached, which is correct for a durable store and usually wrong for a cache — a cache that rejects writes stops absorbing load exactly when it is needed. `allkeys-lru` and `allkeys-lfu` evict across the whole keyspace; the `volatile-*` variants evict only keys carrying a TTL, and they behave like `noeviction` when no such keys remain, which is a common surprise.
- Understand that Redis LRU and LFU are approximations. Redis samples a small number of candidate keys per eviction rather than maintaining a global ordering, with the sample size controlled by `maxmemory-samples`; a larger sample is more accurate and more expensive. LFU additionally decays counters over time, so a key that was hot yesterday does not stay protected forever.
- Reduce the memory that has to be managed before tuning eviction. Shorter TTLs, smaller value encodings, hash field packing for small objects, and removing unbounded key families often recover more headroom than any policy change.
- Failure modes to name: `used_memory` counted without fragmentation so the process is far larger than Redis reports; a `volatile-*` policy paired with keys that have no TTL, producing write errors under pressure; eviction of the wrong tenant's keys because everything shares one instance; and latency spikes when a mass expiry cycle and eviction run together.

## References

- [Redis key eviction reference](https://redis.io/docs/latest/develop/reference/eviction/)
- [Redis memory optimization guide](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/)
- Further reading (blog): [Redis blog](https://redis.io/blog/)

## What to learn next

- Official documentation: [Redis key eviction reference](https://redis.io/docs/latest/develop/reference/eviction/)
- Manual or specification: [Redis configuration reference](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
- Maintainer or personal blog: [Salvatore Sanfilippo — random notes on improving the Redis LRU algorithm](https://antirez.com/news/109)
- Technical blog: [Dan Luu — caches, LRU versus random](https://danluu.com/2choices-eviction/)
- Hands-on guide: [Redis memory usage command reference](https://redis.io/docs/latest/commands/memory-usage/)
