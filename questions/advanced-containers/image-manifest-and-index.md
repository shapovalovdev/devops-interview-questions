---
title: Distinguish an OCI image manifest from an image index
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, images, multi-platform, registries]
sources:
  - url: https://github.com/opencontainers/image-spec/blob/main/image-index.md
    source_type: standard
    verified_on: 2026-08-06
---

# Distinguish an OCI image manifest from an image index

How does a registry tag select the right image for more than one CPU architecture?

## Answer guide

- A manifest describes one image: its configuration object and ordered layer descriptors. An image index is a higher-level descriptor list that can point to manifests for multiple platforms.
- A client chooses a compatible manifest using platform metadata such as operating system and architecture. The selected platform artifact has its own digest.
- Publish and test every platform variant intentionally; an index cannot make an amd64 binary runnable on arm64. Also verify that native dependencies and base images exist for each target.
- Pinning the index digest locks the index content, while pinning a platform manifest locks one variant. Choose based on whether deployment should follow a multi-platform release or a fixed platform artifact.

## References

- [OCI Image Index Specification](https://github.com/opencontainers/image-spec/blob/main/image-index.md)
- Further reading (blog): [Docker: Advanced Dockerfiles with BuildKit and multistage builds](https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/)
