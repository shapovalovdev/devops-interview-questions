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

- [GitHub Docs: Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Further reading: GitHub Docs—secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
