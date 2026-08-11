---
title: Set security testing boundaries
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://owasp.org/www-project-application-security-verification-standard/
    source_type: standard
    verified_on: 2026-08-10
  - url: https://www.zaproxy.org/docs/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set security testing boundaries

A team has SAST, dependency scanning, and a ZAP scan all wired into the same pipeline stage, the build takes an hour, and nobody triages the 900 findings. Which security tests belong in the pipeline, and which do not?

## Answer guide

- Place each tool where its feedback is actionable and its runtime fits. Secret scanning and dependency scanning are fast and produce high-signal findings tied to a specific line or lockfile entry, so they belong on every pull request and can block. SAST belongs there too but only on the diff, since full-repository analysis of a large codebase takes far longer than a review cycle. Dynamic scanning needs a running application, so it belongs in a post-deploy job against a deployed environment, and a ZAP full scan or spider is a nightly job, not a merge gate.
- Give the pipeline a target rather than a tool list. OWASP ASVS provides levelled, testable requirements — L1 for anything internet-facing, L2 for applications handling sensitive data — so you can map each requirement to the check that verifies it and see what nothing covers. That mapping is what stops the estate from having three overlapping scanners on injection and no coverage at all of access control, which is the category automated tools are worst at and which dominates real breaches.
- Gate on new findings, not on the total. Establish a baseline, fail the build only on findings introduced by the change, and set the blocking threshold by severity plus reachability rather than CVSS alone — a critical CVE in a transitive dependency your code never calls is not the same risk as a medium one on the request path, and treating them identically is what produced 900 untriaged findings. Every rule that fires must have an owner and a suppression mechanism that lives in version control with a reason and an expiry.
- Failure modes: DAST run against an environment with no seeded data or authenticated session, so it exercises the login page and reports nothing about the application; a scanner pointed at a shared environment where its traffic triggers other teams' alerts or writes real records; suppressions added with no expiry so the exception list becomes the policy; and the assumption that a green pipeline means the design is safe, when authorisation logic, business-logic abuse, and multi-step flows still need threat modelling and manual testing.

## References

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP ZAP documentation](https://www.zaproxy.org/docs/)
- Further reading (blog): [Snyk — how static application security testing works](https://snyk.io/articles/application-security/static-application-security-testing/)

## What to learn next

- Official documentation: [OWASP ZAP documentation](https://www.zaproxy.org/docs/)
- Manual or specification: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Maintainer or personal blog: [Jim Gumbley — a guide to threat modelling for software teams](https://martinfowler.com/articles/agile-threat-modelling.html)
- Technical blog: [Snyk — how static application security testing works](https://snyk.io/articles/application-security/static-application-security-testing/)
- Hands-on guide: [OWASP ZAP — getting started](https://www.zaproxy.org/getting-started/)
