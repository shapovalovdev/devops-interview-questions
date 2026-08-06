---
title: Validate telemetry data quality after a release
theme: observability
difficulty: middle
type: troubleshooting
tags: [observability, monitoring, deployment, troubleshooting]
sources:
  - url: https://opentelemetry.io/docs/concepts/observability-primer/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Validate telemetry data quality after a release

How do you determine whether a release broke observability rather than the service itself?

## Answer guide

- Compare request volume from an independent edge or synthetic signal with application metrics, then check for changed metric names, labels, resource attributes, trace continuity, and log parsing errors.
- Validate dashboards and alerts against known traffic in a pre-production environment and use release annotations to correlate schema changes with gaps.
- Treat missing, stale, or suddenly cardinal metrics as telemetry incidents with an owner, rollback path, and quality SLO where the data is operationally critical.
- Do not assume no alerts means healthy. Conversely, avoid changing alert thresholds first: establish whether the underlying signal, scraper, collector, or query semantics changed.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry: Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- [Further reading: Prometheus instrumentation practices](https://prometheus.io/docs/practices/instrumentation/)
