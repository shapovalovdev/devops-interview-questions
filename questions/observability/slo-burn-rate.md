---
title: Explain an SLO error-budget burn-rate alert
theme: observability
difficulty: senior
type: theory
tags: [observability, monitoring, reliability, incident-response]
---

# Explain an SLO error-budget burn-rate alert

What does a burn-rate alert measure, and why can it be better than alerting on a fixed error-percentage threshold?

## Answer guide

- It relates the current rate of bad events to the allowed error budget over an objective window.
- It prioritizes incidents that threaten the reliability target at a meaningful pace.
- Multiple short and long windows balance fast detection against transient noise.
