---
title: Design a hypothesis-driven chaos experiment
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, experimentation, resilience, testing-strategy]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Design a hypothesis-driven chaos experiment

Walk through the design of an experiment from hypothesis to written result.

## Answer guide

- Start from a belief worth testing. Write the steady state as a measurable output metric with a threshold and a window, name the real-world event you will simulate, and predict the outcome: "if the recommendation service returns errors for thirty per cent of requests, the home page still renders within 800 ms at p95 because the client falls back to a cached list." An experiment with no prediction cannot be wrong, and therefore teaches nothing.
- Define the variables explicitly: the target selector, the fault type and magnitude, the fraction of traffic or instances affected, the duration, and the ramp. Then define the controls — the abort condition, the halt mechanism, the maximum blast radius, and a comparison group such as an unaffected cell or the same service one hour earlier — so you can distinguish the fault's effect from ordinary variance.
- Material constraints: run it where the traffic and topology make the result transferable, capture the baseline in the same conditions, and keep the fault small enough that a wrong prediction is survivable. Automate the run so it is repeatable, and re-run it after the fix so the experiment becomes a regression test rather than a one-off stunt.
- Record the result whether or not it matched, including the surprises. Failure modes: changing several variables at once so the cause is ambiguous, running so briefly that autoscaling and circuit breakers never engage, declaring success because no alert fired when no alert existed, and never re-running the experiment, which lets the system quietly regress after the next deployment.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [AWS Fault Injection Service experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [LitmusChaos — chaos workflows](https://docs.litmuschaos.io/docs/concepts/chaos-workflow)
