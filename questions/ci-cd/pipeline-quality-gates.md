---
title: Design CI/CD quality gates for a service
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, delivery, deployment, automation, security, cgoa]
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

## What to learn next

- Official documentation: [GitHub required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/build-and-test-code)
