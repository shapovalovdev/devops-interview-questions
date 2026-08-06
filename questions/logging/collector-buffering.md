---
title: Design collector buffering and backpressure
theme: logging
difficulty: middle
type: scenario
tags: [logging, observability, reliability, capacity-planning]
sources:
  - url: https://docs.fluentbit.io/manual/administration/buffering-and-storage
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design collector buffering and backpressure

What should happen when a log backend is slow or unavailable?

## Answer guide

- Give the collector bounded memory and, where durability matters, bounded disk buffering with a documented retry policy. Size both from peak event rate, record size, and the outage period the business accepts; unlimited queues convert a backend outage into node exhaustion.
- Decide explicitly whether each class of logs may be dropped, sampled, or must be durably retried. Preserve critical audit or security records separately from verbose diagnostics, attach delivery metrics, and make drops observable with counters and reason labels.
- Backpressure can propagate to an application if its logging library blocks, so test backend outage behavior under load. The safe choice may be asynchronous emission with bounded loss for normal logs, while critical events use a dedicated durable path and operational alerting.

## References

- [Fluent Bit buffering and storage](https://docs.fluentbit.io/manual/administration/buffering-and-storage)
- Further reading (blog): [Grafana engineering blog](https://grafana.com/blog/)

## What to learn next

- Official documentation: [Fluent Bit buffering](https://docs.fluentbit.io/manual/administration/buffering-and-storage)
- Manual or specification: [OpenTelemetry Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)
- Maintainer or personal blog: [Fluent Bit blog](https://fluentbit.io/blog/)
- Technical blog: [Grafana engineering blog](https://grafana.com/blog/)
- Hands-on guide: [Fluent Bit storage configuration](https://docs.fluentbit.io/manual/administration/buffering-and-storage#filesystem-buffering)
