---
title: Run data-layer chaos without risking the data
theme: chaos-engineering
difficulty: senior
type: scenario
tags: [chaos-engineering, databases, storage, recovery]
sources:
  - url: https://www.postgresql.org/docs/current/high-availability.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Run data-layer chaos without risking the data

Which database faults are safe to inject, and which are not?

## Answer guide

- Separate availability faults from integrity faults. Killing a replica, failing over a primary, adding replication lag, saturating connections, partitioning a quorum member, and slowing storage I/O are reversible: the data is intact and the experiment tests failover time, client reconnection, read-your-writes behaviour, and how the application copes with a read-only window. Corrupting pages, deleting data, or dropping the write-ahead log are not experiments; they are restore drills and belong to a separate, carefully staged exercise.
- The interesting findings are usually in the client, not the server. Do the drivers notice a promoted primary, or do they hold connections to a demoted node? Does the pool reconnect with backoff or stampede? Do queued writes get retried non-idempotently and double-apply? Does the application serve stale reads from a lagging replica without saying so? Measure replication lag, failover duration, error classes, and duplicate or lost records with a continuous correctness check running throughout.
- Material constraints: a verified restore, not just a backup; a rehearsed point-in-time recovery path; capacity to run the check without competing with production; and awareness that failover is often slower than the client timeout, so the application sees an outage even when the database recovers correctly. Set the abort condition on data correctness, not only on latency.
- Failure modes: an experiment that triggers a real automatic failover that then cannot fail back; split-brain when a partitioned primary keeps accepting writes; a lagging replica promoted with data loss; migrations or backups running concurrently; and cross-service damage when a shared database is faulted, since consumers you did not consult are also on the other end of that connection. Get explicit consent from every dependent team and prefer a dedicated non-production copy with production-shaped data whenever the risk is to correctness rather than to availability.

## References

- [PostgreSQL — high availability, load balancing and replication](https://www.postgresql.org/docs/current/high-availability.html)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [PostgreSQL — high availability and replication](https://www.postgresql.org/docs/current/high-availability.html)
- Manual or specification: [PostgreSQL — continuous archiving and point-in-time recovery](https://www.postgresql.org/docs/current/continuous-archiving.html)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — data integrity](https://sre.google/sre-book/data-integrity/)
