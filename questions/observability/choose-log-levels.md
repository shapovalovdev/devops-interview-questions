---
title: Choose useful application log levels
theme: observability
difficulty: junior
type: scenario
tags: [observability, logging, troubleshooting, security, pca]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/data-model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose useful application log levels

How should a service choose log levels without turning production logs into noise?

## Answer guide

- Use levels to communicate operational actionability: `ERROR` for failed work requiring investigation, `WARN` for abnormal recoverable conditions, `INFO` for meaningful lifecycle or business events, and `DEBUG` for temporary diagnostic detail.
- Emit structured fields such as timestamp, severity, service identity, operation, outcome, and trace context so records can be queried reliably.
- Set normal production verbosity deliberately and make debug logging bounded and reversible. A level is not a substitute for a metric or alert.
- Never log credentials, tokens, raw personal data, or unrestricted request bodies. Excessive warning logs train responders to ignore real degradation and inflate ingest cost.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [Further reading: OpenTelemetry logging concepts](https://opentelemetry.io/docs/concepts/signals/logs/)
