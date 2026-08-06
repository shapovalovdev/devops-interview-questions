---
title: Create an application-consistent volume snapshot
theme: storage
difficulty: middle
type: scenario
tags: [storage, databases, reliability, automation]
sources:
  - url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html
    source_type: official-api
    verified_on: 2026-08-06
---

# Create an application-consistent volume snapshot

What would you do before snapshotting a volume that contains a transactional database?

## Answer guide

- Establish the database's recovery requirements first. A storage snapshot captures blocks written at snapshot time, but cached writes and multi-volume ordering can make it only crash-consistent.
- Use the database's documented backup, checkpoint, freeze, or replication procedure as applicable; coordinate all participating volumes and record the snapshot set and database recovery metadata.
- Monitor completion, retention, encryption, and cross-boundary copies, then restore into an isolated environment and run database integrity and application checks.
- Do not claim consistency merely because the cloud API accepted a snapshot. Incomplete WAL/log capture, unfrozen writes, or separately captured volumes can make restore impossible or require lengthy recovery.

## References

- [EC2 CreateSnapshot API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html)
- Further reading (blog): [AWS Storage Blog: restoring EBS snapshots without latency surprises](https://aws.amazon.com/blogs/storage/addressing-i-o-latency-when-restoring-amazon-ebs-volumes-from-ebs-snapshots/)
