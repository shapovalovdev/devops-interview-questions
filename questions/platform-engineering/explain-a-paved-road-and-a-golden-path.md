---
title: Explain a paved road and a golden path
theme: platform-engineering
difficulty: junior
type: theory
tags: [platform-engineering, golden-path, guardrails, delivery]
sources:
  - url: https://backstage.io/docs/features/software-templates/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Explain a paved road and a golden path

What do "paved road" and "golden path" mean on a platform, and how does a paved road differ from a rule?

## Answer guide

- A paved road is the supported, opinionated route through a task — create a service, ship a change, add a database — where the platform has already made the hard choices and takes responsibility for keeping them working. A golden path is one concrete instantiation of that road: a specific templated journey, such as Backstage's software templates, that scaffolds a repository, wires the pipeline, registers the catalog entry, and provisions the runtime in one action.
- The mechanism is pre-integration plus defaults. A Backstage template is a parameterised set of actions — fetch a skeleton, publish a repository, register the entity — so the team's first commit already carries the pipeline, the ownership metadata, and the runtime configuration the platform expects. The road is "paved" because that integration is done ahead of time, not negotiated per team.
- The critical distinction: a paved road is chosen because it is the fastest route, not because it is compulsory. Rules and mandatory guardrails are a separate control layer — admission policy, required checks, budget limits — and they apply to teams both on and off the road. Conflating the two produces a road nobody wants and a rule nobody can escape. A healthy platform states both: what is easy by default, and what is enforced regardless.
- Failure modes: a template that is generated once and then diverges, so the "road" only exists at day zero and every team is off-road by month three; a golden path that covers scaffolding but not the operational half — alerting, on-call, cost, deprecation — so teams walk off it as soon as the service is live; enforcement dressed up as a paved road, which destroys the credibility of both; and multiple half-maintained templates for the same use case, so "the" golden path is ambiguous.

## References

- [Backstage software templates](https://backstage.io/docs/features/software-templates/)
- Further reading (blog): [Evan Bottcher — what I talk about when I talk about platforms](https://martinfowler.com/articles/talk-about-platforms.html)

## What to learn next

- Official documentation: [Backstage software templates](https://backstage.io/docs/features/software-templates/)
- Manual or specification: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Maintainer or personal blog: [Evan Bottcher — what I talk about when I talk about platforms](https://martinfowler.com/articles/talk-about-platforms.html)
- Technical blog: [Spotify engineering blog](https://engineering.atspotify.com/)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)
