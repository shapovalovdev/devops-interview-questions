---
title: Coordinate a major incident across teams
theme: sre
difficulty: senior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/emergency-response/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Coordinate a major incident across teams

Coordinate a major incident across teams is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Establish command, scope, priorities, and an out-of-band communication channel early; focus first on reducing customer harm and preserving safe operational control.
- Coordinate dependency owners and executives through regular factual updates, record decisions, and maintain alternatives when normal dashboards, chat, or deployment systems are unavailable.
- Do not let urgency bypass change discipline or overload one expert with communications. Verify recovery independently and plan the transition from emergency response to follow-up work.

## References

- [Google SRE: Emergency Response](https://sre.google/sre-book/emergency-response/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
