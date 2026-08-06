---
title: Select startup, readiness, and liveness probes
theme: certification-last-minute-review
difficulty: middle
type: scenario
tags: [kubernetes, healthchecks, reliability, cka, ckad]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Select startup, readiness, and liveness probes

How do the three probe types change traffic and restart behavior?

## Answer guide

- A readiness probe controls whether a Pod is considered ready for Service traffic. It should represent ability to serve the relevant request, not merely that the process has started.
- A liveness probe causes the kubelet to restart a container after failure; using a dependency check as liveness can turn a transient outage into a restart storm. A startup probe delays liveness and readiness checks while a slow application initializes.
- Set realistic timeouts and thresholds based on observed startup and request behavior. Test failure paths and inspect probe events; do not make a probe expensive or dependent on an overloaded downstream system.

## References

- [Kubernetes: liveness, readiness, and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- Further reading (blog): [Pete Goodman — Kubernetes probes](https://www.petermgoodman.com/kubernetes-probes/)

## What to learn next

- Official documentation: [Kubernetes probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- Manual or specification: [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- Maintainer or personal blog: [Pete Goodman — probes](https://www.petermgoodman.com/kubernetes-probes/)
- Technical blog: [Google Cloud — liveness probes](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes)
- Hands-on guide: [Kubernetes configure liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
