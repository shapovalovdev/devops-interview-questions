---
title: Evaluate cache consistency trade-offs
theme: caching
difficulty: senior
type: scenario
tags: [caching, performance, reliability, databases]
sources:
  - url: https://redis.io/docs/latest/develop/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Evaluate cache consistency trade-offs

A product owner asks why the profile page occasionally shows a name the user changed two minutes ago. Explain what consistency a cache can and cannot offer, and how you would decide what is acceptable here.

## Answer guide

- A cache does not weaken the database's consistency; it adds a second copy with its own update path, and every guarantee you have is about how long the two may disagree and whether a single user can observe their own write. Frame the requirement in those terms rather than as strong or eventual: a bounded staleness window, expressed as a maximum age the business accepts per data class, plus read-your-writes for the session that made the change. Those two are separable, and the profile complaint is almost always a violation of the second, not the first.
- Read-your-writes is cheap to provide and worth providing first. After a write, either delete the key and route that session's next read to the origin, or pin the session to a version token so it will not accept a cached value older than the write it just made. Everyone else can tolerate the staleness window. The general staleness bound comes from TTL plus invalidation latency plus replication lag, and each term has to be measured, since a cache invalidated correctly but reading from a lagging replica repopulates stale data and the bug looks identical.
- Costs rise steeply as you tighten the window. TTL alone is the cheapest and gives a bound but no promptness. Explicit invalidation on write is prompt but only as reliable as the delivery path, so an invalidation lost during a partition leaves an entry stale until TTL — the TTL is the backstop, which is why an infinite TTL with perfect invalidation is a trap. Versioned or immutable keys avoid invalidation entirely by never mutating a value, at the cost of more keys and lower hit rate. Anything stronger, such as a write that is not acknowledged until the cache agrees, converts a cache outage into a write outage.
- Decide per data class, not per system: a display name tolerates a minute, a permission or entitlement check usually tolerates nothing and should not be cached at the same layer, and a price shown before a charge needs revalidation at the point of commitment rather than a shorter TTL. Failure modes: multi-region caches where each region's invalidation arrives independently so two users see different values; negative cache entries that outlive the record's creation; and staleness that is invisible because nobody exports the age of served values, so the only detector is a customer complaint.

## References

- [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Further reading (blog): [Cloudflare Blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Manual or specification: [HTTP caching specification](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Martin Kleppmann](https://martin.kleppmann.com/)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Redis getting started](https://redis.io/docs/latest/develop/get-started/)
