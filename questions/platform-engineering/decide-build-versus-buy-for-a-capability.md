---
title: Decide build versus buy for a capability
theme: platform-engineering
difficulty: senior
type: scenario
tags: [platform-engineering, build-vs-buy, cost-optimization, architecture]
sources:
  - url: https://learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering
    source_type: official-docs
    verified_on: 2026-08-11
---

# Decide build versus buy for a capability

The platform needs a secrets manager, a feature-flag service, and a developer portal. How do you decide which to build and which to buy?

## Answer guide

- Decide per capability against one question: is this capability differentiating for your organization? Almost nothing in a platform is — secrets storage, flag evaluation, and portal rendering are solved problems where a vendor or upstream project has spent more engineering years than you can. Build only where your requirement is genuinely unusual (a regulatory constraint no product satisfies, an integration with an internal system no vendor will ever support) or where the capability is the thin glue that binds the bought pieces to your organization's specific model. That glue — the abstraction, the catalog conventions, the golden paths — is where a platform team's differentiated work actually lives.
- The honest comparison is total cost of ownership over three to five years, not licence versus zero. Against a vendor's price, put your build's ongoing cost: on-call for it, security patching, upgrades, the feature backlog it will accumulate, documentation, and the opportunity cost of the roadmap it displaces. Against the vendor, put the costs people forget: integration and identity work, data egress, per-seat growth as headcount grows, the migration cost if you leave, and the fact that a bought capability still needs a platform owner. Adopting open source is a third option with its own arithmetic — no licence, but you own operations and the upgrade treadmill.
- Constraints that should be decisive rather than advisory: whether the capability sits on the critical path of production traffic or only of changes; whether your data can legally sit in the vendor's tenancy; whether an exit is possible, which means checking for an export path and an open interface before signing, not after; and whether you have the staffing to operate what you build at the availability you would promise. Prefer options with a standard interface — OpenFeature for flags, OpenTelemetry for signals — so the swap cost is bounded.
- Failure modes: building because the team wants to, dressed up as a requirements gap; buying and then wrapping it in so much custom integration that you own a fork anyway; a proof of concept that skipped scale, identity federation and audit, which are where these products actually differ; ignoring the internal politics of a capability another team already runs badly; and the reverse mistake of buying a portal without deciding what content and ownership model goes into it, which produces an expensive empty catalog.

## References

- [Microsoft — what is platform engineering](https://learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering)
- Further reading (blog): [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)

## What to learn next

- Official documentation: [Microsoft — what is platform engineering](https://learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering)
- Manual or specification: [OpenFeature specification and reference](https://openfeature.dev/docs/reference/intro/)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)
