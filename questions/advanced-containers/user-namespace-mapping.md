---
title: Explain user namespace UID and GID mapping
theme: advanced-containers
difficulty: middle
type: theory
tags: [containers, linux, namespaces, user-namespace, security]
sources:
  - url: https://man7.org/linux/man-pages/man7/user_namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain user namespace UID and GID mapping

Why can root in a container map to an unprivileged ID on the host?

## Answer guide

- A user namespace maps user and group IDs between the namespace and its parent. A process can have UID 0 for namespace-local permission checks while mapping to a non-root host ID.
- File ownership, bind mounts, capabilities, and nested namespaces must be evaluated against the mapping. Test access from both inside and outside the container rather than assuming names imply equal privilege.
- Mapping does not authorize arbitrary host files and it does not erase kernel attack surface. Incorrect ownership ranges or insecure host mounts can cause outages or weaken the separation.

## References

- [Linux man-pages: user namespaces](https://man7.org/linux/man-pages/man7/user_namespaces.7.html)
- Further reading (blog): [Docker: user namespace remapping](https://www.docker.com/blog/understanding-the-docker-user-namespace-remapping/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
