---
title: Debug failed container egress
theme: container-networking
difficulty: middle
type: troubleshooting
tags: [containers, docker, networking, dns, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/network/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug failed container egress

A container can reach peer containers but not an external API. What is your debugging sequence?

## Answer guide

- Establish whether failure is name resolution, TCP connection, TLS negotiation, or application authorization. Run a minimal test from the affected container, not only from the host.
- Inspect the container route and network attachment, then compare egress from a known-good container on the same network. Check host routing, firewall, proxy, and cloud egress policy at the first failed boundary.
- Verify the destination's allow list sees the source address produced by the actual egress path; Docker networking can involve address translation.
- Do not add broad privileged networking or publish an inbound port to solve outbound failure. That changes the problem and weakens isolation without proving the cause.

## References

- [Docker Docs: Container networking](https://docs.docker.com/engine/network/)
- Further reading (blog): [Docker: Networking drivers and use cases](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
