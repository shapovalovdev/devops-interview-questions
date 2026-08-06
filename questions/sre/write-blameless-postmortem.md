---
title: Write a blameless postmortem
theme: sre
difficulty: middle
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/postmortem-culture/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Write a blameless postmortem

Write a blameless postmortem is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Describe the timeline, customer impact, contributing technical and organizational conditions, detection gaps, and recovery actions without reducing the event to individual fault.
- Use evidence such as logs, change records, and decisions known at the time; create owned, prioritized follow-ups that reduce recurrence or time to recover.
- Blameless does not mean consequence-free or vague. Do not use hindsight language, skip uncomfortable system factors, or close actions without verifying their effect.

## References

- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
