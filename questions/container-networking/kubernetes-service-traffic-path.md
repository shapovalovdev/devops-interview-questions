---
title: Trace Kubernetes Service traffic
theme: container-networking
difficulty: senior
type: troubleshooting
tags: [containers, kubernetes, networking, dns, troubleshooting, cca, ckne]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/service/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Trace Kubernetes Service traffic

A Kubernetes Service resolves but requests fail. How do you trace the traffic path without assuming a specific CNI implementation?

## Answer guide

- Confirm the Service selector matches ready Pods and that endpoint data exists. DNS resolution only establishes the Service virtual address or name; it does not prove a usable backend.
- Test the target port and readiness from a workload in the same namespace and examine the Pod listener, labels, readiness gates, and Service `targetPort` mapping.
- Then inspect implementation-specific kube-proxy or CNI dataplane evidence. Kubernetes defines the Service abstraction, while packet forwarding details and observability vary by cluster implementation.
- Check NetworkPolicy and application TLS or authorization separately. Do not disable policy or expose a NodePort merely to bypass a missing endpoint or wrong target port.

## References

- [Kubernetes Docs: Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- Further reading (blog): [Kubernetes: Services, load balancing, and networking](https://kubernetes.io/blog/2017/10/Using-CoreDNS-for-Service-Discovery/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker networking tutorial](https://docs.docker.com/network/tutorials/)
