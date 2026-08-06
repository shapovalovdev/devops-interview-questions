---
title: How would you design a systems-performance observability program across teams?
theme: systems-performance
difficulty: staff
type: scenario
tags: [performance, observability, governance, reliability]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How would you design a systems-performance observability program across teams?

## Answer guide

- Define shared user outcomes and a small set of comparable signals: request latency distributions, traffic, errors, saturation, resource pressure, and cost. Publish ownership, cardinality limits, retention, and privacy boundaries with service teams.
- Provide common dashboards, tracing conventions, profiling access, baselines, and incident playbooks while allowing workload-specific signals. Make instrumentation quality measurable through coverage, alert usefulness, and time-to-diagnosis reviews.
- Fund the program as a product with reliability and security controls. Unbounded telemetry costs, sensitive attributes, inconsistent clocks, and vendor lock-in can defeat it; periodically retire metrics that do not support decisions.

## References

- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Further reading (blog): [Brendan Gregg — Performance Analysis](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry](https://opentelemetry.io/docs/)
- Manual or specification: [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Maintainer or personal blog: [Brendan Gregg — methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Honeycomb Blog](https://www.honeycomb.io/blog)
- Hands-on guide: [Prometheus documentation](https://prometheus.io/docs/)
