---
title: Choose object storage for durable application data
theme: cloud
difficulty: junior
type: scenario
tags: [aws, cloud, storage, reliability]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose object storage for durable application data

When should a team use Amazon S3 rather than a local filesystem, and what controls should it add?

## Answer guide

- S3 stores objects in buckets and is appropriate for data accessed by key through an API, such as artifacts, backups, and static assets. Instance-local disks are tied to the instance lifecycle unless separately designed for persistence.
- Define object naming, ownership, encryption, access policy, lifecycle, and recovery requirements before adoption. Use an application identity with only the required bucket and prefix permissions.
- Enable versioning or another recovery control where accidental overwrite or deletion matters, then test recovery; lifecycle rules can permanently remove data and must match retention requirements.
- Do not treat object storage as a POSIX filesystem. Rename, locking, latency, consistency expectations, and partial-write behavior differ from a local filesystem and application code must use the object API correctly.

## References

- [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Further reading: Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
