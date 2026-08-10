---
title: Evolve a log schema without breaking consumers
theme: logging
difficulty: senior
type: scenario
tags: [logging, observability, change-management, reliability, otca]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/data-model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evolve a log schema without breaking consumers

How would you change a widely used log field from a string to a structured value?

## Answer guide

- Treat schemas as contracts with dashboards, alerts, parsers, retention rules, and external consumers. Inventory those consumers, define the desired type and semantics, and introduce a new versioned field rather than silently changing the meaning of an existing one.
- During migration, dual-write where cost and sensitivity allow, update readers to prefer the new field, and measure adoption and parsing failures. Avoid ambiguous transformations such as converting a free-form message into a presumed canonical status; preserve original evidence when it matters.
- Remove the old field only after the documented compatibility period and after checking saved queries, exports, and downstream pipelines. Schema validation in CI and sampled production records catch regressions, but a rollback plan is still needed when collector or backend mappings reject the new type.

## References

- [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Further reading (blog): [Elastic: ECS versioning](https://www.elastic.co/docs/reference/ecs/)

## What to learn next

- Official documentation: [Elastic Common Schema](https://www.elastic.co/docs/reference/ecs)
- Manual or specification: [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Elastic Common Schema introduction](https://www.elastic.co/docs/reference/ecs/)
- Hands-on guide: [Migrating to ECS](https://www.elastic.co/docs/reference/ecs/migrating-to-ecs)
