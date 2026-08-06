---
title: Test a disaster-recovery plan
theme: sre
difficulty: senior
type: scenario
tags: [reliability, monitoring, incident-response, troubleshooting]
sources:
  - url: https://docs.cloud.google.com/architecture/framework/reliability
    source_type: official-docs
    verified_on: 2026-08-06
---

# Test a disaster-recovery plan

Test a disaster-recovery plan is an SRE interview topic. Explain the mechanism, operational constraints, and failure modes.

## Answer guide

- Test recovery against explicit recovery time and recovery point objectives using realistic loss of a region, dependency, identity path, or data component.
- Exercise people, access, backups, replication, runbooks, and customer communications; measure actual restore time and data loss, then track gaps to closure.
- A backup is not proof of recovery. Avoid tabletop-only confidence, unverified permissions, and failover tests that never include the dependencies needed for a usable service.

## References

- [Google Cloud: Reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Google Cloud Blog: SRE fundamentals](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors: Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog: DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud: SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
