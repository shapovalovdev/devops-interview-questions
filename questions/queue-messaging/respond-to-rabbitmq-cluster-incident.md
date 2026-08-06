---
title: Respond to a RabbitMQ cluster incident
theme: queue-messaging
difficulty: senior
type: troubleshooting
tags: [rabbitmq, message-queues, incident-response, troubleshooting, reliability]
sources:
  - url: https://www.rabbitmq.com/docs/clustering
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/quorum-queues
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to a RabbitMQ cluster incident

During a node outage, publishers time out and a quorum queue has no leader. What is the safe incident approach?

## Answer guide

- Establish node, network, disk, and quorum health before changing topology. A quorum queue needs a majority of replicas to elect a leader; restore a safe majority or follow the documented recovery procedure rather than force-starting competing copies.
- Protect producers with confirms and bounded retries, and protect consumers from duplicate work through idempotency. Pause nonessential traffic if backlog or disk alarms threaten the cluster.
- Do not delete queue data or reset nodes just to clear alarms: that may convert an availability incident into data loss. Record the failure domain and validate recovery with publish/consume and backlog checks.

## References

- [RabbitMQ clustering](https://www.rabbitmq.com/docs/clustering)
- [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues)
- Further reading (blog): [RabbitMQ quorum queue recovery](https://www.rabbitmq.com/blog/2020/04/20/rabbitmq-3.8.3-quorum-queue-improvements)
