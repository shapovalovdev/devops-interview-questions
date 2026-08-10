---
title: Establish a container runtime hardening baseline
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, security, seccomp, capabilities, rootless, governance]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish a container runtime hardening baseline

What should a platform baseline require to reduce runtime attack surface without blocking ordinary workloads?

## Answer guide

- Default to a non-root user, dropped capabilities, no privileged mode, no host namespaces, controlled mounts, a read-only root where practical, and the runtime default seccomp profile. Make deviations explicit and reviewable.
- Enforce the baseline through templates or admission controls, test it against supported workloads, and expose clear diagnostics and an exception path. Patch the host kernel and runtime using an owned lifecycle.
- Hardening is ineffective if users can reach an unrestricted daemon socket or deploy arbitrary host mounts. Excessively rigid controls also cause bypasses, so measure exceptions and improve safe platform interfaces.

## References

- [Docker Docs: security](https://docs.docker.com/engine/security/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
