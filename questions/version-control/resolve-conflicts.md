---
title: Resolve a Git merge conflict safely
theme: version-control
difficulty: middle
type: troubleshooting
tags: [git, version-control, troubleshooting, change-management]
sources:
  - url: https://git-scm.com/docs/git-merge
    source_type: official-docs
    verified_on: 2026-08-06
---

# Resolve a Git merge conflict safely

Walk through resolving a merge conflict in a production-bound change. What must you verify besides removing conflict markers?

## Answer guide

- Stop and identify the two intended changes and their order. Inspect the conflict markers, surrounding code, tests, configuration, and the base version; do not choose one side mechanically because both edits may be required.
- Edit a coherent result, stage the resolved paths, and continue the merge or rebase. Use `git status` to distinguish unresolved paths from a completed resolution, and abort if the chosen integration direction is no longer safe.
- Run focused and full checks appropriate to the change, especially migrations, generated assets, dependency lockfiles, and deployment configuration. Ask the relevant owners when the conflict spans a contract boundary.
- A textual resolution can compile while changing runtime behavior. Treat it as a new integration change requiring review, not clerical cleanup.

## References

- [Git documentation: git-merge](https://git-scm.com/docs/git-merge)
- Further reading (blog): [GitHub Docs — resolving a merge conflict](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)

## What to learn next

- Official documentation: [Git: git-merge](https://git-scm.com/docs/git-merge)
- Manual or specification: [Pro Git: basic merge conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- Maintainer or personal blog: [Julia Evans — Git tips](https://jvns.ca/blog/2024/06/21/git-tips/)
- Technical blog: [GitHub Docs — resolving conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts)
- Hands-on guide: [Git: git-mergetool](https://git-scm.com/docs/git-mergetool)
