---
title: Reason about NetworkPolicy enforcement and default deny
theme: certification-last-minute-review
difficulty: middle
type: theory
tags: [kubernetes, networking, security, cka, cks, kcsa]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reason about NetworkPolicy enforcement and default deny

What must be true for a NetworkPolicy to restrict traffic?

## Answer guide

- NetworkPolicy is an API that selects Pods and declares allowed ingress or egress peers and ports. It applies only if the installed network plugin implements enforcement; Kubernetes itself does not provide a packet filter.
- A selected Pod becomes isolated for a direction when a policy includes that direction. Policies are additive: traffic is allowed when it is permitted by the applicable policies, not when a later policy denies it.
- Build a default-deny posture gradually, including DNS and required control-plane or dependency traffic. Test from representative namespaces and inspect the CNI's policy observability because an empty endpoint set and a denied flow can look similar to clients.

## References

- [Kubernetes: Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- Further reading (blog): [Isovalent — NetworkPolicy tutorial](https://isovalent.com/blog/post/2021-07-15-enforcing-kubernetes-network-policies/)

## What to learn next

- Official documentation: [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- Manual or specification: [NetworkPolicy API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
- Maintainer or personal blog: [Isovalent — enforcing policies](https://isovalent.com/blog/post/2021-07-15-enforcing-kubernetes-network-policies/)
- Technical blog: [Google Cloud — NetworkPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
- Hands-on guide: [Kubernetes declare NetworkPolicy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)
