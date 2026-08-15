# Distributed systems: related materials

Use these materials to connect the Questions to primary documentation and practical operations. The free Google SRE Book is available online lawfully from its publisher; do not redistribute commercial books or exam material.

## What to learn next

- Official documentation: [etcd learning guides](https://etcd.io/docs/v3.6/learning/)
- Manual or specification: [RFC index](https://www.rfc-editor.org/rfc-index.html)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

This Theme is the failure-and-consistency spine the backend and SRE paths
share, and its order is earned rather than chosen. Timeouts, retries, and
backoff come first because everything later either retries or survives a
retried caller; idempotent writes and circuit breakers follow in that order,
and load shedding closes the failure stage by protecting the service instead of
the dependency. Delivery comes next — at-least-once consumption, dead-letter
queues, event-schema evolution, the outbox, saga compensation — each assuming
the retry and idempotency vocabulary from the opening. Then the replication
ladder, each rung defined against the one below it: consistency and
availability, leader election, quorum design, fencing tokens, replication lag,
read-your-writes, linearizable reads. Clock skew belongs at leader election,
anti-entropy repair at replication, and service discovery with client load
balancing once retries exist to hide transient failures. Finish with the
operational tier — multi-region failover, the cross-service consistency
incident, high-risk state changes, tenant fairness, and end-to-end
data-integrity controls — staff-level precisely because they spend the whole
ladder.
