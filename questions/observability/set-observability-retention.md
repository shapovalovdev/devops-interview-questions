---
title: Set telemetry retention and query-cost controls
theme: observability
difficulty: senior
type: scenario
tags: [observability, monitoring, logging, cost-optimization, prometheus, pca]
sources:
  - url: https://sre.google/workbook/monitoring/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set telemetry retention and query-cost controls

How would you control observability cost without removing the evidence needed for incidents and planning?

## Answer guide

- Classify signals by operational purpose: retain high-resolution SLI and recent incident data long enough to respond, then downsample or aggregate older capacity-planning data.
- Set separate retention, sampling, cardinality, and query limits for metrics, logs, and traces, based on service criticality, legal obligations, and actual investigation needs.
- Track ingest volume, active series, storage growth, query latency, and cost per tenant/service; review exceptions with the teams creating the data.
- A blanket short retention may erase evidence before a slow-burn incident is understood. A blanket long retention is costly and increases privacy exposure, especially for raw logs.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE Workbook: Monitoring](https://sre.google/workbook/monitoring/)
- [Further reading: Prometheus storage](https://prometheus.io/docs/prometheus/latest/storage/)

## What to learn next

- Official documentation: [Prometheus storage and retention](https://prometheus.io/docs/prometheus/latest/storage/)
- Manual or specification: [Google SRE Book — free online edition](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Brian Brazil — Robust Perception monitoring blog](https://www.robustperception.io/blog/)
- Technical blog: [Grafana Labs engineering blog](https://grafana.com/blog/)
- Hands-on guide: [Thanos compactor — retention and downsampling](https://thanos.io/tip/components/compact.md/)
