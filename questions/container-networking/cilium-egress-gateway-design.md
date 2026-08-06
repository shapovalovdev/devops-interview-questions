---
title: Design controlled egress with Cilium Egress Gateway
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, security, reliability, cca, ckne]
sources:
  - url: https://docs.cilium.io/en/stable/network/egress-gateway/egress-gateway/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design controlled egress with Cilium Egress Gateway

How would you give selected workloads a stable source address for external allowlists using Cilium Egress Gateway?

## Answer guide

- Select source workloads and destination CIDRs or services deliberately, then assign an egress gateway node and source address that external systems can allowlist.
- Confirm the supported Cilium mode and routing prerequisites, including node reachability and return-path behavior, before applying policy to production workloads.
- Test matching and non-matching workload traffic, failover behavior, DNS-dependent destinations, and external logs that confirm the expected source address.
- Egress Gateway is a traffic-steering control, not a substitute for destination authorization or application encryption. A bad selector, unavailable gateway node, asymmetric routing, or overlooked dependency can disrupt egress, so use staged policies and monitor drops.

## References

- [Cilium Egress Gateway](https://docs.cilium.io/en/stable/network/egress-gateway/egress-gateway/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
