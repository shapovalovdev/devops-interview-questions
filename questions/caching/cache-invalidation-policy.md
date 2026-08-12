---
title: Design cache invalidation policy
theme: caching
difficulty: middle
type: scenario
tags: [caching, performance, reliability, databases]
sources:
  - url: https://redis.io/docs/latest/develop/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design cache invalidation policy

An order's total is cached under three different keys, and a discount change updated only one of them. Write the invalidation policy that prevents this class of bug, and say what its backstop is.

## Answer guide

- Start by making invalidation derivable rather than remembered. Every cached value needs a declared dependency set — which entities it was computed from — and a key scheme that lets a change to an entity name the keys to drop: a prefix or a tag per entity such as `order:{id}:*`, or a registered index from entity to key. Three hand-maintained keys with an invalidation written at one call site is the failure mode by construction, because the fourth reader will add a fourth key and not know about the writer.
- Invalidate from the write path that owns the data, once, rather than from every caller. Put the delete in the repository or in a change-data-capture consumer on the database's log, so a write from a batch job, a migration, or an admin tool triggers the same invalidation as the API. Delete rather than update, so the next reader repopulates from the origin and concurrent writers cannot leave the cache holding the loser's value. Where the cost of a miss is unacceptable, refresh asynchronously after the delete rather than writing the value inline.
- An alternative that removes the problem is to never mutate a cached value: include a version in the key, so a change writes `order:{id}:v7` and readers that resolve the current version simply stop referencing v6, which then ages out. This makes invalidation atomic and multi-region-safe, at the cost of more keys, a lower hit rate immediately after a change, and a version pointer that itself has to be current. Immutable content-addressed keys are the same idea taken further and are the right choice for derived artifacts.
- TTL is the backstop and it is not optional. Invalidation is a message that can be lost, dropped during a partition, or skipped by a code path nobody updated, so every entry needs a maximum age that bounds the damage — and a policy of no TTL because invalidation is exhaustive is how a wrong value survives for months. Failure modes: an invalidation issued before the database transaction commits, so a concurrent reader repopulates the old value; wildcard deletes implemented with `KEYS` in production, which blocks the server; and CDN or client caches holding the same value with a TTL you cannot reach, so origin invalidation fixes nothing the user sees.

## References

- [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Further reading (blog): [Cloudflare Blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Manual or specification: [HTTP caching specification](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Martin Kleppmann](https://martin.kleppmann.com/)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Redis getting started](https://redis.io/docs/latest/develop/get-started/)
