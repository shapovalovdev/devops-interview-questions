---
title: Enable IPv6 container networking safely
theme: container-networking
difficulty: middle
type: scenario
tags: [containers, docker, networking, dns, reliability]
sources:
  - url: https://docs.docker.com/engine/daemon/ipv6/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Enable IPv6 container networking safely

What should an operator validate before enabling IPv6 for Docker networks?

## Answer guide

- Enable IPv6 deliberately in the daemon and create networks with suitable IPv6 addressing. Confirm routing and address allocation in the target environment rather than assuming IPv4 configuration applies unchanged.
- Review DNS records, client preference behavior, published-port bindings, and host firewall rules for both address families. A service may appear healthy on IPv4 while failing for IPv6 clients.
- Avoid overlapping or accidentally publicly routable ranges, and define who owns route advertisement and egress controls.
- Test dual-stack observability and incident procedures: logs and allow lists must preserve IPv6 addresses, and troubleshooting should compare each protocol family independently.

## References

- [Docker Docs: IPv6 networking](https://docs.docker.com/engine/daemon/ipv6/)
- Further reading (blog): [Docker: Network drivers and use cases](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
