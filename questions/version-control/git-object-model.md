---
title: Explain Git's object model
theme: version-control
difficulty: junior
type: theory
tags: [git, version-control]
sources:
  - url: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Git's object model

What are blobs, trees, commits, and refs in Git, and why does that model matter when investigating a repository?

## Answer guide

- A blob stores file content, a tree records names and modes pointing to blobs or other trees, and a commit points to a root tree plus parent commit IDs and author metadata. Git identifies these objects by content-derived object IDs.
- A branch name is a movable ref to a commit; a tag is normally a named ref too. The working tree and index are mutable views used to construct the next snapshot, rather than the permanent history itself.
- This model makes history inspection and recovery understandable: compare tree snapshots, inspect parents, and locate reachable or dangling objects before attempting repair. Hash IDs alone are not a security boundary against an untrusted repository.
- Avoid equating a branch with a folder of changes. Deleting a ref can make commits unreachable, while clones, reflogs, or another ref may still retain them until pruning occurs.

## References

- [Pro Git: Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- Further reading (personal blog): [Julia Evans — confusing Git terminology](https://jvns.ca/)

## What to learn next

- Official documentation: [Git glossary](https://git-scm.com/docs/gitglossary)
- Manual or specification: [Pro Git: Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- Maintainer or personal blog: [Julia Evans — Git objects](https://jvns.ca/)
- Technical blog: [GitHub Blog — Git's database internals](https://github.blog/open-source/git/)
- Hands-on guide: [Pro Git: plumbing and porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
