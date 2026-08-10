---
title: Debug latency without averaging away the incident
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, latency, performance, monitoring, metrics]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug latency without averaging away the incident

## Answer guide

- Segment latency by percentile, endpoint, region, status, dependency, and request size. A stable average can hide a failing tail, while client-side latency can include DNS, queues, retries, and network time absent from server spans.
- Correlate the latency shift with saturation, errors, deployments, garbage collection, database waits, and downstream spans. Use a low-risk sample or profiler only after defining the question it must answer.
- Mitigate the bottleneck with load reduction, queueing limits, caching, or capacity while validating correctness. Raising timeouts blindly ties up more resources and can convert slow responses into a cascading failure.

## References

- [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE Book — Handling Overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Brendan Gregg — The USE Method](https://www.brendangregg.com/usemethod.html)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [OpenTelemetry metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)
- Hands-on guide: [Prometheus histograms](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg](https://www.brendangregg.com/blog/)
- Technical blog: [Grafana Labs blog](https://grafana.com/blog/)
