---
title: Cherry-pick a targeted fix safely
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, delivery, troubleshooting]
sources:
  - url: https://git-scm.com/docs/git-cherry-pick
    source_type: official-docs
    verified_on: 2026-08-06
---

# Cherry-pick a targeted fix safely

When is cherry-picking appropriate for a release branch, and what checks prevent an unsafe backport?

## Answer guide

- Cherry-pick applies the change introduced by an existing commit onto the current branch as a new commit. It is useful for a narrow, independently safe fix when merging the whole source branch would bring unrelated work.
- Inspect the original commit, its parents, dependencies, tests, configuration assumptions, and any preceding migration. Resolve conflicts as a semantic integration problem and run the release branch's validation after the pick.
- Record the originating commit and backport rationale in the pull request, release note, or commit message so later maintenance can recognize duplicate work and removal order.
- Avoid cherry-picking a merge commit or a tightly coupled sequence without understanding its mainline and dependencies. Repeated picks across long-lived branches can create divergence that masks the real integration strategy.

## References

- [Git documentation: git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
- Further reading (blog): [GitHub Docs — cherry-picking commits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)

## What to learn next

- Official documentation: [Git: git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
- Manual or specification: [Pro Git: maintenance and data recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)
- Maintainer or personal blog: [Julia Evans — Git tips](https://jvns.ca/)
- Technical blog: [GitHub Blog — Git workflow guidance](https://github.blog/open-source/git/)
- Hands-on guide: [Git: git-show](https://git-scm.com/docs/git-show)
