---
title: How do you design a performance observability strategy across many services?
theme: performance-engineering
difficulty: staff
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://opentelemetry.io/docs/concepts/observability-primer/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you design a performance observability strategy across many services?

A platform of 200 services has per-team dashboards, three tracing backends, and a telemetry bill growing faster than traffic. How do you design a performance observability strategy across all of it?

## Answer guide

- Define the small set every service must emit and make that set the cheapest path. A latency histogram with agreed buckets, request and error counts, saturation signals for the resources on the path, and traces with propagated context answer most performance questions, and standardising them lets dashboards and alerts be generated centrally rather than maintained 200 times. Everything beyond the core stays optional and team-owned. Route all of it through a collector layer you control, so sampling, redaction, relabelling, and backend choice become policy changes instead of 200 code changes.
- Use each signal for what it is good at and link rather than duplicate. Metrics are cheap, aggregated, and complete, so alerting and objectives ride on them; traces are expensive and per-event, so they explain one specific slow request; logs carry detail that is not dimensional. Connect them with exemplars from histogram buckets to traces and trace and span IDs in log lines. Head sampling at one percent is cheap and discards precisely the slow requests you needed, so for a performance programme tail-based sampling in the collector, which keeps slow and failed traces at the cost of buffering, is usually the right trade.
- Cost scales with active series and span volume, so the levers are cardinality limits, tiered retention (short at full resolution, long downsampled), and sampling rate — set centrally with a per-team budget rather than discovered on an invoice. Cross-service comparison requires a shared measurement boundary and sane clock discipline, without which the platform-wide view is not a view of anything. Keep instrumentation vendor-neutral over OTLP even where the backend is not, because consolidating three backends is a multi-quarter migration and re-instrumenting 200 services is what makes it fail.
- A strategy that only adds signals produces a system nobody queries during an incident and a bill nobody can defend, so it has to say what stops being collected. Generated alerts still need per-service thresholds, or the platform ships 200 flapping pages and the organisation learns to ignore them. And observability sits on the request path whenever instrumentation is synchronous: a blocking exporter, a full-sampling profiler, or a collector under backpressure adds latency to the very service it was installed to watch.

## References

- [OpenTelemetry: Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
