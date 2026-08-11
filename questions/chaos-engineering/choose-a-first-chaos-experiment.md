---
title: Choose a first chaos experiment safely
theme: chaos-engineering
difficulty: junior
type: scenario
tags: [chaos-engineering, fault-injection, blast-radius, reliability]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Choose a first chaos experiment safely

Your team has never run a chaos experiment. Which one do you run first, and how do you keep it safe?

## Answer guide

- Pick the smallest fault that the system is already designed to survive, so a green result is meaningful and a red result is cheap. Terminating one replica of a stateless, multi-replica service behind a load balancer is the canonical first experiment: the architecture already claims to tolerate it, the fault is trivially reversible, and the recovery path is the same one an ordinary rolling update uses.
- Run it first in a non-production environment to shake out tooling, permissions, and alert noise, then repeat it in production during business hours when the people who own the service are watching. Scope it to one instance in one availability zone, one tenant, or a single canary cell, and write the abort condition down before you start.
- Material constraints: you need a baseline for the steady-state metric, a rollback that does not depend on the component under test, and agreement from the service owner and whoever answers the pager. Book the window, announce it, and make sure the experiment is distinguishable from a real incident in chat and in the alert stream.
- Failure modes: starting with a dramatic fault such as a region evacuation, running during a code freeze or a peak sales event, injecting into a component with hidden singleton state, and forgetting that automated remediation — an autoscaler, a self-healing operator, or an on-call responder — may mask the very behaviour you wanted to observe.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [AWS Fault Injection Service experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html)
- Maintainer or personal blog: [Kolton Andrus — articles on the Gremlin blog](https://www.gremlin.com/blog/author/kolton-andrus)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [AWS Fault Injection Service getting started](https://docs.aws.amazon.com/fis/latest/userguide/getting-started.html)
