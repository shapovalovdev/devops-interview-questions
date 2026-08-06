---
title: Use build secrets without embedding credentials
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, build-secrets, security, supply-chain]
sources:
  - url: https://docs.docker.com/build/building/secrets/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use build secrets without embedding credentials

How should a build fetch a private dependency without leaving the credential in the image?

## Answer guide

- Pass the credential as a BuildKit secret or SSH mount only to the `RUN` instruction that needs it; do not use `ARG`, `ENV`, or `COPY` for secret values.
- Scope the credential to the repository and operation, inject it from the CI secret store, and revoke or rotate it independently of the image.
- Ensure the command does not print the secret and does not copy it into an artifact, package-manager config, cache export, or later stage.
- A secret mount protects build inputs, not every third-party tool. Review build logs and cache configuration, and test that an image inspection cannot recover the credential.

## References

- [Docker Docs: Build secrets](https://docs.docker.com/build/building/secrets/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
