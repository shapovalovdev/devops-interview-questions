---
title: Explain local branches and remote-tracking branches
theme: version-control
difficulty: junior
type: theory
tags: [git, version-control, delivery]
sources:
  - url: https://git-scm.com/docs/git-branch
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/git-fetch
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain local branches and remote-tracking branches

What is the difference between a local branch and `origin/main`, and what changes each one?

## Answer guide

- A local branch is a mutable local ref that you can commit on. `origin/main` is conventionally a remote-tracking ref: the local record of the remote branch's last fetched state, not a writable branch on the server.
- `git fetch` updates remote-tracking refs according to its refspec without integrating them into the checked-out branch. A merge or rebase then chooses how to incorporate that fetched history locally.
- Push updates a remote ref only if server policy and the proposed ref update permit it. Check the configured upstream and compare local, upstream, and fetched commits before pushing a release or hotfix.
- Avoid assuming a remote-tracking name is live. It can be stale until fetched, and several remotes can have a branch called `main`; use explicit remote names in incident work.

## References

- [Git documentation: git-branch](https://git-scm.com/docs/git-branch)
- [Git documentation: git-fetch](https://git-scm.com/docs/git-fetch)
- Further reading (blog): [GitHub Blog — Git remote workflows](https://github.blog/open-source/git/)

## What to learn next

- Official documentation: [Git: git-branch](https://git-scm.com/docs/git-branch)
- Manual or specification: [Pro Git: remote branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches)
- Maintainer or personal blog: [Julia Evans — Git terminology](https://jvns.ca/)
- Technical blog: [GitHub Docs — working with remotes](https://docs.github.com/en/get-started/git-basics/about-remote-repositories)
- Hands-on guide: [Git: git-remote](https://git-scm.com/docs/git-remote)
