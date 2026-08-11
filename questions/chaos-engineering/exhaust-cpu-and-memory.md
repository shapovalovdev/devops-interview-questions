---
title: Exhaust CPU and memory deliberately
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, fault-injection, cpu, memory]
sources:
  - url: https://chaos-mesh.org/docs/simulate-heavy-stress-on-kubernetes/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Exhaust CPU and memory deliberately

How do you run a resource-exhaustion experiment without simply killing the host?

## Answer guide

- Place the stress precisely. Chaos Mesh StressChaos runs stressors inside the target pod's cgroup, so the pressure is bounded by that container's limits; a stress process on the host competes with everything on the node instead. Choose according to the hypothesis: "the service degrades gracefully when its own CPU limit is reached" is a container-scoped question, while "the node's other workloads survive a noisy neighbour" is a node-scoped one.
- CPU and memory fail differently. CPU saturation is elastic — throttling raises latency and queue depth but the process keeps running, and cgroup v2 exposes the throttling directly so you can prove the mechanism rather than infer it. Memory exhaustion is a cliff: the kernel out-of-memory killer terminates a process by score, which may not be the process you were stressing, and in Kubernetes an over-limit container is killed and restarted rather than throttled.
- Material constraints: set requests and limits before the experiment so the blast radius has a hard boundary, keep enough headroom for the kubelet and system daemons, and know your eviction thresholds — node memory pressure evicts pods in priority and QoS order, so a low-priority experiment can push out an unrelated critical workload. Watch throttling ratio, working set, page cache, OOM kill counts, restart counts, and the user-facing latency metric together.
- Failure modes: stressing a node hosting the control plane or the monitoring stack; a stressor that outlives the experiment because its parent was killed first; autoscalers that mask the effect by adding capacity mid-run, so the hypothesis is never actually tested; and reading a restart as recovery when the service actually lost in-flight requests and warm cache on the way.

## References

- [Chaos Mesh — simulate heavy stress on Kubernetes](https://chaos-mesh.org/docs/simulate-heavy-stress-on-kubernetes/)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [Chaos Mesh — simulate heavy stress on Kubernetes](https://chaos-mesh.org/docs/simulate-heavy-stress-on-kubernetes/)
- Manual or specification: [Linux control group v2 administrator guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Mikolaj Pawlikowski — chaos engineering writing](https://mikolajpawlikowski.com/)
- Technical blog: [Grafana Labs blog](https://grafana.com/blog/)
- Hands-on guide: [Kubernetes — managing resources for containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
