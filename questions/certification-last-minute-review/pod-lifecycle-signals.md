---
title: Read Pod phase, container state, and restart evidence
theme: certification-last-minute-review
difficulty: junior
type: troubleshooting
tags: [kubernetes, containers, cka, ckad, kcna, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Read Pod phase, container state, and restart evidence

What evidence distinguishes a pending Pod, a crashing container, and a completed workload?

## Answer guide

- Pod phase is a coarse summary, not a diagnosis. Read `kubectl describe pod` events and each container's waiting, running, or terminated state, including reason, exit code, and timestamps.
- `Pending` often means scheduling, image, volume, or admission work is unfinished. `CrashLoopBackOff` is a kubelet backoff around repeated container termination; use `kubectl logs --previous` to retrieve the prior failed instance.
- A `Succeeded` Pod can be correct for a Job and wrong for a long-lived Service. Compare restart policy and controller intent before changing probes or commands, and preserve event evidence because it is retained for limited time.

## References

- [Kubernetes: Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- Further reading (blog): [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [Kubernetes Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- Manual or specification: [Pod API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google Cloud — troubleshooting CrashLoopBackOff](https://cloud.google.com/kubernetes-engine/docs/troubleshooting/crashloopbackoff-events)
- Hands-on guide: [Kubernetes debug running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
