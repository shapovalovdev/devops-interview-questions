---
title: Explain why column stores win analytics
theme: databases
difficulty: junior
type: theory
tags: [databases, clickhouse, performance]
sources:
  - url: https://clickhouse.com/docs/en/about-us/distinctive-features
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.postgresql.org/docs/current/indexes-types.html
    source_type: official-docs
    verified_on: 2026-08-17
---

# Explain why column stores win analytics

Why does a column-oriented engine answer aggregate queries over billions of rows faster than a row-store with B-tree indexes?

## Answer guide

- Storage layout is the answer: a column store keeps each column's values together on disk, so a query touching five columns of a hundred reads five contiguous ranges instead of walking every row. An analytic query typically selects few columns but scans many rows, and that asymmetry is exactly what the layout exploits; a row store must load whole rows — all columns — to compute over any of them.
- Compression compounds it: values of one column repeat and cluster, so run-length, dictionary, and delta encodings shrink the data dramatically before it is even read, which means fewer disk reads and more of the working set in memory. Row pages interleave heterogeneous types and compress far worse.
- The B-tree index is not the escape hatch it seems: an index helps find a few rows, but an aggregation over a large fraction of the table defeats index selectivity, and the row store falls back to a full scan that still pays the load-every-row cost. Column stores instead sort data by key columns (ClickHouse's ORDER BY) so range filters skip entire blocks, and they can skip blocks via min/max metadata without reading them — the same instinct behind SQL Server columnstore indexes, which bolt a columnar structure onto a row-store engine for exactly these queries.
- The honest trade-off is the mirror image: a column store reassembles a row from scattered pieces, so fetching many wide rows one at a time — the OLTP pattern — is slower, which is why engines like ClickHouse are purpose-built for analytics and not a replacement for a transactional row store.

## References

- [ClickHouse documentation: distinctive features of column-oriented storage](https://clickhouse.com/docs/en/about-us/distinctive-features)
- [PostgreSQL documentation: index types (B-tree behavior)](https://www.postgresql.org/docs/current/indexes-types.html)
- Further reading (blog): [ClickHouse blog: architecture and performance articles](https://clickhouse.com/blog/)

## What to learn next

- Official documentation: [ClickHouse documentation](https://clickhouse.com/docs/en/)
- Manual or specification: [ClickHouse CREATE TABLE syntax](https://clickhouse.com/docs/en/sql-reference/statements/create/table)
- Maintainer or personal blog: [ClickHouse engineering blog](https://clickhouse.com/blog/)
- Technical blog: [Percona engineering blog: OLAP and analytics databases](https://www.percona.com/blog/)
- Hands-on guide: [ClickHouse quick start](https://clickhouse.com/docs/en/quick-start)
