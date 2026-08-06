---
title: What should a performance regression check in CI actually prove?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# What should a performance regression check in CI actually prove?

## Answer guide

- Start by defining the user-visible outcome and workload boundary before choosing a number. For stable environments, thresholds, and gates, record the request class, time window, traffic mix, dependency versions, and the service-level objective or explicit decision that the measurement will inform.
- Measure a repeatable baseline, then change one plausible cause at a time. Compare latency distribution, throughput, errors, resource saturation, and cost against the same workload; use traces or profiles to connect an observed symptom to the resource or dependency doing the work.
- Treat the result as conditional rather than universal. Cache state, retries, background jobs, autoscaling, noisy neighbors, and sampling can change the outcome. Define an abort or rollback condition, retain raw evidence, and verify that an apparent improvement does not move delay, failures, or cost to another component.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
