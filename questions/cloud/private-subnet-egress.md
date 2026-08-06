---
title: Provide controlled Internet egress from a private subnet
theme: cloud
difficulty: middle
type: scenario
tags: [aws, cloud, networking, security, reliability]
sources:
  - url: https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Provide controlled Internet egress from a private subnet

How would instances without public IP addresses download approved updates from the Internet?

## Answer guide

- Keep the workloads in a private subnet and route their Internet-bound IPv4 traffic to a NAT gateway placed in a public subnet with a route to an Internet gateway. The NAT gateway translates outbound traffic; it does not make the private instances directly reachable from the Internet.
- Restrict destination and port access using security controls, private endpoints where a managed service supports them, and egress logging. Prefer endpoints for AWS services when they eliminate unnecessary Internet paths.
- Make the design AZ-aware: a NAT gateway is scoped to one AZ, and cross-AZ dependency can add cost and reduce resilience. Choose the number of gateways based on availability and cost requirements.
- A route alone is insufficient: missing gateway routes, restrictive NACLs, DNS failures, or lack of public NAT addressing can still block egress.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS VPC: NAT gateway scenarios](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html)
- [Further reading: VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)

## What to learn next

- Official documentation: [AWS NAT gateway scenarios](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html)
- Manual or specification: [AWS PrivateLink VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- Hands-on guide: [Amazon VPC workshops](https://catalog.workshops.aws/vpc/en-US)
