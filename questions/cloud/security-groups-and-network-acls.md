---
title: Choose security groups and network ACLs deliberately
theme: cloud
difficulty: middle
type: theory
tags: [aws, cloud, networking, security]
sources:
  - url: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/virtual-network/network-security-groups-overview
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/firewall/docs/firewalls
    source_type: official-docs
    verified_on: 2026-08-16
---

# Choose security groups and network ACLs deliberately

How do AWS security groups and network ACLs differ, and where should each be used?

## Answer guide

- Security groups apply to associated elastic network interfaces and are stateful: an allowed request's return traffic is allowed. Network ACLs apply at the subnet boundary and are stateless, so return traffic requires matching rules.
- Use security groups as the primary workload-level allowlist, preferably referencing another security group instead of broad CIDRs. Use network ACLs for coarse subnet controls or defense-in-depth requirements.
- Start with deny-by-default exposure and allow only known ports, protocols, sources, and destinations. Verify both ingress and egress because broad egress can enable data exfiltration.
- A common incident is allowing inbound traffic in an NACL but omitting ephemeral return ports, or changing a security group while the instance is associated with a different group than expected.
- The stateful-versus-stateless split recurs across providers: Azure network security groups (optionally scoped by application security groups) and Google Cloud firewall rules are stateful like security groups, while a stateless subnet ACL owes the same explicit return-traffic rule as any router ACL.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Further reading: Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [Azure — network security groups overview](https://learn.microsoft.com/azure/virtual-network/network-security-groups-overview)
- [Google Cloud — firewall rules](https://cloud.google.com/firewall/docs/firewalls)

## What to learn next

- Official documentation: [AWS VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- Manual or specification: [AWS VPC network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- Hands-on guide: [Amazon VPC workshops](https://catalog.workshops.aws/vpc/en-US)
