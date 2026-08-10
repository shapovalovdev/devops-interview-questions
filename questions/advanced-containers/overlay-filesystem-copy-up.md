---
title: Explain overlay filesystem copy-up and container writes
theme: advanced-containers
difficulty: senior
type: theory
tags: [containers, filesystem, images, performance, storage]
sources:
  - url: https://docs.docker.com/engine/storage/drivers/overlayfs-driver/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain overlay filesystem copy-up and container writes

Why can writing a file from an image layer have unexpected performance or storage consequences?

## Answer guide

- Overlay storage presents lower image layers and an upper writable layer as one filesystem. When a process modifies a lower-layer file, OverlayFS copies it into the upper layer before changing it.
- Keep mutable application data outside image layers in a suitable volume, and benchmark write-heavy paths with the deployed storage driver. Image layout can influence copy-up cost and cache behavior.
- Large or frequently modified lower-layer files can amplify disk use and latency. Assuming every runtime uses identical overlay semantics leads to portability and incident-response mistakes.

## References

- [Docker Docs: OverlayFS storage driver](https://docs.docker.com/engine/storage/drivers/overlayfs-driver/)
- Further reading (blog): [Docker: storage drivers](https://www.docker.com/blog/containers-101-attach-a-volume-to-a-container/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
