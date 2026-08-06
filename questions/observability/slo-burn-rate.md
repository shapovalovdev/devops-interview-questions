---
title: Explain an SLO error-budget burn-rate alert
theme: observability
difficulty: senior
type: theory
tags: [observability, monitoring, reliability, incident-response]
sources:
  - url: https://sre.google/workbook/alerting-on-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain an SLO error-budget burn-rate alert

What does a burn-rate alert measure, and why can it be better than alerting on a fixed error-percentage threshold?

## Answer guide

- Burn rate is the current bad-event rate divided by the error-budget rate allowed by an SLO. A burn rate of 1 consumes the entire budget exactly over the SLO window; higher values exhaust it sooner.
- It alerts on user-impacting budget risk instead of a fixed error percentage that may be harmless for one objective and catastrophic for another.
- Use a long window to establish sustained impact and a shorter window to detect a fast regression. Choose thresholds from the percentage of budget to spend and the response time the team can sustain.
- Do not page solely on a burn-rate number for low-traffic services or an invalid SLI. Validate the event denominator, exclude agreed non-user-impacting traffic, and use a ticket or dashboard for slow budget consumption.

## References

- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
- [Further reading: Google SRE Workbook—Monitoring](https://sre.google/workbook/monitoring/)
