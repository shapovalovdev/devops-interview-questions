---
title: Build a safe Kubernetes cluster upgrade runbook
theme: certification-last-minute-review
difficulty: senior
type: scenario
tags: [kubernetes, cka, reliability, rolling-update, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a safe Kubernetes cluster upgrade runbook

Which sequence reduces risk when upgrading a kubeadm-managed cluster?

## Answer guide

- Check the supported version-skew policy, release notes, backups, add-on compatibility, capacity, and rollback boundaries before beginning. Upgrade the control plane before kubelets and respect the documented supported version sequence.
- Drain one worker at a time with an explicit plan for DaemonSets, local storage, PodDisruptionBudgets, and workloads that cannot move. A drain that blocks is evidence to investigate, not a reason to force every eviction.
- Validate node readiness, critical workloads, networking, storage, and observability after each stage. Record versions and commands so a second operator can continue safely if the change window is interrupted.

## References

- [Kubernetes: upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- Further reading (blog): [Kubernetes.io — release change considerations](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25/)

## What to learn next

- Official documentation: [kubeadm upgrade](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- Manual or specification: [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google Cloud — upgrade clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster)
- Hands-on guide: [Kubernetes drain a node safely](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
