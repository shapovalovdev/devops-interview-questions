---
title: Explain an SLO error-budget burn-rate alert
theme: observability
difficulty: senior
type: theory
tags: [observability, monitoring, reliability, incident-response, prometheus, pca]
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

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
- [Further reading: Google SRE Workbook—Monitoring](https://sre.google/workbook/monitoring/)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Workbook — Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
- Maintainer or personal blog: [Björn Rabenstein — alerting on SLOs at SoundCloud](https://developers.soundcloud.com/blog/alerting-on-slos)
- Technical blog: [Google Cloud — SRE fundamentals: SLIs, SLAs and SLOs](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)
- Hands-on guide: [Google Cloud — SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
