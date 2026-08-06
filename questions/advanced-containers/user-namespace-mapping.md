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
