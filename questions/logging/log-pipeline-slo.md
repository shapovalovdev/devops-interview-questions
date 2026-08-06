---
title: Define an SLO for a log delivery pipeline
theme: logging
difficulty: senior
type: scenario
tags: [logging, reliability, monitoring, observability]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define an SLO for a log delivery pipeline

What would you measure to know whether an observability logging pipeline is reliable?

## Answer guide

- Define the service from the consumer's view: for an accepted eligible record, it should become searchable within a stated freshness window and retain required fields. Measure ingestion acceptance, end-to-end delay, parse success, delivery loss, query availability, and completeness for critical sources.
- Use a synthetic canary record with a unique but non-sensitive identifier to continuously verify the full path from producer through collection to query. Compare source-side and backend counts by source and reason; backend acceptance alone cannot show records dropped before it.
- Set objectives by data class. Best-effort debug logs can have a different loss and latency target from audit data. Alert on burn rate and pipeline saturation, then test failure modes such as a full disk, unavailable backend, certificate expiry, and metadata API outage.

## References

- [Google SRE Book: service level objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Honeycomb: observability pipelines](https://www.honeycomb.io/blog/observability-pipelines)

## What to learn next

- Official documentation: [OpenTelemetry Collector internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)
- Manual or specification: [Google SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/)
- Maintainer or personal blog: [Liz Fong-Jones' writing](https://www.lizthegrey.com/)
- Technical blog: [Honeycomb observability pipelines](https://www.honeycomb.io/blog/observability-pipelines)
- Hands-on guide: [OpenTelemetry Collector monitoring](https://opentelemetry.io/docs/collector/monitoring/)
