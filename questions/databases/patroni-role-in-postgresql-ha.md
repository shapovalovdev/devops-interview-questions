---
title: Explain what Patroni does for PostgreSQL high availability
theme: databases
difficulty: middle
type: theory
tags: [databases, postgresql, patroni, availability]
sources:
  - url: https://patroni.readthedocs.io/en/latest/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.postgresql.org/docs/current/high-availability.html
    source_type: official-docs
    verified_on: 2026-08-17
---

# Explain what Patroni does for PostgreSQL high availability

What problem does Patroni solve that PostgreSQL streaming replication alone does not?

## Answer guide

- Patroni is a cluster manager for PostgreSQL: it wraps an existing primary-with-replicas topology with automated leader election, health checks, controlled promotion, and a single authoritative cluster state stored in a distributed configuration store (DCS) such as etcd, Consul, or ZooKeeper. PostgreSQL itself ships replication but no built-in quorum or promotion brain, which is the gap Patroni fills.
- The DCS holds the cluster leader key; every node periodically updates its health and the leader periodically renews its key. When the primary fails to renew, the remaining nodes elect the most advanced replica, promote it, and fence the old primary from client traffic (via watchdog, REST API checks, or proxy reconfiguration such as HAProxy consulting Patroni health endpoints).
- Operationally, Patroni also automates rolling restarts and upgrades, keeps `postgresql.conf` and replication parameters in one place (the DCS-merged configuration), and rejoining a former primary as a replica, which are the repetitive tasks that fail at 3 a.m. when done by hand.
- Concepts port across engines: the leader-key-and-quorum pattern mirrors MongoDB replica set elections or ScyllaDB raft-based topology, and MySQL solves the same promotion problem differently in InnoDB Cluster's group replication layer — understanding Patroni is understanding distributed database control planes in general, with PostgreSQL-specific mechanics underneath.

## References

- [Patroni documentation](https://patroni.readthedocs.io/en/latest/)
- [PostgreSQL documentation: high availability, load balancing, and replication](https://www.postgresql.org/docs/current/high-availability.html)
- Further reading (blog): [Percona database engineering blog: PostgreSQL high availability topics](https://www.percona.com/blog/)

## What to learn next

- Official documentation: [Patroni documentation](https://patroni.readthedocs.io/en/latest/)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Percona engineering blog: PostgreSQL HA and Patroni articles](https://www.percona.com/blog/)
- Technical blog: [pganalyze — PostgreSQL replication articles](https://pganalyze.com/blog)
- Hands-on guide: [Patroni source repository with sample configurations](https://github.com/patroni/patroni)
