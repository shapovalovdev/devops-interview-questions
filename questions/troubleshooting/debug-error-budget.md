---
title: Triage an error-budget burn alert
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, reliability, monitoring, incident-response]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage an error-budget burn alert

## Answer guide

- Validate the SLI numerator, denominator, window, exclusions, and current traffic mix before treating a burn calculation as customer impact. A bad instrumentation rollout can burn an apparent budget without a service regression.
- Determine the burn rate and remaining budget, then compare errors and latency by user journey, cohort, and dependency. Use that evidence to decide whether to pause risky releases, mitigate capacity, or open an incident.
- Preserve the SLO definition and alert query in the incident record. Do not relax the objective during an outage to make a dashboard green; change an SLO only through the normal product and reliability review process.

## References

- [Google SRE Book — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE Book — Practical Alerting](https://sre.google/sre-book/practical-alerting/)
- Further reading (blog): [Alex Hidalgo — SLOs](https://www.alexhidalgo.com/)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Hands-on guide: [Prometheus alerting](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
- Maintainer or personal blog: [Alex Hidalgo](https://www.alexhidalgo.com/)
- Technical blog: [Google SRE error-budget policy](https://sre.google/workbook/error-budget-policy/)
