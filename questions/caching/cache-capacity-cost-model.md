---
title: Build a cache capacity and cost model
theme: caching
difficulty: staff
type: scenario
tags: [caching, capacity-planning, cost-optimization, performance, memory]
sources:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Build a cache capacity and cost model

Finance asks why the cache tier costs what it does, and whether it can be halved. How do you build a model that answers both?

## Answer guide

- Start from the working set rather than from the total data size. The quantity that matters is the volume of distinct entries actually re-read within their TTL, which is a function of request skew, not of how much data exists. Measure it: sample keys over a window, count distinct keys and their re-reference intervals, and plot hit ratio against simulated memory. That curve, not a rule of thumb, is the model.
- Model the marginal return honestly. Hit ratio against memory is strongly concave for skewed workloads: the first gigabyte buys most of the benefit and the last one buys very little. The right question is therefore not "what memory gives the best hit ratio" but "at what point does another gigabyte cost more than the origin capacity it saves", which turns capacity into a comparison between two prices.
- Include the real per-entry overhead. Cached bytes are not the value's serialized size: add key length, per-object metadata, pointer and encoding overhead, allocator rounding, and fragmentation, and reserve headroom for replication buffers, client output buffers, and background save copy-on-write. A model built on payload size alone typically underestimates by a wide margin, and Redis and Memcached both document how their internal representation drives this.
- Price the alternatives against the same benefit. Compression, a smaller serialization format, shorter keys, tighter TTLs, or moving cold entries to flash-backed storage all reduce required memory without buying instances. Compare each against simply provisioning origin capacity, and note the second-order cost of a lower hit ratio, which is extra origin CPU, extra database connections, and worse tail latency.
- Close the loop with failure economics and validation. State what happens at the reduced size during a cold start, a failover, and a traffic peak, since the cheapest tier that works in steady state may not survive a full refill. Then validate the model rather than trusting it: benchmark with representative key sizes and skew, and re-derive the working set periodically, because a schema change or a new feature can shift it faster than any budget cycle.

## References

- [Redis memory optimization guide](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/)
- [Redis benchmarking documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/)
- Further reading (blog): [Redis blog](https://redis.io/blog/)

## What to learn next

- Official documentation: [Redis memory optimization guide](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/)
- Manual or specification: [Memcached internals manual](https://github.com/memcached/memcached/wiki/UserInternals)
- Maintainer or personal blog: [Dormando — Memcached maintainer notes](https://www.dormando.me/)
- Technical blog: [Redis blog](https://redis.io/blog/)
- Hands-on guide: [Redis benchmarking documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/)
