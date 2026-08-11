---
title: State a steady-state hypothesis
theme: chaos-engineering
difficulty: junior
type: theory
tags: [chaos-engineering, experimentation, metrics, monitoring]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# State a steady-state hypothesis

What is a steady-state hypothesis, and what makes one usable in an experiment?

## Answer guide

- A steady-state hypothesis is a falsifiable statement that a measurable property of normal system behaviour will keep holding while a specific fault is applied. A usable one names the metric, the threshold, the observation window, and the fault: for example, checkout success rate stays above 99.5 per cent over five minutes while one of three payment-service replicas is terminated.
- Choose output metrics that reflect user-visible behaviour rather than internal state. Requests per second, successful orders, stream starts, and p99 latency describe whether the system is doing its job; CPU utilisation and pod restart counts describe how it is doing it and will move during any experiment without telling you whether users were harmed.
- Material constraints: the metric must be already instrumented, must have a known baseline including its normal variance and daily cycle, and must be observable at a resolution faster than the experiment. A metric whose scrape interval is one minute cannot falsify a hypothesis about a two-minute experiment.
- Failure modes: hypotheses stated so loosely that any outcome confirms them, thresholds set from a single quiet afternoon rather than from real variance, and metrics that are averaged across tenants or regions so that a severe local failure disappears into an aggregate that still looks healthy.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [Prometheus histograms and quantiles](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Grafana Labs blog](https://grafana.com/blog/)
- Hands-on guide: [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
