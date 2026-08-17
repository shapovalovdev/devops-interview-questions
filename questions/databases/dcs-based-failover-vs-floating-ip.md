---
title: Justify DCS-based leader election over floating-IP failover
theme: databases
difficulty: senior
type: theory
tags: [databases, postgresql, patroni, distributed-systems, availability]
sources:
  - url: https://patroni.readthedocs.io/en/latest/faq.html
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://etcd.io/docs/v3.5/
    source_type: official-docs
    verified_on: 2026-08-17
---

# Justify DCS-based leader election over floating-IP failover

Why is leader election through a distributed configuration store safer than floating-IP or cron-script failover for a database cluster?

## Answer guide

- A DCS such as etcd gives failover decisions a quorum and a linearizable lease: a candidate becomes leader only by acquiring the leader key, and the old leader loses the key the moment it fails to renew, so two primaries cannot both believe they hold authority. A floating IP move proves only that a network address moved, not that the new holder of the address is the most advanced replica or that the old primary stopped accepting writes.
- Floating-IP and cron-based scripts race against each other: detection runs on a timer, the IP move and the promotion are separate steps with no atomicity, and a network partition leaves both nodes up with the IP on one and the writes on the other. That is the classic split-brain with divergent timelines; reconciliation then means discarding one side's acknowledged writes.
- The DCS pattern also encodes eligibility: Patroni promotes the replica with the least replication lag that can still see the DCS, so a stale replica cannot win an election it would immediately lose data from, and DCS inaccessibility deliberately freezes the cluster instead of guessing — fail-safe beats fail-fast for durable state. MySQL Group Replication reaches the same quorum conclusion inside the server itself (with binlog-based recovery of rejoining members), which shows the pattern is about consensus, not about etcd specifically.
- The trade-off to state honestly is a new critical dependency: the DCS itself must be sized for quorum (three or five nodes) and monitored, and its loss pauses failovers even though the current primary keeps serving reads and writes.

## References

- [Patroni FAQ: how failover and the DCS interact](https://patroni.readthedocs.io/en/latest/faq.html)
- [etcd documentation: what etcd provides](https://etcd.io/docs/v3.5/)
- Further reading (blog): [Percona database engineering blog: PostgreSQL high availability topics](https://www.percona.com/blog/)

## What to learn next

- Official documentation: [Patroni documentation](https://patroni.readthedocs.io/en/latest/)
- Manual or specification: [etcd v3.5 documentation](https://etcd.io/docs/v3.5/)
- Maintainer or personal blog: [etcd project blog](https://etcd.io/blog/)
- Technical blog: [Percona engineering blog: quorum and HA deep dives](https://www.percona.com/blog/)
- Hands-on guide: [etcd clustering operations](https://etcd.io/docs/v3.5/op-guide/)
