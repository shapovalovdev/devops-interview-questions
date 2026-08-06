---
title: Use fencing tokens to prevent stale writers
theme: distributed-systems
difficulty: middle
type: scenario
tags: [reliability, security, databases]
sources:
  - url: https://etcd.io/docs/v3.6/learning/api/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use fencing tokens to prevent stale writers

How do fencing tokens make a lock safer when a previous lock holder resumes late?

## Answer guide

- Issue a monotonically increasing token whenever ownership is granted, and require the protected resource to persist and reject tokens older than the latest accepted token. The token protects the resource even if an old client believes its lease remains valid.
- Store the token comparison at the point of side effect, not only in the lock client. Define the resource boundary, token durability, failover behavior, and whether a multi-step operation needs one transaction or compensating recovery.
- Leases and heartbeats can expire while a process is paused or partitioned. Without downstream fencing, a stale writer can overwrite a newer owner after reconnecting; logging only the lock state will not repair an already-applied effect.

## References

- [etcd: API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Further reading (personal blog): [Martin Kleppmann: distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)

## What to learn next

- Official documentation: [etcd leases](https://etcd.io/docs/v3.6/learning/api/#lease-api)
- Manual or specification: [etcd API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [AWS Builders' Library: avoiding fallback](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/)
- Hands-on guide: [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
