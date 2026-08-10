---
title: Control metric-label cardinality
theme: observability
difficulty: middle
type: troubleshooting
tags: [observability, monitoring, prometheus, troubleshooting, pca, otca]
sources:
  - url: https://prometheus.io/docs/practices/naming/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control metric-label cardinality

Why is a metric backend failing under high cardinality, and how would you fix it?

## Answer guide

- Every unique metric name plus label-value set forms a time series. Labels such as request ID, email address, full URL, or timestamp multiply series without a useful aggregate.
- Identify the exploding label with cardinality analysis, then remove it, normalize it to a bounded route/template, or move per-request detail to traces and logs.
- Keep labels bounded and meaningful for aggregation, such as operation, status class, region, or workload. Enforce a cardinality budget in instrumentation review.
- Do not fix the symptom only by adding backend capacity or silently dropping all telemetry. Both can postpone failure while preserving an expensive, misleading metric design.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Prometheus: Metric and label naming](https://prometheus.io/docs/practices/naming/)
- [Further reading: Prometheus instrumentation practices](https://prometheus.io/docs/practices/instrumentation/)

## What to learn next

- Official documentation: [Prometheus configuration and metric relabeling](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- Manual or specification: [OpenMetrics specification](https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md)
- Maintainer or personal blog: [Brian Brazil — cardinality is key](https://www.robustperception.io/cardinality-is-key/)
- Technical blog: [Grafana Labs engineering blog](https://grafana.com/blog/)
- Hands-on guide: [OpenTelemetry Collector filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/filterprocessor)
