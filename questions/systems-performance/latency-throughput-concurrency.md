---
title: How are latency, throughput, and concurrency related during load?
theme: systems-performance
difficulty: junior
type: theory
tags: [performance, capacity-planning, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How are latency, throughput, and concurrency related during load?

## Answer guide

- Throughput is completed work per time, latency is elapsed time per operation, and concurrency is in-flight work. Measure them at the same boundary, such as a service endpoint or queue.
- With a stable system, Little's Law relates average concurrency to throughput multiplied by average latency. As offered load approaches a bottleneck, queues grow and latency rises before throughput necessarily increases.
- Use percentiles and error rate, not averages alone. Timeouts, retries, admission control, and finite client pools can hide or amplify overload, so validate the workload model before extrapolating capacity.

## References

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/)
- [Google SRE Workbook](https://sre.google/workbook/)
- Further reading (personal blog): [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/)
- Manual or specification: [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Grafana latency histograms](https://grafana.com/docs/grafana/latest/)
