---
title: What cross-team contracts prevent performance regressions in a platform?
theme: performance-engineering
difficulty: staff
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/metrics/
    source_type: official-docs
    verified_on: 2026-08-06
---

# What cross-team contracts prevent performance regressions in a platform?

Twenty teams ship into one platform and every incident opens with an argument about whose latency number is correct. What contracts between those teams actually prevent performance regressions?

## Answer guide

- Three contracts carry most of the weight. A telemetry contract: every service emits the same latency metric, with the same name, unit, buckets, and attributes, measured at the same boundary. A budget contract: each endpoint publishes a p99 it will hold and each caller knows its allocation within the parent's target. A change contract: dependency owners announce and canary changes that move those numbers. The first is a precondition for the others, because teams measuring at different boundaries can argue indefinitely without either being wrong.
- Standardise on OpenTelemetry semantic conventions rather than local naming, so a metric such as HTTP server request duration means the same thing in every service and platform dashboards and alerts can be generated instead of hand-built twenty times. Fix the unit the specification prescribes (durations in seconds), the histogram boundaries around the shared objective, and the required attributes, then ship it as a default instrumentation library and collector pipeline so conformance is the path of least effort. Cap attribute cardinality at the collector, because one team's unbounded label degrades everyone's alerting.
- Contracts need versions and migrations. Semantic conventions themselves evolve, and a renamed metric silently breaks every alert and recording rule built on it, so dual-emit across a deprecation window rather than cutting over. Keep the mandated set small enough to be genuinely universal and let teams add whatever else they want above it. Make conformance testable in CI — asserting metric name, unit, and required attributes — because an automated check is worth more than a standards document nobody opens.
- A contract with no owner and no enforcement point decays into a wiki page within two quarters. Budgets handed down without the callee's agreement, or without the capacity to meet them, are ignored, and budgets with no consequence on breach are advisory by definition. The subtler failure is measuring conformance instead of outcomes: every team can emit the correct metric while no single owner is accountable for the end-to-end latency a user experiences, at which point the contracts are all satisfied and the product is still slow.

## References

- [OpenTelemetry: Metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
