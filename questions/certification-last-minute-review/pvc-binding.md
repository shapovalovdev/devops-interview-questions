---
title: Debug a PersistentVolumeClaim that stays Pending
theme: certification-last-minute-review
difficulty: middle
type: troubleshooting
tags: [kubernetes, storage, volumes, cka, ckad, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a PersistentVolumeClaim that stays Pending

Which facts decide whether a PersistentVolumeClaim can bind?

## Answer guide

- A PVC requests storage by access mode, size, storage class, and optionally selectors. Binding requires a compatible PV or a provisioner that can create one through the referenced StorageClass.
- Inspect PVC events, the StorageClass provisioner and binding mode, and any existing PV's capacity, access modes, claim reference, and topology. `WaitForFirstConsumer` intentionally delays provisioning until scheduling supplies topology context.
- Do not edit a bound PV casually or delete a claim to force progress: reclaim policy may delete underlying data. Correct the request or storage configuration and verify backup and recovery expectations before recreating stateful resources.

## References

- [Kubernetes: Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- Further reading (blog): [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- Manual or specification: [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google Cloud — persistent disks in GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes)
- Hands-on guide: [Kubernetes configure a Pod to use a PVC](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)
