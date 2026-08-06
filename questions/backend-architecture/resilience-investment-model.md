---
title: Prioritize backend resilience investments
theme: backend-architecture
difficulty: staff
type: scenario
tags: [reliability, availability, capacity-planning]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prioritize backend resilience investments

How should leadership decide whether to invest in redundancy, a rewrite, or operational improvement?

## Answer guide

- Start with user journeys and SLOs, then quantify error budget consumption, incident history, dependency concentration, recovery time, cost, and delivery opportunity. Rank investments by the risk reduced per unit effort rather than by technology novelty.
- Assign owners, target measures, milestone decisions, and a test that demonstrates the expected protection, such as a dependency-loss game day or restore exercise. Keep a capacity and reliability roadmap visible to product planning.
- Adding replicas without validating failover may only multiply cost, while chasing perfect availability can starve feature work. Use evidence and revisit estimates after incidents; test whether monitoring detects the exact failure the investment claims to address.

## References

- [Google SRE: service level objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Google: error budgets](https://cloud.google.com/blog/products/devops-sre/embracing-error-budget-based-risk-management)

## What to learn next

- Official documentation: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Manual or specification: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Maintainer or personal blog: [Charity Majors' blog](https://charity.wtf/)
- Technical blog: [Google Cloud blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google SRE reliability workbook chapter](https://sre.google/workbook/alerting-on-slos/)
