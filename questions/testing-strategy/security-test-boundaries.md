---
title: Set security testing boundaries
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set security testing boundaries

How should a team make this testing strategy decision?

## Answer guide

- Define the user-facing risk and choose a test boundary that produces useful evidence without delaying every change.
- Make dependencies, data, and environment ownership explicit so results are reproducible and failures can be diagnosed.
- Balance test cost against feedback speed and release confidence; use the result together with review and operational signals.
- Reassess after incidents and architecture changes, because an uncontrolled or unowned check becomes a source of false confidence.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [OWASP ZAP documentation](https://www.zaproxy.org/docs/)
- Manual or specification: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Maintainer or personal blog: [Jim Gumbley — a guide to threat modelling for software teams](https://martinfowler.com/articles/agile-threat-modelling.html)
- Technical blog: [Snyk — how static application security testing works](https://snyk.io/articles/application-security/static-application-security-testing/)
- Hands-on guide: [OWASP ZAP — getting started](https://www.zaproxy.org/getting-started/)
