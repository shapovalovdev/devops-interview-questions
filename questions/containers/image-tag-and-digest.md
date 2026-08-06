---
title: Distinguish image tags from digests
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, images, image-tags, image-digests]
sources:
  - url: https://docs.docker.com/reference/cli/docker/image/pull/#pull-an-image-by-digest-immutable-identifier
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish image tags from digests

What is the difference between an image tag and an image digest, and when should deployment use each?

## Answer guide

- A tag is a mutable human-readable reference in a registry; publishers can move it to a different image. A digest identifies immutable image content for a particular manifest.
- Use a digest, or record the resolved digest, when reproducibility and auditability matter. Tags are convenient selection labels such as release channels, not proof of the deployed bytes.
- A digest does not itself establish that content is safe or approved; pair it with provenance, scanning, and an admission or deployment policy appropriate to the environment.
- Avoid assuming a tag resolves identically across time, registries, or platforms. Multi-platform images can select a platform-specific manifest under one higher-level reference.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker CLI reference: pull by digest](https://docs.docker.com/reference/cli/docker/image/pull/#pull-an-image-by-digest-immutable-identifier)
- [Further reading: OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/README.md)
