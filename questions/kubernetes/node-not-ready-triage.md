---
title: Triage a Kubernetes node that becomes NotReady
theme: kubernetes
difficulty: senior
type: troubleshooting
tags: [kubernetes, cka, linux, monitoring, troubleshooting, reliability]
sources:
  - url: https://kubernetes.io/docs/tasks/debug/debug-cluster/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a Kubernetes node that becomes NotReady

A production node changes to `NotReady`. What evidence do you collect and how do you reduce impact safely?

## Answer guide

- Establish whether the node is unreachable, the kubelet cannot report status, or the control plane cannot process reports. Inspect Node conditions, events, leases, taints, kubelet and runtime logs, resource/disk/inode pressure, certificates, DNS/network reachability, and recent host or cluster changes.
- Protect workloads before remediation: cordon the node to stop new placement, then decide whether a controlled drain is safe given PodDisruptionBudgets, local data, daemon workloads, and remaining capacity. Do not blindly drain or reboot a node that may host irreplaceable state or a control-plane role.
- Check the kubelet-to-API path and the container runtime separately. A running runtime does not prove kubelet health; conversely, a healthy kubelet cannot report through a failed network, expired credential, overloaded API server, or misconfigured node identity.
- Repair the smallest verified fault and watch the node return to Ready, workloads reschedule, and application SLOs recover. Preserve logs and timeline evidence; repeated NotReady events usually need a capacity, host-lifecycle, CNI, or platform-owner follow-up rather than repeated manual restarts.

## References

- [Kubernetes: Troubleshooting clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [Kubernetes: Node status](https://kubernetes.io/docs/reference/node/node-status/)
- Further reading (blog): [Kubernetes: Node heartbeats with Lease API](https://kubernetes.io/blog/2019/12/17/node-heartbeats/)
