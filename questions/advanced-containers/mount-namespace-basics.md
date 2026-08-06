---
title: Explain mount namespaces and a container root filesystem
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, linux, namespaces, mount-namespace, filesystem]
sources:
  - url: https://man7.org/linux/man-pages/man7/mount_namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain mount namespaces and a container root filesystem

How does a container get a filesystem view that differs from the host?

## Answer guide

- A mount namespace owns a process's mount table. A runtime constructs a root filesystem, bind mounts required paths, and starts the container process with that namespace as its filesystem view.
- Mount propagation determines whether later mount and unmount events cross namespace boundaries. Set propagation deliberately for workloads that mount filesystems or use nested runtimes.
- Read-only roots reduce accidental mutation but do not protect writable mounts, tmpfs, secrets, or volumes. A host-path mount can expose host data and is a major isolation decision.

## References

- [Linux man-pages: mount namespaces](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html)
- Further reading (blog): [Docker: bind mounts](https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)
