---
title: Validate Kubernetes NetworkPolicy enforcement
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, security, least-privilege]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Validate Kubernetes NetworkPolicy enforcement

How do you introduce default-deny NetworkPolicies without accidentally assuming Kubernetes enforces them itself?

## Answer guide

- NetworkPolicy expresses permitted Pod traffic, but a cluster needs a compatible network plugin to enforce it. Verify that capability and its documented behavior before treating a manifest as a control.
- Start with namespace-scoped default-deny policy, inventory required DNS and service flows, and add explicit ingress and egress allowances with tests.
- Observe denied traffic and application failures during staged rollout. Policies are additive, and selector errors or missing egress allowances can produce outages.
- NetworkPolicy is not a substitute for authentication, TLS, or cloud perimeter controls. Keep ownership clear across the CNI, platform, and application teams.

## References

- [Kubernetes Docs: Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- Further reading (blog): [Kubernetes: Network policies](https://kubernetes.io/blog/2021/04/20/defending-your-cluster-cloud-native-threat-detection-response/)
