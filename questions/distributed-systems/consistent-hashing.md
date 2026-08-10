---
title: Rebalance a consistent-hash partitioned service
theme: distributed-systems
difficulty: senior
type: scenario
tags: [databases, capacity-planning, reliability]
sources:
  - url: https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Rebalance a consistent-hash partitioned service

How do you add capacity to a hash-partitioned system without causing a customer outage?

## Answer guide

- Model ownership, replication factor, hot-key distribution, and movement volume before changing membership. A hash ring limits average movement but does not make it zero; use controlled streaming, capacity headroom, and validation that every range remains sufficiently replicated.
- Drain or add nodes incrementally, rate-limit repair and transfer, and monitor client error rate, latency, disk space, and replica health. Keep routing metadata and application clients compatible with the transition and preserve a rollback or pause point.
- Uniform hashes do not cure skewed tenants or oversized partitions. Simultaneous rebalances can saturate network and disks, while a node declared healthy before its data is ready can serve incomplete or overloaded ranges.

## References

- [Apache Cassandra: Dynamo architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html)
- Further reading (personal blog): [Aphyr: Cassandra](https://aphyr.com/posts/294-jepsen-cassandra)

## What to learn next

- Official documentation: [Cassandra operations](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)
- Manual or specification: [Cassandra architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [Datastax: data modeling](https://www.datastax.com/blog)
- Hands-on guide: [Cassandra quickstart](https://cassandra.apache.org/_/quickstart.html)
