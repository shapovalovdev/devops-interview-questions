---
title: Plan a migration onto the paved road
theme: platform-engineering
difficulty: senior
type: scenario
tags: [platform-engineering, migration, golden-path, adoption]
sources:
  - url: https://sre.google/sre-book/reliable-product-launches/
    source_type: standard
    verified_on: 2026-08-11
---

# Plan a migration onto the paved road

Eighty existing services need to move from a legacy deployment system onto the new platform. How do you plan and sequence it?

## Answer guide

- Start by refusing to treat the eighty as one population. Inventory and classify them by the properties that actually determine migration cost — stateless versus stateful, has an owning team versus orphaned, in active development versus frozen, standard HTTP versus something exotic — and you will typically find three groups: a large majority that a scripted conversion handles, a middle band needing a day of human work each, and a tail of five to ten specials that will consume more effort than the rest combined. Plan the majority as a repeatable pipeline and the tail as individually scoped projects; do not average them into one estimate.
- Sequence to build evidence and momentum: migrate one service you own end to end, then two willing teams, then a cohort, publishing a launch checklist that captures everything each wave discovered — the way a launch coordination checklist accumulates the failure modes previous launches found. Automate the conversion itself (a tool that reads the legacy descriptor and emits the platform manifest) rather than writing a migration guide, because eighty hand-migrations produce eighty subtly different results. Run both systems in parallel per service with a fast, tested rollback until the service has survived a real production week.
- Constraints: the migration must be worth it to the migrating team, not only to the platform team, so lead with a capability they want and be honest about what they lose. Freeze the legacy system to new services on day one, or you will be migrating a moving target. Budget platform capacity explicitly — if the platform team is also the migration team, its roadmap stops — and set a policy for the tail in advance: which specials get bespoke platform support, which are exempted permanently, and which are decommissioned instead of migrated.
- Failure modes: a top-down deadline with no automation, which converts into eighty simultaneous escalations in the final month; discovering mid-migration that a shared dependency (an internal DNS convention, a mutual TLS trust store, a database firewall rule) assumed the legacy environment; orphaned services with no owner blocking the shutdown because nobody can approve their downtime; parallel running for so long that both systems must be maintained indefinitely; and declaring success at ninety-five per cent while the legacy system stays alive for the remaining four services, so none of the projected savings arrive.

## References

- [Google SRE book — reliable product launches at scale](https://sre.google/sre-book/reliable-product-launches/)
- Further reading (blog): [GitLab blog](https://about.gitlab.com/blog/)

## What to learn next

- Official documentation: [Google SRE book — reliable product launches at scale](https://sre.google/sre-book/reliable-product-launches/)
- Manual or specification: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Maintainer or personal blog: [Matthew Skelton — blog](https://blog.matthewskelton.net/)
- Technical blog: [GitLab blog](https://about.gitlab.com/blog/)
- Hands-on guide: [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
