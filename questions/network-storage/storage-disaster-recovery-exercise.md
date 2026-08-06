---
title: Run a storage disaster-recovery exercise
theme: network-storage
difficulty: staff
type: scenario
tags: [storage, reliability, security, monitoring, governance]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/34/r1/final
    source_type: official-docs
    verified_on: 2026-08-06
---

# Run a storage disaster-recovery exercise

What evidence should a storage disaster-recovery exercise produce?

## Answer guide

- Define the scenario, systems, data classification, success criteria, RPO, RTO, authority, communications, and safety controls before the exercise. Restore into an isolated environment and validate integrity, access controls, application consistency, dependencies, and observable service behavior.
- Capture measured restore time, recovered point in time, gaps, manual steps, credentials or keys used, capacity consumed, and decisions made. Convert findings into owned remediation work and repeat the exercise after material architecture or procedure changes.
- A job log that says backup completed is weak evidence. An untested restore may fail because data is incomplete, keys are unavailable, versions are incompatible, capacity is missing, or a runbook assumes access that incident responders do not have.

## References

- [NIST SP 800-34: contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/final)
- Further reading (blog): [Google Cloud Blog: disaster recovery](https://cloud.google.com/blog/products/management-tools)

## What to learn next

- Official documentation: [CISA resilience resources](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience)
- Manual or specification: [NIST SP 800-34](https://csrc.nist.gov/pubs/sp/800/34/r1/final)
- Maintainer or personal blog: [Charity Majors blog](https://charity.wtf/)
- Technical blog: [Google Cloud management tools blog](https://cloud.google.com/blog/products/management-tools)
- Hands-on guide: [AWS disaster recovery guidance](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
