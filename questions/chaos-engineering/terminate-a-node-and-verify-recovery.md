---
title: Terminate a node and verify real recovery
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, kubernetes, recovery, capacity]
sources:
  - url: https://kubernetes.io/docs/concepts/architecture/nodes/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Terminate a node and verify real recovery

You terminate a worker node without draining it. What do you measure, and what counts as recovery?

## Answer guide

- An abrupt termination is deliberately different from a drain. A drain evicts pods politely and respects disruption budgets; a hard termination makes the control plane infer the loss from missed heartbeats. The node lease and node-monitor grace period decide how long the node stays Ready in the API, and until then endpoints keep pointing at pods that no longer exist. That gap — not the rescheduling — is usually the source of user-visible errors.
- Measure the whole sequence with timestamps: node marked NotReady, pods marked for deletion, endpoints withdrawn, replacements scheduled, images pulled, containers started, readiness achieved, caches warmed, error rate back to baseline. Recovery is the last of those, not the first. A cluster that reschedules in twenty seconds but needs four minutes to warm a cache has a four-minute recovery time.
- Material constraints: you need spare capacity for the replacement pods or the cluster autoscaler must provision a node, which adds minutes and can fail on quota or instance availability. Topology-spread constraints and anti-affinity determine whether losing one node takes out several replicas of the same service. Anything with local state — a StatefulSet with local volumes, a cache, an in-progress job — recovers on a different timeline from stateless work.
- Failure modes: terminating a control-plane or etcd member by accident; losing a node that was quietly hosting a singleton such as an ingress controller replica or a cluster-critical operator; discovering that pod anti-affinity was never applied so three of five replicas were co-located; and treating a green dashboard as recovery when the replacement pod is Ready but not yet serving correctly.

## References

- [Kubernetes — nodes, leases, and node status](https://kubernetes.io/docs/concepts/architecture/nodes/)
- Further reading (blog): [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [Kubernetes — nodes, leases, and node status](https://kubernetes.io/docs/concepts/architecture/nodes/)
- Manual or specification: [AWS Fault Injection Service actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)
- Maintainer or personal blog: [Adrian Cockcroft — architecture and resilience writing](https://adrianco.medium.com/)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Kubernetes — safely drain a node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
