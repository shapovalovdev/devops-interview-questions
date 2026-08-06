---
title: Design a seccomp profile for a container workload
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, linux, seccomp, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/security/seccomp/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a seccomp profile for a container workload

How should a team tailor seccomp without breaking a production application?

## Answer guide

- Seccomp filters system calls at the kernel boundary. Begin with the runtime default profile, identify the application and dependency syscall needs under representative load, and make the narrowest documented exception.
- Keep the profile with the workload definition, test it on each supported architecture and kernel family, and log denials in a safe pre-enforcement phase where possible.
- An allowlist copied from another application may fail after a runtime or library upgrade. A broad unconfined profile removes a useful containment layer and should trigger security review.

## References

- [Docker Docs: seccomp security profiles](https://docs.docker.com/engine/security/seccomp/)
- Further reading (blog): [Docker: seccomp profiles](https://www.docker.com/blog/securing-containers-with-seccomp/)
