---
title: Evaluate Cilium kube-proxy replacement
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, performance, reliability, cca]
sources:
  - url: https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate Cilium kube-proxy replacement

When is Cilium kube-proxy replacement appropriate, and how would you roll it out safely?

## Answer guide

- It moves Kubernetes Service handling into Cilium's eBPF datapath; assess it as a cluster networking design change, not a performance toggle.
- Confirm the supported Cilium and Kubernetes versions, required kernel capabilities, API-server reachability settings, service types, and any integrations that assume kube-proxy behavior.
- Rehearse on a representative cluster and test ClusterIP, NodePort, LoadBalancer, external traffic policy, DNS, and rollback before production adoption.
- A partial or incompatible rollout can break service reachability. Keep a tested migration plan, observe service errors and datapath health, and avoid mixing undocumented feature combinations during an incident.

## References

- [Cilium kube-proxy replacement](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
