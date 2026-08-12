---
title: Establish service ownership and reliability accountability
theme: sre
difficulty: staff
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting, cnpa, cba]
sources:
  - url: https://sre.google/sre-book/service-best-practices/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish service ownership and reliability accountability

Establish service ownership and reliability accountability is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Give each service a durable owner responsible for user objectives, dependencies, on-call readiness, lifecycle decisions, and documented operational interfaces.
- Publish a service catalog with escalation paths, SLOs, runbooks, data classification, and dependency contracts. Review ownership after reorganizations, acquisitions, and platform migrations.
- Do not confuse a team name with accountability. Shared components and abandoned services need explicit maintenance, deprecation, or transfer plans before an incident exposes the gap.

## References

- [Google SRE: Production Services Best Practices](https://sre.google/sre-book/service-best-practices/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
