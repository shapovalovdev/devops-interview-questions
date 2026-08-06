---
title: Design multi-tenant messaging security
theme: queue-messaging
difficulty: staff
type: scenario
tags: [kafka, rabbitmq, message-queues, security, least-privilege, governance]
sources:
  - url: https://kafka.apache.org/documentation/#security
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/access-control
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design multi-tenant messaging security

What boundaries are needed when several teams share Kafka or RabbitMQ?

## Answer guide

- Authenticate workloads with rotatable identities and authorize least-privilege operations by topic/group or virtual host/resource. Encrypt client and inter-node traffic where required, isolate administrative access, and audit sensitive changes.
- Separate environments and critical tenants through naming, ACLs, quotas, and, when needed, dedicated clusters. Treat event payloads as potentially sensitive: access control does not remove data-classification, retention, or redaction obligations.
- A broad wildcard permission or shared credential can expose every tenant's events. Automate access reviews and test both permitted and denied paths; do not put secrets or raw regulated data in messages merely because the broker is private.

## References

- [Apache Kafka security](https://kafka.apache.org/documentation/#security)
- [RabbitMQ access control](https://www.rabbitmq.com/docs/access-control)
- Further reading (blog): [Kafka security best practices](https://www.confluent.io/blog/apache-kafka-security-authorization-authentication-encryption/)
