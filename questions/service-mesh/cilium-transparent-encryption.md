---
title: Plan Cilium transparent workload encryption
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, kubernetes, networking, security, mtls, cca]
sources:
  - url: https://docs.cilium.io/en/stable/security/network/encryption-ipsec/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan Cilium transparent workload encryption

How would you introduce Cilium transparent encryption for traffic between workloads without assuming it replaces every application-security control?

## Answer guide

- Choose the documented Cilium encryption mechanism that fits the environment, verify kernel and node prerequisites, and plan key distribution, rotation, and observability before enabling it.
- Start with a representative cluster or node pool, confirm protected paths with connectivity tests and metrics, and make the encryption boundary explicit to application and security owners.
- Preserve application TLS and authentication where end-to-end identity, protocol-level authorization, or traffic beyond the Cilium-managed path requires them.
- Encryption configuration can affect MTU, routing, performance, and interoperability during a mixed rollout. Incorrect keys or incompatible nodes can interrupt traffic, so stage the change, monitor drops, and retain a tested rollback path.

## References

- [Cilium IPsec transparent encryption](https://docs.cilium.io/en/stable/security/network/encryption-ipsec/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
