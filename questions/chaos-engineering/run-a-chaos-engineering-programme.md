---
title: Run a chaos engineering programme across many teams
theme: chaos-engineering
difficulty: staff
type: scenario
tags: [chaos-engineering, platform-engineering, governance, leadership]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Run a chaos engineering programme across many teams

How do you take chaos engineering from one enthusiastic team to an organisation-wide practice?

## Answer guide

- Build a paved road rather than a central chaos team that runs experiments on other people's services. The platform provides the injection tooling, a scoped and audited permission model, experiment templates for the common faults, automatic stop conditions wired to each service's own objectives, a scheduling and announcement mechanism, and a result store. Service teams keep ownership of the hypothesis, the run, and the fixes, because they are the only ones who know what steady state means for their users.
- Sequence adoption by readiness, not by enthusiasm. A service qualifies when it has an owner, a service level objective with instrumentation, a runbook, and an on-call rotation; experiments on a service without those produce findings nobody will act on. Start with the tier-one journeys, publish the results including the embarrassing ones, and let the evidence recruit the next teams. Attach experiments to existing rituals — production readiness reviews, launch checklists, postmortem action items — so they are not extra work invented from nothing.
- Govern with a small number of real controls: role-based access to fault types, mandatory blast-radius limits and stop conditions enforced by the platform rather than by convention, an approval path only for the genuinely dangerous classes such as data-layer and region-wide faults, an audit trail, and an error-budget rule that says when experiments pause. Chaos Mesh permission management and Azure Chaos Studio's security model are examples of the platform enforcing this instead of a wiki page asking politely.
- Measure the programme by findings acted on and by incidents avoided or shortened, not by experiments executed — counting runs creates a metric teams can satisfy with trivial faults. Failure modes: a central team accumulating knowledge the service teams never gain; a mandate that forces experiments onto unready services and produces resentment plus a backlog of unowned findings; tooling that only one specialist can operate; and a programme that quietly dies because nobody funded fixing what it found.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [Chaos Mesh — manage user permissions](https://chaos-mesh.org/docs/manage-user-permissions/)
- Maintainer or personal blog: [Nora Jones — resilience engineering writing](https://medium.com/@NoraJones)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — evolving the SRE engagement model](https://sre.google/sre-book/evolving-sre-engagement-model/)
