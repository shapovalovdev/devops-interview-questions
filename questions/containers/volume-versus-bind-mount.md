---
title: Choose a Docker volume or a bind mount
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, storage, volumes]
sources:
  - url: https://docs.docker.com/engine/storage/volumes/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a Docker volume or a bind mount

How do Docker-managed volumes differ from bind mounts, and which would you use for service data versus local source-code iteration?

## Answer guide

- A volume is managed by Docker and stored outside the container's writable layer; Docker supplies lifecycle commands and it is the preferred mechanism for persistent container data.
- A bind mount exposes a chosen host path directly into a container. It is useful for local development or when the host path is deliberately part of the integration contract.
- Use a named volume or external managed storage for production service data, with backup, restore, ownership, and retention defined outside the image. Use a bind mount for source iteration only when host coupling is intended.
- Bind mounts can obscure image files at the target path and grant host-file access; wrong paths or permissions cause environment-specific failures. Neither mount type substitutes for a database-consistency backup strategy.

## References

- [Docker Docs: Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Further reading: Docker Docs on bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
