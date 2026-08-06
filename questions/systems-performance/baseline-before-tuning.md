---
title: Why establish a baseline before performance tuning?
theme: systems-performance
difficulty: junior
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.brendangregg.com/methodology.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Why establish a baseline before performance tuning?

## Answer guide

- Capture a reproducible healthy baseline for the workload: request rate, latency percentiles, errors, CPU, memory, I/O, network, and configuration versions. This turns a vague regression into a comparison.
- Change one hypothesis at a time and repeat the same measurement window. Keep raw data and environment details because cache warmth, noisy neighbors, and traffic mix can otherwise explain apparent gains.
- Define a user-facing success criterion first. A microbenchmark can improve while tail latency, cost, reliability, or another service becomes worse; rollback if the controlled comparison does not meet the criterion.

## References

- [Brendan Gregg: Performance Methodologies](https://www.brendangregg.com/methodology.html)
- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/)
- Further reading (personal blog): [Brendan Gregg — Active Benchmarking](https://www.brendangregg.com/activebenchmarking.html)

## What to learn next

- Official documentation: [Google SRE workbook](https://sre.google/workbook/)
- Manual or specification: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Google Cloud Blog](https://cloud.google.com/blog/)
- Hands-on guide: [Prometheus querying basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
