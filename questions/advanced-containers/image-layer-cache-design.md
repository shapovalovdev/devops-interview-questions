---
title: Design a Dockerfile for predictable cache reuse
theme: advanced-containers
difficulty: middle
type: scenario
tags: [docker, images, containers, automation]
sources:
  - url: https://docs.docker.com/build/cache/invalidation/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a Dockerfile for predictable cache reuse

How would you organize a Dockerfile so routine source changes do not invalidate expensive dependency-install layers?

## Answer guide

- Build cache keys depend on the Dockerfile instruction and its inputs. Put layers whose inputs change rarely before layers that copy changing application code, so a source edit can reuse an already-built dependency layer.
- Copy dependency manifests first, install dependencies, then copy the remaining source. A manifest change must invalidate the install layer; a normal source edit should only invalidate later layers.
- Use `.dockerignore` to keep generated files, VCS data, and secrets out of the build context. Otherwise a changed irrelevant file can invalidate `COPY`, and a copied secret can remain in an image layer.
- Multi-stage builds reduce the runtime image, but they are not a cache guarantee: pin or deliberately refresh base images and measure cache hit rate in the actual builder (especially remote CI builders).

## References

- [Docker Docs: Build cache invalidation](https://docs.docker.com/build/cache/invalidation/)
- Further reading (blog): [Docker: Build cache optimization](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
