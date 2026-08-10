---
title: Decide when containers should share a namespace
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, linux, namespaces, networking, process-isolation]
sources:
  - url: https://man7.org/linux/man-pages/man7/namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Decide when containers should share a namespace

When is sharing PID, network, or IPC namespaces appropriate, and what changes operationally?

## Answer guide

- Share a namespace only for a defined cooperation need, such as a tightly coupled sidecar on localhost. Document which namespace is shared and which processes own lifecycle, ports, and cleanup.
- Sharing changes observability and blast radius: processes can see or signal peers in a shared PID namespace, and network peers share local ports and socket visibility. Apply identity and policy at remaining boundaries.
- Accidental namespace sharing can expose credentials, permit interference, or make incident diagnosis ambiguous. Isolated namespaces can instead add operational complexity when the components genuinely require local coordination.

## References

- [Linux man-pages: namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- Further reading (blog): [Docker: networking overview](https://www.docker.com/blog/docker-networking-tutorial/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
