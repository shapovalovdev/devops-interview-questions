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
---

# Make a container stop gracefully

Why does PID 1 matter in a container, and how do you prevent a stop request from becoming a forced kill?

## Answer guide

- Docker sends the configured stop signal to the container's main process, normally SIGTERM, then sends SIGKILL after the timeout if it has not exited. The main process must handle its shutdown contract.
- Use an exec-form entrypoint so the application is PID 1, or use a small init/supervisor when the container genuinely manages child processes. A shell wrapper must `exec` the long-running process or correctly forward signals and reap children.
- Make shutdown bounded: stop accepting new work, drain or checkpoint according to the service semantics, then exit before the deployment timeout.
- Test termination under load. A too-short grace period risks lost work; an unbounded shutdown delays rollouts and can exhaust capacity.

## References

- [Dockerfile reference: ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint)
- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: shell-form ENTRYPOINT and signals](https://docs.docker.com/reference/dockerfile/#shell-form-entrypoint-example)
- [Further reading: Docker Docs on stop signals](https://docs.docker.com/reference/dockerfile/#stopsignal)
