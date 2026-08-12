---
title: Control Docker build context with .dockerignore
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, dockerfile, security, cba]
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

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: .dockerignore files](https://docs.docker.com/build/concepts/context/#dockerignore-files)
- [Further reading: Docker Docs on build context](https://docs.docker.com/build/concepts/context/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
