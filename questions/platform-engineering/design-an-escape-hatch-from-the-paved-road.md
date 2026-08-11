---
title: Design an escape hatch from the paved road
theme: platform-engineering
difficulty: senior
type: scenario
tags: [platform-engineering, golden-path, crossplane, self-service]
sources:
  - url: https://docs.crossplane.io/latest/get-started/get-started-with-composition/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Design an escape hatch from the paved road

A team's workload cannot be expressed in your platform abstraction. What do you offer them?

## Answer guide

- Offer a graded set of exits rather than a binary on-or-off-the-platform choice. In order of preference: an existing parameter they did not know about; a new parameter added to the abstraction because their need generalises; a scoped override that lets them patch specific fields of the generated resources while the platform still owns everything else; a different composition — a second implementation of the same platform API for their class of workload; and only last, full ownership of the underlying resources with a documented, time-boxed exception. Crossplane's model makes the middle options concrete: one composite resource definition can be satisfied by several compositions, so the team keeps the platform API while the resolution differs.
- The design rule is that an escape hatch must keep the platform's invariants even when it abandons the platform's opinions. A team that patches the container spec should still get the ownership labels, the network policy, the cost tag, the log pipeline and the admission checks; what they lose is the platform's guarantee about the field they overrode. Encode that split explicitly — a set of platform-managed fields that overrides cannot touch, and a set of team-overridable fields — rather than letting an override mean "we no longer manage this object at all".
- Constraints: every escape hatch is future migration debt, so record who took which exit and why, and review the register as product input. Three teams taking the same override is a missing feature in the abstraction; one team taking a unique override may be a genuine special. State the support consequence plainly — an overridden field is outside the platform SLO and the team owns its failures — and make it visible in the catalog so an incident responder can see that this workload is not standard.
- Failure modes: no escape hatch at all, which produces a shadow platform in someone's repository and a fleet you cannot see; an escape hatch so easy that it becomes the default path; overrides expressed as raw provider YAML pasted in, which the platform can neither validate nor upgrade; exceptions with no expiry that silently become permanent architecture; and a second composition maintained by one person who then changes team, leaving a class of workloads with an unowned implementation.

## References

- [Crossplane — get started with composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition/)
- Further reading (blog): [CNCF blog](https://www.cncf.io/blog/)

## What to learn next

- Official documentation: [Crossplane documentation](https://docs.crossplane.io/)
- Manual or specification: [Score specification reference](https://docs.score.dev/docs/score-specification/score-spec-reference/)
- Maintainer or personal blog: [Evan Bottcher — what I talk about when I talk about platforms](https://martinfowler.com/articles/talk-about-platforms.html)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Crossplane — get started with composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition/)
