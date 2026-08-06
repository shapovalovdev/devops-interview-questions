---
title: Choose between Git revert and reset for a bad change
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, delivery, troubleshooting]
sources:
  - url: https://git-scm.com/docs/git-revert
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose between Git revert and reset for a bad change

A defective commit is already on a shared branch. When should you create a revert rather than rewriting history with reset?

## Answer guide

- `git revert` creates a new commit that applies the inverse of a selected commit. It preserves the shared branch's history, which makes it the usual recovery for a bad change already pulled, reviewed, or deployed by other people.
- `git reset` moves a branch reference and can discard or unstage local changes depending on its mode. Updating a shared remote to that rewritten history normally needs a force push and can disrupt collaborators with descendants of the old tip.
- Before reverting, inspect the target and its dependent changes: an inverse patch can conflict or be unsafe after later migrations, configuration changes, or releases. Revert the smallest safe unit, validate it in CI, and communicate the deployment effect.
- Coordinated history rewriting can be reasonable for an explicitly private or protected recovery branch, but it needs an agreed stop-the-line procedure and a force-with-lease style safeguard; it is not a substitute for a production rollback.

## References

- [Git documentation: git-revert](https://git-scm.com/docs/git-revert)
- Further reading (blog): [GitHub Blog: undoing changes in Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)
