---
title: Use named build targets for CI and debugging
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, dockerfile, multi-stage-builds, ci-cd]
sources:
  - url: https://docs.docker.com/build/building/multi-stage/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use named build targets for CI and debugging

When should CI build a named intermediate stage instead of only the final image?

## Answer guide

- Name stages and use `--target` when a test, lint, or debug workflow needs the toolchain stage without producing the runtime image.
- Keep production validation tied to the final stage as well. Passing unit tests in a builder image does not prove the runtime image contains required files, users, or libraries.
- Make stage contracts clear: a test stage should consume the intended source and dependencies, while the final stage copies only reviewed outputs.
- Avoid treating intermediate stages as production artifacts unless they have their own support, patching, and access-control policy.

## References

- [Docker Docs: Stop at a specific build stage](https://docs.docker.com/build/building/multi-stage/)
- Further reading (blog): [Docker: Advanced Dockerfiles with BuildKit and multistage builds](https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/)
