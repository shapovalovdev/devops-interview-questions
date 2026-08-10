---
title: Explain consistency and availability during a network partition
theme: distributed-systems
difficulty: junior
type: theory
tags: [availability, reliability, networking]
sources:
  - url: https://etcd.io/docs/v3.6/learning/why/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain consistency and availability during a network partition

What trade-off must a replicated service make when replicas cannot communicate?

## Answer guide

- A system must make an explicit safety decision when a partition makes it impossible to know whether another replica has accepted a conflicting operation. A consensus-backed control plane normally rejects or delays writes without quorum, preserving one ordered history rather than acknowledging divergent state.
- Availability is not a global adjective: state which operation, replica set, quorum rule, and failure model are being discussed. Reads may have different guarantees from writes, and a stale read can be acceptable only when the caller explicitly tolerates it.
- Do not treat partitions as rare theoretical events. Lost packets, asymmetric reachability, slow disks, and bad timeouts can look like partitions; an unsafe fail-open leader or uncontrolled retries can create split-brain, duplicate work, or irreversible data corruption.

## References

- [etcd: Why etcd](https://etcd.io/docs/v3.6/learning/why/)
- Further reading (personal blog): [Martin Kleppmann: Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html)

## What to learn next

- Official documentation: [etcd learning](https://etcd.io/docs/v3.6/learning/)
- Manual or specification: [etcd API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [Cloudflare: consensus and coordination](https://raft.github.io/)
- Hands-on guide: [etcd: interact with the API](https://etcd.io/docs/v3.6/tasks/)
