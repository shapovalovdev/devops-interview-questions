---
title: Control Docker build context with .dockerignore
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, dockerfile, security]
sources:
  - url: https://docs.docker.com/build/concepts/context/#dockerignore-files
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control Docker build context with .dockerignore

Why should an application repository define a `.dockerignore` file, and what must it exclude?

## Answer guide

- The build context is the file set sent to the builder. A `.dockerignore` file removes matching paths before the build, reducing transfer and preventing accidental `COPY` of irrelevant files.
- Exclude dependency directories, test outputs, local configuration, VCS data where it is not needed, credentials, and other files that do not belong in the image.
- Do not rely on `.dockerignore` as a secret-management control: a secret that is needed during a build needs a dedicated secret mechanism, and a secret already copied into a layer can remain recoverable from image history.
- Validate patterns against the actual build context. Over-broad exclusions can make builds fail only in CI; missing exclusions can leak sensitive material or invalidate cache unnecessarily.

## References

- [Docker Docs: .dockerignore files](https://docs.docker.com/build/concepts/context/#dockerignore-files)
- [Further reading: Docker Docs on build context](https://docs.docker.com/build/concepts/context/)
