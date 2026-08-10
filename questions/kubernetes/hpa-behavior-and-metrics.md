---
title: Configure HorizontalPodAutoscaler behavior
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, monitoring, capacity-planning, reliability, cka, ckad]
sources:
  - url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure HorizontalPodAutoscaler behavior

How does an HPA make scaling decisions, and what must be true before relying on it?

## Answer guide

- The HPA periodically adjusts a scalable workload's desired replicas from observed metrics and the configured target; resource utilization calculations need relevant resource requests.
- Set sensible minimum and maximum replicas, scale-up/down behavior, and metrics that reflect the bottleneck rather than only a convenient signal.
- Ensure a metrics API is available, application startup and readiness are considered, and cluster/node capacity can accommodate the extra Pods.
- Autoscaling cannot repair a dependency outage or unlimited queue growth; watch saturation, errors, and scaling delay, and test a load pattern before production use.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Kubernetes: Metrics APIs](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)

## What to learn next

- Official documentation: [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- Manual or specification: [HorizontalPodAutoscaler v2 API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)
- Maintainer or personal blog: [Daniel Weibel — autoscaling apps on Kubernetes with custom metrics](https://learnkube.com/autoscaling-apps-kubernetes)
- Technical blog: [CNCF — autoscaling simplified: how to scale applications in Kubernetes](https://www.cncf.io/blog/2024/02/05/autoscaling-simplified-how-to-scale-your-applications-in-kubernetes/)
- Hands-on guide: [HorizontalPodAutoscaler walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
