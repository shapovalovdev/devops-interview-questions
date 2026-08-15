# Certification last-minute review: related materials

Use official Kubernetes documentation for version-specific behavior; rehearse operational tasks in a disposable cluster.

## What to learn next

- Official documentation: [Kubernetes documentation](https://kubernetes.io/docs/home/)
- Manual or specification: [Kubernetes API reference](https://kubernetes.io/docs/reference/kubernetes-api/)
- Maintainer or personal blog: [Ahmet Alp Balkan](https://ahmet.im/blog/)
- Technical blog: [Kubernetes Blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes tasks](https://kubernetes.io/docs/tasks/)

## Suggested study order

Read this Theme as a rehearsal, in roughly the order the exam weights the
platform. Begin at the Pod: its specification, phase and container state,
restart evidence, probes, requests and limits, and security context. Move
outward through the services around it — ConfigMaps versus Secrets, Service
discovery, the Service with no reachable backends, DNS debugging, NetworkPolicy
and default deny, the RBAC denial without broadening access — because scenario
items fail at one of these layers far more often than at exotic ones. Take
scheduling (node selectors, affinity, taints, tolerations,
PodDisruptionBudgets) before the storage and control-plane items: a Pending PVC
or an unavailable control plane presumes you can already reason about where a
Pod runs. The runbook set — Jobs and CronJobs without uncontrolled retries, the
etcd backup and restore, the cluster upgrade runbook, the disaster-recovery
exercise, leading an incident while preserving recovery options — converts the
same knowledge into sequence and hands. Close with the two meta-questions,
prioritizing review under a two-hour deadline and keeping preparation ethical,
which is how the last week before the exam should actually run.
