---
title: Correlate trace context with logs
theme: logging
difficulty: middle
type: scenario
tags: [logging, observability, debugging, distributed-systems, otca]
sources:
  - url: https://www.w3.org/TR/trace-context/
    source_type: standard
    verified_on: 2026-08-06
---

# Correlate trace context with logs

How would you add trace-to-log correlation without making logs depend on a tracing backend?

## Answer guide

- Propagate a standards-based trace context through incoming and outgoing boundaries, then inject the current trace and span identifiers into structured log records. The identifiers are correlation keys; the logging system still functions when tracing is sampled, disabled, or queried elsewhere.
- Log the service resource and event timestamp as well as IDs. A trace ID alone does not identify which deployment emitted a record, and asynchronous work needs an explicit message or job correlation rule when it starts a new trace.
- Treat identifiers as opaque and validate propagation at HTTP, queue, scheduled-job, and retry boundaries. Missing context, malformed untrusted headers, and sampled-away spans are normal failure modes; emit a new trusted root context where policy requires and surface propagation errors.

## References

- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [OpenTelemetry logging correlation](https://opentelemetry.io/docs/specs/otel/logs/)
- Further reading (blog): [Honeycomb OpenTelemetry guidance](https://docs.honeycomb.io/send-data/opentelemetry/)

## What to learn next

- Official documentation: [OpenTelemetry context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- Manual or specification: [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Honeycomb OpenTelemetry guidance](https://docs.honeycomb.io/send-data/opentelemetry/)
- Hands-on guide: [OpenTelemetry instrumentation](https://opentelemetry.io/docs/languages/)
