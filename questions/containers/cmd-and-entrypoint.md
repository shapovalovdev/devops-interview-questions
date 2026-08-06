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
---

# Choose between CMD and ENTRYPOINT in a Docker image

How do `CMD` and `ENTRYPOINT` interact, and which form best supports a container that accepts useful runtime arguments?

## Answer guide

- `ENTRYPOINT` declares the image's executable; `CMD` supplies its default command or, with an exec-form `ENTRYPOINT`, default arguments. Runtime arguments replace `CMD` defaults while retaining that entrypoint.
- Prefer JSON/exec form for both when the image is an executable: it avoids an implicit shell, preserves argument boundaries, and lets the application receive signals directly.
- Use `CMD` alone when users should freely replace the command. Use an entrypoint plus default arguments when the executable is stable but its configuration is normally overridden.
- A shell-form entrypoint can leave a shell as PID 1 and may not forward stop signals or pass arguments as intended. Test `docker run image --help` and graceful stopping, not only the default invocation.

## References

- [Dockerfile reference: ENTRYPOINT and CMD interaction](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact)
- [Further reading: Docker Docs on running containers](https://docs.docker.com/engine/containers/run/)
