---
title: Choose block-volume performance for a workload
theme: storage
difficulty: middle
type: scenario
tags: [storage, capacity-planning, reliability, cost-optimization]
sources:
  - url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose block-volume performance for a workload

How would you size a block volume for a database that has both steady writes and periodic read-heavy jobs?

## Answer guide

- Measure working-set size, read/write mix, I/O sizes, percentile latency, IOPS, throughput, queueing, and the host's attached-storage limits during representative peaks.
- Select a volume class and provisioned capacity/performance that meet the service SLO with headroom, then load-test the complete host-volume-database path.
- Separate workloads or use replicas when batch scans compete with latency-sensitive writes; monitor cost and demand after release.
- Capacity alone does not guarantee IOPS or throughput, and a volume configuration may still be limited by the instance. Avoid sizing from an average metric or a synthetic benchmark alone.

## References

- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- Further reading (blog): [AWS Storage Blog: EBS latency monitoring](https://aws.amazon.com/blogs/storage/understanding-and-monitoring-latency-for-amazon-ebs-volumes-using-amazon-cloudwatch/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
