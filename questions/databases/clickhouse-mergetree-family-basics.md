---
title: Explain ClickHouse MergeTree table engine basics
theme: databases
difficulty: senior
type: theory
tags: [databases, clickhouse, storage, performance]
sources:
  - url: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/
    source_type: official-docs
    verified_on: 2026-08-17
---

# Explain ClickHouse MergeTree table engine basics

What do parts, background merges, ORDER BY, and partitioning each contribute to how a MergeTree table behaves?

## Answer guide

- Inserts create immutable parts, each sorted by the table's ORDER BY key and holding one or more granules — the units column reads and block-skipping metadata work on. Background merges continually combine smaller parts into larger ones (hence "MergeTree"), which is how the engine absorbs frequent small inserts over time without an in-place update path; the mechanism resembles an LSM tree's compaction more than a B-tree's page splits, and more than the in-place page reorganization InnoDB performs for MySQL tables.
- ORDER BY is the single most consequential choice: it is not a uniqueness constraint but the physical clustering key, deciding which range filters can skip blocks, how well per-column compression works, and how expensive a full part rewrite will be later. Changing it on a large table means rewriting history, so it must be designed around the dominant query shapes (for logs: facility, then time) rather than defaulted.
- PARTITION BY is the coarse second axis: partitions bound individual parts, make wholesale drop operations cheap (dropping yesterday's partition is metadata work, not data rewriting), and enable TTL expressions per partition. Over-partitioning is the classic mistake — thousands of tiny partitions multiply part counts, exhaust merge capacity, and can fail inserts outright, so partition at a granularity you will actually drop or expire (a day or a month), not per tenant-hour.
- Read the family as variations on this core: ReplacingMergeTree collapses rows by key during merges (eventual, not immediate, deduplication), SummingMergeTree pre-aggregates, and the replication variant ReplicatedMergeTree adds consensus-coordinated part sets through a coordination layer — the composition that turns the engine into production infrastructure.

## References

- [ClickHouse documentation: MergeTree table engine](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree)
- [ClickHouse documentation: MergeTree family of table engines](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/)
- Further reading (blog): [ClickHouse blog: table engine and performance articles](https://clickhouse.com/blog/)

## What to learn next

- Official documentation: [ClickHouse MergeTree documentation](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree)
- Manual or specification: [ClickHouse CREATE TABLE syntax](https://clickhouse.com/docs/en/sql-reference/statements/create/table)
- Maintainer or personal blog: [ClickHouse engineering blog](https://clickhouse.com/blog/)
- Technical blog: [Percona engineering blog: OLAP storage internals](https://www.percona.com/blog/)
- Hands-on guide: [ClickHouse quick start](https://clickhouse.com/docs/en/quick-start)
