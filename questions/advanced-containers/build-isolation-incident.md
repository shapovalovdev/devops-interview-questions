---
title: Respond to a suspected malicious container build
theme: advanced-containers
difficulty: senior
type: troubleshooting
tags: [containers, docker, security, incident-response, supply-chain]
sources:
  - url: https://docs.docker.com/build/building/secrets/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to a suspected malicious container build

A CI build may have executed a malicious Dockerfile. What do you contain and investigate first?

## Answer guide

- Stop further builds on the affected worker or trust domain, preserve build logs and configuration, and identify the source revision, contexts, secrets, cache imports/exports, and image digests involved.
- Revoke or rotate credentials exposed to the worker, including registry, source-control, package, and cloud credentials. Assume logs and cache may have observed secret material until disproved.
- Determine whether the Dockerfile used secret, SSH, network, or insecure entitlements and whether artifacts were pushed. Quarantine suspect images and invalidate promotion approvals.
- Restore from known-good builder images and tighten isolation or permissions before resuming. Do not delete evidence or rely on a rerun to prove the first build was harmless.

## References

- [Docker Docs: Build secrets](https://docs.docker.com/build/building/secrets/)
- Further reading (blog): [Docker security advisory: runc, BuildKit, and Moby](https://www.docker.com/blog/docker-security-advisory-multiple-vulnerabilities-in-runc-buildkit-and-moby/)
