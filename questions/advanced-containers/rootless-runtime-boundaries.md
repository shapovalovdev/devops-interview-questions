---
title: Evaluate rootless container runtime boundaries
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, linux, rootless, user-namespace, security]
sources:
  - url: https://docs.docker.com/engine/security/rootless/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate rootless container runtime boundaries

What risk does rootless container operation reduce, and what does it not solve?

## Answer guide

- Rootless mode runs the daemon and containers inside a user namespace, reducing the impact of a daemon or container process compromise on the host's root account.
- Assess compatibility for storage, networking, privileged ports, cgroup delegation, observability, and build tooling before adopting it. Use supported subordinate UID/GID mappings and document operational differences.
- Rootless is not a blanket security guarantee: exposed APIs, vulnerable kernels, dangerous mounts, and excessive in-container privileges remain risks. Unsupported workarounds can quietly restore host-level privilege.

## References

- [Docker Docs: rootless mode](https://docs.docker.com/engine/security/rootless/)
- Further reading (blog): [Docker: user namespace remapping](https://www.docker.com/blog/understanding-the-docker-user-namespace-remapping/)
