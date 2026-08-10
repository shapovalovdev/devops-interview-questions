---
title: Design cross-region storage recovery
theme: storage
difficulty: senior
type: scenario
tags: [storage, cloud, reliability, incident-response, availability]
sources:
  - url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design cross-region storage recovery

How would you make a stateful service recoverable after a regional outage?

## Answer guide

- Set RTO/RPO per data class, then choose replication or scheduled copies that meet them across a separately operated region/account and include encryption keys, identities, network configuration, and application dependencies.
- Automate and monitor copy lag, integrity, retention, and restore permissions; regularly rehearse regional failover with representative data and traffic routing.
- Document data-consistency boundaries and the decision authority for failover, because asynchronous copies can lose recent acknowledged writes.
- A copied snapshot without bootstrapping, keys, DNS, capacity, or tested runbooks is not regional recovery. Cross-region replication also does not prevent a logical corruption from being replicated.

## References

- [Copy Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html)
- Further reading (blog): [Google Cloud Blog: cross-region backup](https://cloud.google.com/blog/products/storage-data-transfer/backup-and-dr-service-adds-cross-region-backups)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
