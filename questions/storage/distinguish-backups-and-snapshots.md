---
title: Distinguish backups from storage snapshots
theme: storage
difficulty: junior
type: theory
tags: [storage, reliability, incident-response]
sources:
  - url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish backups from storage snapshots

When is a storage snapshot insufficient as the only backup control?

## Answer guide

- A snapshot captures a point-in-time representation of a volume or service; the consistency and isolation properties depend on the product and workload.
- A backup strategy also defines independent retention, access control, off-site or cross-account protection, recovery objectives, and a tested restoration procedure.
- Quiesce or use application-native backup coordination when crash consistency is not enough, then record the restore steps and validate a restore against a representative environment.
- Snapshots in the same account, region, or failure domain can be deleted, encrypted, or made unavailable by the same incident. A successful snapshot job is not evidence that recovery works.

## References

- [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)
- Further reading (blog): [Google Cloud Blog: Backup and DR](https://cloud.google.com/blog/products/storage-data-transfer/introducing-google-cloud-backup-and-dr)
