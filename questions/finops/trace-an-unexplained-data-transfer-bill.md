---
title: Trace an unexplained data transfer bill
theme: finops
difficulty: middle
type: troubleshooting
tags: [finops, data-transfer, networking, cost-optimization]
sources:
  - url: https://cloud.google.com/vpc/network-pricing
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
    source_type: official-docs
    verified_on: 2026-08-11
---

# Trace an unexplained data transfer bill

Data transfer is now the second-largest line on the bill and nobody knows why. How do you find the source?

## Answer guide

- Decompose the charge by usage type before touching any architecture. Billing exports separate internet egress, inter-region transfer, cross-availability-zone traffic, NAT gateway data processing, load balancer processed bytes, and per-endpoint charges. These have very different unit rates and very different causes, and lumping them together sends you down the wrong path.
- The common culprits are structural. Cross-zone chatter between a service and a database or cache placed in a different zone; traffic to a public service endpoint routed out through a NAT gateway instead of a private endpoint or gateway endpoint, which charges both per gigabyte processed and per gigabyte transferred; replication or backup crossing regions; and a chatty client pulling far more from an internal API than anyone modelled.
- Use flow-level evidence, not intuition: VPC flow logs or their equivalent, aggregated by source and destination prefix and by zone, will identify the top talkers in an afternoon. Match the top pairs against the billing usage types to confirm the mechanism before proposing a fix.
- Structural fixes in rough order of value: keep request paths zone-local and make the client aware of topology; replace NAT egress to provider services with gateway or private endpoints; move cross-region replication to a compressed or batched channel or reconsider whether it is needed; put a CDN in front of anything served repeatedly to the internet; and compress or make responses less chatty at the protocol level.
- Constraints and failure modes: rates differ sharply by direction, region pair, and destination, so a fix that works in one region may not in another; zone-local routing can conflict with an availability requirement to spread load; and a CDN moves cost rather than removing it if the content is not cacheable. Always confirm the saving in the next billing export instead of declaring victory from the design change.

## References

- [Google Cloud VPC network pricing](https://cloud.google.com/vpc/network-pricing)
- [AWS NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- Further reading (blog): [Cloudflare — the egregious egress analysis](https://blog.cloudflare.com/aws-egregious-egress/)

## What to learn next

- Official documentation: [Google Cloud VPC network pricing](https://cloud.google.com/vpc/network-pricing)
- Manual or specification: [Google Cloud network service tiers](https://cloud.google.com/network-tiers/docs/overview)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [Cloudflare — the egregious egress analysis](https://blog.cloudflare.com/aws-egregious-egress/)
- Hands-on guide: [AWS NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
