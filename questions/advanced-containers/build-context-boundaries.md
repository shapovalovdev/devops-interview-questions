---
title: Explain Docker build-context boundaries
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, docker, dockerfile, security]
sources:
  - url: https://docs.docker.com/build/building/context/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Docker build-context boundaries

Why can a Dockerfile not normally copy arbitrary files from the builder host?

## Answer guide

- A build receives an explicit context, such as a directory, Git repository, URL, or stdin. `COPY` and `ADD` resolve source files within that supplied context rather than arbitrary host paths.
- This boundary makes remote and local builds portable and limits accidental disclosure of host files. `.dockerignore` further excludes paths before the context is sent.
- Passing a large repository or secrets in the context harms cache performance and risks embedding them in layers. Inspect context rules as security controls, not only as build-speed tuning.
- If a build truly needs separate inputs, use an explicitly declared named context or a secret/SSH mount where supported, with least privilege and CI access controls.

## References

- [Docker Docs: Build context](https://docs.docker.com/build/building/context/)
- Further reading (blog): [Docker: Dockerfiles now support multiple build contexts](https://www.docker.com/blog/dockerfiles-now-support-multiple-build-contexts/)
