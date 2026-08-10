---
title: Explain a read-through cache
theme: caching
difficulty: junior
type: theory
tags: [caching, databases, architecture, reliability]
sources:
  - url: https://redis.io/docs/latest/develop/use/patterns/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain a read-through cache

What is a read-through cache, and how does it differ operationally from a cache the application populates itself?

## Answer guide

- In a read-through cache the cache layer owns the miss path. The application only ever asks the cache; on a miss the cache client or a loader component fetches from the origin, stores the value, and returns it. The application code contains no explicit load-and-populate branch.
- The practical difference is where the miss logic lives, not what the data ends up looking like. Because the loader is centralised, TTL, jitter, serialization format, and single-flight coalescing are configured once instead of being reimplemented at every call site — that consistency is the main reason to choose the pattern.
- The trade is control and coupling. The cache layer now needs credentials, connection pools, and timeouts for the origin, and it becomes a hard dependency: if the loader cannot reach the origin, the application has no local fallback path to write itself. Errors surface as cache errors, which makes attributing an incident harder unless the loader propagates the underlying cause.
- Write behaviour must be decided separately. Read-through says nothing about writes; you still choose whether writes go through the cache, around it with an explicit invalidation, or behind it asynchronously. Pairing read-through with an origin-only write path and no invalidation is the usual source of unexplained staleness.
- Failure modes to name: a loader without request coalescing turning one expired hot key into a thundering herd, a loader that caches exceptions as if they were values, and a shared loader whose timeout is longer than the caller's, so the caller gives up while the cache keeps holding a connection.

## References

- [Redis programming patterns documentation](https://redis.io/docs/latest/develop/use/patterns/)
- Further reading (blog): [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## What to learn next

- Official documentation: [Redis programming patterns documentation](https://redis.io/docs/latest/develop/use/patterns/)
- Manual or specification: [Memcached text and meta protocol specification](https://github.com/memcached/memcached/blob/master/doc/protocol.txt)
- Maintainer or personal blog: [Marc Brooker — caches, modes, and unstable systems](https://brooker.co.za/blog/2021/08/27/caches.html)
- Technical blog: [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
- Hands-on guide: [Redis getting started guide](https://redis.io/docs/latest/develop/get-started/)
