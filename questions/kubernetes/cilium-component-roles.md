---
title: Explain the roles of Cilium agents, operator, and Envoy
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, networking, security, observability, cca]
sources:
  - url: https://docs.cilium.io/en/stable/overview/intro/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the roles of Cilium agents, operator, and Envoy

What responsibilities belong to the Cilium agent, Cilium operator, and Envoy when Cilium runs in Kubernetes?

## Answer guide

- The Cilium agent runs on every node, programs the local datapath and enforces connectivity, identity, and policy decisions for local workloads.
- The operator performs cluster-scoped control-plane work, such as managing shared resources, so that every node does not independently call a cloud API or reconcile the same object.
- Envoy provides proxy functions needed for L7 policy, Gateway API, and traffic management; it works with Cilium rather than replacing the eBPF datapath.
- Check the deployed version and enabled features before diagnosing ownership. A missing agent affects a node, while an unavailable operator or Envoy can affect shared allocation or L7 behavior; do not grant broad privileges merely to mask the distinction.

## References

- [Cilium and Hubble introduction](https://docs.cilium.io/en/stable/overview/intro/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
