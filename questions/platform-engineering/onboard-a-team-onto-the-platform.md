---
title: Onboard a team onto the platform
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, onboarding, adoption, developer-experience]
sources:
  - url: https://backstage.io/docs/overview/adopting
    source_type: official-docs
    verified_on: 2026-08-11
---

# Onboard a team onto the platform

A new product team is joining the platform next sprint. What does onboarding look like, and what do you measure?

## Answer guide

- Design onboarding around one measurable outcome: time from "a new engineer has a laptop" to "their change is serving production traffic". Work backwards from that to the steps — access and group membership, the scaffolded repository, a running non-production instance, a first merged and deployed change, an alert routed to the right rotation, and the cost tag that makes the workload visible in the bill. Anything on that path that requires a human decision is where the clock stops, so those are the items to automate first.
- Run it as a paired activity for the first few teams rather than a document handoff. The Backstage adoption guidance makes the same point structurally: start with a small set of real components and real owners rather than a big-bang import, because the friction you discover with two teams is the friction eighty teams will hit. Record every question the team asks; a repeated question is a defect in the defaults or the documentation, not a training gap.
- Constraints: onboarding cost is platform capacity, and it does not scale linearly if it stays manual, so track how much platform-engineer time each new team consumes and treat a flat or rising number as a signal to invest in automation. New teams also arrive with existing services, so onboarding must cover importing a running workload, not only greenfield scaffolding. Access provisioning usually depends on identity and HR systems the platform team does not own — get that dependency named early, because it is the most common source of a two-week delay.
- Failure modes: an onboarding checklist that is accurate for the first team and stale by the third; a "day one" experience that ends at a running hello-world and leaves the team to discover on-call, cost and compliance obligations later; treating onboarding as complete at the first deploy rather than at the first successfully handled incident; and no follow-up, so a team that quietly stalls halfway is counted as onboarded in the adoption report.

## References

- [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
- Further reading (blog): [Spotify engineering blog](https://engineering.atspotify.com/)

## What to learn next

- Official documentation: [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
- Manual or specification: [Backstage software catalog system model](https://backstage.io/docs/features/software-catalog/system-model)
- Maintainer or personal blog: [Nicole Forsgren](https://nicolefv.com/)
- Technical blog: [Spotify engineering blog](https://engineering.atspotify.com/)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)
