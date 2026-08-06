---
title: Set platform and product-service boundaries
theme: backend-architecture
difficulty: staff
type: scenario
tags: [platform-engineering, governance, dependencies, cnpa]
sources:
  - url: https://sre.google/workbook/platform-engineering.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set platform and product-service boundaries

How should a staff engineer decide which backend capabilities belong on a shared platform?

## Answer guide

- Put broadly repeated, security-sensitive, or operationally expensive capabilities behind a product-like platform interface when it has stable consumers and an accountable owner. Keep product-specific domain decisions with the teams that understand their customers and economics.
- Define supported APIs, tenancy, service objectives, onboarding, migration, cost attribution, and an explicit exception path. Measure adoption and developer outcomes rather than judging platform success by the number of abstractions shipped.
- A platform that forces one product model on all teams becomes a delivery bottleneck, while copy-pasted critical controls create inconsistent risk. Start with a thin paved road, maintain escape hatches, and review whether an interface remains worth owning.

## References

- [Google SRE workbook: platform engineering](https://sre.google/workbook/platform-engineering.html)
- Further reading (blog): [Martin Fowler: platforms](https://martinfowler.com/articles/talk-about-platforms.html)

## What to learn next

- Official documentation: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [Spotify Engineering](https://engineering.atspotify.com/)
- Hands-on guide: [Backstage documentation](https://backstage.io/docs/overview/what-is-backstage/)
