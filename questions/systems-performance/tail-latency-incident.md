---
title: How do you investigate a tail-latency incident when average latency is normal?
theme: systems-performance
difficulty: senior
type: troubleshooting
tags: [performance, monitoring, incident-response, reliability]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you investigate a tail-latency incident when average latency is normal?

## Answer guide

- Use percentile or histogram data by endpoint, dependency, region, and request class. Averages hide a small slow cohort that may dominate user impact, retry volume, or deadline exhaustion.
- Trace representative slow requests across queues, connection pools, CPU scheduling, storage, and downstream calls. Compare them with fast requests to find differing payloads, placement, cache state, or retries.
- Confirm sampling bias and coordinated-omission risks in the measurement system. Raising timeouts may reduce visible errors while increasing concurrency and queueing, so pair mitigation with backpressure and a causal fix.

## References

- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Further reading (personal blog): [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram practices](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Google Cloud Blog](https://cloud.google.com/blog/)
- Hands-on guide: [Grafana histogram visualization](https://grafana.com/docs/grafana/latest/)
