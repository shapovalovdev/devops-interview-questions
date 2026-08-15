---
title: Choose Regions and Availability Zones for a workload
theme: cloud
difficulty: junior
type: theory
tags: [aws, cloud, availability, reliability]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/reliability/availability-zones-overview
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/compute/docs/regions-zones
    source_type: official-docs
    verified_on: 2026-08-16
---

# Choose Regions and Availability Zones for a workload

What is the distinction between an AWS Region and an Availability Zone, and how should it affect workload placement?

## Answer guide

- A Region is a separate geographic area; an Availability Zone (AZ) is an isolated location within a Region. AZs are connected with low-latency networking but are designed to reduce correlated facility failures.
- Start with multiple AZs for a production regional workload when the service supports it. Place redundant compute and data replicas across AZs, and test that a single-AZ loss does not exceed the service objective.
- Use a second Region only for requirements such as geographic disaster recovery, data-residency needs, or resilience beyond a regional event. It adds replication, consistency, routing, and operating complexity.
- Do not call a workload highly available merely because it has two instances: both can share one AZ, one dependency, or one erroneous deployment path.
- The placement reasoning is portable: an Azure region contains availability zones just as an AWS Region does (with availability sets as the older, separate-update-domain mechanism), and Google Cloud calls the equivalent fault domains inside a region zones. A second region for DR carries the same replication and consistency cost on every provider.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Fault Isolation Boundaries: Availability Zones](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html)
- [Further reading: AWS Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- [Azure — Availability Zones overview](https://learn.microsoft.com/azure/reliability/availability-zones-overview)
- [Google Cloud — Regions and zones](https://cloud.google.com/compute/docs/regions-zones)

## What to learn next

- Official documentation: [AWS Availability Zone guidance](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html)
- Manual or specification: [AWS Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Cloud Quest](https://aws.amazon.com/training/digital/aws-cloud-quest/)
