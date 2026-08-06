---
title: Produce a traceable semantic-version release
theme: ci-cd
difficulty: junior
type: scenario
tags: [ci-cd, git, delivery, automation]
sources:
  - url: https://semver.org/
    source_type: standard
    verified_on: 2026-08-06
---

# Produce a traceable semantic-version release

How should a pipeline create a release version that users can trace back to code and artifacts?

## Answer guide

- Select a version according to the project’s published compatibility policy; semantic versioning communicates intended API compatibility, not proof that no regression exists.
- Create an annotated, protected release tag pointing to the reviewed commit, then build and publish the artifact once with that version and its immutable digest.
- Publish release notes, checksums or attestations, and rollback guidance. Avoid retagging a released version: consumers may cache or verify the original content.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Semantic Versioning specification](https://semver.org/)
- [Further reading: Git—tag documentation](https://git-scm.com/docs/git-tag)
