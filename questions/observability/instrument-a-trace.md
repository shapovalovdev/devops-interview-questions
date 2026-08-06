---
title: Instrument a distributed trace for an API request
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, debugging, troubleshooting]
sources:
  - url: https://opentelemetry.io/docs/concepts/signals/traces/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Instrument a distributed trace for an API request

How would you instrument an API request so a responder can find a slow downstream call?

## Answer guide

- Create or continue a server span at the request boundary and create child spans around meaningful internal and client operations, including database and remote calls.
- Propagate context over supported transports so downstream spans join the same trace, and record status, duration, bounded attributes, and exceptions according to the telemetry contract.
- Name spans for stable operations rather than raw IDs or URLs. Include resource identity so the trace can be placed in its deployment context.
- Do not create a span for every loop iteration or attach secrets and unbounded user input. Instrumentation overhead and sensitive attributes require sampling, review, and redaction controls.

## References

- [OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [Further reading: OpenTelemetry context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
