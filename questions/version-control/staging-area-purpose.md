---
title: Explain the purpose of Git's staging area
theme: version-control
difficulty: junior
type: theory
tags: [git, version-control, delivery]
sources:
  - url: https://git-scm.com/docs/git-add
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the purpose of Git's staging area

Why does Git have an index (staging area), and how should an engineer use it when preparing a change?

## Answer guide

- The index is the proposed contents of the next commit. `git add` updates selected paths in that index; `git commit` records the indexed tree, not every current working-tree edit.
- Use it to form a small coherent commit: review the diff, stage only related hunks or files, and make the message describe the change that CI and reviewers can reason about. Keep generated files and secrets out of it.
- Confirm both `git diff` and `git diff --cached` before committing, because they show different comparisons. A partial stage can be intentional but is easy to misunderstand during an urgent fix.
- Do not treat staging as a backup or an approval workflow. It is local state and can be replaced by later add/reset operations; use commits and reviewed remote branches for durable collaboration.

## References

- [Git documentation: git-add](https://git-scm.com/docs/git-add)
- Further reading (blog): [GitHub Blog — undo almost anything with Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)

## What to learn next

- Official documentation: [Git: git-add](https://git-scm.com/docs/git-add)
- Manual or specification: [Pro Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- Maintainer or personal blog: [Julia Evans — Git terminology](https://jvns.ca/)
- Technical blog: [GitHub Blog — Git tips](https://github.blog/open-source/git/)
- Hands-on guide: [Pro Git: interactive staging](https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging)
