---
title: Govern an error-budget policy
theme: sre
difficulty: staff
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/embracing-risk/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern an error-budget policy

Govern an error-budget policy is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Publish a consistent policy that connects SLO measurement to delivery behavior, exception authority, security treatment, and escalation for sustained budget exhaustion.
- Review policies with product, security, and engineering leaders; make trade-offs and overrides visible, then examine whether repeated exhaustion signals flawed objectives or underinvestment.
- Do not use budgets as a punitive scorecard or apply one target to unlike services. Gaming the SLI or overriding every stop condition removes the control loop.

## References

- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
