---
title: Evaluate a Kubernetes disaster-recovery exercise
theme: certification-last-minute-review
difficulty: staff
type: scenario
tags: [kubernetes, reliability, storage, incident-response, cka]
sources:
  - url: https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate a Kubernetes disaster-recovery exercise

What proves that a Kubernetes recovery plan works?

## Answer guide

- Define plausible loss scenarios separately: a deleted workload, a failed node, control-plane loss, region loss, and corrupted application data require different recovery mechanisms. Name the recovery point and recovery time objectives for each.
- Exercise restoration in a safe environment using the same credentials, artifacts, and documented order expected in a real incident. Verify cluster state, persistent data consistency, external dependencies, and user-visible behavior rather than only successful commands.
- Record gaps as owned improvements: backup freshness, secret recovery, DNS or load-balancer dependencies, runbook ambiguity, and communication. A plan is not validated by a backup job alone; it must meet objectives under constrained conditions.

## References

- [Kubernetes: cluster administration overview](https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/)
- Further reading (blog): [John Allspaw — blame-free postmortems](https://www.etsy.com/codeascraft/blameless-postmortems/)

## What to learn next

- Official documentation: [Kubernetes cluster administration](https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/)
- Manual or specification: [etcd disaster recovery](https://etcd.io/docs/v3.5/op-guide/recovery/)
- Maintainer or personal blog: [John Allspaw — postmortem culture](https://www.etsy.com/codeascraft/blameless-postmortems/)
- Technical blog: [Google SRE — emergency response](https://sre.google/sre-book/emergency-response/)
- Hands-on guide: [Kubernetes etcd operations](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
