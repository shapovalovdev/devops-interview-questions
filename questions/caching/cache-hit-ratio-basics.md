---
title: Interpret a cache hit ratio honestly
theme: caching
difficulty: junior
type: theory
tags: [caching, performance, monitoring, metrics]
sources:
  - url: https://redis.io/docs/latest/commands/info/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Interpret a cache hit ratio honestly

What does a cache hit ratio actually tell you, and what does it hide?

## Answer guide

- The hit ratio is hits divided by total lookups over a window. It answers one narrow question: how often a lookup was served from the cache rather than from the origin. Redis exposes the raw counters as `keyspace_hits` and `keyspace_misses` in `INFO stats`, and they are monotonic counters since the last reset, so a ratio computed from lifetime totals describes the whole uptime of the process, not the current minute.
- Compute the ratio over a rate window rather than from lifetime counters, otherwise a long-running node hides a regression: a process with a year of good history will still report a healthy lifetime ratio while it is missing on every request today.
- A high ratio does not prove the cache is helping. If the cached values are cheap to recompute, a 99 percent hit ratio saves little; if the remaining one percent of misses are the expensive queries, the origin still carries the real load. Pair the ratio with origin request rate and with latency percentiles for both hits and misses.
- A ratio can also be high for bad reasons: stale values that nobody invalidated, or a key space so coarse that different users share an entry. Watch eviction counts, expired-key counts, and value age alongside the ratio.
- Failure modes to name: a ratio that looks fine while the cache is down because the client counts only the requests it managed to send; per-node ratios averaged across a cluster hiding one cold or unbalanced node; and a ratio measured at the client that ignores network timeouts counted as neither hit nor miss.

## References

- [Redis INFO command reference](https://redis.io/docs/latest/commands/info/)
- Further reading (blog): [Cloudflare blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Redis INFO command reference](https://redis.io/docs/latest/commands/info/)
- Manual or specification: [RFC 9211 — the HTTP Cache-Status response header](https://www.rfc-editor.org/rfc/rfc9211.html)
- Maintainer or personal blog: [Marc Brooker — caches, modes, and unstable systems](https://brooker.co.za/blog/2021/08/27/caches.html)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [Prometheus histograms and summaries](https://prometheus.io/docs/practices/histograms/)
