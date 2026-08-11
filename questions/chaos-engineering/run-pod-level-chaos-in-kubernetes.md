---
title: Run pod-level chaos in Kubernetes
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, kubernetes, fault-injection, availability]
sources:
  - url: https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Run pod-level chaos in Kubernetes

What do pod kill, pod failure, and container kill actually test, and how do you scope them?

## Answer guide

- The three faults are not interchangeable. Pod kill deletes the pod so the controller creates a replacement elsewhere, testing scheduling, image pull, warm-up, and connection re-establishment. Pod failure keeps the object but makes it unavailable for a duration, testing endpoint removal and client retry without churning the scheduler. Container kill restarts one container inside a pod, testing sidecar coupling and whether the main process depends on a proxy that just vanished.
- Scope with the selectors the tool gives you: namespace, label selector, and a mode such as one, fixed, fixed-percent, or random-max-percent, so a stray label change cannot escalate the run to every pod. Combine this with a PodDisruptionBudget as an independent guard — voluntary evictions respect it, and it also documents the minimum availability the service actually claims.
- Material constraints: readiness probes and endpoint propagation determine how long clients keep sending traffic to a doomed pod, so measure error rate during the transition, not just after it. Termination grace period, preStop hooks, and connection draining decide whether in-flight requests are lost. Anti-affinity and topology-spread constraints decide whether the replacement lands somewhere that actually improves availability.
- Failure modes: killing a pod that holds a leader lease or a singleton job; deleting the only replica of a StatefulSet member and triggering a real recovery; forcing a delete with a zero grace period so drain logic never runs, which tests something you never intended; and running against a namespace whose controller has no capacity to reschedule, turning a bounded experiment into a sustained outage.

## References

- [Chaos Mesh — simulate pod chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [Chaos Mesh — simulate pod chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/)
- Manual or specification: [PodDisruptionBudget API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)
- Maintainer or personal blog: [Mikolaj Pawlikowski — chaos engineering writing](https://mikolajpawlikowski.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [LitmusChaos installation and first experiment](https://docs.litmuschaos.io/docs/getting-started/installation)
