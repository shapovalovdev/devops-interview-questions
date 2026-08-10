---
title: Diagnose an MTU mismatch across container paths
theme: container-networking
difficulty: senior
type: troubleshooting
tags: [containers, docker, networking, tcp, troubleshooting, performance]
sources:
  - url: https://docs.docker.com/engine/network/drivers/overlay/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an MTU mismatch across container paths

Some requests fail only for larger responses across hosts. How do you investigate a suspected MTU mismatch?

## Answer guide

- Compare the effective MTU from container interface through the Docker network, host interface, and underlay. Encapsulation can reduce usable payload relative to a physical NIC's configured MTU.
- Reproduce with controlled packet sizes and observe retransmissions or ICMP feedback where permitted. Compare same-host and cross-host paths to localize the added encapsulation boundary.
- Choose a network MTU compatible with the smallest path, then roll it out with connectivity and performance tests. Changing it blindly can disrupt existing connections.
- Do not disable PMTU-related behavior as a permanent workaround. Firewalls that block needed control traffic and inconsistent cloud or VPN paths must be addressed in the design.

## References

- [Docker Docs: Overlay network driver](https://docs.docker.com/engine/network/drivers/overlay/)
- Further reading (blog): [Docker: Networking drivers and use cases](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
