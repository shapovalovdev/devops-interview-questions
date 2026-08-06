---
title: Classify an alert as a page, ticket, or log
theme: sre
difficulty: junior
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/service-best-practices/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Classify an alert as a page, ticket, or log

Classify an alert as a page, ticket, or log is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Page only when a trained responder must act immediately to protect a user objective; create a ticket for work that can wait, and retain logs for diagnosis or analysis.
- Give every page an owner, runbook, severity, symptom, and clear action. Test the notification route and use deduplication and grouping to prevent alert storms.
- Do not page on every infrastructure metric or treat email as paging. Review noisy alerts after incidents because habituation delays response to genuinely urgent signals.

## References

- [Google SRE: Production Services Best Practices](https://sre.google/sre-book/service-best-practices/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
