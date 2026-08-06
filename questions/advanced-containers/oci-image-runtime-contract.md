---
title: Explain the OCI image and runtime contract
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, images, container-runtime, docker]
sources:
  - url: https://github.com/opencontainers/image-spec/blob/main/spec.md
    source_type: standard
    verified_on: 2026-08-06
---

# Explain the OCI image and runtime contract

What is the boundary between an OCI image and an OCI runtime bundle?

## Answer guide

- An OCI image is content-addressed configuration plus ordered filesystem layers and descriptors. It is an artifact for distribution, not a running process.
- To run it, an implementation unpacks a root filesystem and combines it with a runtime configuration describing the process, mounts, namespaces, Linux capabilities, and resources.
- Image configuration supplies defaults such as entrypoint, environment, and working directory, but the runtime or orchestrator can override them. Do not assume an image alone defines production isolation.
- Digest integrity identifies retrieved content; it does not establish that content is trustworthy. Verify provenance and apply runtime policy separately.

## References

- [OCI Image Specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
