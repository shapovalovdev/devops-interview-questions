---
title: Debug a Service with no reachable backends
theme: certification-last-minute-review
difficulty: junior
type: troubleshooting
tags: [kubernetes, networking, dns, cka, ckad, kcna, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/service/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a Service with no reachable backends

A Service exists but requests fail. What is the shortest reliable investigation?

## Answer guide

- Confirm the client's namespace, Service DNS name, port, and protocol. A Service exposes a stable virtual endpoint, but it does not create healthy application listeners by itself.
- Compare the Service selector with Pod labels, then inspect EndpointSlices and the selected Pods' readiness state. A selector mismatch or unready Pods produces no usable endpoints even though the Service object is valid.
- Verify `targetPort` against the container's actual listening port and test from a Pod in the cluster. If endpoints are present but traffic still fails, investigate NetworkPolicy, the CNI, and application binding rather than repeatedly recreating the Service.

## References

- [Kubernetes: Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- Further reading (blog): [Kelsey Hightower — Kubernetes Services](https://medium.com/google-cloud/kubernetes-services-7e5f0d2dcfc1)

## What to learn next

- Official documentation: [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- Manual or specification: [EndpointSlice API](https://kubernetes.io/docs/concepts/services-networking/service/#endpointslices)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes Services](https://medium.com/google-cloud/kubernetes-services-7e5f0d2dcfc1)
- Technical blog: [Google Cloud — Kubernetes Services](https://cloud.google.com/kubernetes-engine/docs/concepts/service)
- Hands-on guide: [Kubernetes connect applications with a Service](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)
