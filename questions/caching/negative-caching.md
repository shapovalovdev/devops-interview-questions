---
title: Cache negative results safely
theme: caching
difficulty: middle
type: scenario
tags: [caching, reliability, availability, databases]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9111.html
    source_type: standard
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/commands/expire/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Cache negative results safely

Lookups for identifiers that do not exist are hammering the database. Should you cache the misses, and how?

## Answer guide

- Yes, cache the negative result, but treat it as a different kind of entry. A miss that is not cached means every request for a non-existent key reaches the origin, so an attacker or a buggy client enumerating identifiers can generate unbounded origin load while the hit ratio still looks healthy. Storing an explicit tombstone value converts that into a cache hit.
- Give negative entries their own, much shorter TTL. The cost of a stale negative is different from the cost of a stale positive: a stale tombstone hides a record that has just been created, which users experience as "I saved it and it vanished". Seconds to low minutes is typical, and the create path must invalidate the tombstone rather than relying on expiry.
- Distinguish "known absent" from "could not determine". Never cache a timeout, a connection error, or a 5xx as an absence — that converts a transient origin failure into a durable wrong answer that outlives the incident. Only cache a definitive negative answer from the origin, and encode it as a distinct sentinel so the read path cannot confuse it with an empty value.
- HTTP has the same distinction built in: `404` and `410` are cacheable by default under RFC 9111's heuristic rules, while `502` and `503` are not cacheable without explicit freshness information. Relying on defaults without setting explicit `Cache-Control` on error responses is how an origin blip becomes a cached error at the edge.
- Failure modes to name: tombstones that share the eviction budget with real values and push out useful entries; a probabilistic filter used instead of tombstones without accounting for false positives; and negative caching applied to authorization decisions, where a cached "not permitted" outlives the grant that should have fixed it.

## References

- [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [Redis EXPIRE command reference](https://redis.io/docs/latest/commands/expire/)
- Further reading (blog): [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## What to learn next

- Official documentation: [MDN HTTP caching guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Marc Brooker — caches, modes, and unstable systems](https://brooker.co.za/blog/2021/08/27/caches.html)
- Technical blog: [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
- Hands-on guide: [web.dev — love your cache](https://web.dev/articles/love-your-cache)
