---
title: Monitor a distributed service
theme: sre
difficulty: middle
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Monitor a distributed service

Monitor a distributed service is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Monitor user-facing symptoms first, then the service’s critical dependencies and resource saturation. Use a small set of actionable signals tied to known decisions and objectives.
- Correlate metrics, structured logs, traces, deploy markers, and topology while preserving cardinality and cost limits. Make dashboards show scope, change, and error context.
- Do not collect every possible metric or alert on raw component noise. Missing telemetry, inconsistent labels, and expensive high-cardinality data can hide the incident instead of explaining it.

## References

- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
