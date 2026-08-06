---
title: Prevent cascading failures
theme: sre
difficulty: senior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/addressing-cascading-failures/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent cascading failures

Prevent cascading failures is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Contain failure at boundaries with timeouts, bounded retries, circuit breaking, bulkheads, backpressure, and graceful degradation designed around critical user journeys.
- Set and test compatible limits across callers and dependencies, isolate tenants or regions where appropriate, and observe queue depth, retry rates, and saturation during experiments.
- Do not add retries without budgets or assume every dependency can recover at once. Recovery surges and hidden shared dependencies frequently re-trigger a cascade.

## References

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
