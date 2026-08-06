---
title: Establish an effective on-call handoff
theme: sre
difficulty: middle
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/being-on-call/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish an effective on-call handoff

Establish an effective on-call handoff is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Handoff should transfer current customer impact, active mitigations, unresolved risks, pending changes, and ownership—not merely the pager rotation.
- Use a durable incident or handoff record with timestamps, links to dashboards and tickets, and an explicit acknowledgement from the incoming responder.
- Do not hide fatigue or assume context is obvious. Escalate when coverage, access, or expertise is insufficient; ambiguous ownership is a common incident amplifier.

## References

- [Google SRE: Being On-Call](https://sre.google/sre-book/being-on-call/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
