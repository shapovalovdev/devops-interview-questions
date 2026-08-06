---
title: Release a multi-platform container image
theme: containers
difficulty: senior
type: scenario
tags: [containers, docker, images, multi-platform, registries, automation]
sources:
  - url: https://docs.docker.com/build/building/multi-platform/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Release a multi-platform container image

How do you release one image reference for both amd64 and arm64 workloads without losing release traceability?

## Answer guide

- Build and test artifacts for each target platform, then publish a multi-platform image index/manifest list that points to the platform-specific manifests under a controlled release reference.
- Ensure every architecture receives equivalent source revision, dependency policy, scanning, and functional tests. A successful amd64 build is not evidence that the arm64 image starts or behaves correctly.
- Record the top-level and platform-specific digests in release evidence. Deployment resolution can select different platform manifests under one tag or index.
- Prefer native builders for performance and fidelity where practical; emulation can be slower and may not expose every architecture-specific behavior. Define how a platform-specific rollback is handled.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)
- [Further reading: OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/image-index.md)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
