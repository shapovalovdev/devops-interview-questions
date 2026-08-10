---
title: Migrate a company from fragmented logging to a common platform
theme: logging
difficulty: staff
type: scenario
tags: [logging, platform-engineering, change-management, leadership]
sources:
  - url: https://opentelemetry.io/docs/collector/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Migrate a company from fragmented logging to a common platform

How would you plan a migration from many logging agents and backends without losing operational capability?

## Answer guide

- Inventory sources, owners, data classifications, current delivery paths, contracts, and essential searches before selecting a migration sequence. Categorize workloads by risk and start with a representative low-risk service; a lift-and-shift that ignores unknown parsers and audit dependencies creates hidden outages.
- Introduce a compatible collector or bridge, dual-deliver a bounded sample where cost permits, and compare event counts, freshness, fields, access controls, and saved queries. Provide dashboards and runbooks that show teams the new path is equivalent or better before cutover.
- Govern exit criteria and rollback: define what loss, latency, and schema drift are acceptable, migrate tenants in waves, and retire old pipelines only after retention obligations and incident evidence are covered. Track adoption and exceptions publicly so the program does not become permanent fragmentation.

## References

- [OpenTelemetry Collector documentation](https://opentelemetry.io/docs/collector/)
- Further reading (blog): [Grafana: migrate to Loki](https://grafana.com/docs/loki/latest/operations/storage/migrate-to-tsdb/)

## What to learn next

- Official documentation: [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
- Manual or specification: [OpenTelemetry logs specification](https://opentelemetry.io/docs/specs/otel/logs/)
- Maintainer or personal blog: [OpenTelemetry blog](https://opentelemetry.io/blog/)
- Technical blog: [Grafana Loki migration](https://grafana.com/docs/loki/latest/operations/storage/migrate-to-tsdb/)
- Hands-on guide: [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
