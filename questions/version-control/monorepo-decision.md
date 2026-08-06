---
title: Make a monorepo versus multirepo decision
theme: version-control
difficulty: staff
type: scenario
tags: [git, version-control, platform-engineering, operations, governance]
sources:
  - url: https://git-scm.com/docs/git-sparse-checkout
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/partial-clone
    source_type: official-docs
    verified_on: 2026-08-06
---

# Make a monorepo versus multirepo decision

How would you decide whether related services and libraries should live in one repository or several?

## Answer guide

- Evaluate change coupling, ownership boundaries, build and test topology, dependency release cadence, access requirements, discoverability, CI cost, and developer experience. A monorepo can make cross-component changes atomic; multiple repositories can make boundaries and permissions clearer.
- Prototype the operational model: affected-target builds, code ownership, dependency versioning, checkout performance, release automation, and incident rollback. Git facilities such as sparse checkout and partial clone mitigate some scale costs but do not solve organizational coupling.
- Set success measures and a migration plan with compatibility periods, redirects, archival rules, and source-of-truth ownership. Revisit the decision as architecture and team structure change.
- Avoid treating repository count as an architectural purity test. Either model fails when build ownership, interfaces, and release responsibilities are unclear.

## References

- [Git documentation: git-sparse-checkout](https://git-scm.com/docs/git-sparse-checkout)
- [Git documentation: partial clone](https://git-scm.com/docs/partial-clone)
- Further reading (blog): [GitHub Blog — Git performance](https://github.blog/open-source/git/)

## What to learn next

- Official documentation: [Git: sparse checkout](https://git-scm.com/docs/git-sparse-checkout)
- Manual or specification: [Pro Git: distributed workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows)
- Maintainer or personal blog: [Derrick Stolee's Git blog](https://stolee.dev/)
- Technical blog: [GitHub Blog — Git performance](https://github.blog/open-source/git/)
- Hands-on guide: [Git: partial clone](https://git-scm.com/docs/partial-clone)
