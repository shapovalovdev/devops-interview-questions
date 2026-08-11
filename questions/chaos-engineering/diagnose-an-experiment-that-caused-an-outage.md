---
title: Diagnose an experiment that caused a real outage
theme: chaos-engineering
difficulty: senior
type: troubleshooting
tags: [chaos-engineering, incident-response, blast-radius, troubleshooting]
sources:
  - url: https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Diagnose an experiment that caused a real outage

A scoped experiment escalated into a customer-visible outage. Walk through the response and the follow-up.

## Answer guide

- Handle it as an incident, not as an experiment that went long. Halt the injection, declare the incident with the normal severity process, hand incident command to the usual responder, and state clearly in the channel that a chaos experiment was running and has been stopped — responders who do not know that will chase a phantom root cause. Preserve the experiment definition, its start and stop timestamps, and the tool's audit log before anything is cleaned up.
- Then establish whether stopping the fault restored service. If it did, the escalation path was through the fault; if it did not, the experiment triggered a state change — a failover that has not failed back, a cache that was poisoned, a queue that has backed up, an autoscaler that scaled the wrong way, a circuit breaker stuck open — and recovery needs its own explicit action. Verify recovery against the same steady-state metric the hypothesis named.
- In the review, separate two questions that people routinely merge. First, why did the system fail this badly — that is the genuine finding, and it would have surfaced during a real event with worse timing. Second, why did the controls not contain it: was the selector broader than intended, the stop condition bound to a slow or missing metric, the abort path dependent on the failing component, or the blast radius widened without re-checking the smaller scope? Both produce action items, but only the second is a defect in the practice.
- Failure modes to avoid afterwards: banning chaos engineering outright, which discards the finding and keeps the weakness; blaming the operator instead of the control design; and skipping the re-run after the fix, so nobody ever learns whether the system now survives the fault. Tighten scope and stop conditions, then run the same experiment again at the smallest scope and work back up.

## References

- [AWS Fault Injection Service stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [AWS Fault Injection Service stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html)
- Manual or specification: [Chaos Mesh — define the scope of a chaos experiment](https://chaos-mesh.org/docs/define-chaos-experiment-scope/)
- Maintainer or personal blog: [John Allspaw — Kitchen Soap](https://www.kitchensoap.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [Google SRE book — managing incidents](https://sre.google/sre-book/managing-incidents/)
