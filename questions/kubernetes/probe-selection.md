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
