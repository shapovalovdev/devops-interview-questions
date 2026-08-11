---
title: Investigate a cache that stopped hitting
theme: caching
difficulty: junior
type: troubleshooting
tags: [caching, troubleshooting, latency, monitoring]
sources:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/admin/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Investigate a cache that stopped hitting

Latency doubled after a deploy and the cache hit ratio fell to nearly zero. How do you find the cause?

## Answer guide

- Separate the two possibilities first: either lookups are missing because the entries are gone, or they are missing because the keys changed. Compare the key strings the application is generating now with the ones stored before the deploy. A new serializer, an added field in the key, a changed key prefix, or a namespace bumped for a migration all produce a total miss with a perfectly healthy cache.
- If the keys are unchanged, check whether the data disappeared. Look for a restart, a failover to an empty replica, a `FLUSHALL` from a migration script, or an eviction storm. Redis exposes uptime, connected replicas, and eviction and expiry counters through `INFO`, and the administration guide describes the restart and failover behaviour that empties an in-memory dataset.
- If the entries exist but are not being used, suspect the client. Check connection errors, timeouts shorter than the cache's response time, a circuit breaker left open, TLS or authentication failures after a credential rotation, and a client library that silently treats every error as a miss.
- Confirm the direction of causation before changing anything. A cold cache raises origin load, which raises origin latency, which can raise cache client timeouts, which produces more misses. Read the timeline: which metric moved first, and does it line up with the deploy, a config change, or an infrastructure event.
- Recover deliberately rather than by restarting. Restarting the application does not repopulate the cache and a stampede of simultaneous refills can finish off an already-loaded origin. Rate-limit the refill, keep request coalescing on, and roll back the key-format change if that was the cause.

## References

- [Redis administration guide](https://redis.io/docs/latest/operate/oss_and_stack/management/admin/)
- Further reading (blog): [Redis blog](https://redis.io/blog/)

## What to learn next

- Official documentation: [Redis administration guide](https://redis.io/docs/latest/operate/oss_and_stack/management/admin/)
- Manual or specification: [Memcached internals manual](https://github.com/memcached/memcached/wiki/UserInternals)
- Maintainer or personal blog: [Rachel Kroll — writing about operational failures](https://rachelbythebay.com/w/)
- Technical blog: [Redis blog](https://redis.io/blog/)
- Hands-on guide: [Redis latency monitoring](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor/)
