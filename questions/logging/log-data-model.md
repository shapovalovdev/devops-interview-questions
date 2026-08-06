---
title: Choose fields for a log data model
theme: logging
difficulty: junior
type: theory
tags: [logging, observability, debugging]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/data-model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose fields for a log data model

What makes a log record useful to both humans and machines?

## Answer guide

- Start with an event timestamp, severity, body or event name, service identity, deployment version, and source location. Add attributes for the operation, outcome, error classification, and correlation identifiers. A stable schema lets users filter and aggregate without fragile regular expressions.
- Separate resource attributes that describe the producing process, host, container, or service from event attributes that vary per record. Use documented names and types, including a rule for null or absent fields; otherwise dashboards silently mix incompatible values after a deployment.
- Do not put unbounded objects, secrets, raw request bodies, or high-cardinality identifiers into every record. Record an opaque identifier and fetch protected detail elsewhere when justified. Version the schema, validate emitters in tests, and make field changes observable during rollout.

## References

- [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Further reading (blog): [Elastic engineering blog](https://www.elastic.co/blog/)

## What to learn next

- Official documentation: [Elastic Common Schema reference](https://www.elastic.co/docs/reference/ecs)
- Manual or specification: [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Elastic engineering blog](https://www.elastic.co/blog/)
- Hands-on guide: [Elastic Common Schema base fields](https://www.elastic.co/docs/reference/ecs/ecs-base)
