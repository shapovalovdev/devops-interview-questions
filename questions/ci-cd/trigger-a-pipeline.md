---
title: Choose CI pipeline triggers
theme: ci-cd
difficulty: junior
type: scenario
tags: [ci-cd, automation, git, delivery]
sources:
  - url: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose CI pipeline triggers

Which events should trigger validation, release, and production deployment workflows?

## Answer guide

- Run validation on pull requests and relevant pushes so proposed changes receive feedback before merge and the protected branch is also verified.
- Trigger release publication from a protected tag or trusted main-branch event, and deploy only an artifact produced by that release workflow.
- Scope path, branch, and event filters deliberately. Broad triggers waste capacity; overly narrow filters can skip a dependency or workflow change. Treat fork-originated events as untrusted and do not expose deployment secrets to them.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Further reading: GitHub Docs—secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)

## What to learn next

- Official documentation: [GitHub Actions events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Troy Hunt](https://www.troyhunt.com/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/build-and-test-code)
