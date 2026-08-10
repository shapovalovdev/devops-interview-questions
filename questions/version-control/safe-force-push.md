---
title: Repair a shared branch with a force push safely
theme: version-control
difficulty: senior
type: scenario
tags: [git, version-control, delivery, change-management, troubleshooting]
sources:
  - url: https://git-scm.com/docs/git-push
    source_type: official-docs
    verified_on: 2026-08-06
---

# Repair a shared branch with a force push safely

When can a force push be justified, and what procedure reduces the risk of losing collaborators' work?

## Answer guide

- Prefer a new revert or a normal corrective commit on a shared protected branch. Consider history rewriting only for a clearly scoped recovery where incorrect commits must be removed and branch policy permits it.
- Freeze concurrent updates, identify every affected ref and downstream consumer, retain a recovery ref, and verify the intended replacement history locally. Use `--force-with-lease` so the push refuses if the remote changed since the expected value.
- Communicate exact recovery commands and branch state to collaborators, update automation references, and run the same CI and release checks required for an ordinary integration.
- `--force-with-lease` protects against some races but is not a universal safety guarantee, especially with stale or shared tracking refs. Backup, review, and server controls are still necessary.

## References

- [Git documentation: git-push](https://git-scm.com/docs/git-push)
- Further reading (blog): [GitHub Blog — undo almost anything with Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)

## What to learn next

- Official documentation: [Git: git-push](https://git-scm.com/docs/git-push)
- Manual or specification: [Pro Git: rewriting history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
- Maintainer or personal blog: [Julia Evans — Git terminology](https://jvns.ca/)
- Technical blog: [GitHub Docs — non-fast-forward errors](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors)
- Hands-on guide: [Git: force-with-lease](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-leaseltrefnamegt)
