---
title: Diagnose missing trace context across services
theme: observability
difficulty: middle
type: troubleshooting
tags: [observability, debugging, troubleshooting, security, pca, otca]
sources:
  - url: https://www.w3.org/TR/trace-context/
    source_type: standard
    verified_on: 2026-08-06
---

# Diagnose missing trace context across services

Traces split at a service boundary. How do you diagnose and fix context propagation?

## Answer guide

- Check that the caller injects and the receiver extracts the same propagation format, for example W3C Trace Context `traceparent`, on the actual HTTP, messaging, or RPC carrier.
- Ensure middleware runs at the correct boundary and that asynchronous work captures and restores context rather than creating an unrelated root span.
- Test a request end-to-end and inspect headers and resulting parent/trace IDs, while respecting gateways that intentionally remove untrusted headers.
- Treat external trace context as untrusted and do not put secrets or personal data in propagated baggage. A missing parent must not make the service fail its user request.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [Further reading: OpenTelemetry propagators](https://opentelemetry.io/docs/specs/otel/context/api-propagators/)

## What to learn next

- Official documentation: [OpenTelemetry context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- Manual or specification: [W3C Trace Context recommendation](https://www.w3.org/TR/trace-context/)
- Maintainer or personal blog: [Liz Fong-Jones — distributed tracing writing](https://www.lizthegrey.com/)
- Technical blog: [Honeycomb engineering blog](https://www.honeycomb.io/blog/)
- Hands-on guide: [Jaeger getting started](https://www.jaegertracing.io/docs/latest/getting-started/)
