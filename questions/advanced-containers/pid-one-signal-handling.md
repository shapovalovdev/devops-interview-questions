---
title: Design correct PID 1 signal handling in a container
theme: advanced-containers
difficulty: junior
type: scenario
tags: [containers, linux, pid-1, signals, reliability]
sources:
  - url: https://docs.docker.com/engine/containers/run/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design correct PID 1 signal handling in a container

Your service ignores graceful termination during deployment. How should its container entrypoint behave?

## Answer guide

- Run the service as the intended PID 1 using exec-form entrypoints, or use a small init that forwards signals and reaps children. Docker sends the configured stop signal before forcefully killing the container.
- The application must handle its termination signal, stop accepting work, drain within the configured grace period, and exit nonzero only for a failure. Test this lifecycle under the production orchestrator.
- A shell wrapper that does not exec can absorb signals or leave zombies. An overly short grace period turns normal shutdown into data loss, while an unlimited one can block replacement capacity.

## References

- [Docker Docs: running containers](https://docs.docker.com/engine/containers/run/)
- Further reading (blog): [Docker: best practices for RUN, CMD, and ENTRYPOINT](https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
