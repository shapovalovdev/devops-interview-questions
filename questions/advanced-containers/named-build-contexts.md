---
title: Use named build contexts without losing traceability
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, dockerfile, supply-chain, automation]
sources:
  - url: https://docs.docker.com/build/building/context/#named-contexts
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use named build contexts without losing traceability

When are named build contexts useful, and what release controls do they need?

## Answer guide

- Named contexts make explicitly supplied additional inputs available to Dockerfile instructions that accept `--from`; they are useful for shared source, generated inputs, or a separate build target.
- Pin remote source revisions or image digests and record them in build metadata. An unpinned branch or tag makes the result non-reproducible.
- Keep inputs minimal and trust-scoped. A named context can widen the build's access even though it avoids copying arbitrary parent-directory files.
- Prefer a self-contained Dockerfile when it is simpler. Multiple contexts add configuration that must be reproduced locally, in CI, and during incident investigation.

## References

- [Docker Docs: Named contexts](https://docs.docker.com/build/building/context/#named-contexts)
- Further reading (blog): [Docker: Dockerfiles now support multiple build contexts](https://www.docker.com/blog/dockerfiles-now-support-multiple-build-contexts/)
