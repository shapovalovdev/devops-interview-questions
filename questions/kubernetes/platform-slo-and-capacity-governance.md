---
title: Set Kubernetes platform SLO and capacity governance
theme: kubernetes
difficulty: staff
type: scenario
tags: [kubernetes, observability, capacity-planning, reliability, governance]
sources:
  - url: https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set Kubernetes platform SLO and capacity governance

How would you define service objectives and capacity ownership for a shared Kubernetes platform?

## Answer guide

- Define measurable platform outcomes separately from application outcomes: API availability/latency, scheduling latency, node readiness, workload start latency, and supported service reliability.
- Build demand and headroom models from requests, actual usage, pending Pods, autoscaler behavior, failure-domain loss, and planned maintenance rather than average CPU alone.
- Assign ownership for cluster capacity, namespace quotas, workload requests, and escalation, with dashboards and error-budget actions that make trade-offs visible.
- Do not promise application availability solely from a healthy cluster: dependencies, application configuration, and workload resource choices remain shared responsibilities.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Cluster autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)
- [Kubernetes: Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
