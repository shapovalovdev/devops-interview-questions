# Caching: related materials

Treat the upstream Redis, Memcached, Varnish, and CDN manuals attached to each
Question as the authority for product-specific behaviour, and RFC 9111 as the
authority for HTTP cache semantics. Caching questions almost always reduce to
three separate decisions — where the copy lives, how long it may be wrong, and
what happens when the copy is missing or the cache itself is gone — so read the
specification for the correctness rules and the vendor manuals for the operating
limits. The individual-author and vendor blogs below give context and war
stories; they are not evidence for factual claims.

## What to learn next

- Official documentation: [Redis developer documentation](https://redis.io/docs/latest/develop/)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Salvatore Sanfilippo — antirez writings on Redis](https://antirez.com/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## Legal free books

No commercial caching title is linked here: avoid unauthorized copies. The IETF
HTTP specifications, the Redis and Memcached manuals, the Varnish users guide,
and the freely published Google SRE book are all lawfully free to read and cover
the same ground for interview preparation.

## Suggested study order

Start with placement, TTL, hit ratio, and the difference between cache-aside and
read-through. Then work through invalidation, key scoping, eviction, stampede
control, negative caching, and the operational behaviour of Redis and Memcached
under memory pressure and failover. Finish with multi-region coherence, capacity
and cost models, SLOs that survive a degraded cache, and the governance of a
shared cache platform.
