---
title: Maintain a base-image update policy
theme: containers
difficulty: senior
type: scenario
tags: [containers, docker, images, image-digests, security, supply-chain, cks]
sources:
  - url: https://docs.docker.com/build/building/best-practices/#pin-base-image-versions
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://docs.podman.io/en/latest/markdown/podman-auto-update.1.html
    source_type: official-docs
    verified_on: 2026-08-16
---

# Maintain a base-image update policy

How do you get both reproducible builds and timely base-image security updates?

## Answer guide

- Pin the base image to a version and preferably a digest so a build can be reproduced and reviewed. Record who approved the reference and which workload consumes it.
- Run an automated, reviewable update process that discovers new approved base digests, rebuilds dependent images, tests them, scans results, and promotes them through normal release controls.
- A tag-only policy allows silent upstream changes; a permanently pinned digest policy can leave known vulnerabilities unaddressed. The control is deliberate update cadence plus evidence, not either extreme alone.
- Define an emergency path for critical vulnerabilities, including compatibility testing, rollback, exception expiry, and an inventory of affected running digests.
- Digest pinning is engine-neutral at both ends: an image digest is an OCI content-addressed reference, and podman runs the same discover-rebuild-promote loop with `io.containers.autoupdate` labels and `podman auto-update` — the control is the cadence and the evidence, not the daemon.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Pin base image versions](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions)
- [Further reading: Docker Docs on image security best practices](https://docs.docker.com/build/building/best-practices/#build-and-test-your-images-in-ci)
- [Podman docs: podman-auto-update](https://docs.podman.io/en/latest/markdown/podman-auto-update.1.html)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
