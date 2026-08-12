---
title: Recognise when a platform team is the wrong answer
theme: platform-engineering
difficulty: staff
type: scenario
tags: [platform-engineering, leadership, team-topologies, architecture]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platforms/
    source_type: standard
    verified_on: 2026-08-11
---

# Recognise when a platform team is the wrong answer

An executive wants to form a platform team. When should you argue against it, and what do you propose instead?

## Answer guide

- Argue against it when the arithmetic does not work or the problem is not a platform problem. A platform earns its cost by amortising work across many consumers, so with three product teams and twenty engineers the platform team consumes a large fraction of capacity to serve a set too small to amortise it — the answer there is shared libraries, a reference implementation, and a well-configured managed service. Argue against it equally when the real problem is a single badly-owned legacy system, an unclear service ownership model, or a quality problem in one team, because standing up a platform will not fix any of those and will add an interface between the problem and the people who could fix it.
- Watch for the tell that this is a reorganisation looking for a rationale: the proposal names the team before naming the users, has no product owner, and is justified by "everyone else has one". A useful counter-proposal is to identify the two or three concrete pieces of extraneous work every team currently repeats and fund exactly those as products, with the smallest team that can own them — which sometimes turns into a platform team in eighteen months, on evidence, and sometimes correctly never does.
- Alternatives worth naming explicitly: an enabling team that raises capability and dissolves, which fits when the gap is skill rather than missing infrastructure; a temporary collaboration between two stream-aligned teams to build the shared capability, then handing it to whichever will own it; buying a managed platform outright when the differentiating work is genuinely elsewhere; or a rotation model where product engineers spend a fixed term on shared infrastructure. The CNCF white paper's framing helps here — the goal is reduced friction and cognitive load for many teams, and if a cheaper structure delivers that, the platform team is unjustified.
- Failure modes of forming one anyway: a platform team staffed by moving the people who currently keep production running, so both jobs degrade; a team with an infrastructure mandate but no authority over the standards it must enforce, which turns it into a request queue; a platform built for a scale the organization will not reach for five years; a team that becomes a dumping ground for every unwanted system; and — the one that is hardest to reverse — an abstraction layer maintained by three people that every product team now depends on to reach production.

## References

- [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Further reading (blog): [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)

## What to learn next

- Official documentation: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Manual or specification: [Team Topologies key concepts](https://teamtopologies.com/key-concepts)
- Maintainer or personal blog: [Manuel Pais — writing on team interactions and platforms](https://medium.com/@manupaisable)
- Technical blog: [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)
- Hands-on guide: [Google SRE book — introduction](https://sre.google/sre-book/introduction/)
