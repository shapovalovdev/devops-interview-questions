---
title: Make a container stop gracefully
theme: containers
difficulty: middle
type: troubleshooting
tags: [containers, docker, signals, reliability, troubleshooting]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#entrypoint
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://github.com/opencontainers/runtime-spec/blob/main/runtime.md
    source_type: standard
    verified_on: 2026-08-16
---

# Make a container stop gracefully

Why does PID 1 matter in a container, and how do you prevent a stop request from becoming a forced kill?

## Answer guide

- Docker sends the configured stop signal to the container's main process, normally SIGTERM, then sends SIGKILL after the timeout if it has not exited. The main process must handle its shutdown contract.
- Use an exec-form entrypoint so the application is PID 1, or use a small init/supervisor when the container genuinely manages child processes. A shell wrapper must `exec` the long-running process or correctly forward signals and reap children.
- Make shutdown bounded: stop accepting new work, drain or checkpoint according to the service semantics, then exit before the deployment timeout.
- Test termination under load. A too-short grace period risks lost work; an unbounded shutdown delays rollouts and can exhaust capacity.
- Signal handling follows the OCI runtime contract: the spec's lifecycle defines signal-then-timeout-then-kill termination, and podman stop or containerd's stop apply the same SIGTERM-to-SIGKILL sequence — the image's shutdown contract is the part that must be portable.

## References

- [Dockerfile reference: ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint)
- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: shell-form ENTRYPOINT and signals](https://docs.docker.com/reference/dockerfile/#shell-form-entrypoint-example)
- [Further reading: Docker Docs on stop signals](https://docs.docker.com/reference/dockerfile/#stopsignal)
- [OCI Runtime Specification: lifecycle](https://github.com/opencontainers/runtime-spec/blob/main/runtime.md)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
