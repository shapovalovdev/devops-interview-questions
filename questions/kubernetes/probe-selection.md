---
title: Select Kubernetes readiness, liveness, and startup probes
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, reliability, troubleshooting, cka, ckad, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Select Kubernetes readiness, liveness, and startup probes

How do you choose the three probe types for a service with a slow initialization phase and a dependency outage?

## Answer guide

- Startup probes protect slow initialization from premature liveness restarts.
- Readiness controls whether a Pod receives traffic and should reflect its ability to serve safely.
- Liveness detects a stuck process and kubelet restarts a failed liveness check; do not use it to restart healthy Pods solely because an external dependency is unavailable.
- Use an endpoint that is cheap, deterministic, and scoped to the probe purpose. Aggressive thresholds or dependency-coupled probes can create a restart storm or remove all healthy capacity.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Liveness, readiness, and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [Kubernetes: Pod lifecycle and probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

## What to learn next

- Official documentation: [Kubernetes concepts: liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- Manual or specification: [kubelet configuration v1beta1 API reference](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/)
- Maintainer or personal blog: [Agata Skorupka — start sidecar first: readiness probes and startup ordering](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)
- Technical blog: [Fairwinds — understanding Kubernetes liveness probe best practices](https://www.fairwinds.com/blog/a-guide-to-understanding-kubernetes-liveness-probes-best-practices)
- Hands-on guide: [Configure liveness, readiness and startup probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
