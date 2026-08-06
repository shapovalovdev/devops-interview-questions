---
title: Manage storage cost and capacity as a portfolio
theme: storage
difficulty: staff
type: scenario
tags: [storage, cost-optimization, capacity-planning, governance, reliability]
sources:
  - url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Manage storage cost and capacity as a portfolio

How would you control storage spend while protecting the performance and recovery needs of many teams?

## Answer guide

- Allocate usage and cost by owner, workload tier, region, data class, and lifecycle stage; track provisioned versus consumed capacity, IOPS/throughput demand, snapshots, replicas, and orphaned resources.
- Forecast growth and recovery capacity, then use tiered storage, retention policy, right-sizing, and decommission workflows only after checking service objectives and restoration requirements.
- Establish cost and capacity review cadences with product owners and publish unit economics that make trade-offs visible before provisioning.
- Cutting capacity from averages can violate peak latency or recovery needs. Cost optimization must not delete the sole backup, remove headroom, or rely on opaque shared charges.

## References

- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- Further reading (blog): [AWS Storage Blog: EBS price-performance](https://aws.amazon.com/blogs/storage/improve-your-application-resiliency-with-larger-and-faster-gp3-volumes/)
