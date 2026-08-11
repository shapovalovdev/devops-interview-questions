---
title: Justify continued platform investment
theme: platform-engineering
difficulty: staff
type: scenario
tags: [platform-engineering, cost-optimization, leadership, product-management]
sources:
  - url: https://dora.dev/research/2024/dora-report/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Justify continued platform investment

Two years in, a CFO asks what the platform team's eight engineers have returned. What do you present?

## Answer guide

- Present a case built on three separable claims, each with its own evidence, because they fail differently. First, cost avoided: infrastructure spend per workload before and after standardisation, duplicated tooling retired, and the engineer-hours that used to go into work the platform now does once. Second, capability delivered: things that were previously impossible or required a specialist, such as a new service reaching production in a day, or a fleet-wide dependency upgrade completed in a week. Third, risk reduced: patch coverage, audit evidence produced automatically, and the shrinking tail of unowned or unpatched systems.
- Be careful and explicit about the delivery-outcome argument. The DORA research provides population-level evidence that platform engineering is associated with better outcomes, and the 2024 report is unusually useful precisely because it also reports the friction — the finding that platform adoption is not uniformly positive on every measure, including some throughput and stability effects during transition. Presenting that nuance yourself is what makes the rest of your numbers credible; a slide claiming your platform caused a delivery improvement, with no counterfactual and no cost, will be read as advocacy.
- Constraints on the argument: you cannot run a control group, so use cohort comparisons (migrated versus not-yet-migrated, matched on service type) and be honest that they are observational. Convert to money only where the conversion is defensible — hours saved times a loaded rate is a soft number and a hostile reader knows it, whereas a decommissioned licence is hard. Include your own total cost: eight salaries plus the platform's own infrastructure. And frame the counterfactual concretely — without the platform, these forty teams each maintain their own deployment tooling — because that is the real alternative, not zero spend.
- Failure modes: claiming savings for engineer time that was never reallocated to anything; attributing a company-wide delivery trend to the platform when a reorganisation or a hiring wave explains it better; presenting adoption as if it were value; hiding the transition dip so that the first person who finds it discredits the whole case; and having no answer to "what would you cut first", which is the question actually being asked.

## References

- [DORA — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)
- Further reading (blog): [Google Cloud DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)

## What to learn next

- Official documentation: [DORA research library](https://dora.dev/research/)
- Manual or specification: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Maintainer or personal blog: [Nicole Forsgren](https://nicolefv.com/)
- Technical blog: [Google Cloud DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [DORA capability catalog](https://dora.dev/capabilities/)
