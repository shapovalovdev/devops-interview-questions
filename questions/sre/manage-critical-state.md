---
title: Manage critical state for reliability
theme: sre
difficulty: senior
type: theory
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://sre.google/sre-book/managing-critical-state/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Manage critical state for reliability

Manage critical state for reliability is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Define consistency, availability, durability, and recovery requirements for the state before choosing replication, consensus, or storage mechanisms.
- Protect writes with clear ownership and quorum semantics, monitor replication lag and data integrity, and test backups and restoration under realistic concurrency and partial failure.
- Do not assume a highly available store makes every client correct. Split-brain, stale reads, unsafe failover, and schema changes can corrupt business outcomes.

## References

- [Google SRE: Managing Critical State](https://sre.google/sre-book/managing-critical-state/)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
