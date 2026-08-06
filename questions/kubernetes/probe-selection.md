---
title: Select Kubernetes readiness, liveness, and startup probes
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, reliability, troubleshooting]
---

# Select Kubernetes readiness, liveness, and startup probes

How do you choose the three probe types for a service with a slow initialization phase and a dependency outage?

## Answer guide

- Startup probes protect slow initialization from premature liveness restarts.
- Readiness controls whether a Pod receives traffic and should reflect its ability to serve safely.
- Liveness detects a stuck process; do not use it to restart healthy Pods solely because an external dependency is unavailable.
