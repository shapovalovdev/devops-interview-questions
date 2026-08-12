---
title: Explain cache-aside basics
theme: caching
difficulty: junior
type: scenario
tags: [caching, performance, reliability, databases]
sources:
  - url: https://redis.io/docs/latest/develop/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain cache-aside basics

Walk through what the application code does on a read and on a write when it uses a cache-aside pattern against Redis, and name the race that this pattern is known for.

## Answer guide

- On a read the application asks the cache first. On a hit it returns the value; on a miss it queries the database, writes the value back to the cache with a TTL, and returns it. On a write it updates the database and then deletes the cache entry rather than overwriting it. The application owns every step, which is the defining property: the cache is a passive key-value store that knows nothing about the origin, so any client that skips the pattern is free to leave stale data behind.
- Delete on write rather than update on write, for two reasons. Writing the new value into the cache means computing it in a code path that may not have the full object, and any two concurrent writers can land in the opposite order in the database and in the cache. A delete makes the next reader repopulate from the database, so the cache converges on the origin instead of on whichever writer happened to finish second. Set a TTL regardless — it bounds how long any missed invalidation can hurt you.
- The known race is a concurrent read and write. A reader misses, reads value A from the database, and then stalls; a writer commits value B and deletes the cache key; the stalled reader now writes A back and it persists until the TTL expires. Nothing in plain cache-aside prevents this. The usual mitigations are a modest TTL so the window is bounded, a check-and-set write using Redis `WATCH`/`MULTI` or a `SET` with a version token so a stale populate is rejected, or delaying a second delete after the write.
- Operational consequences: the pattern only caches what has been asked for, so it is naturally lazy and every cold start hammers the database until the working set is resident. Concurrent misses on the same hot key all query the origin at once unless you coalesce them with a lock or single-flight. And because misses are served from the database, a cache outage converts to origin load rather than to errors — which is the correct failure mode, but only if the origin can survive the traffic, so measure that rather than assuming it.

## References

- [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Further reading (blog): [Cloudflare Blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Manual or specification: [HTTP caching specification](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Martin Kleppmann](https://martin.kleppmann.com/)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Redis getting started](https://redis.io/docs/latest/develop/get-started/)
