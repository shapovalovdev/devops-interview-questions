---
title: Run a production-readiness review
theme: sre
difficulty: middle
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/evolving-sre-engagement-model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Run a production-readiness review

Run a production-readiness review is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Review ownership, architecture, capacity, security, observability, SLOs, failure modes, operational procedures, and rollback before deciding whether a service is ready to operate.
- Require evidence from load, recovery, and deployment tests; record risks with owners and a date. Ensure on-call access and runbooks exist before transferring responsibility.
- Do not make the review a ceremonial checklist. A launch with unknown dependencies or no rollback should retain explicit risk acceptance and a constrained rollout plan.

## References

- [Google SRE: The SRE Engagement Model—production readiness review](https://sre.google/sre-book/evolving-sre-engagement-model/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
