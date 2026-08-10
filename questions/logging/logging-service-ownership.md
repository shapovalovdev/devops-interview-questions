---
title: Define ownership boundaries for a logging service
theme: logging
difficulty: staff
type: scenario
tags: [logging, platform-engineering, reliability, leadership]
sources:
  - url: https://sre.google/sre-book/production-environment/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define ownership boundaries for a logging service

What should the platform team own, and what should application teams own, in a centralized logging service?

## Answer guide

- The platform should own the secure, available collection and query service, documented contracts, shared libraries, defaults, capacity, and incident response for the platform. Application teams own event semantics, data classification, source instrumentation, dashboard meaning, and response to their service signals.
- Make the boundary executable through service-level objectives, support channels, versioned interfaces, quota policies, and on-call escalation. If a collector cannot parse a team-specific format, the platform needs a supportable extension process rather than silently taking ownership of every business schema.
- Review the model with incident data. Ambiguity appears as tickets that bounce between teams, unowned cost, or alerts without runbooks. Fund enablement and lifecycle work; a central backend without accountable producer owners will accumulate low-quality, risky data.

## References

- [Google SRE Book: production environment](https://sre.google/sre-book/production-environment/)
- Further reading (blog): [Google SRE: toil](https://sre.google/workbook/eliminating-toil/)

## What to learn next

- Official documentation: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [OpenTelemetry logs specification](https://opentelemetry.io/docs/specs/otel/logs/)
- Maintainer or personal blog: [Liz Fong-Jones' writing](https://www.lizthegrey.com/)
- Technical blog: [Google SRE toil guidance](https://sre.google/workbook/eliminating-toil/)
- Hands-on guide: [OpenTelemetry Collector troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/)
