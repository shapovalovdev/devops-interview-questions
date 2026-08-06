---
title: Choose the right boundary for Git hooks
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, ci-cd, security]
sources:
  - url: https://git-scm.com/docs/githooks
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose the right boundary for Git hooks

What checks belong in local Git hooks, and which must run in CI or server-side controls?

## Answer guide

- Local hooks can provide fast feedback for formatting, linting, commit-message conventions, and accidental secret checks. They run on a developer machine and may be skipped, altered, or absent, so treat them as ergonomic assistance.
- CI is the authoritative reproducible gate for tests, policy, artifacts, and checks that need controlled credentials or standardized tool versions. Server-side branch and push protections can reject disallowed refs before shared history changes.
- Keep hook setup documented and quick enough that people do not bypass it. Pin tooling where practical and ensure hook failures show an actionable command for local reproduction.
- Never depend on a client-side hook as the sole supply-chain or security control. An attacker or a hurried contributor can invoke Git without it.

## References

- [Git documentation: githooks](https://git-scm.com/docs/githooks)
- Further reading (blog): [GitHub Docs — Git hooks](https://docs.github.com/en/get-started/git-basics)

## What to learn next

- Official documentation: [Git: githooks](https://git-scm.com/docs/githooks)
- Manual or specification: [Pro Git: customizing Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- Maintainer or personal blog: [Julia Evans — Git tips](https://jvns.ca/blog/2024/06/21/git-tips/)
- Technical blog: [GitHub Blog — secure development](https://github.blog/security/)
- Hands-on guide: [Git: git-config core.hooksPath](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corehooksPath)
