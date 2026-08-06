---
title: Govern data retention and deletion across storage systems
theme: storage
difficulty: staff
type: scenario
tags: [storage, governance, security, reliability, cost-optimization]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern data retention and deletion across storage systems

How would you establish retention controls that meet legal, recovery, privacy, and cost needs?

## Answer guide

- Define data classes, accountable owners, minimum/maximum retention, legal-hold triggers, deletion authority, recovery-copy requirements, and evidence requirements with legal, security, and product stakeholders.
- Encode policy in approved storage configurations and lifecycle controls, maintain an inventory of datasets and copies, and review exceptions with an expiry and audit trail.
- Reconcile policy with backup and disaster-recovery windows so required deletion does not silently survive in uncontrolled copies and needed recovery data is not purged too early.
- One global retention rule rarely fits every dataset. Unowned copies, untested lifecycle rules, and indefinite exceptions create both compliance exposure and runaway cost.

## References

- [Amazon S3 lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- Further reading (blog): [Google Cloud Blog: backup retention and DR](https://cloud.google.com/blog/products/storage-data-transfer/introducing-google-cloud-backup-and-dr)
