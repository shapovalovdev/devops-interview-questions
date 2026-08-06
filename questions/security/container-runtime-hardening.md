---
title: Harden a container runtime workload
theme: security
difficulty: middle
type: scenario
tags: [security, containers, least-privilege, linux, cks, kcsa]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/190/final
    source_type: standard
    verified_on: 2026-08-06
---

# Harden a container runtime workload

What baseline controls would you apply before running a containerized service in production?

## Answer guide

- Use a maintained minimal image, run as a non-root user, drop unnecessary capabilities, make the filesystem read-only where compatible, and set CPU/memory limits.
- Separate workloads by sensitivity and restrict runtime, registry, and host access. Scan and update images, then deploy a pinned digest rather than an unreviewed tag.
- Test the service under the restrictions and document exceptions; many applications assume writable paths, a specific UID, or network access.
- Containers share a host kernel, so they are not a complete security boundary. Privileged containers, host mounts, broad capabilities, and an exposed daemon socket greatly increase escape and host-compromise risk.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST SP 800-190: Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
- [Docker: Runtime privilege and Linux capabilities](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
