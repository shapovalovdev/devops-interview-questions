---
title: Compare on-demand, committed, and spot pricing
theme: finops
difficulty: junior
type: theory
tags: [finops, commitment-discounts, spot-instances, cost-optimization]
sources:
  - url: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/docs/cuds
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html
    source_type: official-docs
    verified_on: 2026-08-11
---

# Compare on-demand, committed, and spot pricing

What are the three main compute purchasing models, and what does a workload have to be like for each to be a good fit?

## Answer guide

- On-demand is the reference rate: no commitment, no interruption, highest unit price. It is the right choice for genuinely unpredictable or short-lived usage and for the top slice of a fleet that you are not confident will persist.
- Committed discounts — AWS Savings Plans and Reserved Instances, Google Cloud committed use discounts, Azure reservations — trade a one- or three-year spend or capacity commitment for a lower rate. The mechanism is a billing-time discount applied to matching usage each hour; if you run less than you committed, you still pay, and if you run more the excess bills at on-demand. They suit the durable baseline of a fleet.
- Spot, preemptible, and Azure Spot capacity sell spare capacity at a deep discount with the provider's right to reclaim it, typically with a short interruption notice. They suit interruptible, checkpointable, horizontally scalable work such as batch, CI, media encoding, and stateless queue consumers.
- Constraints and failure modes: commitments are scoped, so a plan bought for one region, family, or payment option may not cover where the workload actually moves; commitment coverage that outruns the real baseline turns a discount into waste; spot capacity is not guaranteed and can be reclaimed for an entire instance pool at once; and treating spot as free capacity for a stateful or latency-critical tier converts a saving into an availability incident.

## References

- [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- [Google Cloud committed use discounts](https://cloud.google.com/docs/cuds)
- [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- Further reading (blog): [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

## What to learn next

- Official documentation: [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- Manual or specification: [FinOps Framework — rate optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Compute blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [EC2 Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
