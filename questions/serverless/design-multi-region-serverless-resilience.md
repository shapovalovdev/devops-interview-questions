---
title: Design multi-region resilience for a serverless application
theme: serverless
difficulty: staff
type: scenario
tags: [cloud, availability, reliability, architecture, incident-response]
sources:
  - url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design multi-region resilience for a serverless application

Leadership asks for a multi-region serverless architecture after a regional incident. What do you build, and what do you tell them it will not fix?

## Answer guide

- Start from objectives, not topology. Fix a recovery time and recovery point objective per business capability, then pick the cheapest pattern that meets them: warm standby with routing failover, active-active with regional data ownership, or backup-and-restore for capabilities that can tolerate hours. Managed functions themselves are trivially reproducible in another region; the hard part is state and identity.
- Data determines the design. Multi-region replication is asynchronous, so an active-active design must decide how conflicts resolve—region-scoped write ownership, last-writer-wins with a defensible clock, or conflict-free structures—and must accept a non-zero recovery point. If the business cannot accept lost writes, you are building warm standby with a controlled failover, not active-active, and you should say so plainly.
- Make failover exercisable. Health checks and routing policy must be able to shift traffic without a code deploy; deployment pipelines must reach every region from one artifact; quotas, reserved concurrency, and warm capacity must be pre-raised in the standby region because a cold region silently throttles under full production load. Event sources, queues, and schedulers need explicit per-region behaviour so failover does not double-process or stop processing.
- State the residual risks honestly: control-plane dependencies concentrated in a home region, an identity or DNS provider that is itself a shared global dependency, a bad deployment or a poison event that replicates to both regions instantly, and correlated failure through a shared third party. Multi-region protects against regional infrastructure failure, not against your own bad change.
- Failure modes to expect: a standby that has never served real traffic and fails on first use, drift between regional configurations, failover runbooks that assume a human can reach a console in the failed region, doubled cost with no tested benefit, and a fallback path that quietly breaks idempotency so a failover produces duplicate customer-visible side effects.

## References

- [AWS Well-Architected reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- Further reading (blog): [AWS Architecture Blog — resilience articles](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [AWS Well-Architected reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- Manual or specification: [Serverless multi-tier architectures whitepaper](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/welcome.html)
- Maintainer or personal blog: [Marc Brooker — availability and failure modes in distributed systems](https://brooker.co.za/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)
