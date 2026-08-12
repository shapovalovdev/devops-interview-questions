---
title: Measure platform adoption
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, adoption, product-management, internal-developer-platform]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
    source_type: standard
    verified_on: 2026-08-11
---

# Measure platform adoption

Leadership asks for an adoption number for the platform. What do you count, and what does the number let you conclude?

## Answer guide

- Define the unit before the number. "Teams onboarded" is the weakest possible measure because it counts a one-time event; count instead the share of *workloads on the paved road* and the share of *activity flowing through it* — deploys made via the platform pipeline versus outside it, services whose runtime is platform-managed, repositories created from a template that are still using it. Report the denominator explicitly, because "80% adoption" over an eligible set that excludes every hard service is a statement about the exclusion, not the platform.
- Instrument adoption from platform telemetry rather than a spreadsheet: the catalog gives you the entity list and its owners, the control plane gives you which entities it actually reconciles, and the pipeline gives you the event stream. That combination lets you compute depth as well as breadth — a team that scaffolds through the platform but deploys with its own scripts is one capability adopted out of four, and a per-capability funnel shows exactly where teams drop off. The CNCF platform engineering maturity model treats this measurement discipline as an axis in its own right, moving from anecdote to instrumented product signals.
- Constraints on interpretation: adoption is a proxy for value only when it is voluntary. Under a mandate the number tells you the mandate was enforced and nothing else, so a mandated platform needs satisfaction and support-demand measures to recover the signal. Segment by team type — a mobile team, a data team and a batch team have different eligible surfaces — and separate new workloads (leading indicator) from migrated ones (lagging). Note that this is adoption of *your* product, distinct from delivery-outcome measurement, which is a separate question and a different data set.
- Failure modes: counting a team as adopted at first login; a percentage that rises purely because the eligible set shrank when legacy services were reclassified; ignoring partial adoption and abandonment, so a team that migrated off is still in the total; and using the number as a target for individual platform engineers, which reliably produces onboarding pushed onto teams who did not want it.

## References

- [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Further reading (blog): [Google Cloud application development blog](https://cloud.google.com/blog/products/application-development)

## What to learn next

- Official documentation: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Manual or specification: [Backstage software catalog system model](https://backstage.io/docs/features/software-catalog/system-model)
- Maintainer or personal blog: [Nicole Forsgren](https://nicolefv.com/)
- Technical blog: [Google Cloud application development blog](https://cloud.google.com/blog/products/application-development)
- Hands-on guide: [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
