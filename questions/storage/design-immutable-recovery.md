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
- Further reading (blog): [AWS Storage Blog: ransomware-resilient storage](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
