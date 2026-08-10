---
title: Operate a reliable telemetry collection pipeline
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, logging, reliability, prometheus, pca, otca]
sources:
  - url: https://opentelemetry.io/docs/collector/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Operate a reliable telemetry collection pipeline

What reliability controls should a production telemetry collection pipeline have?

## Answer guide

- Define receivers, processors, exporters, routing, retry, queue, and memory limits explicitly, and monitor ingest rate, dropped data, retry count, queue depth, and exporter latency.
- Isolate tenants or critical signals where practical and use backpressure and bounded queues so an unavailable backend does not exhaust application or collector resources.
- Test backend outages, configuration rollouts, and schema changes; provide a fallback diagnostic path when telemetry is degraded.
- Telemetry must not be allowed to take down the workload it observes. Unlimited buffering, synchronous application exports, and silently dropped signals make incidents harder to investigate.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry Collector documentation](https://opentelemetry.io/docs/collector/)
- [Further reading: OpenTelemetry Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)

## What to learn next

- Official documentation: [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
- Manual or specification: [OTLP protocol specification](https://opentelemetry.io/docs/specs/otlp/)
- Maintainer or personal blog: [Frederic Branczyk — cloud-native monitoring infrastructure](https://brancz.com/)
- Technical blog: [CNCF Blog](https://www.cncf.io/blog/)
- Hands-on guide: [Scaling the OpenTelemetry Collector](https://opentelemetry.io/docs/collector/scaling/)
