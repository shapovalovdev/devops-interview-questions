---
title: Govern release risk across a product portfolio
theme: ci-cd
difficulty: staff
type: scenario
tags: [ci-cd, governance, deployment, reliability, monitoring]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern release risk across a product portfolio

How would you make release controls proportionate to risk across many services?

## Answer guide

- Classify services and changes by customer impact, reversibility, data sensitivity, and dependency criticality; assign corresponding evidence, rollout, and approval requirements.
- Standardize telemetry and error-budget signals so teams can automate promotion and halt decisions, while retaining a documented emergency path.
- Review outcomes such as escaped defects, rollback time, and exception rates to tune controls. A single universal gate either under-protects critical systems or burdens low-risk changes without improving reliability.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [Further reading: Google SRE Book—service level objectives](https://sre.google/sre-book/service-level-objectives/)
