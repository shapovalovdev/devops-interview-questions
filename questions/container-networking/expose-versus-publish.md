---
title: Distinguish EXPOSE from port publishing
theme: container-networking
difficulty: junior
type: theory
tags: [containers, docker, networking, tcp, security]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#expose
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish EXPOSE from port publishing

What is the difference between Dockerfile `EXPOSE` and publishing a container port?

## Answer guide

- `EXPOSE` documents that an image expects to listen on a port; it does not publish that port to the host. Publishing is requested when the container is run, for example with `-p`.
- A published port creates a host-to-container mapping. Its host address matters: a loopback binding limits who can reach it, whereas a wildcard binding may expose it on host interfaces.
- Keep image intent separate from deployment exposure. The same image can safely run behind an internal network in one environment and be explicitly published in another.
- Do not infer application health from either instruction. Confirm the process bind address, published mapping, host firewall, and upstream proxy or load balancer.

## References

- [Docker Docs: EXPOSE instruction](https://docs.docker.com/reference/dockerfile/#expose)
- Further reading (blog): [Docker: Port publishing and network hardening](https://www.docker.com/blog/docker-engine-28-hardening-container-networking-by-default/)
