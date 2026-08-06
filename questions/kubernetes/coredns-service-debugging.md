---
title: Debug CoreDNS and Kubernetes Service resolution
theme: kubernetes
difficulty: senior
type: troubleshooting
tags: [kubernetes, cka, ckad, networking, dns, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug CoreDNS and Kubernetes Service resolution

Pods cannot resolve an internal Service name. How do you isolate the fault without assuming DNS is the only problem?

## Answer guide

- First identify the exact name and namespace expected. Kubernetes DNS search rules make a short name namespace-relative; test the fully qualified Service name from a Pod in the affected network path and compare its resolver configuration with a known-good Pod.
- Verify the CoreDNS Pods, their Service and EndpointSlices, Corefile configuration, API permissions, and CoreDNS logs. Also confirm the CNI allows Pod-to-DNS traffic and that any NetworkPolicy permits DNS egress and CoreDNS ingress; Kubernetes supplies the API model but the network plugin enforces policy.
- Separate name resolution from reachability: a successful DNS answer does not prove the Service has ready endpoints or that the application listens on the target port. Inspect the Service, EndpointSlices, readiness, and connection path after resolution succeeds.
- Avoid changing cluster-wide DNS configuration as the first response. Preserve the failing query, source Pod, answer/error, latency, and recent CoreDNS/CNI/policy changes; an unsafe Corefile edit can turn a scoped outage into a cluster-wide dependency failure.

## References

- [Kubernetes: Debugging DNS resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)
- [Kubernetes: DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- Further reading (blog): [Kubernetes: Scaling DNS service](https://kubernetes.io/blog/2018/12/14/kubernetes-1-13-release-announcement/)
