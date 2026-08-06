---
title: Distinguish snapshots from backups
theme: network-storage
difficulty: middle
type: theory
tags: [storage, reliability, security, performance]
sources:
  - url: https://docs.ceph.com/en/latest/rbd/rbd-snapshot/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish snapshots from backups

Why is a storage snapshot useful but not automatically a backup?

## Answer guide

- A snapshot records a point-in-time view within a storage system and can make fast local rollback or cloning possible. A backup is an independently managed recoverable copy with retention, integrity, authorization, and restore procedures designed for a stated recovery objective.
- Determine application consistency before snapshotting: quiesce or coordinate databases and transactional systems when required, label snapshots with owner and purpose, and test restore into an isolated environment. Replicate or export backups into a separate failure and administrative domain.
- A snapshot on the same cluster can be lost to the same hardware, operator, credential, ransomware, or policy failure as its source. Long chains or high churn can also affect performance and recovery; retain only tested restore points with clear ownership.

## References

- [Ceph RBD snapshots](https://docs.ceph.com/en/latest/rbd/rbd-snapshot/)
- Further reading (blog): [Ceph developer blog](https://ceph.io/en/news/blog/)

## What to learn next

- Official documentation: [Ceph RBD snapshots](https://docs.ceph.com/en/latest/rbd/rbd-snapshot/)
- Manual or specification: [NIST SP 800-34 contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/final)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog/channel/storage)
- Hands-on guide: [Ceph RBD operations](https://docs.ceph.com/en/latest/rbd/rbd/) 
