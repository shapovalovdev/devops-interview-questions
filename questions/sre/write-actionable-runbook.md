---
title: Write an actionable runbook
theme: sre
difficulty: junior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/workbook/alerting-on-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Write an actionable runbook

Write an actionable runbook is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- An actionable runbook states what the alert means, how to confirm impact, safe mitigations, escalation contacts, and explicit rollback or stop conditions.
- Link commands or dashboards to expected evidence, name required permissions, and keep actions idempotent where possible. Exercise the runbook during drills and update it after real use.
- Avoid vague instructions such as investigate logs. A stale runbook, missing access, or destructive command can turn a small alert into a longer outage.

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
