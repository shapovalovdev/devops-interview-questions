---
title: Combine black-box and white-box monitoring
theme: observability
difficulty: middle
type: theory
tags: [observability, monitoring, reliability, troubleshooting, prometheus, pca]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Combine black-box and white-box monitoring

How do black-box and white-box monitoring differ, and why use both?

## Answer guide

- Black-box monitoring observes a system from outside, such as a synthetic client checking a public API; it detects user-visible availability and path failures.
- White-box monitoring uses internal telemetry such as queue depth, error counters, and resource saturation to explain behavior and forecast capacity risks.
- Use black-box signals for end-to-end user outcomes and white-box signals for diagnosis and early warning, correlating them through service and region identity.
- A green internal dashboard does not prove a user can reach the service, while synthetic success can miss partial tenant or dependency failures. Neither alone provides complete coverage.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Further reading: Google SRE Workbook—Monitoring](https://sre.google/workbook/monitoring/)

## What to learn next

- Official documentation: [Prometheus Blackbox exporter](https://github.com/prometheus/blackbox_exporter)
- Manual or specification: [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- Maintainer or personal blog: [Brian Brazil — Robust Perception monitoring blog](https://www.robustperception.io/blog/)
- Technical blog: [AWS Builders' Library — instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
- Hands-on guide: [Prometheus first steps](https://prometheus.io/docs/prometheus/latest/getting_started/)
