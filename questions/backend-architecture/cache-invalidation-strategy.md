---
title: Design cache invalidation for mutable data
theme: backend-architecture
difficulty: senior
type: scenario
tags: [performance, databases, reliability]
sources:
  - url: https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design cache invalidation for mutable data

How should a backend prevent a cache from serving unacceptable stale data?

## Answer guide

- Define the authoritative store, cache key ownership, freshness requirement, and invalidation signal for each read model. Use TTL as a bounded recovery mechanism, then choose write-through, explicit invalidation, versioned keys, or event-driven updates based on the consistency contract.
- Prevent stampedes with request coalescing, bounded stale-while-revalidate, or controlled refresh, and record cache hit rate, stale age, invalidation lag, and backend load. Treat cache values as untrusted serialized data with schema and tenant boundaries.
- An invalidation event can be lost, duplicated, or reordered, so it cannot be the only correctness mechanism. Global locks can become unavailable; test a writer crash, subscriber lag, cache eviction, and an authorization change.

## References

- [Redis: distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)
- Further reading (blog): [Shopify: caching without overcaching](https://shopify.engineering/caching-without-overcaching)

## What to learn next

- Official documentation: [Redis documentation](https://redis.io/docs/latest/)
- Manual or specification: [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [Shopify Engineering](https://shopify.engineering/)
- Hands-on guide: [Redis tutorials](https://redis.io/learn/)
