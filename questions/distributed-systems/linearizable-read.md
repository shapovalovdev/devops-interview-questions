---
title: Choose a linearizable read
theme: distributed-systems
difficulty: senior
type: theory
tags: [databases, reliability, availability]
sources:
  - url: https://etcd.io/docs/v3.6/learning/api/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a linearizable read

When does a control-plane read need linearizability, and what does that cost?

## Answer guide

- Use a linearizable read when a decision must reflect the latest successfully committed state, such as checking leadership, a lock, quota, or membership before a destructive action. The read is ordered with the replicated log according to the system's documented guarantee.
- Separate this from a local serializable read of a replica, which may be faster but stale. State the required freshness, quorum or leader contact, deadline, and fallback; often a cache is suitable for display data but unsafe for coordination.
- Linearizable reads can become unavailable or slow during quorum loss and add control-plane load. If callers bypass the guarantee under pressure, they reintroduce split-brain; monitor stale-read usage and make degraded behavior a deliberate product decision.

## References

- [etcd: API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Further reading (personal blog): [Aphyr: linearizability](https://aphyr.com/posts/313-strong-consistency-models)

## What to learn next

- Official documentation: [etcd API reference](https://etcd.io/docs/v3.6/dev-guide/api_reference_v3/)
- Manual or specification: [etcd API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [CockroachDB: transaction isolation](https://www.cockroachlabs.com/docs/stable/demo-serializable)
- Hands-on guide: [etcdctl commands](https://etcd.io/docs/v3.6/dev-guide/interacting_v3/)
