---
title: Consolidate two competing internal platforms
theme: platform-engineering
difficulty: staff
type: scenario
tags: [platform-engineering, migration, governance, internal-developer-platform]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
    source_type: standard
    verified_on: 2026-08-11
---

# Consolidate two competing internal platforms

After an acquisition you have two internal platforms with overlapping capabilities and two teams that each believe theirs should win. How do you resolve it?

## Answer guide

- Separate the question into three that can be answered independently: which *interface* survives (what developers write and learn), which *implementation* survives per capability (what runs underneath), and which *team* owns the result. Conflating them is what makes the decision political, because "our platform wins" is heard as "your team loses". In practice the best outcome is often one interface, a mixed set of implementations chosen capability by capability on technical merit, and one team formed from both — and saying that structure out loud early changes the conversation from a contest into a design problem.
- Decide on evidence, with the criteria agreed before anyone knows which platform they favour: number and criticality of workloads on each, migration cost in each direction, operational maturity measured against something neutral like the CNCF maturity model's axes, the compliance posture each already satisfies, and how many engineers currently know each system. Weight migration cost heavily and asymmetrically — moving two hundred workloads off platform A to reach a marginally better platform B is rarely worth it, and "the technically better platform" is the wrong tiebreaker when the population sizes differ by an order of magnitude.
- Constraints: an acquisition brings contractual, data-residency and audit obligations that may make one platform non-negotiable for a subset of workloads, so establish that before the technical comparison. Plan for a long coexistence — both platforms will run for a year or more — which means a shared identity, catalog and cost view across both from early on, so the organization has one picture even while it has two systems. Retain the losing platform's key engineers deliberately; they hold the operational knowledge of the workloads you are about to migrate, and they are the most likely to leave.
- Failure modes: a "best of both" merge that builds a third platform nobody asked for while both originals keep running; deciding by seniority of sponsor and then discovering the migration cost afterwards; declaring a winner without funding the migration, so the loser becomes a permanent unowned legacy; letting each side keep a parallel golden path "temporarily", which fixes the split permanently; and spending the consolidation budget on interface unification while the two underlying control planes, and their two on-call rotations, both survive.

## References

- [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Further reading (blog): [CNCF blog](https://www.cncf.io/blog/)

## What to learn next

- Official documentation: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Manual or specification: [Backstage software catalog system model](https://backstage.io/docs/features/software-catalog/system-model)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
