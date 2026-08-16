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
platform, from the Pod outward through the surrounding services to the runbooks
and the two meta-questions that run the last week.

1. [Read Pod phase, container state, and restart evidence](../../questions/certification-last-minute-review/pod-lifecycle-signals.html)
    — The exam weights the Pod first, and phase, container state, and restart
    evidence are how every scenario item opens.
2. [Select startup, readiness, and liveness probes](../../questions/certification-last-minute-review/probe-selection.html)
    — Probes decide restart evidence before any surrounding service can be
    blamed for it.
3. [Explain requests, limits, QoS, and a Pending Pod](../../questions/certification-last-minute-review/resource-requests-limits.html)
    — Requests, limits, and QoS explain the Pending Pod that scenario items love
    to hide.
4. [Review a Pod security context for least privilege](../../questions/certification-last-minute-review/security-context-review.html)
    — The security context review completes the Pod-level opening the exam
    always starts from.
5. [Choose ConfigMaps and Secrets without overstating protection](../../questions/certification-last-minute-review/configmap-secret-boundaries.html)
    — ConfigMaps versus Secrets is the first layer around the Pod, and scenario
    items fail here far more often than at exotic ones.
6. [Debug a Service with no reachable backends](../../questions/certification-last-minute-review/service-endpoints-debug.html)
    — The Service with no reachable backends is the canonical scenario failure
    at the service layer.
7. [Debug Kubernetes DNS before changing application code](../../questions/certification-last-minute-review/dns-debugging.html)
    — DNS debugging recurs inside Kubernetes with harder symptoms than the host
    version ever shows.
8. [Reason about NetworkPolicy enforcement and default deny](../../questions/certification-last-minute-review/networkpolicy-semantics.html)
    — Default deny and enforcement semantics decide whether the isolation the
    exam describes actually exists.
9. [Diagnose an RBAC denial without broadening access](../../questions/certification-last-minute-review/rbac-least-privilege.html)
    — The RBAC denial without broadening access is the last surrounding layer
    and the easiest one to flunk.
10. [Combine node selectors, affinity, taints, and tolerations](../../questions/certification-last-minute-review/scheduling-constraints.html)
    — Scheduling comes before storage and control-plane items because a Pending
    PVC presumes placement reasoning already works.
11. [Use PodDisruptionBudgets without blocking maintenance](../../questions/certification-last-minute-review/pod-disruption-budget.html)
    — Disruption budgets complete the scheduling story for the voluntary
    disruptions the exam asks about.
12. [Debug a PersistentVolumeClaim that stays Pending](../../questions/certification-last-minute-review/pvc-binding.html)
    — The Pending PVC is the storage item the scheduling tier just made legible.
13. [Triage an unavailable Kubernetes control plane](../../questions/certification-last-minute-review/control-plane-triage.html)
    — An unavailable control plane presumes you can already reason about where
    the workloads run.
14. [Operate Jobs and CronJobs without uncontrolled retries](../../questions/certification-last-minute-review/job-cronjob-cleanup.html)
    — Jobs and CronJobs without uncontrolled retries open the runbook set that
    converts knowledge into sequence.
15. [Plan and validate an etcd backup and restore](../../questions/certification-last-minute-review/etcd-backup-restore.html)
    — The etcd backup and restore is the runbook the exam trusts you can
    validate, not just describe.
16. [Build a safe Kubernetes cluster upgrade runbook](../../questions/certification-last-minute-review/cluster-upgrade-runbook.html)
    — The upgrade runbook spends the version-skew and drain discipline the
    runbook set just assembled.
17. [Evaluate a Kubernetes disaster-recovery exercise](../../questions/certification-last-minute-review/staff-disaster-recovery-exercise.html)
    — The disaster-recovery exercise converts the runbooks into a rehearsed
    motion with evidence.
18. [Lead a Kubernetes incident while preserving recovery options](../../questions/certification-last-minute-review/staff-incident-command.html)
    — Leading an incident while preserving recovery options is the runbook set's
    human tier.
19. [Prioritize certification review under a two-hour deadline](../../questions/certification-last-minute-review/staff-certification-prioritization.html)
    — The two-hour deadline question is how the last week before the exam should
    actually run.
20. [Keep certification preparation ethical and operationally useful](../../questions/certification-last-minute-review/staff-certification-boundaries.html)
    — Keeping preparation ethical closes the Theme because rehearsal that cheats
    the exam cheats the job.
