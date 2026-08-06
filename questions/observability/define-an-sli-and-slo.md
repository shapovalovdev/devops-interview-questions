---
title: Define an SLI and SLO for an API
theme: observability
difficulty: junior
type: theory
tags: [observability, monitoring, reliability]
sources:
  - url: https://sre.google/workbook/implementing-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define an SLI and SLO for an API

How would you define a service-level indicator (SLI) and service-level objective (SLO) for a customer-facing API?

## Answer guide

- An SLI is a quantitative measure of a user-relevant outcome, such as the fraction of valid API requests served successfully or within an agreed latency threshold.
- An SLO is the target for that SLI over a stated window, for example 99.9% successful eligible requests in 30 days. It is not the same as a contractual SLA.
- Define the event, eligibility rules, data source, aggregation, window, and owner before selecting a target. Measure at the user boundary where possible.
- Excluding errors merely because they are inconvenient creates a misleading SLI. Start with a measurable objective, review it with product and users, and revise it when user expectations or architecture changes.

## References

- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Further reading: Google SRE—Service level objectives](https://sre.google/sre-book/service-level-objectives/)
