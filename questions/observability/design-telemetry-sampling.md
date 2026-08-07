---
title: Design trace sampling without losing incidents
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, troubleshooting, cost-optimization, pca]
sources:
  - url: https://opentelemetry.io/docs/concepts/sampling/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design trace sampling without losing incidents

How would you reduce trace cost while retaining useful incident evidence?

## Answer guide

- Start with head sampling when a fixed predictable rate is sufficient, or use tail sampling when decisions need final attributes such as error status or latency.
- Always retain or preferentially retain error, high-latency, and selected critical-journey traces, then document the sampling decision in trace metadata and dashboards.
- Estimate volume from request rate, spans per request, attribute size, and retention; validate that sampling produces representative data for normal traffic too.
- Sampling is not a privacy control and cannot recover spans dropped before a tail decision. Sampling every error can still overwhelm storage during a broad outage, so apply bounded policies.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry: Sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [Further reading: OpenTelemetry Collector tail sampling processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor)

## What to learn next

- Official documentation: [OpenTelemetry sampling concepts](https://opentelemetry.io/docs/concepts/sampling/)
- Manual or specification: [OpenTelemetry tracing SDK specification — sampling](https://opentelemetry.io/docs/specs/otel/trace/sdk/)
- Maintainer or personal blog: [Liz Fong-Jones — reliability and observability writing](https://www.lizthegrey.com/)
- Technical blog: [Honeycomb engineering blog](https://www.honeycomb.io/blog/)
- Hands-on guide: [OpenTelemetry Collector probabilistic sampler processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor)
