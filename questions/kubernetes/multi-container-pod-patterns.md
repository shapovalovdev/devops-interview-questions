---
title: Choose an init container or sidecar for an application Pod
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, containers, deployment, reliability, ckad]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose an init container or sidecar for an application Pod

When should an application use an init container, a sidecar, or neither?

## Answer guide

- Use an init container for work that must finish before application containers start, such as obtaining bootstrap configuration, creating a required directory, or waiting for a dependency according to a bounded readiness rule. Its failure prevents the Pod from progressing, so make the action idempotent and observable.
- Use a sidecar for a companion process that must run alongside the application, such as a local proxy or log shipper. Give it explicit resource requests, probes where appropriate, and lifecycle behavior that does not unexpectedly keep a completed workload alive.
- Keep cross-cutting work outside the Pod when it does not require shared localhost or shared volumes; a platform service is often easier to patch, scale, and secure than duplicating an agent in every Pod. Do not use an init container as an unbounded dependency wait: it can create a rollout deadlock and hide the real dependency failure.

## References

- [Kubernetes: Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
- [Kubernetes: Init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
- Further reading (blog): [Kubernetes sidecar containers](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/)

## What to learn next

- Official documentation: [Kubernetes concepts: sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
- Manual or specification: [KEP-753: sidecar containers enhancement proposal](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/753-sidecar-containers/README.md)
- Maintainer or personal blog: [Emanuel Evans — extending applications on Kubernetes with multi-container Pods](https://learnkube.com/sidecar-containers-patterns)
- Technical blog: [Kubernetes blog — introducing native sidecar containers](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/)
- Hands-on guide: [Adopting sidecar containers tutorial](https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/)
