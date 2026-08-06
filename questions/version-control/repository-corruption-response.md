---
title: Respond to suspected Git repository corruption
theme: version-control
difficulty: senior
type: troubleshooting
tags: [git, version-control, troubleshooting, recovery, reliability]
sources:
  - url: https://git-scm.com/docs/git-fsck
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/git-clone
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to suspected Git repository corruption

How would you investigate a repository reporting missing or corrupt Git objects without destroying recovery evidence?

## Answer guide

- Stop cleanup and preserve a copy of the repository and error output. Run `git fsck` to inspect object connectivity and integrity, then identify whether the problem is local storage, an interrupted transfer, a bad remote, or an expected unreachable object.
- Compare with a known-good remote or independent clone, fetch missing reachable objects where appropriate, and restore from authoritative backups or mirrors rather than editing object files manually.
- Verify refs, release tags, CI checkouts, and the repaired object graph before declaring recovery complete. Record the scope, affected commits, host, storage health, and prevention action.
- Do not run aggressive garbage collection or overwrite the only broken copy first. Those actions can remove dangling objects that are valuable for reconstruction.

## References

- [Git documentation: git-fsck](https://git-scm.com/docs/git-fsck)
- [Git documentation: git-clone](https://git-scm.com/docs/git-clone)
- Further reading (blog): [GitHub Blog — Git database internals](https://github.blog/open-source/git/git-database-internals-i-packed-object-store/)

## What to learn next

- Official documentation: [Git: git-fsck](https://git-scm.com/docs/git-fsck)
- Manual or specification: [Pro Git: data recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)
- Maintainer or personal blog: [Derrick Stolee's Git blog](https://stolee.dev/)
- Technical blog: [GitHub Blog — Git database internals](https://github.blog/open-source/git/git-database-internals-i-packed-object-store/)
- Hands-on guide: [Git: git-gc](https://git-scm.com/docs/git-gc)
