---
title: Triage a Kubernetes control-plane availability incident
theme: kubernetes
difficulty: senior
type: troubleshooting
tags: [kubernetes, incident-response, observability, reliability]
sources:
  - url: https://kubernetes.io/docs/tasks/debug/debug-cluster/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a Kubernetes control-plane availability incident

The API server is intermittently unavailable. How do you investigate without making the outage worse?

## Answer guide

- Establish scope first: distinguish API reachability, authentication, authorization, scheduler/controller progress, node health, and data-plane symptoms from application failures.
- Check API server and datastore health, request latency/error metrics, controller/scheduler logs, certificates, resource saturation, and recent changes using the distribution's supported operational interface.
- Reduce load or halt risky automation before restarting components; preserve logs and cluster state, and communicate a clear change freeze and recovery owner.
- Avoid blindly deleting control-plane Pods or datastore data: recovery and quorum procedures are distribution- and datastore-specific and can turn an availability event into data loss.

## References

- [Kubernetes: Debugging clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [Kubernetes: Operating etcd clusters](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
