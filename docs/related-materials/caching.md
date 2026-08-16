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

Placement, TTL, and hit ratio come before invalidation and stampedes because
every later mechanism tightens or backs up the contract a bound on wrongness
sets.

1. [Compare cache placement layers](../../questions/caching/cache-placement-layers.html)
    — Where the copy lives is the first of the three decisions every caching
    question ultimately reduces to.
2. [Explain cache-aside basics](../../questions/caching/cache-aside-basics.html)
    — Cache-aside is the pattern most services actually run, so it anchors the
    mechanics tier before any variation.
3. [Explain a read-through cache](../../questions/caching/read-through-cache-basics.html)
    — Read-through is the managed counterpoint, and the difference between them
    only teaches when placed side by side.
4. [Choose a TTL for a cached value](../../questions/caching/ttl-selection-basics.html)
    — The TTL is the explicit contract for how wrong a value may be and for how
    long, set before keys or invalidation tighten it.
5. [Interpret a cache hit ratio honestly](../../questions/caching/cache-hit-ratio-basics.html)
    — Reading a hit ratio honestly calibrates the mechanics before the policy
    questions arrive.
6. [Design cache keys safely](../../questions/caching/cache-key-design.html) —
    Keys carry the tenant and representation boundaries, so they precede
    invalidation — policy built on unsafe keys is wasted work.
7. [Design cache invalidation policy](../../questions/caching/cache-invalidation-policy.html)
    — Invalidation is the hard problem, and it needs safe keys and the TTL
    backstop already in place.
8. [Choose a cache eviction policy](../../questions/caching/cache-eviction-policy.html)
    — Eviction governs what the cache keeps when memory runs out, the mechanical
    sibling of invalidation.
9. [Prevent a cache stampede](../../questions/caching/cache-stampede-control.html)
    — A stampede is what the invalidation and TTL model produces at expiry, so
    it follows them directly.
10. [Cache negative results safely](../../questions/caching/negative-caching.html)
    — Caching failures and misses extends the same wrongness contract to values
    that are absent.
11. [Tune Redis maxmemory and eviction behaviour](../../questions/caching/redis-maxmemory-tuning.html)
    — Redis under memory pressure is where the operational tier starts, because
    eviction becomes an incident when maxmemory is wrong.
12. [Operate Redis replication and failover for a cache tier](../../questions/caching/redis-failover-operations.html)
    — Failover is the cache tier's outage rehearsal, and it presumes the tuning
    that shaped its steady state.
13. [Operate Memcached memory and slab allocation](../../questions/caching/memcached-slab-tuning.html)
    — Memcached's slab allocator is the counter-example that keeps Redis habits
    from hardening into folklore.
14. [Design cache coherence across regions](../../questions/caching/multi-region-cache-coherence.html)
    — Multi-region coherence widens every earlier contract across distance and
    replication.
15. [Build a cache capacity and cost model](../../questions/caching/cache-capacity-cost-model.html)
    — The capacity and cost model prices the tier the coherence question just
    made global.
16. [Set SLOs that survive a degraded cache](../../questions/caching/cache-slo-degradation-policy.html)
    — SLOs that survive a degraded cache promise the degradation the tiers above
    rehearsed.
17. [Govern a shared cache platform](../../questions/caching/shared-cache-platform-governance.html)
    — Governing a shared cache platform is the close, because a cache other
    teams depend on is a product.
