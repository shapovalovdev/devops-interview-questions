---
title: Explain a metrics time series and its labels
theme: observability
difficulty: junior
type: theory
tags: [observability, monitoring, prometheus]
sources:
  - url: https://prometheus.io/docs/concepts/data_model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a metrics time series and its labels

What is a metrics time series, and how should labels be chosen?

## Answer guide

- A time series is a stream of timestamped numeric samples identified by a metric name and a complete set of label key-value pairs.
- Use a name and unit that describe one measurable thing, then use labels for bounded dimensions needed to aggregate or filter, such as operation, status class, or region.
- Keep label names and values stable so dashboards and alerts retain their meaning across releases; document the owner and intended aggregation.
- Do not put unique request IDs, user identifiers, or raw paths in labels. Each new value creates more series, increasing memory, storage, query cost, and failure risk.

## References

- [Prometheus: Data model](https://prometheus.io/docs/concepts/data_model/)
- [Further reading: Prometheus metric and label naming](https://prometheus.io/docs/practices/naming/)
