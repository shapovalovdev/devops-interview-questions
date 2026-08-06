---
title: Use multiple Git worktrees safely
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, operations, troubleshooting]
sources:
  - url: https://git-scm.com/docs/git-worktree
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use multiple Git worktrees safely

When would you use `git worktree` instead of repeatedly switching branches, and what constraints must you remember?

## Answer guide

- A linked worktree provides another working directory tied to the same repository object database, allowing an engineer to keep a hotfix, review, or long-running test checkout beside current work.
- Add each worktree on a distinct branch, inspect its status independently, and remove it through `git worktree remove` when finished. Shared objects reduce clone cost, but local uncommitted files and build outputs remain per worktree.
- Git normally prevents checking out the same branch in two worktrees because two working trees advancing one ref is confusing. Use detached HEAD deliberately only when that limitation is understood.
- Do not let a worktree bypass review or isolation policy. It is a local convenience, not a separate repository, permission boundary, or replacement for clean CI environments.

## References

- [Git documentation: git-worktree](https://git-scm.com/docs/git-worktree)
- Further reading (personal blog): [Julia Evans — Git worktrees](https://jvns.ca/blog/2024/02/15/git-worktrees/)

## What to learn next

- Official documentation: [Git: git-worktree](https://git-scm.com/docs/git-worktree)
- Manual or specification: [Pro Git: Git internals](https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables)
- Maintainer or personal blog: [Julia Evans — Git worktrees](https://jvns.ca/blog/2024/02/15/git-worktrees/)
- Technical blog: [GitHub Blog — Git tips](https://github.blog/open-source/git/)
- Hands-on guide: [Git: git-worktree add](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-add)
