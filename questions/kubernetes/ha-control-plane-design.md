---
title: Design a highly available kubeadm control plane
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, cka, availability, reliability, networking]
sources:
  - url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a highly available kubeadm control plane

How would you design an HA control plane for a kubeadm cluster, and what failures must the design tolerate?

## Answer guide

- Put a stable, highly available control-plane endpoint in front of multiple API servers. Clients and joining nodes must use that endpoint, not the address of one control-plane node, or an otherwise redundant control plane still has a single-client failure point.
- Choose a supported etcd topology: stacked etcd is simpler but shares node failures with API servers; external etcd separates failure domains but adds an independently operated quorum. Use an odd number of members where practical, spread them across real failure domains, and protect quorum latency and disk performance.
- Add control-plane nodes with kubeadm using the shared endpoint and certificate/key distribution procedure. Validate leader loss, API endpoint failover, scheduler/controller availability, and workload continuity before calling the design HA.
- HA improves availability, not recoverability from every error. Keep encrypted, tested etcd backups and a distribution-specific restore runbook; do not perform destructive member removal, certificate changes, or network changes during an incident without first preserving state and establishing quorum facts.

## References

- [Kubernetes: Creating highly available clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
- [Kubernetes: Operating etcd clusters for Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- Further reading (blog): [Kubernetes: Production considerations for etcd](https://kubernetes.io/blog/2023/10/12/bootstrap-an-etcd-cluster-with-kubeadm/)

## What to learn next

- Official documentation: [Highly available kubeadm topology options](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/)
- Manual or specification: [etcd API and Raft consistency model](https://etcd.io/docs/v3.5/learning/api/)
- Maintainer or personal blog: [Daniele Polencic — why etcd breaks at scale in Kubernetes](https://learnkube.com/etcd-breaks-at-scale)
- Technical blog: [CNCF — making etcd incidents easier to debug in production Kubernetes](https://www.cncf.io/blog/2026/03/12/making-etcd-incidents-easier-to-debug-in-production-kubernetes/)
- Hands-on guide: [Create a highly available cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
