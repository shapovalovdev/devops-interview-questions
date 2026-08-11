---
title: Decide whether a cache is the right answer
theme: caching
difficulty: staff
type: theory
tags: [caching, architecture, performance, governance, capacity-planning]
sources:
  - url: https://www.postgresql.org/docs/current/runtime-config-resource.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Decide whether a cache is the right answer

A team proposes adding a cache to fix a latency problem. As the reviewing engineer, how do you decide whether to approve it?

## Answer guide

- Insist on the measurement before the mechanism. Establish where the time is actually spent: a slow query that needs an index, an N+1 access pattern, a serialization cost, a missing connection pool, or genuine unavoidable work. A cache added on top of an unindexed query hides the defect, and the defect returns at full force during every cold start, deploy, or failover.
- Check that the workload has the properties a cache needs: reads substantially outnumber writes, the same values are read repeatedly within their useful lifetime, the working set fits in an affordable amount of memory, and the data can tolerate being wrong for a stated period. If any of these fails, the cache adds cost and a new failure mode without a durable win.
- Consider the cheaper alternatives explicitly, because a cache is a permanent operational commitment. Tuning the database's own buffers and planner, adding a covering index, materialising a view, precomputing on write, batching, or simply provisioning more origin capacity are all options with far less invalidation risk. PostgreSQL's `shared_buffers` and related settings, for example, already implement a well-tuned cache that many teams never adjust before adding a second one in front of it.
- Price the whole cost. A cache brings a new tier to run and patch, a memory bill, an invalidation design, a cold-start plan, an on-call surface, and an ongoing correctness risk in every future code change that writes the underlying data. Compare that against the measured benefit and against the alternative of making the origin faster once.
- If you approve it, require the operating contract up front: what the staleness budget is, what happens when the cache is unavailable, how the key space is scoped and bounded, how invalidation is triggered, what the hit ratio and origin load look like when healthy, and who owns it. A cache approved without those answers becomes an unowned dependency that nobody can safely remove later.

## References

- [PostgreSQL resource consumption configuration reference](https://www.postgresql.org/docs/current/runtime-config-resource.html)
- [Amazon ElastiCache caching strategies and best practices](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html)
- Further reading (blog): [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## What to learn next

- Official documentation: [PostgreSQL resource consumption configuration reference](https://www.postgresql.org/docs/current/runtime-config-resource.html)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Dan Luu — caches, LRU versus random](https://danluu.com/2choices-eviction/)
- Technical blog: [AWS Builders' Library — caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
- Hands-on guide: [Google SRE book — table of contents](https://sre.google/sre-book/table-of-contents/)
