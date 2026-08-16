# Queue Messaging: related materials

Use the Apache Kafka and RabbitMQ sources attached to each Question as the
authority for product-specific behaviour. The links below are a stable learning
path for the Theme; individual-author and vendor blogs provide context, not
evidence for factual claims.

## What to learn next

- Official documentation: [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- Manual or specification: [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)
- Maintainer or personal blog: [Matthias J. Sax — Gently Down the Stream](https://www.gentlydownthe.stream/)
- Technical blog: [Redpanda engineering blog](https://www.redpanda.com/blog)
- Hands-on guide: [Confluent Kafka tutorials](https://developer.confluent.io/tutorials/)

## Legal free books

No general-purpose messaging book is listed here: avoid linking unauthorized
copies of commercial titles. The upstream manuals, specifications, and
maintainer-authored articles above are free to read and are the safer starting
point. Add a book only when its publisher explicitly provides it without charge.

## Suggested study order

Semantics, routing, and delivery guarantees before platform mechanics, and the
platform questions — security, recovery, SLOs — last.

1. [Choose a work queue or an event log](../../questions/queue-messaging/choose-a-queue-or-log.html)
    — Queue versus log semantics decide deletion, replay, and ordering before
    any platform is chosen.
2. [Explain RabbitMQ exchanges, bindings, and queues](../../questions/queue-messaging/explain-rabbitmq-routing.html)
    — Routing through exchanges and bindings is the vocabulary of the queue
    side.
3. [Acknowledge RabbitMQ work safely](../../questions/queue-messaging/acknowledge-rabbitmq-work-safely.html)
    — Acknowledgements make at-least-once work safe on the queue side.
4. [Explain at-most-once, at-least-once, and exactly-once claims](../../questions/queue-messaging/explain-delivery-semantics.html)
    — Delivery semantics are end-to-end claims, and exactly-once stops at the
    consumer.
5. [Explain Kafka topics and partitions](../../questions/queue-messaging/explain-kafka-topics-and-partitions.html)
    — Topics and partitions are the log platform's unit of both parallelism and
    ordering.
6. [Preserve required ordering in asynchronous processing](../../questions/queue-messaging/preserve-order-in-async-processing.html)
    — Ordering per key is what partitions make possible, made deliberate here.
7. [Commit Kafka offsets after processing effects](../../questions/queue-messaging/commit-kafka-offsets-after-effects.html)
    — Committing offsets after effects is the smallest dual-write, met before
    any general pattern.
8. [Handle Kafka consumer rebalances safely](../../questions/queue-messaging/handle-kafka-consumer-rebalances.html)
    — Rebalances are the log platform's failure choreography for consumers.
9. [Choose Kafka retention or log compaction](../../questions/queue-messaging/choose-kafka-retention-or-compaction.html)
    — Retention versus compaction is what the log keeps, and for whom.
10. [Manage event schema evolution](../../questions/queue-messaging/manage-event-schema-evolution.html)
    — Schema evolution keeps producers and consumers compatible across time.
11. [Plan Kafka partition capacity](../../questions/queue-messaging/plan-kafka-partition-capacity.html)
    — Partition capacity prices the parallelism everything above assumed.
12. [Design multi-tenant messaging security](../../questions/queue-messaging/design-multi-tenant-messaging-security.html)
    — The platform tier opens with tenants kept apart on shared brokers.
13. [Design Kafka disaster recovery](../../questions/queue-messaging/design-kafka-disaster-recovery.html)
    — Disaster recovery for the log platform replays what retention kept.
14. [Triage Kafka consumer lag](../../questions/queue-messaging/triage-kafka-consumer-lag.html)
    — Consumer lag is the platform's daily symptom, triaged before the worst
    day.
15. [Respond to a RabbitMQ cluster incident](../../questions/queue-messaging/respond-to-rabbitmq-cluster-incident.html)
    — The RabbitMQ cluster incident is the queue side's own worst day.
16. [Define messaging platform SLOs](../../questions/queue-messaging/define-messaging-slos.html)
    — Reliability SLOs close the Theme by promising what the platform delivers.
