---
title: Advertise Kubernetes routes with Cilium BGP Control Plane
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, reliability, troubleshooting, cca]
sources:
  - url: https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane-configuration/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Advertise Kubernetes routes with Cilium BGP Control Plane

How would you design and validate Cilium BGP Control Plane so external networks can reach selected Kubernetes Services?

## Answer guide

- Enable the BGP control plane only after agreeing ASN, peer, address-family, route advertisement, and failure behavior with the network team; it advertises routes but does not create in-cluster datapath reachability.
- Use the Cilium BGP custom resources to select nodes, define peer settings, and limit advertised Pod CIDRs or Service addresses to the intended scope.
- Verify sessions, received and advertised routes, Service endpoint behavior, and external probes; test a node and peer failure before production cutover.
- A selector mismatch, ASN mismatch, overbroad advertisement, or unsupported address family can create black holes or leak routes. Protect router credentials, observe route changes, and define withdrawal and rollback procedures.

## References

- [Cilium BGP control-plane resources](https://docs.cilium.io/en/stable/network/bgp-control-plane/bgp-control-plane-configuration/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
