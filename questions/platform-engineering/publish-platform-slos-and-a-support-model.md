---
title: Publish platform SLOs and a support model
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, slo, reliability, internal-developer-platform]
sources:
  - url: https://sre.google/workbook/implementing-slos/
    source_type: standard
    verified_on: 2026-08-11
---

# Publish platform SLOs and a support model

Teams say the platform is unreliable; the platform team says it is fine. What do you publish to settle the argument?

## Answer guide

- Publish objectives on the journeys teams actually depend on, plus the support model that says what happens when one is missed. For a platform that means separate objectives per capability and per operation class, because "the platform" is not one service: time from template submission to a working repository, control-plane API availability and latency, build queue wait, secret retrieval availability, and — critically — whether a running workload keeps serving while the platform's control plane is down. Availability of the data plane and availability of the control plane are different promises and must be stated separately.
- Follow the SRE workbook's construction: an SLI as a ratio of good events to valid events with the qualifying conditions written down, an SLO as a target over a stated window, and an error budget as the permitted shortfall that governs how much change the platform pushes. Then attach the support model — a published tier for each capability, the hours it is covered, the response expectation for an outage versus a request, the escalation path, and the office-hours or enablement channel for everything that is not an outage.
- Constraints: your SLI must be measured where the developer experiences it, not inside your own service, so a queue wait or template run is measured end to end including the parts you delegate. Do not promise a tier you cannot staff — a 24/7 objective on a capability owned by a five-person team with no follow-the-sun rotation is a promise to page one person forever. Objectives for capabilities you resell from a cloud provider cannot exceed what that provider offers, so state the dependency explicitly.
- Failure modes: an aggregate uptime number that stays green while the one action teams care about is broken; measuring only successful requests, so a total outage that returns no requests looks like perfect availability; no error-budget consequence, so a missed objective changes nothing; a support model that exists in a document but not in the on-call rota; and objectives set from what the platform currently achieves rather than from what consuming teams need to meet their own.

## References

- [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Further reading (blog): [Google Cloud DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)

## What to learn next

- Official documentation: [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Manual or specification: [Google SRE book — service level objectives](https://sre.google/sre-book/service-level-objectives/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Google Cloud DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google SRE workbook — error budget policy](https://sre.google/workbook/error-budget-policy/)
