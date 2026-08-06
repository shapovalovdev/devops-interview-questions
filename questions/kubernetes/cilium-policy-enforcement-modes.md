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
