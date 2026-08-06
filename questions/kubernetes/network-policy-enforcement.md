---
title: Restrict Pod traffic with NetworkPolicy
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, networking, security, least-privilege]
---

# Restrict Pod traffic with NetworkPolicy

How would you allow an API Pod to receive traffic only from its frontend and call only its database?

## Answer guide

- Select the target Pods with labels and declare explicit ingress and egress peers and ports.
- Confirm the installed CNI enforces NetworkPolicy and test allowed and denied paths.
