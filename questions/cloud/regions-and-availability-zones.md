---
title: Choose Regions and Availability Zones for a workload
theme: cloud
difficulty: junior
type: theory
tags: [aws, cloud, availability, reliability]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/aws-infrastructure-security/availability-zones.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose Regions and Availability Zones for a workload

What is the distinction between an AWS Region and an Availability Zone, and how should it affect workload placement?

## Answer guide

- A Region is a separate geographic area; an Availability Zone (AZ) is an isolated location within a Region. AZs are connected with low-latency networking but are designed to reduce correlated facility failures.
- Start with multiple AZs for a production regional workload when the service supports it. Place redundant compute and data replicas across AZs, and test that a single-AZ loss does not exceed the service objective.
- Use a second Region only for requirements such as geographic disaster recovery, data-residency needs, or resilience beyond a regional event. It adds replication, consistency, routing, and operating complexity.
- Do not call a workload highly available merely because it has two instances: both can share one AZ, one dependency, or one erroneous deployment path.

## References

- [AWS Infrastructure Security: Availability Zones](https://docs.aws.amazon.com/whitepapers/latest/aws-infrastructure-security/availability-zones.html)
- [Further reading: AWS Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
