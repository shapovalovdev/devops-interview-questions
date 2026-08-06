---
title: Reduce alert fatigue without hiding risk
theme: observability
difficulty: senior
type: scenario
tags: [observability, monitoring, incident-response, reliability]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reduce alert fatigue without hiding risk

An on-call team receives many pages that do not require action. What would you change?

## Answer guide

- Inventory pages by service, condition, responder action, user impact, and outcome. Remove or downgrade alerts that have no timely action, and consolidate duplicates around the affected SLO.
- Tune with evidence: use sustained windows, grouping, inhibition, deduplication, and severity routing while retaining a visible non-page signal for investigation.
- Require an owner and runbook for every page, review alert quality after incidents, and measure page volume, precision, acknowledgement delay, and missed user impact.
- Suppressing a noisy alert without preserving detection can create a blind spot. Avoid blanket maintenance silences and do not use a human acknowledgement as proof that a service recovered.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Further reading: Google SRE Workbook—Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
