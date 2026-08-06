---
title: Explain Pod lifecycle and container restarts
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, troubleshooting, reliability, cka, ckad, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Pod lifecycle and container restarts

What do Pod phases and container restart counts tell you during an incident?

## Answer guide

- Pod phase is a high-level summary: `Pending`, `Running`, `Succeeded`, `Failed`, or `Unknown`; it is not a complete health signal.
- Inspect container state, reason, exit code, events, logs, and `restartCount`; kubelet restarts a failed container according to the Pod restart policy.
- `Running` only means at least one primary container started successfully, so an unready or crash-looping workload can still show that phase.
- Avoid treating a restart count as the cause: distinguish an application exit, probe-driven restart, eviction, image failure, and node failure before changing configuration.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [Kubernetes: Debug running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
