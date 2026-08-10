---
title: Design a production troubleshooting experiment
theme: troubleshooting
difficulty: senior
type: scenario
tags: [troubleshooting, runbooks, debugging, change-management, reliability]
sources:
  - url: https://sre.google/sre-book/effective-troubleshooting/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Design a production troubleshooting experiment
## Answer guide
- Write a falsifiable hypothesis, population, expected signal, measurement window, stop condition, and the smallest reversible intervention. Make clear which variable the experiment changes and what confounders remain.
- Obtain the appropriate change authority and use a canary, shadow path, or isolated cohort where available. Monitor customer impact and infrastructure saturation continuously, with a tested rollback that can be executed quickly.
- Record the result even when it disproves the hypothesis, then choose the next experiment from evidence. Avoid broad configuration sweeps; they create correlated failure and make an apparently successful result impossible to interpret.
## References
- [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Google SRE Book — Testing for Reliability](https://sre.google/sre-book/testing-reliability/)
- Further reading (blog): [John Allspaw — experiments and learning](https://www.kitchensoap.com/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Hands-on guide: [Kubernetes progressive delivery](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Maintainer or personal blog: [John Allspaw](https://www.kitchensoap.com/)
- Technical blog: [AWS Builders’ Library](https://aws.amazon.com/builders-library/)
