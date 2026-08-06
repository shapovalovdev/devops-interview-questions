---
title: Triage a production incident
theme: sre
difficulty: middle
type: troubleshooting
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a production incident

Triage a production incident is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- First establish user impact, scope, severity, and a stable incident lead; protect restoration work before attempting a complete root-cause explanation.
- Compare healthy and unhealthy regions, versions, dependencies, and recent changes. Apply the lowest-risk reversible mitigation, record observations, and communicate a regular update cadence.
- Avoid changing many variables at once or declaring recovery from a single metric. Continue monitoring after mitigation because retries, queues, and dependent systems can fail later.

## References

- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
