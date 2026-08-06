---
title: Decide whether to advance or stop a canary deployment
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, deployment, monitoring, reliability]
---

# Decide whether to advance or stop a canary deployment

Which signals should control promotion of a small canary release?

## Answer guide

- Compare error rate, latency, saturation, and relevant business outcomes against a stable baseline.
- Define observation duration and rollback thresholds before release; stop automatically when thresholds breach.
