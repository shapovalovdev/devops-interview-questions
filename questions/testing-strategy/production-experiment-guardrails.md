---
title: Set production experiment guardrails
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://openfeature.dev/docs/reference/intro/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set production experiment guardrails

Product wants to run a pricing experiment on 10% of live checkout traffic, and the platform team wants assurance it cannot become an incident. What guardrails have to exist before the flag is switched on, and who is allowed to turn it off?

## Answer guide

- Separate the release decision from the experiment decision, and give each its own mechanism. Ship the code dark behind a flag evaluated through a defined interface — OpenFeature-style, so the SDK and the provider can change without touching call sites — with a fail-closed default: if evaluation errors or the provider is unreachable, the control path runs. Targeting must be deterministic on a stable unit such as account or session ID, so a user does not flip between variants mid-checkout and corrupt both the experience and the measurement.
- Guardrail metrics are not the experiment's success metrics. Before launch, name the small set of signals that abort the experiment regardless of how the pricing metric performs — error ratio, checkout completion rate, p99 latency, payment declines — with a threshold and an evaluation window each, wired to automated evaluation rather than a dashboard someone might be watching. Run a pre-experiment A/A test on the same split to measure how much those metrics vary with no change at all; that variance sets the thresholds honestly.
- Kill authority has to be explicit and cheap to exercise. The flag must be switchable to control by whoever is on call, without a deploy, a code review, or the experiment owner's approval, and the switch must take effect within a bounded time you have actually measured, including SDK cache and CDN TTLs. Write down the blast-radius ramp — 1%, 5%, 10% with a soak at each — a hard end date after which the flag defaults off, and the cleanup ticket, because a flag whose owner has left the team is a permanent untested branch.
- Failure modes: an experiment that changes something irreversible, so aborting does not undo it — money moved, an email sent, a record written in the variant's schema — which makes it a migration wearing an experiment's clothes; guardrails evaluated on aggregate traffic where a 10% arm's regression is invisible; caching or CDN layers keyed without the variant so the two arms contaminate each other; and flag evaluation inside a hot path with a synchronous network call, where the guardrail itself becomes the latency incident.

## References

- [OpenFeature documentation](https://openfeature.dev/docs/reference/intro/)
- [Google SRE Workbook — canarying releases](https://sre.google/workbook/canarying-releases/)
- Further reading (blog): [Netflix TechBlog — automated canary analysis with Kayenta](https://netflixtechblog.com/automated-canary-analysis-at-netflix-with-kayenta-3260bc7acc69)

## What to learn next

- Official documentation: [OpenFeature documentation](https://openfeature.dev/docs/reference/intro/)
- Manual or specification: [Google SRE Workbook — canarying releases](https://sre.google/workbook/canarying-releases/)
- Maintainer or personal blog: [Pete Hodgson — feature toggles](https://martinfowler.com/articles/feature-toggles.html)
- Technical blog: [Netflix TechBlog — automated canary analysis with Kayenta](https://netflixtechblog.com/automated-canary-analysis-at-netflix-with-kayenta-3260bc7acc69)
- Hands-on guide: [Argo Rollouts — experiments](https://argo-rollouts.readthedocs.io/en/stable/features/experiment/)
