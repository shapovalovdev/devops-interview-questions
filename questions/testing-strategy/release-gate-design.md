---
title: Design release gates as risk controls
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://argo-rollouts.readthedocs.io/en/stable/features/analysis/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/sre-book/release-engineering/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design release gates as risk controls

The release checklist has grown to eleven mandatory gates, the median change takes three days to reach production, and both of the last two incidents were caused by changes that passed every gate. How do you redesign the gates as risk controls?

## Answer guide

- Classify each gate by the risk it removes and by whether a machine can evaluate it. A gate earns its latency only if it can fail, has failed for a real defect, and catches something no later control catches. Then split them by position: pre-deploy gates — tests, policy-as-code checks, signature and provenance verification — assert properties of the artifact, while progressive-delivery gates observe the change carrying real traffic and are the only ones that see load-dependent regressions, data-shaped bugs, and environment drift. Eleven gates that are all the first kind explains both symptoms at once.
- The second kind needs a mechanism, not a meeting. An automated analysis step — an Argo Rollouts AnalysisTemplate, or Kayenta-style canary analysis — queries the metrics backend on a fixed interval and count during the canary, evaluates explicit success and failure conditions on a small set of signals such as error ratio, a latency percentile, and saturation, and promotes or aborts without a human in the path. Compare the canary against a baseline of the previous version running concurrently under the same traffic, never against yesterday's numbers, or you are measuring the diurnal cycle.
- Two constraints decide whether this works. Traffic: the canary needs enough requests and enough time for the gated metric to be distinguishable from noise, so a low-volume service must canary over a time window rather than a small traffic percentage, and gating a rare error on a 1% slice for ten minutes produces a coin flip. Authority: a gate that anyone can wave through without a recorded reason is documentation, and an advisory gate converges on ignored. Keep human approval only where judgement cannot be encoded, and make the rest policy-as-code so the decision is auditable.
- Failure modes: gates routinely waived under release pressure, which measure politics rather than risk; analysis on a metric that lags the failure it should catch, so promotion happens before the evidence exists; an abort path that cannot actually be executed because a schema migration was not backward-compatible, turning a working detector into a useless one; and overlapping gates that check the same defect three times while the genuinely untested path ships unexamined.

## References

- [Argo Rollouts — analysis and progressive delivery](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/)
- [Google SRE Book — release engineering](https://sre.google/sre-book/release-engineering/)
- Further reading (blog): [AWS Builders' Library — automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)

## What to learn next

- Official documentation: [Argo Rollouts — analysis and progressive delivery](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/)
- Manual or specification: [Google SRE Book — release engineering](https://sre.google/sre-book/release-engineering/)
- Maintainer or personal blog: [Jez Humble and Dave Farley — continuous testing](https://continuousdelivery.com/foundations/test-automation/)
- Technical blog: [AWS Builders' Library — automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)
- Hands-on guide: [Flagger — Istio canary deployment tutorial](https://docs.flagger.app/tutorials/istio-progressive-delivery)
