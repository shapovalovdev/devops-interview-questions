---
title: Choose between write-through and write-behind caching
theme: caching
difficulty: senior
type: theory
tags: [caching, databases, architecture, reliability, distributed-systems]
sources:
  - url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/develop/use/patterns/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Choose between write-through and write-behind caching

When would you accept a write-behind cache, and what must be true of the system before you do?

## Answer guide

- Define both precisely. Write-through updates the cache and the system of record synchronously within the write request, so the cache never holds a value the store has not accepted. Write-behind acknowledges the write once it is in the cache and flushes to the store asynchronously, so the cache is temporarily the only place the newest data exists.
- Write-through buys correctness and predictable recovery at the cost of latency: every write pays for the slowest of the two systems, and a store outage becomes a write outage. It also warms the cache with data that may never be read, which wastes memory on write-heavy, read-sparse workloads. Write-around — writing only to the store and invalidating the cache — is often the better default for those.
- Write-behind buys write latency and origin smoothing, and it costs you durability. Between the acknowledgement and the flush, a node loss silently discards accepted writes unless the buffer is itself replicated and persisted. That is only acceptable when the data can be reconstructed, when the loss window is bounded and explicitly accepted by the product, or when the buffer is a real durable log rather than cache memory.
- Order and idempotency matter more in write-behind. Concurrent writes to the same key must not be flushed out of order, retries must be idempotent, and the flush must survive partial failure without duplicating side effects. In practice this pushes teams toward a durable log with an outbox or change-data-capture consumer, which is a different architecture that happens to look like a cache from the caller's side.
- Failure modes to name: a growing flush backlog that is invisible until it exceeds memory; a store rejecting a flushed write, leaving the cache holding a value the database refused; read-your-writes breaking for clients routed to a different replica; and a "write-behind" implementation with no bounded queue, which converts a store slowdown into an out-of-memory kill.

## References

- [Amazon ElastiCache caching strategies and best practices](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html)
- [Redis programming patterns documentation](https://redis.io/docs/latest/develop/use/patterns/)
- Further reading (blog): [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## What to learn next

- Official documentation: [Amazon ElastiCache caching strategies and best practices](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html)
- Manual or specification: [Redis keyspace notifications reference](https://redis.io/docs/latest/develop/use/keyspace-notifications/)
- Maintainer or personal blog: [Martin Kleppmann — using logs to build a solid data infrastructure](https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html)
- Technical blog: [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
- Hands-on guide: [Redis programming patterns documentation](https://redis.io/docs/latest/develop/use/patterns/)
