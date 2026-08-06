---
title: Compare metrics, logs, and traces during an incident
theme: observability
difficulty: middle
type: theory
tags: [observability, monitoring, debugging, incident-response]
sources:
  - url: https://opentelemetry.io/docs/concepts/observability-primer/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Compare metrics, logs, and traces during an incident

How do metrics, logs, and traces complement each other when diagnosing a production problem?

## Answer guide

- Metrics are numeric time series: use them to detect changes, calculate rates and error ratios, and drive low-cost alerts. They explain *that* a population is unhealthy, not a single request's cause.
- Logs are timestamped event records: use structured fields to inspect a particular failure, audit a decision, or find an exception. Unbounded payloads and high-volume debug logs make them expensive and can expose sensitive data.
- Traces model a request as causally related spans across process boundaries. They reveal where latency or an error entered a dependency chain, but sampling can omit the exact request.
- Correlate signals with stable resource attributes and trace/span identifiers. Start with an SLI or alert, narrow with metrics, then pivot to a trace and the relevant logs; do not make an individual log line the alerting signal.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry: Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- [Further reading: OpenTelemetry log correlation](https://opentelemetry.io/docs/specs/otel/logs/)
