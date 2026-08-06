---
title: Design a reproducible container image build
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, docker, images, supply-chain, ci-cd]
sources:
  - url: https://docs.docker.com/build/ci/github-actions/reproducible-builds/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a reproducible container image build

What controls make an image build reproducible enough to investigate a production artifact?

## Answer guide

- Record the source revision, Dockerfile syntax, builder version, build arguments, target platform, base-image digests, and final artifact digest. Pinning tags alone is insufficient because tags can move.
- Remove avoidable nondeterminism such as changing download URLs, implicit current time, and unpinned package indexes. Where exact byte reproducibility is not feasible, state the expected variance.
- Rebuild independently and compare digests or explain differences through retained build metadata. A cache hit is not proof of reproducibility.
- Balance strict pinning with patch velocity: create an automated, reviewed process to refresh trusted base images and dependencies rather than freezing vulnerable inputs indefinitely.

## References

- [Docker Docs: Reproducible builds with GitHub Actions](https://docs.docker.com/build/ci/github-actions/reproducible-builds/)
- Further reading (blog): [Docker: Intro guide to Dockerfile best practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
