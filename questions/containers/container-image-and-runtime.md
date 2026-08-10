---
title: Distinguish a container image from a running container
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, images, ckad, kcna, lfcs, must-know]
sources:
  - url: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish a container image from a running container

What is the difference between a container image and a container created from it?

## Answer guide

- An image is a read-only, packaged template: filesystem layers plus configuration such as its default command. A container is one runnable instance created from that image.
- Starting a container adds a thin writable layer and runtime configuration; writes there belong to that instance, so two containers from one image do not share ordinary writable files.
- Image layers are content-addressed build artifacts and are reused where possible. The container's writable layer is not a durable data-store or a release artifact.
- Put durable application data in a managed data service or a volume with an explicit backup and restore plan. Treating the writable layer as persistence makes replacement, scaling, and recovery unreliable.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/)
- [Further reading: Docker Docs on container storage](https://docs.docker.com/engine/storage/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
