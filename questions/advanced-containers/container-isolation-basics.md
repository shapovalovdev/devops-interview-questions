---
title: Explain the Linux primitives behind container isolation
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, linux, namespaces, cgroups, process-isolation]
sources:
  - url: https://man7.org/linux/man-pages/man7/namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the Linux primitives behind container isolation

Which Linux primitives make a container distinct from another process?

## Answer guide

- A container is an ordinary host process configured with namespaces for views of global resources, cgroups for resource accounting and limits, and filesystem/mount setup; it is not a virtual machine.
- Namespaces isolate identifiers and visibility, while cgroups control CPU, memory, I/O, and process resources. The runtime also applies credentials, capabilities, and optional seccomp policy before exec.
- These mechanisms are layered rather than absolute: kernel vulnerabilities, dangerous privileges, host mounts, or a privileged runtime socket can defeat the boundary. Treat workloads as mutually distrustful only with defense in depth.

## References

- [Linux man-pages: namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- Further reading (blog): [Docker: What is a container?](https://www.docker.com/resources/what-container/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
