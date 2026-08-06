---
title: Build a small runtime image with multi-stage builds
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, dockerfile, multi-stage-builds, images, security]
sources:
  - url: https://docs.docker.com/build/building/multi-stage/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a small runtime image with multi-stage builds

How would you build an application that needs compilers during build but not at runtime?

## Answer guide

- Use separate `FROM` stages: compile or package in a builder stage, then copy only the required artifact and runtime dependencies into a deliberately chosen final stage.
- Name stages and copy explicit outputs with `COPY --from`; this makes the runtime contents reviewable and prevents build tools, source trees, and transient caches from being carried forward by accident.
- A smaller final image can reduce attack surface and transfer time, but it must still include required certificates, shared libraries, users, and diagnostic approach appropriate to operations.
- Test the final stage, not only the builder. A common failure is an artifact linked to a library or expecting a path that existed only in the build image.

## References

- [Docker Docs: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Further reading: Dockerfile reference: COPY --from](https://docs.docker.com/reference/dockerfile/#copy---from)
