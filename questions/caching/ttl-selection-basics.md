---
title: Choose a TTL for a cached value
theme: caching
difficulty: junior
type: scenario
tags: [caching, performance, reliability, latency]
sources:
  - url: https://redis.io/docs/latest/commands/expire/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Choose a TTL for a cached value

A team asks you to pick the TTL for a newly cached lookup. How do you decide, and what do you check afterwards?

## Answer guide

- Start from the staleness the business can tolerate, not from a round number. Ask how wrong the value is allowed to be and for how long: a currency rate, a feature flag, and a product description have very different answers, and the TTL is the explicit contract for that tolerance.
- Then check the cost side. TTL sets the floor on origin load: with a steady request rate, the origin sees roughly one refresh per key per TTL. Shortening a TTL multiplies origin traffic by the same factor, so the choice is a trade between freshness and the load the origin can absorb.
- Know the mechanics of your store. In Redis, `EXPIRE` sets a per-key timeout that is cleared by any command that overwrites the value without preserving the TTL, such as a plain `SET`. `SET` with the `KEEPTTL` option, or re-applying the expiry on every write, avoids silently converting a temporary entry into a permanent one. Redis also expires keys both lazily on access and by a background sampling cycle, so memory is not released at the exact instant of expiry.
- Add jitter. Identical TTLs written during a deploy or a warm-up expire together and produce a synchronised miss storm against the origin. Randomising the TTL by a small percentage spreads the refreshes.
- Operational failure modes: an unbounded key space with a long TTL that grows until eviction starts, a TTL longer than the invalidation path can compensate for, and a TTL so short that the cache never pays for its own round trip. Verify with hit ratio, origin request rate, and value age after the change.

## References

- [Redis EXPIRE command reference](https://redis.io/docs/latest/commands/expire/)
- Further reading (blog): [Fastly blog](https://www.fastly.com/blog)

## What to learn next

- Official documentation: [Redis EXPIRE command reference](https://redis.io/docs/latest/commands/expire/)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Salvatore Sanfilippo — antirez writings on Redis](https://antirez.com/)
- Technical blog: [Fastly blog](https://www.fastly.com/blog)
- Hands-on guide: [MDN HTTP caching guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
