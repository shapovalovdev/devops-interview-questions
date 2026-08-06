---
title: Plan anti-entropy repair
theme: distributed-systems
difficulty: senior
type: scenario
tags: [databases, recovery, reliability]
sources:
  - url: https://cassandra.apache.org/doc/latest/cassandra/managing/operating/repair.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan anti-entropy repair

Why does an eventually consistent data store need repair, and how would you operate it safely?

## Answer guide

- Replication can miss writes while a replica is unavailable, so repair compares replicas and transfers missing or divergent ranges before retention policies make recovery impossible. Schedule repair with topology, replication factor, and repair window in mind rather than assuming ordinary reads will heal all state.
- Budget network, disk, CPU, and compaction capacity; observe range coverage, transferred data, failures, and backlog. Prefer incremental, segmented execution and verify quorum health before and after operations so repair does not destabilize an already degraded cluster.
- Running all nodes at once can cause congestion and timeout cascades. Skipping repair past hint or tombstone retention can resurrect deleted data or leave permanent inconsistency; document how to rebuild an irrecoverable replica instead of improvising during an outage.

## References

- [Apache Cassandra: repair](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/repair.html)
- Further reading (personal blog): [Aphyr: Jepsen analyses](https://aphyr.com/tags/jepsen)

## What to learn next

- Official documentation: [Cassandra repair operations](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/repair.html)
- Manual or specification: [Cassandra architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [Datastax: repairs](https://www.datastax.com/blog)
- Hands-on guide: [Cassandra nodetool](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/nodetool/nodetool.html)
