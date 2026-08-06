---
title: Plan service capacity
theme: sre
difficulty: middle
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/software-engineering-in-sre/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan service capacity

Plan service capacity is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Forecast demand from business plans and measured growth, then model the limiting resource, redundancy margin, and lead time required to add safe capacity.
- Load-test representative workloads, monitor saturation and queueing, and reserve headroom for failures, deployments, and traffic skew rather than planning only for average load.
- Do not extrapolate from one quiet period or assume cloud quotas are infinite. Revisit forecasts after product launches and test the scale-up and scale-down controls.

## References

- [Google SRE: Software Engineering in SRE—capacity-planning case study](https://sre.google/sre-book/software-engineering-in-sre/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
