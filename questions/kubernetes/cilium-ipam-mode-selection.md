---
title: Choose a Cilium IPAM mode for a Kubernetes cluster
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, networking, cloud, reliability, cca, ckne]
sources:
  - url: https://docs.cilium.io/en/stable/network/concepts/ipam/crd/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a Cilium IPAM mode for a Kubernetes cluster

How would you choose and validate Cilium IP address management for an on-premises cluster versus a cloud-integrated cluster?

## Answer guide

- Start with the cluster routing model and address authority: CRD-backed or Kubernetes modes fit different self-managed designs, while provider-specific modes integrate with supported cloud address resources.
- Model Pod CIDR capacity, node growth, dual-stack requirements, route propagation, and cloud API quotas before installation; the allocator choice changes who owns allocation and what failure modes apply.
- Validate allocated addresses through Cilium and Kubernetes resources, then test scheduling and cross-node connectivity under a controlled scale event.
- Do not switch modes casually on a live production cluster. Incorrect CIDRs, exhausted provider addresses, or delayed status reconciliation can leave new Pods pending or unreachable, so plan migration and rollback explicitly.

## References

- [Cilium CRD-backed IPAM](https://docs.cilium.io/en/stable/network/concepts/ipam/crd/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
