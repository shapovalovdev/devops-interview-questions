---
title: Design CI/CD quality gates for a service
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, delivery, deployment, automation, security]
sources:
  - url: https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-nodejs
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design CI/CD quality gates for a service

Which checks would you place between a pull request and production deployment, and what risk does each check reduce?

## Answer guide

- Run deterministic formatting, linting, unit tests, and a reproducible build before merge; they provide fast feedback on source-level regressions.
- Run integration/contract tests where a disposable dependency is available, and scan dependencies, source, and produced artifacts. A passing scan is risk evidence, not a guarantee of no vulnerability.
- Require review and protected-branch checks before publishing one immutable, traceable artifact. Treat deployment approval separately from build success.
- Promote through a staged environment with explicit health and rollback thresholds. Gates that are slow, flaky, or have no owner become bypasses, so measure their duration and false-failure rate.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Building and testing Node.js](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-nodejs)
- [Further reading: GitHub Docs—secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
