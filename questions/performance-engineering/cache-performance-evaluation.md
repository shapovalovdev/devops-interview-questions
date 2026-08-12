---
title: How do you evaluate whether a cache improves a service?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://redis.io/docs/latest/develop/reference/client-side-caching/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you evaluate whether a cache improves a service?

A team added a cache and reports a 92 percent hit rate as proof it worked. What else do you need before accepting that the service is better off?

## Answer guide

- Hit rate is an input, not the outcome. Judge the cache on end-to-end p50 and p99 with it enabled versus disabled under the same workload, together with the origin's request rate and saturation. A 92 percent hit rate is compatible with a worse p99: the remaining 8 percent now pay a cache lookup plus origin latency plus possibly a lock wait, and if the cached items were the cheap ones the cache bought nothing. The value is roughly hit ratio times the cost avoided per hit, weighed against the added cost of every miss.
- The number hides which requests miss. Measure hit-path and miss-path latency separately, and check whether misses concentrate on a subset — new items, one tenant, one key prefix — because a cache that serves the already-fast requests while missing the slow ones adds latency without removing meaningful load. Also account for the dependency it creates: absorbing 92 percent of reads means a cold start, a flush, or a failover presents the origin with more than ten times its steady-state read load.
- Correctness is part of the evaluation, since the characteristic failure of a caching layer is wrong data rather than slow data. Decide the staleness the product tolerates, set the TTL from that, and be explicit about the invalidation model — write-through, write-around, or TTL-only. Track memory footprint and eviction rate too: a cache already evicting at its ceiling has a hit rate that will fall as soon as the working set grows. Redis client-side caching with RESP3 tracking removes a network hop but introduces an invalidation-message path that can itself drop or lag.
- Two failure modes dominate in production. A thundering herd on a hot key expiring means many concurrent requests miss at once and all hit the origin together, which request coalescing, a probabilistic early refresh, or a short per-key lock prevents. Synchronised TTLs from a bulk load create a mass-expiry cliff, which TTL jitter fixes. Beyond that, a cache masking an unindexed query or an inefficient origin converts a bounded inefficiency into an outage the first time the cache is unavailable, so verify the origin survives a deliberate cache-off window before you rely on it.

## References

- [Redis: Client-side caching](https://redis.io/docs/latest/develop/reference/client-side-caching/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
