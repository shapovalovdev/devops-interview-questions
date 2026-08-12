---
title: Choose between mandated and voluntary adoption
theme: platform-engineering
difficulty: staff
type: scenario
tags: [platform-engineering, adoption, governance, leadership]
sources:
  - url: https://dora.dev/capabilities/platform-engineering/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Choose between mandated and voluntary adoption

Adoption has stalled at sixty per cent and leadership offers to mandate the platform. Do you take the mandate?

## Answer guide

- Answer by first finding out *why* the remaining forty per cent have not moved, because a mandate is a valid instrument for one of those reasons and destructive for the others. If teams have not moved because migration is unfunded and nothing forces prioritisation, a mandate with funding and a date works. If they have not moved because the platform genuinely does not serve their workload, a mandate converts a product gap into a compliance problem, and you will spend the next year building exceptions. The DORA platform-engineering capability material is explicit that adoption should be earned through a platform teams choose, and that treating internal users as a captive audience removes the feedback that keeps the product honest.
- The defensible middle position is: mandate the outcome, not the tool. Require the properties — deployments are auditable, secrets are not in repositories, workloads have an owner and an SLO, patching happens within N days — and make the platform overwhelmingly the cheapest way to satisfy them. Teams that meet the requirements another way are compliant, which keeps the pressure on your product to be the easy route rather than the required one, and gives you a real comparison when someone does it better.
- Constraints if you do accept a mandate: it must come with funded migration capacity, a date derived from the tail's actual cost, a named exception authority, and a written scope for what is *not* mandated. Accept it only when the platform is demonstrably ready for the workload classes being mandated — do not accept it as a way to force the roadmap. And change your measurement at the same time: once adoption is compelled it stops being evidence of value, so satisfaction, support demand, and escape-hatch usage become the signals that tell you whether the product is good.
- Failure modes: a mandate announced without funding, which produces compliance theatre and shadow systems; the platform team becoming the enforcement body, which destroys the collaborative relationship it needs to do product discovery; exceptions granted by whoever escalates hardest, which teaches everyone that escalation is the process; a mandate that stops at "must be on the platform" without saying which capabilities, so teams do the minimum; and celebrating the resulting one-hundred-per-cent number as if it meant the same thing as sixty per cent voluntary did.

## References

- [DORA — platform engineering capability](https://dora.dev/capabilities/platform-engineering/)
- Further reading (blog): [Google Cloud application development blog](https://cloud.google.com/blog/products/application-development)

## What to learn next

- Official documentation: [DORA — platform engineering capability](https://dora.dev/capabilities/platform-engineering/)
- Manual or specification: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Maintainer or personal blog: [Nicole Forsgren](https://nicolefv.com/)
- Technical blog: [Google Cloud application development blog](https://cloud.google.com/blog/products/application-development)
- Hands-on guide: [DORA capability catalog](https://dora.dev/capabilities/)
