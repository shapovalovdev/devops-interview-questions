---
title: Size and staff a platform team
theme: platform-engineering
difficulty: staff
type: scenario
tags: [platform-engineering, leadership, capacity-planning, cost-optimization]
sources:
  - url: https://sre.google/sre-book/eliminating-toil/
    source_type: standard
    verified_on: 2026-08-11
---

# Size and staff a platform team

You are asked how many engineers the platform needs for the next year, and what mix. How do you answer?

## Answer guide

- Build the number from committed load rather than from a ratio. Sum four buckets: operational load (on-call, support requests, incident follow-up), keep-the-lights-on work (upgrades, certificate and dependency churn, provider deprecations you do not control), migration and onboarding work you have already promised, and only what remains is new capability. In most platform teams the first three consume more than half the capacity, which is why a headcount request justified purely by a feature roadmap is always wrong by the time it is approved.
- Use a toil ceiling as the governing constraint, in the spirit of the SRE book's argument that manual, repetitive, automatable work must be capped — commonly at half of a person's time — with the excess turned into engineering that removes it. Measure your actual toil for a quarter before you argue: count support tickets by category, on-call interrupts, and manual steps per onboarding. If toil is above the ceiling, the ask is either headcount or a reduction in committed scope, and stating both options is what makes the request credible.
- The mix matters as much as the count. A platform team needs product and user-research capability (often a part-time product owner rather than an engineer), someone who writes documentation well enough that it is read, deep infrastructure skill for the layer beneath the abstraction, and application-development experience so the interface is designed by someone who has consumed one. Provider deprecations and upgrade cycles are a recurring annual cost that does not shrink with automation, so budget it as a standing line. Also account for on-call viability: a rotation needs a minimum size to be sustainable, which sets a floor beneath any capability argument.
- Failure modes: sizing from a "one platform engineer per N developers" ratio borrowed from a company with a different scope; funding the build and not the run, so year two is spent entirely on maintenance; a team too small to hold a humane rotation, which produces attrition and then an even smaller team; staffing exclusively with infrastructure specialists so the abstraction is designed for its builders; treating onboarding and migration effort as free; and having no plan for what gets dropped if the headcount is refused, which guarantees everything is dropped badly.

## References

- [Google SRE book — eliminating toil](https://sre.google/sre-book/eliminating-toil/)
- Further reading (blog): [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)

## What to learn next

- Official documentation: [Google SRE book — eliminating toil](https://sre.google/sre-book/eliminating-toil/)
- Manual or specification: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)
- Hands-on guide: [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
