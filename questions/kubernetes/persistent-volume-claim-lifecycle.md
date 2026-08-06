---
title: Design PersistentVolumeClaim lifecycle for a stateful workload
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, storage, reliability, deployment]
sources:
  - url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design PersistentVolumeClaim lifecycle for a stateful workload

How do PersistentVolumes, PersistentVolumeClaims, StorageClasses, and reclaim policy fit together?

## Answer guide

- A PersistentVolume is storage supplied to the cluster, while a PersistentVolumeClaim is a workload request that binds to compatible storage; a StorageClass can provision storage dynamically.
- The claim is mounted by Pods, allowing the workload manifest to request capacity and access mode without naming the underlying storage implementation.
- Choose access mode, expansion, snapshot/backup capability, topology, and reclaim policy for the data's recovery and availability requirements.
- Deleting a claim can trigger retention or deletion according to policy and provisioner behavior; test restore and failure paths rather than assuming a StatefulSet makes data durable.

## References

- [Kubernetes: Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Kubernetes: Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
