---
title: Choose a Cilium policy-enforcement mode
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, networking, security, reliability, cca]
sources:
  - url: https://docs.cilium.io/en/stable/security/policy/intro/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a Cilium policy-enforcement mode

How would you introduce Cilium network policy enforcement to a cluster that currently allows all workload traffic?

## Answer guide

- Begin by inventorying required flows, DNS, ingress, health checks, and control-plane dependencies, then express observed intent as narrowly scoped policies.
- Cilium enforcement behavior is configuration- and policy-dependent; use the documented mode for the release and confirm how endpoints become isolated before declaring a default-deny posture.
- Stage the rollout by namespace or workload, test positive and negative paths, and use Hubble or policy verdicts to find legitimate missing traffic.
- Enforcement can turn an overlooked dependency into an outage. Avoid a simultaneous platform migration and policy lockdown, retain break-glass access with audit controls, and review labels because an unintended selector changes the security boundary.

## References

- [Cilium policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)

## What to learn next

- Official documentation: [Cilium policy enforcement modes](https://docs.cilium.io/en/stable/security/policy/intro/)
- Manual or specification: [NetworkPolicy v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
- Maintainer or personal blog: [Nico Vibert — exploring eBPF part 3: observing policy decisions with Hubble](https://nicovibert.com/2022/02/21/exploring-ebpf-part-3-hubble/)
- Technical blog: [CNCF — safely managing Cilium network policies with testing and simulation](https://www.cncf.io/blog/2025/11/06/safely-managing-cilium-network-policies-in-kubernetes-testing-and-simulation-techniques/)
- Hands-on guide: [Cilium network policy reference and examples](https://docs.cilium.io/en/stable/security/policy/)
