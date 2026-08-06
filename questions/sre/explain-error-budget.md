---
title: Explain an error budget
theme: sre
difficulty: junior
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/embracing-risk/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain an error budget

Explain an error budget is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- An error budget is the allowed unreliability implied by an SLO during a fixed window; it converts the reliability target into a shared, quantitative risk boundary.
- Track budget consumption from the agreed SLI and use pre-agreed policy to decide whether delivery continues, is slowed, or shifts to reliability work.
- A budget is not a reason to ignore users or freeze all work indefinitely. Protect urgent security fixes and investigate whether bad telemetry or a dependency makes the signal misleading.

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
