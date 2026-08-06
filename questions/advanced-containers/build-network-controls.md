---
title: Control network access during an image build
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, networking, security, supply-chain]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#run---network
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control network access during an image build

Why and how would you limit network access while building a container image?

## Answer guide

- Networked build steps can fetch mutable dependencies or exfiltrate inputs. Use the Dockerfile `RUN --network` setting and builder policy to minimize network use where the build supports it.
- Resolve and verify dependencies deliberately, then perform hermetic or reduced-network build steps when practical. Record the source and digest of approved inputs.
- Do not enable host networking or insecure builder entitlements merely to make a build pass. Those modes expand access and require an explicit, reviewed exception.
- Full isolation is not free: package installation and remote cache access may need controlled connectivity. Measure and document the allowed endpoints and failure behavior.

## References

- [Dockerfile reference: RUN network mode](https://docs.docker.com/reference/dockerfile/#run---network)
- Further reading (blog): [Docker: Dockerfiles now support multiple build contexts](https://www.docker.com/blog/dockerfiles-now-support-multiple-build-contexts/)
