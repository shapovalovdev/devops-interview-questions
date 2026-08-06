---
title: Design a multi-window burn-rate alert
theme: sre
difficulty: middle
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/workbook/alerting-on-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a multi-window burn-rate alert

Design a multi-window burn-rate alert is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Use the SLI error rate relative to the permitted budget rate over a short and a long window, then page when both indicate rapid, sustained budget consumption.
- Choose thresholds from the SLO window and desired detection time; pair a fast page with a slower ticket signal. Include the affected journey, error ratio, and relevant deployment context.
- Tune with historical incidents and test missing-data behavior. Single-window thresholds are often either noisy during spikes or too slow for persistent failures.

## References

- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
