---
title: Design a quorum for replicated writes
theme: distributed-systems
difficulty: junior
type: scenario
tags: [availability, reliability, databases]
sources:
  - url: https://etcd.io/docs/v3.6/learning/api/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a quorum for replicated writes

How do read and write quorums prevent two successful operations from observing disjoint replica sets?

## Answer guide

- Choose replica count and acknowledgement thresholds so every successful read quorum intersects every successful write quorum. The intersection carries a value or a committed log position, but it only yields the advertised guarantee when membership and failure assumptions remain valid.
- Define what is acknowledged: durable local log append, replicated commit, or application of state. Measure tail latency and unavailable capacity because larger quorums reduce tolerance for unavailable members and can make a slow replica visible to clients.
- Never change voting membership by editing configuration on several nodes at once. During loss, reconfiguration, or a delayed member rejoining, inconsistent membership or accepting writes without a valid quorum can elect competing leaders and overwrite newer state.

## References

- [etcd: API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Further reading (personal blog): [Marc's Blog: quorum systems](https://brooker.co.za/blog/2014/05/19/lag.html)

## What to learn next

- Official documentation: [etcd runtime reconfiguration](https://etcd.io/docs/v3.6/op-guide/runtime-configuration/)
- Manual or specification: [etcd API guarantees](https://etcd.io/docs/v3.6/learning/api/)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders' Library: avoiding fallback](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/)
- Hands-on guide: [etcd disaster recovery](https://etcd.io/docs/v3.6/op-guide/recovery/)
