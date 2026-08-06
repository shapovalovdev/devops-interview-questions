---
title: Debug a failing Kubernetes application with built-in CLI tools
theme: kubernetes
difficulty: middle
type: troubleshooting
tags: [kubernetes, troubleshooting, observability, logging, deployment, ckad]
sources:
  - url: https://kubernetes.io/docs/tasks/debug/debug-application/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a failing Kubernetes application with built-in CLI tools

An application is unavailable after a rollout. How do you use Kubernetes CLI tools to isolate the cause?

## Answer guide

- Start with the intended workload and namespace: inspect rollout status, Pod state, owner references, events, and the effective Pod specification. `kubectl describe` exposes scheduling, image, probe, and volume events that a raw status summary can omit.
- Read current and previous container logs, then use `kubectl exec` only when the container is running and an in-container check is necessary. Compare labels to Service selectors and inspect Endpoints or EndpointSlices when the failure is only on the request path.
- Change one hypothesis at a time and verify recovery with readiness and real traffic, not merely a running Pod. Avoid treating a restart as a fix: CrashLoopBackOff, failed probes, bad configuration, resource pressure, and missing endpoints can recur immediately or affect only a subset of replicas.

## References

- [Kubernetes: Debugging Services](https://kubernetes.io/docs/tasks/debug/debug-application/)
- [kubectl logs reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
- Further reading (blog): [Kubernetes debugging techniques](https://kubernetes.io/blog/2024/05/01/cri-streaming-explainer/)
