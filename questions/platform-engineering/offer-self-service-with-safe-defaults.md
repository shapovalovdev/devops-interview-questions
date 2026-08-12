---
title: Offer self-service with safe defaults
theme: platform-engineering
difficulty: junior
type: theory
tags: [platform-engineering, self-service, guardrails, kubernetes]
sources:
  - url: https://docs.score.dev/docs/score-specification/score-spec-reference/
    source_type: official-api
    verified_on: 2026-08-11
---

# Offer self-service with safe defaults

What makes a platform capability genuinely self-service, and what belongs in the defaults?

## Answer guide

- Self-service means a team can go from intent to a working, compliant result without a human in the platform team's queue and without needing to understand the provider underneath. The Score workload specification is a clean illustration: the developer writes a small declarative file naming containers, resources and service ports, and an implementation resolves it into Kubernetes manifests or a Compose file. The developer never writes the provider-specific object, so the platform can change the resolution without changing the request.
- Safe defaults are the values the platform fills in when the developer says nothing: resource requests and limits, replica count and spread, a probe configuration, log and metric pipelines, a network policy, an image source, a retention period, and an owner. The default must be the choice you would defend in a review, because most workloads will never override it. Score's separation of the workload file from environment-specific resource provisioning is what lets the same declaration land on different defaults per environment.
- Constraints: every default needs an escape hatch and the escape hatch needs a cost. A platform with no overrides forces teams off the road; a platform where every field is overridable has no defaults at all. Practically, expose a small, versioned set of knobs, make non-default choices visible in review, and keep the abstraction honest — if a team must know the Kubernetes object to debug their workload, the abstraction leaks and the docs must admit it.
- Failure modes: defaults chosen for the demo rather than for production, so the first real load event hits an unset memory limit; a self-service action that succeeds but leaves an unowned resource nobody pays for or patches; a request path that is automated up to the last step and then waits on an approval, which preserves the queue while claiming self-service; and drift, where the platform's default changes but existing workloads keep the old value silently forever.

## References

- [Score specification reference](https://docs.score.dev/docs/score-specification/score-spec-reference/)
- Further reading (blog): [CNCF blog](https://www.cncf.io/blog/)

## What to learn next

- Official documentation: [Score documentation](https://docs.score.dev/)
- Manual or specification: [Score specification reference](https://docs.score.dev/docs/score-specification/score-spec-reference/)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Score getting started](https://docs.score.dev/docs/get-started/)
