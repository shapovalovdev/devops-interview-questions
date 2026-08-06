---
title: Design a reliable product launch
theme: sre
difficulty: senior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/reliable-product-launches/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a reliable product launch

Design a reliable product launch is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Define launch success in user and reliability terms, validate capacity and dependencies, and release incrementally with measurable gates and a tested rollback.
- Use feature flags, canaries, change windows, ownership, communication plans, and heightened monitoring. Stop or reverse when pre-agreed SLO, safety, or capacity thresholds are crossed.
- Do not confuse deployment completion with successful launch. Large synchronized changes and untested rollback paths increase blast radius when assumptions are wrong.

## References

- [Google SRE: Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
