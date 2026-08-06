---
title: Set storage SLOs for a platform
theme: storage
difficulty: staff
type: scenario
tags: [storage, reliability, observability, governance, capacity-planning]
sources:
  - url: https://sre.google/workbook/implementing-slos/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set storage SLOs for a platform

How would you define storage SLOs that are useful to application teams and operators?

## Answer guide

- Start with user-facing data outcomes: durable acknowledged writes, read/write availability, latency percentiles, recovery-point and recovery-time attainment, and successful restore evidence for each service tier.
- Define service boundaries and dependencies explicitly; a volume control plane, filesystem, replication path, and backup service can have different indicators and owners.
- Establish error budgets, measurement quality, escalation policy, and capacity forecasts. Publish objectives by tier so teams can choose cost and resilience deliberately.
- A single storage-availability percentage can conceal corrupt data, unusable restore points, or unacceptable tail latency. Avoid targets without a measurement path or a decision they inform.

## References

- [Google SRE Workbook: implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Further reading (blog): [AWS Storage Blog: EBS performance insights](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
