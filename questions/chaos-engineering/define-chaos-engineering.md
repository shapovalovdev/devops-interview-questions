---
title: Define chaos engineering and what it is for
theme: chaos-engineering
difficulty: junior
type: theory
tags: [chaos-engineering, resilience, reliability, sre]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Define chaos engineering and what it is for

What is chaos engineering, and how does it differ from ordinary testing?

## Answer guide

- Chaos engineering is the practice of running controlled experiments on a distributed system to build confidence that it withstands turbulent real-world conditions. You state a hypothesis about a measurable steady state, inject a realistic fault, and observe whether the steady state survives. It produces evidence about behaviour under failure rather than a pass or fail assertion about code.
- The mechanism is empirical, not exhaustive. A unit or integration test asserts a known expectation about a known code path; an experiment probes a system whose emergent behaviour nobody fully knows, including timeouts, retries, caches, autoscaling, and human response. The output is often a surprise — a dependency that was believed optional, or a retry storm nobody modelled.
- Material constraints: you need a defined steady-state metric, a way to vary real-world events, a bounded blast radius, and the ability to abort. Without observability good enough to detect harm within seconds, an experiment is just an outage you scheduled yourself.
- Operational failure modes include running experiments on a system that is already unhealthy, treating a green result as proof of resilience when the fault injected was weaker than the real one, and running chaos in an environment whose traffic, data volume, and topology do not resemble production, which yields confidence that does not transfer.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [AWS Fault Injection Service — what it is](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Chaos Mesh quick start](https://chaos-mesh.org/docs/quick-start/)
