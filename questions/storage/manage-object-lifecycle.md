---
title: Design an object-storage lifecycle policy
theme: storage
difficulty: middle
type: scenario
tags: [storage, cost-optimization, reliability, automation]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design an object-storage lifecycle policy

How do you reduce object-storage cost without unexpectedly deleting recoverable data?

## Answer guide

- Classify data by access pattern, retention obligation, restore-time objective, legal hold, and deletion authority. Map each class to transitions and expiry rules that are explicit about versioned objects and incomplete uploads.
- Test policies on a tagged non-production prefix, report projected transitions/deletions, and alert on lifecycle errors and unexpected deletion volume.
- Keep backups and immutable recovery copies outside a policy's accidental or compromised deletion scope; document retrieval delay and cost for archive classes.
- A lifecycle rule is automated deletion. Applying it broadly without version, retention, or restore analysis can turn cost optimization into irreversible data loss.

## References

- [Amazon S3 lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- Further reading (blog): [AWS Storage Blog: S3 lifecycle cost optimization](https://aws.amazon.com/blogs/storage/)
