---
title: Design CI/CD quality gates for a service
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, delivery, deployment, automation, security]
---

# Design CI/CD quality gates for a service

Which checks would you place between a pull request and production deployment, and what risk does each check reduce?

## Answer guide

- Validate formatting, tests, and build reproducibility early.
- Scan dependencies and produced artifacts for known security risks.
- Publish immutable, traceable artifacts only after required checks pass.
- Use staged deployment verification and explicit production-promotion criteria.
