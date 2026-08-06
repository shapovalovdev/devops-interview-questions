---
title: Govern an organization-wide SLO program
theme: observability
difficulty: staff
type: scenario
tags: [observability, monitoring, governance, reliability]
sources:
  - url: https://sre.google/workbook/implementing-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern an organization-wide SLO program

How would you make SLOs influence delivery decisions across many services?

## Answer guide

- Define an SLO policy with service owners, user journeys, error-budget calculation, review cadence, exception process, and the decision consequences of budget burn.
- Start with critical services and a small number of trustworthy user-facing indicators; provide templates and coaching instead of a centrally invented target for every team.
- Connect error-budget state to release risk, incident follow-up, capacity work, and leadership reporting, while preserving team ownership of their service objectives.
- A dashboard-only SLO program changes no behavior. Conversely, automatic release freezes without validating the SLI can punish teams for telemetry defects and create incentives to game measurements.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Further reading: Google SRE Workbook—Error budget policy example](https://sre.google/workbook/error-budget-policy/)
