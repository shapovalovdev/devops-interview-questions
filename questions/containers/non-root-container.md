---
title: Run a containerized service as a non-root user
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, security, least-privilege, cks, kcsa]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#user
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://github.com/opencontainers/image-spec/blob/main/config.md
    source_type: standard
    verified_on: 2026-08-16
---

# Run a containerized service as a non-root user

What changes are needed to run an application image without root privileges?

## Answer guide

- Create a named unprivileged user in the image, make only required runtime paths owned or writable by it, and select it with `USER` (or an explicitly compatible runtime user).
- Verify the application does not require root-only ports, package-manager writes, or writes beneath root-owned application directories. Use a writable temporary directory or mounted data path deliberately.
- Running as non-root reduces the impact of a process compromise but is not a complete containment boundary; do not pair it with broad capabilities, privileged mode, or sensitive host mounts.
- Numeric UID/GID and volume ownership must work in the target runtime. A common failure is a container that starts locally but cannot write to a production-mounted path.
- The identity is an image-config field: the OCI image spec's `config.User` is honored by containerd, podman, and Kubernetes `runAsNonRoot` validation alike, and rootless podman remaps it through user namespaces — numeric-UID and volume-ownership pitfalls apply in every stack.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: USER](https://docs.docker.com/reference/dockerfile/#user)
- [Further reading: Docker Docs on runtime privileges and capabilities](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
- [OCI Image Format: image config](https://github.com/opencontainers/image-spec/blob/main/config.md)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
