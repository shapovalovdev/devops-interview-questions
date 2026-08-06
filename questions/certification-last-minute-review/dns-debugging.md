---
title: Debug Kubernetes DNS before changing application code
theme: certification-last-minute-review
difficulty: middle
type: troubleshooting
tags: [kubernetes, dns, networking, cka, ckad, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug Kubernetes DNS before changing application code

How do you isolate a Service-name lookup failure in a cluster?

## Answer guide

- Test resolution from a comparable Pod and inspect `/etc/resolv.conf`; namespace, search domains, and `ndots` affect the lookup that the application actually performs. A Service name should normally resolve through cluster DNS.
- Verify the CoreDNS Pods, Service, EndpointSlices, and recent logs, then distinguish name resolution from connection failure. A DNS answer for a Service does not prove its endpoints are ready or reachable.
- Check NetworkPolicy and node-to-DNS connectivity only after confirming the queried name and namespace. Avoid editing CoreDNS configuration as a first response; preserve the failing query, response, and client namespace for a reproducible diagnosis.

## References

- [Kubernetes: DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- Further reading (blog): [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [Kubernetes DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- Manual or specification: [CoreDNS Kubernetes plugin](https://coredns.io/plugins/kubernetes/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google Cloud — Kubernetes DNS](https://cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns)
- Hands-on guide: [Kubernetes debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
