---
title: Why can high-cardinality metrics become a performance incident?
theme: performance-engineering
difficulty: middle
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://prometheus.io/docs/practices/naming/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Why can high-cardinality metrics become a performance incident?

An engineer adds a `user_id` label to a request counter and the Prometheus server starts getting OOM-killed. Why does one label do that, and what belongs in a label at all?

## Answer guide

- A metric's cost is its number of distinct label-value combinations, and those combinations multiply rather than add: ten thousand users times five endpoints times four status classes is two hundred thousand series from one counter. Prometheus carries on the order of a couple of kilobytes of memory per active series for index and head-chunk state, so a single unbounded label turns a trivial metric into gigabytes. The working rule is that a label value must come from a small, bounded set known in advance — user and request IDs, raw URLs, email addresses, full error strings, and timestamps are not labels.
- Cardinality costs twice. Ingestion cost scales with active series through the index, head block, and WAL; query cost scales with series matched, so a `sum by (endpoint)` across two hundred thousand series must read and merge all of them and dashboards and alert rules start timing out — the failure arrives as a monitoring outage exactly when you need monitoring. Churn is as damaging as breadth: labels whose values rotate, such as pod name under frequent redeploys or a session identifier, mint new series continuously so the head block never reaches a steady state.
- Normalise before you label. Template the path (`/users/:id`, never `/users/8412`), bucket durations and sizes instead of recording exact values, and collapse a long tail into an explicit `other` value. Unbounded detail belongs in signals stored per event rather than per series: traces, structured logs, and exemplars that link a histogram bucket to the trace that produced it. Enforce the rule mechanically with `metric_relabel_configs` dropping or rewriting labels at scrape time, plus `sample_limit` and label limits on the scrape config so one bad deploy cannot take the server down.
- The damage is retroactive and outlives the fix: removing the label stops new series, but the existing ones remain queryable and resident for the whole retention window, so recovery usually means deleting series or waiting out retention. Recording rules built on the offending metric inherit its cost. And the blast radius does not respect team boundaries — one team's `user_id` label degrades everyone's alerting on a shared Prometheus, which is the argument for reviewing new metric definitions rather than discovering the problem later on a top-series dashboard.

## References

- [Prometheus: Metric and label naming](https://prometheus.io/docs/practices/naming/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
