---
title: Measure and reduce toil
theme: sre
difficulty: middle
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/workbook/eliminating-toil/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Measure and reduce toil

Measure and reduce toil is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Identify repetitive, manual, predictable operational tasks with little enduring engineering value; measure their frequency, duration, interruption cost, and risk.
- Prioritize automation or product fixes by user impact and expected reclaimed time. Build guardrails, observability, and a fallback path around automation before retiring the manual process.
- Do not automate a broken or poorly understood workflow blindly. Keep necessary operational work visible, and treat automation failures as production systems with owners.

## References

- [Google SRE Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
