---
title: Define storage platform service tiers
theme: network-storage
difficulty: staff
type: scenario
tags: [storage, reliability, performance, capacity-planning, governance]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define storage platform service tiers

How would you define service tiers for a shared network-storage platform?

## Answer guide

- Publish a small set of tiers with explicit interfaces: supported protocol and access model, availability and durability target, latency and throughput objective, backup and retention behavior, recovery objective, security boundary, cost model, and escalation path.
- Map each tier to independently measured dependencies and a capacity policy. Give product teams a self-service request path, defaults that are safe for ordinary workloads, and a documented exception process for unusual performance or compliance requirements.
- Avoid promising one universal storage SLA. A shared platform’s availability, tail latency, and restore time vary by topology, workload interference, and chosen service; unclear ownership leads teams to bypass controls or treat a best-effort share as a database-grade service.

## References

- [Google SRE Book: service level objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Google Cloud Blog: SRE](https://cloud.google.com/blog/products/devops-sre)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors blog](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
