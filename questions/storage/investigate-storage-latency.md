---
title: Investigate a storage latency incident
theme: storage
difficulty: middle
type: troubleshooting
tags: [storage, monitoring, troubleshooting, reliability]
sources:
  - url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-performance.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a storage latency incident

An application slows down while CPU is idle. How do you determine whether storage is the bottleneck?

## Answer guide

- Correlate request latency with device latency, queue depth, IOPS, throughput, saturation, filesystem errors, and database wait events over the same interval.
- Compare measured demand with volume and host limits; inspect I/O size and access pattern because random I/O, sequential throughput, and latency-sensitive writes stress systems differently.
- Isolate a safe reproduction or canary before changing volume class, striping, cache, or application concurrency. Record a baseline and validate the result.
- High latency can originate in the application, networked storage, a throttled volume, host limits, or recovery/initialization. Increasing IOPS without locating the constraint wastes cost and can hide a correctness issue.

## References

- [Amazon EBS performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-performance.html)
- Further reading (blog): [AWS Storage Blog: EBS detailed performance statistics](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
