---
title: Debug gaps in production telemetry
theme: observability
difficulty: senior
type: troubleshooting
tags: [observability, monitoring, debugging, troubleshooting]
sources:
  - url: https://opentelemetry.io/docs/collector/resiliency/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug gaps in production telemetry

Metrics and traces disappear during peak traffic. How do you investigate without making the outage worse?

## Answer guide

- Bound the time and scope, then compare workload traffic with SDK export errors, collector queue/drop metrics, CPU and memory, network errors, backend ingest limits, and recent configuration changes.
- Preserve enough evidence to identify whether loss occurs at instrumentation, agent, collector, transport, or backend; use independent black-box checks for the customer outcome.
- Apply the smallest safe mitigation, such as reducing optional attributes, changing sampling, scaling a bottleneck, or rolling back a bad configuration, then verify recovered continuity.
- Do not enable unrestricted debug telemetry in a peak outage. It can increase CPU, cardinality, network traffic, and sensitive-data exposure precisely when the pipeline is constrained.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)
- [Further reading: OpenTelemetry Collector monitoring](https://opentelemetry.io/docs/collector/internal-telemetry/)
