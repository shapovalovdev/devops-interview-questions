---
title: Choose merge or rebase when integrating a branch
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, change-management, delivery]
sources:
  - url: https://git-scm.com/docs/git-merge
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/git-rebase
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose merge or rebase when integrating a branch

When should a team merge rather than rebase, and what risk changes after a branch is shared?

## Answer guide

- A merge creates a commit that joins histories while retaining the existing commits. Rebase reapplies commits onto a new base, creating new commit IDs and a linearized local sequence.
- Rebase private work before review when the team prefers a tidy sequence, resolve each replay conflict carefully, and run tests because a different base can change behavior. Merge when preserving the actual integration event or when rewriting shared commits would disrupt collaborators.
- After a branch is published, coordinate explicitly before rebasing and use a lease-protected force push only where policy allows it. Teammates with descendants of the old history need a recovery plan.
- Neither choice eliminates integration testing. A clean history can still hide semantic conflicts, generated lockfile differences, or incompatible rollout ordering.

## References

- [Git documentation: git-merge](https://git-scm.com/docs/git-merge)
- [Git documentation: git-rebase](https://git-scm.com/docs/git-rebase)
- Further reading (blog): [GitHub Blog — Git merge and rebase](https://github.blog/open-source/git/)

## What to learn next

- Official documentation: [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- Manual or specification: [Pro Git: rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
- Maintainer or personal blog: [Julia Evans — Git terminology](https://jvns.ca/)
- Technical blog: [Atlassian Git tutorials — merge or rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- Hands-on guide: [Pro Git: basic merging and conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
