---
title: Set a platform strategy for organization-wide logging
theme: logging
difficulty: staff
type: scenario
tags: [logging, platform-engineering, governance, leadership]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set a platform strategy for organization-wide logging

How would you create a logging platform strategy for hundreds of independently deployed services?

## Answer guide

- Publish a small supported contract: required resource identity, structured event conventions, correlation, redaction, ownership, and minimum delivery objectives. Offer maintained libraries, collectors, dashboards, and migration paths so teams can meet the contract without every team becoming logging experts.
- Make standards incremental and measurable. Start with high-value services and a compatibility layer for legacy text logs, then report adoption, schema violations, sensitive-data findings, delivery latency, cost, and operator outcomes. Mandates without paved roads drive teams to unmanaged side channels.
- Establish governance that balances platform consistency with local needs: a schema review process, documented exceptions with expiry, tenant and access boundaries, and a funded ownership model. Re-evaluate defaults as volume and regulations change; logging is a product, not a one-time agent rollout.

## References

- [OpenTelemetry logging specification](https://opentelemetry.io/docs/specs/otel/logs/)
- Further reading (blog): [Honeycomb: observability-driven development](https://www.honeycomb.io/blog/observability-driven-development)

## What to learn next

- Official documentation: [OpenTelemetry logs](https://opentelemetry.io/docs/specs/otel/logs/)
- Manual or specification: [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Honeycomb observability-driven development](https://www.honeycomb.io/blog/observability-driven-development)
- Hands-on guide: [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
