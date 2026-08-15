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
  - url: https://github.com/opencontainers/image-spec/blob/main/descriptor.md
    source_type: standard
    verified_on: 2026-08-16
---

# Distinguish image tags from digests

What is the difference between an image tag and an image digest, and when should deployment use each?

## Answer guide

- A tag is a mutable human-readable reference in a registry; publishers can move it to a different image. A digest identifies immutable image content for a particular manifest.
- Use a digest, or record the resolved digest, when reproducibility and auditability matter. Tags are convenient selection labels such as release channels, not proof of the deployed bytes.
- A digest does not itself establish that content is safe or approved; pair it with provenance, scanning, and an admission or deployment policy appropriate to the environment.
- Avoid assuming a tag resolves identically across time, registries, or platforms. Multi-platform images can select a platform-specific manifest under one higher-level reference.
- Digest addressing is spec-level and registry-level: the OCI image specification defines the content descriptor whose hash a digest is, and containerd's image service or `podman pull` resolve `name@sha256:...` identically — only tag convenience syntax varies.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker CLI reference: pull by digest](https://docs.docker.com/reference/cli/docker/image/pull/#pull-an-image-by-digest-immutable-identifier)
- [Further reading: OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/README.md)
- [OCI Image Format: descriptors](https://github.com/opencontainers/image-spec/blob/main/descriptor.md)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
