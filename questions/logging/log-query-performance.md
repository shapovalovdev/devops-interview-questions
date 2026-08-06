---
title: Diagnose a slow expensive log query
theme: logging
difficulty: middle
type: scenario
tags: [logging, performance, capacity-planning, troubleshooting]
sources:
  - url: https://grafana.com/docs/loki/latest/get-started/labels/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a slow expensive log query

How would you improve a slow log query without making the data unusable?

## Answer guide

- First narrow time, service, environment, and known low-cardinality labels, then inspect the backend query plan or statistics. Full-text search over a broad retention window usually scans far more data than an investigation needs; make the investigation hypothesis explicit.
- Index only dimensions with bounded, reusable values. Request IDs, user IDs, raw URLs, and error text are excellent event fields but expensive index labels in systems such as Loki. Put them in the body or structured payload and filter after selecting a bounded stream.
- Measure query latency, scanned bytes, index cardinality, and tenant impact before and after a schema change. A faster dashboard that relies on an uncontrolled label can destabilize ingestion later; use saved queries, limits, and retention tiers as complementary controls.

## References

- [Loki label best practices](https://grafana.com/docs/loki/latest/get-started/labels/)
- Further reading (blog): [Grafana: labels in Loki](https://grafana.com/blog/2020/04/21/how-labels-in-loki-can-make-log-queries-faster-and-more-efficient/)

## What to learn next

- Official documentation: [Loki labels](https://grafana.com/docs/loki/latest/get-started/labels/)
- Manual or specification: [Loki LogQL](https://grafana.com/docs/loki/latest/query/)
- Maintainer or personal blog: [Ed Welch's Grafana writing](https://grafana.com/blog/author/ed-welch/)
- Technical blog: [Grafana on Loki labels](https://grafana.com/blog/2020/04/21/how-labels-in-loki-can-make-log-queries-faster-and-more-efficient/)
- Hands-on guide: [Loki query examples](https://grafana.com/docs/loki/latest/query/query_examples/)
