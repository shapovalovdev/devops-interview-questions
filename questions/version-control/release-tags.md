---
title: Create an auditable release tag
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, delivery, supply-chain]
sources:
  - url: https://git-scm.com/docs/git-tag
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create an auditable release tag

How would you use Git tags to identify a release artifact unambiguously?

## Answer guide

- Tag the exact commit that passed the required build, test, review, and approval gates, and record the immutable commit ID in release metadata. Annotated tags carry a tag message, tagger identity, and optional signature; lightweight tags are only refs.
- Use a documented versioning and tag namespace convention, push the tag explicitly, and configure the build system to derive or verify the artifact provenance from that commit and tag.
- Protect release-tag creation and deletion according to repository policy. Verify the tag exists on the remote and that deployment automation does not silently retag a different commit.
- A tag name alone is not a reproducibility guarantee: mutable dependencies, non-hermetic builds, and mutable container labels can still produce different artifacts from the same commit.

## References

- [Git documentation: git-tag](https://git-scm.com/docs/git-tag)
- Further reading (blog): [GitHub Docs — about releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

## What to learn next

- Official documentation: [Git: git-tag](https://git-scm.com/docs/git-tag)
- Manual or specification: [Pro Git: tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- Maintainer or personal blog: [Julia Evans — Git tips](https://jvns.ca/)
- Technical blog: [GitHub Docs — releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- Hands-on guide: [Git: git-verify-tag](https://git-scm.com/docs/git-verify-tag)
