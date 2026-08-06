---
title: Assign incident-management roles
theme: sre
difficulty: middle
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Assign incident-management roles

Assign incident-management roles is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Separate incident command, technical investigation, operations or mitigation, communications, and documentation so urgent work has clear authority and context is preserved.
- Scale roles with severity and assign named people with backups; the incident commander coordinates decisions while subject-matter experts investigate and execute safely.
- Avoid a committee making every decision or one exhausted engineer doing every role. Reassign roles as scope changes and preserve an audit trail for the postmortem.

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
