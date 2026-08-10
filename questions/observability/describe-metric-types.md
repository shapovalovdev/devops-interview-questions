---
title: Choose a counter, gauge, histogram, or summary
theme: observability
difficulty: junior
type: theory
tags: [observability, monitoring, prometheus, reliability, pca]
sources:
  - url: https://prometheus.io/docs/concepts/metric_types/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a counter, gauge, histogram, or summary

When should you use a counter, gauge, histogram, or summary metric?

## Answer guide

- A counter only increases until reset, so use it for events such as completed requests and calculate rates over time. A gauge can rise and fall, so use it for current queue depth or in-flight work.
- A histogram counts observations in configured buckets and exposes count and sum, allowing a backend to aggregate distributions and estimate quantiles. A summary calculates configured quantiles client-side.
- Choose histogram buckets from operational latency or size thresholds, and use the same bucket scheme for series you need to aggregate.
- Do not use a gauge as an event total or create a new time series per request. Bad bucket choices hide tail latency; unbounded labels can exhaust the monitoring system.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Prometheus: Metric types](https://prometheus.io/docs/concepts/metric_types/)
- [Further reading: Prometheus histogram best practices](https://prometheus.io/docs/practices/histograms/)

## What to learn next

- Official documentation: [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
- Manual or specification: [OpenMetrics specification](https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md)
- Maintainer or personal blog: [Brian Brazil — how does a Prometheus counter work?](https://www.robustperception.io/how-does-a-prometheus-counter-work/)
- Technical blog: [Grafana Labs engineering blog](https://grafana.com/blog/)
- Hands-on guide: [Prometheus instrumentation practices](https://prometheus.io/docs/practices/instrumentation/)
