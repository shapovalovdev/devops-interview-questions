---
title: Evaluate rootless builders for shared CI
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, docker, rootless, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/security/rootless/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate rootless builders for shared CI

What security benefit and operating constraints come with rootless Docker or BuildKit workers?

## Answer guide

- Rootless mode runs the daemon and containers inside a user namespace, reducing the impact of a daemon compromise relative to a rootful daemon. It is defense in depth, not a guarantee against all host impact.
- Validate required features: networking, storage driver behavior, privileged operations, and host integrations can differ or be unavailable. Do not silently fall back to a rootful worker.
- Isolate tenants even with rootless mode through separate credentials, cache namespaces, repository allow-lists, and ephemeral workers. Shared builders still process untrusted code.
- Document debugging and performance differences before migration. A security improvement that makes releases unobservable or forces unsafe exceptions will not hold operationally.

## References

- [Docker Docs: Rootless mode](https://docs.docker.com/engine/security/rootless/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
