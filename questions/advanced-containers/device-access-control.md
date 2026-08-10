---
title: Control device access for a container workload
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, linux, security, least-privilege, filesystem]
sources:
  - url: https://docs.docker.com/engine/containers/run/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control device access for a container workload

A workload requests access to a host device. What should you review before granting it?

## Answer guide

- Identify the exact device operation and provide the narrowest supported device mapping and permissions rather than privileged mode. Treat devices as kernel interfaces, not ordinary files.
- Isolate device-consuming workloads to suitable nodes, validate device ownership and lifecycle, and monitor failures. Prefer a dedicated device plugin or managed service where an orchestration platform provides one.
- Device access can permit data exposure, hardware disruption, or kernel attack paths. A generic host device directory or privileged flag makes review and blast-radius control much harder.

## References

- [Docker Docs: runtime options](https://docs.docker.com/engine/containers/run/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
