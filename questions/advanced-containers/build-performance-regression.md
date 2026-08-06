---
title: Diagnose a container-build performance regression
theme: advanced-containers
difficulty: senior
type: troubleshooting
tags: [containers, docker, build-cache, troubleshooting, performance]
sources:
  - url: https://docs.docker.com/build/cache/optimize/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a container-build performance regression

Build time doubled after a small change. How do you find the cause without weakening release controls?

## Answer guide

- Compare the build graph, context size, cache-hit logs, base-image resolution, dependency steps, target platform, and remote-cache transfer before changing the Dockerfile.
- Identify the first invalidated expensive step. Common causes are broad `COPY`, generated files in context, altered dependency manifests, changed build arguments, or a builder/cache backend change.
- Test a minimal reproduction and retain clean-build correctness. Do not solve a regression by caching secrets, skipping dependency verification, or reusing an unreviewed artifact.
- Measure the full CI critical path, not only local CPU time. Remote cache and emulation can shift cost to network transfer or platform execution.

## References

- [Docker Docs: Optimize cache usage](https://docs.docker.com/build/cache/optimize/)
- Further reading (blog): [Docker: Advanced Dockerfiles with BuildKit and multistage builds](https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/)
