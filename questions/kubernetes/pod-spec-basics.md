---
title: Read the essential parts of a Pod specification
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, containers, deployment, cka, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/pods/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Read the essential parts of a Pod specification

Which parts of a Pod manifest determine what runs and how it is identified?

## Answer guide

- `metadata` supplies a name and labels; labels are the usual selector contract for Services and controllers.
- `spec.containers` defines images, commands, ports, environment, resources, security context, probes, and volume mounts for the workload.
- Pod-level fields define shared networking, volumes, scheduling constraints, service account, and restart behavior.
- A bare Pod is usually unsuitable for a durable application because it has no controller to maintain replica count or replace it after node loss; use an appropriate workload controller.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Kubernetes: Pod API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)
