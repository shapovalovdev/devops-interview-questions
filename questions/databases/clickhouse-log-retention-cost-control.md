---
title: Control ClickHouse cost and retention for log ingestion
theme: databases
difficulty: middle
type: scenario
tags: [databases, clickhouse, logging, cost-optimization, reliability]
sources:
  - url: https://clickhouse.com/docs/en/sql-reference/statements/alter/ttl
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://clickhouse.com/docs/en/sql-reference/statements/alter/delete
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://clickhouse.com/docs/en/use-cases/observability
    source_type: official-docs
    verified_on: 2026-08-17
---

# Control ClickHouse cost and retention for log ingestion

A leasing company's platform team wants to pour application and system logs into ClickHouse instead of a SaaS logging product. What design keeps it cheap and predictable?

## Answer guide

- Let retention be structural, not procedural: define TTL expressions (table-level or per-column) so ClickHouse expires rows and drops whole expired partitions during merges, and pair them with PARTITION BY day so expiry becomes cheap partition drops. The equivalent chore in MySQL or MariaDB is scripted `DROP PARTITION` maintenance, and both share the rule that wholesale expiry must never be per-row deletion. Budget retention by tier — hot days for full logs, weeks for downsampled aggregates — because at ingestion scale the retention policy is the storage bill, and tiering beats keeping everything raw.
- Keep the write path cheap and bounded: batches rather than singleton inserts (small frequent inserts create part explosion and merge debt), asynchronous inserts or a buffering layer for chatty producers, and CODEC/ZSTD compression on string columns — compression of an ordered, columnar layout is often the single largest cost lever. Alert on part counts, merge backlog, and disk growth trend, not just on disk percentage, because those are the early signals of an ingestion pattern the engine cannot absorb.
- Do not design around DELETE. Heavy DELETE-style mutations are heavyweight background rewrites of parts; they contend with merges, hold disk space until rewritten, and scale poorly — the idiomatic answers are TTL expiry, partition drops, and rewriting problematic data rather than surgically deleting rows. This is a real mindset shift coming from row stores, where a DELETE is a routine statement.
- Price the compliance edge explicitly: logs that must truly disappear (personal data) may need careful mutation discipline or per-tenant TTL and partitioning, because "delete it sometime during merges" is not the same guarantee as a synchronous delete — a distinction worth agreeing with security and legal before the first byte lands.

## References

- [ClickHouse documentation: TTL statements](https://clickhouse.com/docs/en/sql-reference/statements/alter/ttl)
- [ClickHouse documentation: DELETE and mutations](https://clickhouse.com/docs/en/sql-reference/statements/alter/delete)
- [ClickHouse documentation: observability use case](https://clickhouse.com/docs/en/use-cases/observability)
- Further reading (blog): [ClickHouse blog: log analytics and cost articles](https://clickhouse.com/blog/)

## What to learn next

- Official documentation: [ClickHouse observability use case](https://clickhouse.com/docs/en/use-cases/observability)
- Manual or specification: [ClickHouse TTL statements](https://clickhouse.com/docs/en/sql-reference/statements/alter/ttl)
- Maintainer or personal blog: [ClickHouse engineering blog](https://clickhouse.com/blog/)
- Technical blog: [Percona engineering blog: OLAP and analytics databases](https://www.percona.com/blog/)
- Hands-on guide: [ClickHouse quick start](https://clickhouse.com/docs/en/quick-start)
