---
title: Debug container DNS resolution
theme: container-networking
difficulty: junior
type: troubleshooting
tags: [containers, docker, networking, dns, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/network/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug container DNS resolution

A container cannot resolve a service name. What do you check before changing DNS settings?

## Answer guide

- First identify whether the name is a Docker network alias, an internal DNS name, or a public name. A name only resolves through Docker's embedded DNS when the containers share an appropriate user-defined network.
- Inspect network attachments and aliases, then query from inside the failing container. Compare its resolver configuration and results with a known-good workload on the same network.
- For external names, test the configured upstream resolver and network egress separately. DNS success does not prove TCP reachability to the returned address.
- Avoid permanently adding host entries as a workaround for a wrong network attachment or broken service-discovery contract; it hides lifecycle and address-change failures.

## References

- [Docker Docs: Container networking](https://docs.docker.com/engine/network/)
- Further reading (blog): [Docker: Understanding Docker networking](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
