---
title: Operate Memcached memory and slab allocation
theme: caching
difficulty: middle
type: scenario
tags: [caching, memcached, memory, capacity, performance]
sources:
  - url: https://github.com/memcached/memcached/wiki/UserInternals
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://github.com/memcached/memcached/wiki/ConfiguringServer
    source_type: official-docs
    verified_on: 2026-08-10
---

# Operate Memcached memory and slab allocation

A Memcached tier is evicting heavily while reporting free memory. What is happening and how do you fix it?

## Answer guide

- Memcached does not allocate memory per item. It divides memory into pages and assigns each page to a slab class that stores items up to a fixed chunk size. An item is stored in the smallest slab class whose chunk fits it, and the unused remainder of that chunk is wasted. This is why a tier can evict from one class while another holds free chunks.
- The symptom of slab imbalance is evictions concentrated in a few classes. When the size distribution of the workload shifts — a new field makes serialized objects cross a chunk boundary — the pages already assigned to the old class are not automatically useful to the new one. Modern versions rebalance pages between classes automatically, and that behaviour is the first thing to confirm is enabled rather than reimplementing it.
- Tune the size distribution before tuning the allocator. Compressing values, trimming unused fields, and splitting oversized objects usually beats growing the tier. The chunk growth factor and the maximum item size are configurable, but changing them alters the whole class layout and needs a restart, which empties the node.
- Capacity is per node, not per cluster. Memcached servers do not know about each other; the client library hashes the key to a server. Adding a node therefore both adds memory and remaps keys, so plan for the miss burst that follows and prefer a consistent-hashing client so that only a fraction of keys move.
- Failure modes to name: evictions read as a memory shortage when they are a slab-class problem; a restart to apply a setting silently taking a whole node's dataset with it; `stats slabs` and `stats items` never being collected so nobody can see the distribution; and an item larger than the maximum item size failing to store while the application treats the failure as a cache miss forever.

## References

- [Memcached internals manual](https://github.com/memcached/memcached/wiki/UserInternals)
- [Memcached server configuration manual](https://github.com/memcached/memcached/wiki/ConfiguringServer)
- Further reading (blog): [Dormando — Memcached maintainer notes](https://www.dormando.me/)

## What to learn next

- Official documentation: [Memcached project wiki](https://github.com/memcached/memcached/wiki)
- Manual or specification: [Memcached text and meta protocol specification](https://github.com/memcached/memcached/blob/master/doc/protocol.txt)
- Maintainer or personal blog: [Dormando — Memcached maintainer notes](https://www.dormando.me/)
- Technical blog: [Scaling Memcache at Facebook, NSDI 2013](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala)
- Hands-on guide: [Memcached caching story tutorial](https://github.com/memcached/memcached/wiki/TutorialCachingStory)
