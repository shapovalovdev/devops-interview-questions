---
title: How should a staff engineer lead a cross-layer performance incident?
theme: systems-performance
difficulty: staff
type: scenario
tags: [performance, incident-response, reliability, debugging]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How should a staff engineer lead a cross-layer performance incident?

## Answer guide

- Establish incident command, impact, a single timeline, and a reversible mitigation objective. Delegate investigation by boundary—client, service, queue, compute, storage, and network—while preserving a shared hypothesis log.
- Prioritize user protection through load shedding, rollback, isolation, or capacity changes with explicit guardrails. Compare telemetry to the last known good state and avoid simultaneous broad changes that destroy causal evidence.
- After recovery, turn findings into owned prevention work: observability gaps, capacity limits, tests, runbooks, and architecture decisions. A blameless review must still identify systemic incentives and unresolved uncertainty.

## References

- [Google SRE Book: Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/)
- Further reading (blog): [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [Google incident management](https://sre.google/sre-book/managing-incidents/)
- Manual or specification: [OpenTelemetry tracing specification](https://opentelemetry.io/docs/specs/otel/trace/)
- Maintainer or personal blog: [Brendan Gregg — methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Etsy Code as Craft](https://www.etsy.com/codeascraft)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/)
