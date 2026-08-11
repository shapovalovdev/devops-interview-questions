---
title: Scope what the platform owns
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, internal-developer-platform, architecture, governance]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platforms/
    source_type: standard
    verified_on: 2026-08-11
---

# Scope what the platform owns

Four teams each ask the platform team to take over a different piece of their stack. How do you decide what the platform owns and what it refuses?

## Answer guide

- Apply a single test to each request: is this capability needed by many teams, is it undifferentiated for them, and can the platform expose it behind a stable interface without needing to know the application's domain? A request that fails the last part — "run our nightly reconciliation job and fix it when the business rules change" — is application work wearing platform clothing, and accepting it puts domain knowledge the platform team does not have on the platform's pager.
- Draw the boundary at the interface, not at the technology. The CNCF white paper's split of capability providers from platform interfaces gives the practical shape: the platform owns the contract (what you can ask for, what is guaranteed, what is versioned) and the implementation behind it, while the consuming team owns everything expressed through that contract. So the platform owns "a Postgres instance with backup, patching and a connection secret"; the team owns its schema, its queries, and its migrations.
- Constraints to state explicitly when you say yes: the support model and hours, what the platform will and will not change without notice, the escape hatch for teams whose need the interface cannot express, and the cost of ownership in platform headcount. Say no with an alternative — a reference implementation, a shared library, or an enablement pairing — rather than a flat refusal, because an unmet need becomes a shadow platform in some team's repository.
- Failure modes: accepting one team's bespoke requirement and discovering it now blocks every future change to the interface; taking the operational burden without the authority to change the design that causes it; a boundary defined by team names rather than by contract, so responsibility shifts every reorganisation; and scope that only ever grows, because nothing was ever written down as out of scope.

## References

- [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Further reading (blog): [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)

## What to learn next

- Official documentation: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Manual or specification: [Team Topologies key concepts](https://teamtopologies.com/key-concepts)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Crossplane — get started with composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition/)
