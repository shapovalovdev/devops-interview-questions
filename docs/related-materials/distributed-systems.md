# Distributed systems: related materials

Use these materials to connect the Questions to primary documentation and practical operations. The free Google SRE Book is available online lawfully from its publisher; do not redistribute commercial books or exam material.

## What to learn next

- Official documentation: [etcd learning guides](https://etcd.io/docs/v3.6/learning/)
- Manual or specification: [RFC index](https://www.rfc-editor.org/rfc-index.html)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

This is the failure-and-consistency spine the backend and SRE paths share, and
its order is earned rather than chosen.

1. [Choose timeouts, retries, and backoff](../../questions/distributed-systems/timeouts-retries-backoff.html)
    — Everything later either retries or survives a retried caller, so deadlines
    and backoff come first.
2. [Make a retried write idempotent](../../questions/distributed-systems/idempotent-operations.html)
    — A retry is only safe advice when the repeated write is safe, so
    idempotency follows immediately.
3. [Use a circuit breaker without masking failure](../../questions/distributed-systems/circuit-breakers.html)
    — The breaker protects the dependency the retries above would happily
    hammer.
4. [Shed load to preserve a critical service](../../questions/distributed-systems/load-shedding.html)
    — Shedding closes the failure stage by protecting the service instead of the
    dependency.
5. [Design service discovery and client load balancing](../../questions/distributed-systems/service-discovery.html)
    — Discovery with client load balancing earns its place once retries exist to
    hide transient failures.
6. [Consume an at-least-once event stream safely](../../questions/distributed-systems/at-least-once-delivery.html)
    — Delivery opens the transport tier by assuming the duplicates the failure
    stage created.
7. [Operate a dead-letter queue](../../questions/distributed-systems/dead-letter-queues.html)
    — Dead-lettering contains the poison messages the delivery tier now admits.
8. [Evolve an event schema safely](../../questions/distributed-systems/schema-evolution.html)
    — Schema evolution keeps events flowing across versions of every producer
    and consumer.
9. [Apply the transactional outbox pattern](../../questions/distributed-systems/outbox-pattern.html)
    — The outbox resolves the dual-write the transaction and delivery tiers
    exposed on purpose.
10. [Coordinate a multi-service saga](../../questions/distributed-systems/saga-compensation.html)
    — Compensation extends the outbox's guarantees across multi-service
    workflows.
11. [Explain consistency and availability during a network partition](../../questions/distributed-systems/consistency-and-availability.html)
    — The replication ladder opens with the partition decision every rung below
    hangs from.
12. [Explain safe leader election](../../questions/distributed-systems/leader-election.html)
    — Leadership is the first mechanism the partition decision actually needs.
13. [Handle clock skew in a distributed service](../../questions/distributed-systems/clock-skew.html)
    — Clock skew belongs at leader election because both are
    trust-in-coordination problems.
14. [Design a quorum for replicated writes](../../questions/distributed-systems/quorum-basics.html)
    — Quorums carry the committed position through the membership the election
    produced.
15. [Use fencing tokens to prevent stale writers](../../questions/distributed-systems/fencing-tokens.html)
    — Fencing makes the stale writer visible and rejectable at the point of side
    effect.
16. [Plan anti-entropy repair](../../questions/distributed-systems/anti-entropy-repair.html)
    — Anti-entropy repair is the replication tier's own healing mechanism,
    defined against replication itself.
17. [Diagnose replication lag](../../questions/distributed-systems/replication-lag.html)
    — Lag is the operational face of the replication the ladder just built.
18. [Provide read-your-writes consistency](../../questions/distributed-systems/read-your-writes.html)
    — Read-your-writes is the user-facing promise extracted from measured lag.
19. [Choose a linearizable read](../../questions/distributed-systems/linearizable-read.html)
    — The linearizable read tops the guarantee ladder and prices it honestly in
    latency.
20. [Design multi-region failover](../../questions/distributed-systems/multi-region-failover.html)
    — The operational tier opens by spending the whole ladder across regions.
21. [Lead a cross-service consistency incident](../../questions/distributed-systems/incident-command.html)
    — The cross-service consistency incident is the ladder breaking in public.
22. [Govern a high-risk distributed state change](../../questions/distributed-systems/change-safety.html)
    — High-risk state changes govern the mutations the ladder made possible.
23. [Protect tenant fairness in a shared distributed platform](../../questions/distributed-systems/tenant-fairness.html)
    — Tenant fairness protects the shared platforms the ladder now underpins.
24. [Establish data-integrity controls across services](../../questions/distributed-systems/data-integrity.html)
    — End-to-end data-integrity controls are the staff capstone consuming every
    mechanism above at once.
