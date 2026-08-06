---
title: Design structured logs for request correlation
theme: logging
difficulty: middle
type: scenario
tags: [logging, observability, debugging, incident-response]
sources:
  - url: https://opentelemetry.io/docs/specs/semconv/general/recording-errors/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design structured logs for request correlation

Which fields should a service emit so an operator can follow one failed request across multiple components?

## Answer guide

- Emit a stable trace or request identifier at the ingress boundary and propagate trace context to downstream calls; include the trace/span identifiers in logs so operators can pivot between logs, traces, and the affected service.
- Record a timestamp, severity, service identity/version, operation, outcome or error type, and narrowly scoped diagnostic fields. Use structured fields with stable names and types instead of parsing prose.
- Treat logging as a data-exposure boundary: scrub credentials, tokens, and unnecessary personal data before export, and use access control and retention policies appropriate to the data that remains.
- Correlation is only useful when propagation survives asynchronous boundaries and sampling. Define how message IDs, retries, and sampled-away traces are represented, and test a failed request end to end.

## References

- [OpenTelemetry semantic conventions: recording errors](https://opentelemetry.io/docs/specs/semconv/general/recording-errors/)
- Further reading (blog): [Honeycomb engineering blog](https://www.honeycomb.io/blog/)

## What to learn next

- Official documentation: [OpenTelemetry logging](https://opentelemetry.io/docs/specs/otel/logs/)
- Manual or specification: [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Maintainer or personal blog: [Charity Majors on structured events](https://charity.wtf/2019/02/05/logs-vs-structured-events/)
- Technical blog: [Honeycomb engineering blog](https://www.honeycomb.io/blog/)
- Hands-on guide: [OpenTelemetry Collector log collection](https://opentelemetry.io/docs/collector/)
