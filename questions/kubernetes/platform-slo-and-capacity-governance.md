---
title: Set Kubernetes platform SLO and capacity governance
theme: kubernetes
difficulty: staff
type: scenario
tags: [kubernetes, observability, capacity-planning, reliability, governance, kcsa, cka]
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

## What to learn next

- Official documentation: [Kubernetes service level indicator (SLI) metrics](https://kubernetes.io/docs/reference/instrumentation/slis/)
- Manual or specification: [Kubernetes metrics reference](https://kubernetes.io/docs/reference/instrumentation/metrics/)
- Maintainer or personal blog: [Daniele Polencic — allocatable resources and node capacity planning](https://learnkube.com/allocatable-resources)
- Technical blog: [CNCF — Kubernetes patterns: capacity planning](https://www.cncf.io/blog/2019/10/08/kubernetes-patterns-capacity-planning/)
- Hands-on guide: [Google SRE Workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
