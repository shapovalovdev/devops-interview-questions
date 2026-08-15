---
title: Choose between CMD and ENTRYPOINT in a Docker image
theme: containers
difficulty: middle
type: theory
tags: [containers, docker, images]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#entrypoint
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://github.com/opencontainers/image-spec/blob/main/config.md
    source_type: standard
    verified_on: 2026-08-16
---

# Choose between CMD and ENTRYPOINT in a Docker image

How do `CMD` and `ENTRYPOINT` interact, and which form best supports a container that accepts useful runtime arguments?

## Answer guide

- `ENTRYPOINT` declares the image's executable; `CMD` supplies its default command or, with an exec-form `ENTRYPOINT`, default arguments. Runtime arguments replace `CMD` defaults while retaining that entrypoint.
- Prefer JSON/exec form for both when the image is an executable: it avoids an implicit shell, preserves argument boundaries, and lets the application receive signals directly.
- Use `CMD` alone when users should freely replace the command. Use an entrypoint plus default arguments when the executable is stable but its configuration is normally overridden.
- A shell-form entrypoint can leave a shell as PID 1 and may not forward stop signals or pass arguments as intended. Test `docker run image --help` and graceful stopping, not only the default invocation.
- `CMD` and `ENTRYPOINT` are spec fields, not Docker inventions: the OCI image config defines `config.Cmd` and `config.Entrypoint`, and containerd or podman combine them with the same override precedence when resolving the container's arguments.

## References

- [Dockerfile reference: ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint)
- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: ENTRYPOINT and CMD interaction](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact)
- [Further reading: Docker Docs on running containers](https://docs.docker.com/engine/containers/run/)
- [OCI Image Format: image config](https://github.com/opencontainers/image-spec/blob/main/config.md)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
