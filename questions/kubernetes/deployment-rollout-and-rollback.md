---
title: Explain a Kubernetes Deployment rollout and rollback
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, deployment, rolling-update, reliability]
---

# Explain a Kubernetes Deployment rollout and rollback

How does a Deployment replace application Pods safely, and what would make you roll it back?

## Answer guide

- A Deployment manages ReplicaSets and incrementally changes active Pods according to its update strategy.
- Readiness probes determine whether new Pods may receive traffic.
- `maxSurge` and `maxUnavailable` control capacity and risk during a rolling update.
- Roll back for failed health checks, error or latency objectives, or a confirmed correctness problem.
