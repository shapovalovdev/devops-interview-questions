---
title: Choose a user-journey SLI
theme: sre
difficulty: junior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a user-journey SLI

Choose a user-journey SLI is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Choose a measurement of a user-visible successful journey, such as valid checkout requests completed within a latency threshold, rather than a convenient host metric.
- Specify eligible events, good events, data source, aggregation, window, and exclusions. Compare server-side telemetry with synthetic or client evidence when it exposes different failures.
- Avoid measuring only averages or excluding hard requests. Validate the indicator during incidents and revise it when the customer journey or architecture changes.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
