---
title: Run a containerized service as a non-root user
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, security, least-privilege]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#user
    source_type: official-docs
    verified_on: 2026-08-06
---

# Run a containerized service as a non-root user

What changes are needed to run an application image without root privileges?

## Answer guide

- Create a named unprivileged user in the image, make only required runtime paths owned or writable by it, and select it with `USER` (or an explicitly compatible runtime user).
- Verify the application does not require root-only ports, package-manager writes, or writes beneath root-owned application directories. Use a writable temporary directory or mounted data path deliberately.
- Running as non-root reduces the impact of a process compromise but is not a complete containment boundary; do not pair it with broad capabilities, privileged mode, or sensitive host mounts.
- Numeric UID/GID and volume ownership must work in the target runtime. A common failure is a container that starts locally but cannot write to a production-mounted path.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: USER](https://docs.docker.com/reference/dockerfile/#user)
- [Further reading: Docker Docs on runtime privileges and capabilities](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
