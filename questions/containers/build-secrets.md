---
title: Use a private dependency credential during an image build
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, build-secrets, security, supply-chain]
sources:
  - url: https://docs.docker.com/build/building/secrets/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use a private dependency credential during an image build

How can a build fetch a private dependency without baking its credential into the image?

## Answer guide

- Pass the credential through the builder's secret mechanism and mount it only in the instruction that needs it. Do not put tokens in `ARG`, `ENV`, source files, or copied configuration.
- Build secrets are designed for sensitive inputs unavailable in the build context; make the dependency fetch use the mounted secret and ensure the final stage copies only the resulting artifact.
- Limit the credential's scope and lifetime, rotate it, and avoid exposing it in build logs or error output. The build runner and secret store remain part of the trust boundary.
- Confirm with image inspection and registry scanning that no credential or private configuration was committed into a layer. A secret mount cannot undo a value previously copied into an earlier layer.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Build secrets](https://docs.docker.com/build/building/secrets/)
- [Further reading: Docker build checks for secrets in ARG or ENV](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
