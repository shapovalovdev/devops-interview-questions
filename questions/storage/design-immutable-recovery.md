---
title: Design immutable recovery copies against ransomware
theme: storage
difficulty: senior
type: scenario
tags: [storage, security, reliability, incident-response]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design immutable recovery copies against ransomware

How do you protect backup data when a compromised administrator may try to delete it?

## Answer guide

- Create recovery copies in an independently controlled account or boundary, limit delete and retention-change permissions, and use retention/immutability features where regulatory and recovery requirements allow.
- Separate backup writers from backup-deletion and key-administration roles, log privileged actions, and regularly restore a protected copy with the required keys and identities.
- Set retention from RPO, threat dwell time, legal obligations, and cost; include a break-glass process with multi-party authorization and audit.
- Immutability that is misconfigured or whose keys are inaccessible can obstruct legitimate recovery. Same-account backups with broad administrator access remain vulnerable to a compromised control plane.

## References

- [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- Further reading (blog): [AWS Storage Blog: ransomware-resilient storage](https://aws.amazon.com/blogs/storage/)
