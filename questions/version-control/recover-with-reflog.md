---
title: Recover a locally lost commit with reflog
theme: version-control
difficulty: middle
type: troubleshooting
tags: [git, version-control, troubleshooting, recovery]
sources:
  - url: https://git-scm.com/docs/git-reflog
    source_type: official-docs
    verified_on: 2026-08-06
---

# Recover a locally lost commit with reflog

After an accidental reset, how would you recover a local commit without making the situation worse?

## Answer guide

- Stop destructive cleanup and inspect `git reflog` for the previous value of HEAD or the branch ref. Reflogs record local ref updates and often expose the commit ID that was moved away from.
- Create a new recovery branch or tag at the candidate commit before changing the original branch again. Inspect its tree and parents, then choose a merge, cherry-pick, or coordinated branch restoration procedure.
- Reflogs are local and expire according to configuration; another clone, remote ref, backup, or object database may be necessary when the original machine is unavailable or pruning has occurred.
- Do not force-push a guessed repair to a shared branch. Preserve evidence, coordinate with collaborators, and verify the intended history and CI results before publishing a recovery.

## References

- [Git documentation: git-reflog](https://git-scm.com/docs/git-reflog)
- Further reading (blog): [GitHub Blog — undo almost anything with Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)

## What to learn next

- Official documentation: [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- Manual or specification: [Pro Git: data recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)
- Maintainer or personal blog: [Julia Evans — Git terminology](https://jvns.ca/)
- Technical blog: [GitHub Blog — undo almost anything](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)
- Hands-on guide: [Git: git-fsck](https://git-scm.com/docs/git-fsck)
