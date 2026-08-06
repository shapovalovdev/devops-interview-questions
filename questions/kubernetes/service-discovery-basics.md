---
title: Explain Kubernetes Service discovery
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, networking, dns, reliability, cka, ckad, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/service/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Kubernetes Service discovery

Why should an application call a Service name instead of a Pod IP?

## Answer guide

- Pods are ephemeral, so their IPs and membership can change as controllers create or remove them.
- A Service defines a stable logical endpoint and usually selects backing Pods by labels; EndpointSlices track the current backends.
- Cluster DNS normally resolves a Service name to its ClusterIP, or to ready endpoint IPs for a headless Service.
- Verify selector labels and ready endpoints when requests fail; a Service object can exist with zero usable backends.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes: DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
