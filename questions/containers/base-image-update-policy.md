---
title: Maintain a base-image update policy
theme: containers
difficulty: senior
type: scenario
tags: [containers, docker, images, image-digests, security, supply-chain]
sources:
  - url: https://docs.docker.com/build/building/best-practices/#pin-base-image-versions
    source_type: official-docs
    verified_on: 2026-08-06
---

# Maintain a base-image update policy

How do you get both reproducible builds and timely base-image security updates?

## Answer guide

- Pin the base image to a version and preferably a digest so a build can be reproduced and reviewed. Record who approved the reference and which workload consumes it.
- Run an automated, reviewable update process that discovers new approved base digests, rebuilds dependent images, tests them, scans results, and promotes them through normal release controls.
- A tag-only policy allows silent upstream changes; a permanently pinned digest policy can leave known vulnerabilities unaddressed. The control is deliberate update cadence plus evidence, not either extreme alone.
- Define an emergency path for critical vulnerabilities, including compatibility testing, rollback, exception expiry, and an inventory of affected running digests.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Pin base image versions](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions)
- [Further reading: Docker Docs on image security best practices](https://docs.docker.com/build/building/best-practices/#build-and-test-your-images-in-ci)
