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

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [Further reading: Google SRE Book—service level objectives](https://sre.google/sre-book/service-level-objectives/)

## What to learn next

- Official documentation: [DORA — streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/)
- Manual or specification: [Google SRE Book — reliable product launches](https://sre.google/sre-book/reliable-product-launches/)
- Maintainer or personal blog: [Pete Hodgson — feature toggles](https://martinfowler.com/articles/feature-toggles.html)
- Technical blog: [Google Cloud — DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [DORA — measure the four key delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/)
