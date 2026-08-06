---
title: Explain the network boundaries of an AWS VPC
theme: cloud
difficulty: junior
type: theory
tags: [aws, cloud, networking, security]
sources:
  - url: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the network boundaries of an AWS VPC

What does an Amazon VPC provide, and what must be configured before a workload is reachable?

## Answer guide

- A VPC is a logically isolated virtual network where you choose address ranges and create subnets, route tables, and network controls. A subnet is scoped to one Availability Zone.
- Reachability requires a valid route in the relevant route table and a permitted traffic path through security controls; public Internet reachability additionally needs the appropriate gateway, public address arrangement, and rules.
- Separate public entry points from application and data tiers with subnets and restrictive controls. Treat subnet names such as "public" as conventions, not enforcement: the route and addressing configuration determine exposure.
- Troubleshooting only the security group misses common causes such as a missing return route, wrong route-table association, DNS setting, or network ACL.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [Amazon VPC User Guide: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Further reading: VPC route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

## What to learn next

- Official documentation: [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- Manual or specification: [Amazon VPC route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- Hands-on guide: [Amazon VPC workshops](https://catalog.workshops.aws/vpc/en-US)
