---
title: Choose StatefulSet or Deployment
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, deployment, storage, reliability, cka, ckad]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose StatefulSet or Deployment

When is a StatefulSet appropriate instead of a Deployment?

## Answer guide

- Use a Deployment for interchangeable, usually stateless replicas where identity and per-replica storage are not part of the application contract.
- Use a StatefulSet when replicas require stable ordinal identity, stable network identity, ordered deployment/scaling, or a distinct PersistentVolumeClaim per Pod.
- A StatefulSet normally pairs with a headless Service for stable network identities; it does not supply replication, backup, or quorum logic for the application.
- Plan disruption, storage failure, and recovery procedures explicitly because ordered behavior can slow rollouts and a forced deletion can violate application safety assumptions.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
