---
title: Measure developer experience
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, developer-experience, product-management, quality]
sources:
  - url: https://queue.acm.org/detail.cfm?id=3454124
    source_type: standard
    verified_on: 2026-08-11
---

# Measure developer experience

Your platform's dashboards are all green but engineers say working with it is painful. How do you measure the experience itself?

## Answer guide

- Measure perception and workflow, not only system output. The SPACE framework's argument is that productivity and experience are multidimensional — satisfaction and wellbeing, performance, activity, communication and collaboration, and efficiency and flow — and that any single metric will be gamed or will mislead. For a platform this means pairing three sources: a periodic survey of the people using it, task-level telemetry from the platform itself, and direct observation of engineers doing real work.
- The mechanism that produces actionable results is measuring named *tasks*, not the platform in general. Instrument the concrete journeys — create a service, get a secret, reproduce a production bug locally, roll back — and for each capture both the system time (how long the tooling took) and the perceived time and difficulty (what the engineer felt). The gap between the two is the most useful signal you will get: a step that takes ninety seconds but is rated painful is usually a confidence or feedback problem, and a step engineers rate as fine but which takes twenty minutes is friction they have learned to accept.
- Constraints: survey questions must be about specific recent experiences rather than general satisfaction, run often enough to attribute change to a release but rarely enough to avoid fatigue, and reported at a granularity that cannot identify an individual. SPACE-style measures are for improving the system, never for comparing teams or people — the moment a dimension becomes a performance target, the reported data stops being true. Sample size is a real limit: a platform with twelve consuming teams cannot support statistically confident quarter-on-quarter comparisons, so use it qualitatively.
- Failure modes: a single "developer NPS" number that moves for reasons nobody can trace; surveying only the teams already on the paved road, which excludes the people whose experience was bad enough to leave; treating an open-comment box as a backlog and then never responding, which kills response rates within two cycles; measuring build duration as a proxy for flow while the real cost is waiting for an environment; and confusing this with delivery-outcome measurement, which answers a different question with different data.

## References

- [ACM Queue — the SPACE of developer productivity](https://queue.acm.org/detail.cfm?id=3454124)
- Further reading (blog): [Abi Noda — measuring developer productivity via humans](https://martinfowler.com/articles/measuring-developer-productivity-humans.html)

## What to learn next

- Official documentation: [DORA capability catalog](https://dora.dev/capabilities/)
- Manual or specification: [ACM Queue — the SPACE of developer productivity](https://queue.acm.org/detail.cfm?id=3454124)
- Maintainer or personal blog: [Abi Noda — measuring developer productivity via humans](https://martinfowler.com/articles/measuring-developer-productivity-humans.html)
- Technical blog: [Stack Overflow blog](https://stackoverflow.blog/)
- Hands-on guide: [Microsoft — developer self-service in platform engineering](https://learn.microsoft.com/en-us/platform-engineering/developer-self-service)
