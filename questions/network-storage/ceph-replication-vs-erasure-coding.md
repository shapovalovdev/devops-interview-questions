---
title: Choose Ceph replication or erasure coding
theme: network-storage
difficulty: senior
type: scenario
tags: [storage, networking, reliability, performance, capacity-planning]
sources:
  - url: https://docs.ceph.com/en/latest/rados/operations/erasure-code/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose Ceph replication or erasure coding

How do replication and erasure coding trade capacity, latency, and failure recovery in Ceph?

## Answer guide

- Replication stores complete copies and generally gives simpler read and write behavior at a capacity cost. Erasure coding splits data into data and coding chunks, reducing raw-capacity overhead for a chosen fault tolerance but adding encoding, network, and repair complexity.
- Select a pool type per workload after measuring small-write behavior, read pattern, recovery bandwidth, hardware topology, and operational skills. Model host, rack, and zone failures through CRUSH placement rules and reserve enough capacity for backfill and recovery.
- Do not compare only usable terabytes. An erasure-coded design can meet durability goals yet miss latency objectives or recover too slowly under concurrent load; a nearly full cluster can also be unable to restore redundancy safely.

## References

- [Ceph: erasure coding](https://docs.ceph.com/en/latest/rados/operations/erasure-code/)
- Further reading (blog): [Ceph developer blog](https://ceph.io/en/news/blog/)

## What to learn next

- Official documentation: [Ceph architecture](https://docs.ceph.com/en/latest/architecture/)
- Manual or specification: [Ceph erasure coding](https://docs.ceph.com/en/latest/rados/operations/erasure-code/)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog/channel/storage)
- Hands-on guide: [Ceph quick start](https://docs.ceph.com/en/latest/start/)
