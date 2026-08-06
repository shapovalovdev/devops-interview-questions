---
title: Design multi-region failover
theme: distributed-systems
difficulty: staff
type: scenario
tags: [availability, recovery, capacity-planning]
sources:
  - url: https://sre.google/sre-book/managing-critical-state/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design multi-region failover

What evidence and safeguards are required before failing a stateful service over to another region?

## Answer guide

- Define the recovery objective in concrete data-loss and recovery-time terms, then choose replication topology, quorum, DNS or traffic control, and capacity to meet it under a regional failure. Validate that the target has current data, write authority, secrets, dependencies, and tested operational ownership.
- Automate observable preconditions and use staged traffic shifts, fencing, and a decision record. Test both planned and unplanned failover, including return-to-primary, while measuring user outcomes rather than only infrastructure health.
- Dual writes or uncontrolled DNS failover can create two active writers. Replication lag, stale credentials, insufficient standby capacity, and dependencies still pinned to the failed region can turn a failover into a prolonged consistency and availability incident.

## References

- [Google SRE: managing critical state](https://sre.google/sre-book/managing-critical-state/)
- Further reading (personal blog): [Marc Brooker: distributed systems](https://brooker.co.za/blog/)

## What to learn next

- Official documentation: [AWS disaster recovery](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- Manual or specification: [Google SRE: managing critical state](https://sre.google/sre-book/managing-critical-state/)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS Architecture Blog: resilience](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS resilience hub](https://docs.aws.amazon.com/resilience-hub/)
