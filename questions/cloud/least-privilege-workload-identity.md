---
title: Apply least privilege to a cloud workload identity
theme: cloud
difficulty: middle
type: scenario
tags: [aws, iam, cloud, security, least-privilege]
---

# Apply least privilege to a cloud workload identity

A service needs read access to a single object-storage prefix. How would you grant access without embedding static credentials?

## Answer guide

- Use a workload identity or short-lived role credentials rather than static configuration credentials.
- Grant only read actions and the resource scope required for the prefix.
- Keep runtime identity separate from human administrator identities.
- Audit use and test that denied actions remain denied.
