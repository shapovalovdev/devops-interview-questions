---
title: Prevent cloud service quotas from becoming an outage
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, capacity-planning, reliability, monitoring]
sources:
  - url: https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent cloud service quotas from becoming an outage

How should a team manage AWS service quotas when planning a large launch or recovery?

## Answer guide

- Inventory quotas that constrain steady state, scaling, and disaster recovery across the accounts and Regions actually used. Service quotas are not universally identical and some can be adjusted while others cannot.
- Monitor usage against relevant quotas, forecast peak and recovery capacity, and request increases well before a launch. Validate the approved value in the target account and Region.
- Include quota consumption in load tests and DR exercises; a regional recovery may need substantially more capacity than normal operation and might contend with other workloads.
- Do not assume an autoscaling policy guarantees capacity. It can request more resources only until a quota, account limit, instance availability, or downstream dependency is reached.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [Further reading: AWS Service Quotas console](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html#intro-how-it-works)
