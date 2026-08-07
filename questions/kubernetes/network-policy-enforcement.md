---
title: Restrict Pod traffic with NetworkPolicy
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, networking, security, least-privilege, cks, kcsa, cka, ckad, kcna, cca, ckne]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Restrict Pod traffic with NetworkPolicy

How would you allow an API Pod to receive traffic only from its frontend and call only its database?

## Answer guide

- Select the target Pods with labels and declare explicit ingress and egress peers and ports.
- Confirm the installed CNI enforces NetworkPolicy and test allowed and denied paths.
- A Pod becomes isolated for ingress or egress only when a matching policy applies for that direction; allowed connections combine the relevant policies.
- Include DNS, control-plane, and required dependency paths, roll out from observability and test namespaces, and remember that Kubernetes defines the API while enforcement details depend on the network implementation.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Kubernetes: Services, load balancing, and networking](https://kubernetes.io/docs/concepts/services-networking/)

## What to learn next

- Official documentation: [Kubernetes concepts: network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- Manual or specification: [NetworkPolicy v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
- Maintainer or personal blog: [Brett Johnson — network policy deep dive: default ingress and egress policies](https://sdbrett.com/post/2020-11-16-network-policy-podselection-deep-dive/)
- Technical blog: [Red Hat — guide to Kubernetes egress network policies](https://www.redhat.com/en/blog/guide-to-kubernetes-egress-network-policies)
- Hands-on guide: [Declare a network policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)
