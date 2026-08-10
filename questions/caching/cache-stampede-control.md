---
title: Prevent a cache stampede
theme: caching
difficulty: middle
type: scenario
tags: [caching, performance, reliability, databases]
sources:
  - url: https://redis.io/docs/latest/develop/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Prevent a cache stampede

How should a team prevent many requests from rebuilding the same expired cache entry?

## Answer guide

- Identify the key, expiry pattern, and backend capacity first; synchronized expiry can turn a normal cache miss into a burst against the source of truth.
- Use request coalescing or a bounded lock for one rebuild, serve a stale value when the freshness contract permits it, and add jitter to expiry times.
- Bound waiting and define fallback behavior. A distributed lock outage, slow rebuild, or poisoned value must not make every caller block indefinitely.
- Measure miss rate, rebuild concurrency, backend saturation, and stale-response age; test cold start and cache-node loss before relying on the pattern.

## References

- [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Further reading (blog): [Cloudflare Blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Manual or specification: [HTTP caching specification](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Martin Kleppmann](https://martin.kleppmann.com/)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Redis getting started](https://redis.io/docs/latest/develop/get-started/)
