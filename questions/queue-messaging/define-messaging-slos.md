---
title: Define messaging platform SLOs
theme: queue-messaging
difficulty: staff
type: scenario
tags: [kafka, rabbitmq, message-queues, observability, reliability, governance]
sources:
  - url: https://kafka.apache.org/documentation/#basic_ops_monitoring
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/monitoring
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define messaging platform SLOs

Which SLOs make a shared messaging platform useful without promising business outcomes it cannot control?

## Answer guide

- Separate platform SLOs—authenticated publish/consume availability, broker durability boundaries, latency, and recovery—from application SLOs such as end-to-end order completion. Define event age and backlog objectives jointly where the platform exposes the data.
- Use indicators such as publish failures, replication/quorum health, consumer lag or queue age, disk headroom, and control-plane error rate. Slice by tenant and criticality so one noisy workload cannot hide another's failure.
- Avoid alerting only on CPU or message count: a low backlog can still mean dropped publishing, and a large backlog may be an intentional batch. Error budgets should drive capacity and change decisions, not blame consumers for every downstream outage.

## References

- [Apache Kafka monitoring](https://kafka.apache.org/documentation/#basic_ops_monitoring)
- [RabbitMQ monitoring](https://www.rabbitmq.com/docs/monitoring)
- Further reading (blog): [Monitoring Kafka](https://www.confluent.io/blog/monitor-kafka-cluster-with-prometheus-grafana/)
