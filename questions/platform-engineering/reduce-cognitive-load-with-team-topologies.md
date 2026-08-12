---
title: Reduce cognitive load with team topologies
theme: platform-engineering
difficulty: senior
type: scenario
tags: [platform-engineering, cognitive-load, team-topologies, leadership]
sources:
  - url: https://teamtopologies.com/key-concepts
    source_type: standard
    verified_on: 2026-08-11
---

# Reduce cognitive load with team topologies

Product teams say they are drowning in infrastructure detail. How do you use team topology concepts to decide what to take off their plate?

## Answer guide

- Diagnose before you build. Cognitive load in the Team Topologies model splits into three kinds — intrinsic (the skill of the job: the language, the domain), extraneous (the accidental mechanics: how to get a cluster role, which of five YAML dialects applies here), and germane (thinking about the business problem). A platform's job is to eliminate extraneous load and protect germane load; it cannot and should not remove intrinsic load. So the first move is to sit with a stream-aligned team and classify what is consuming them, because "drowning in infrastructure" usually turns out to be four specific extraneous items, not a general condition.
- The structural mechanism is the platform as an X-as-a-Service interaction with stream-aligned teams: they consume the platform with minimal collaboration, which is what makes the load reduction real. Team Topologies names three interaction modes — collaboration, X-as-a-Service, and facilitating — and is explicit that collaboration is high-bandwidth and expensive, appropriate for discovering a new capability but not as a steady state. If your platform team is in permanent collaboration with every consumer, you have added a coordination dependency, not removed load.
- Constraints: a stream-aligned team should own a bounded domain it can hold in its head, so if the load is intrinsic — the team owns nine unrelated services — a platform will not fix it and the answer is a boundary change or an enabling team. Time-box collaboration deliberately and agree the exit into X-as-a-Service up front. Conway's law applies to the platform interface too: the seams in your platform API will mirror your platform team's internal structure, so a platform split across three sub-teams tends to expose three unrelated interfaces to one consumer.
- Failure modes: measuring cognitive load with a survey question and no classification, so nothing actionable comes out; a platform that reduces day-one load while adding day-hundred load, because now teams must understand both Kubernetes and your abstraction over it; using "cognitive load" as a rationale for taking ownership away from teams, which removes their ability to fix their own production problems; enabling teams that never leave, becoming a permanent dependency; and reorganizing the org chart while the interaction modes stay exactly as informal as before.

## References

- [Team Topologies key concepts](https://teamtopologies.com/key-concepts)
- Further reading (blog): [Manuel Pais — writing on team interactions and platforms](https://medium.com/@manupaisable)

## What to learn next

- Official documentation: [Team Topologies key concepts](https://teamtopologies.com/key-concepts)
- Manual or specification: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Maintainer or personal blog: [Matthew Skelton — blog](https://blog.matthewskelton.net/)
- Technical blog: [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)
- Hands-on guide: [Team Topologies — the book and its resources](https://teamtopologies.com/book)
