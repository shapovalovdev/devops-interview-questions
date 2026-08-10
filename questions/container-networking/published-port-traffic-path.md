---
title: Trace traffic to a published container port
theme: container-networking
difficulty: middle
type: troubleshooting
tags: [containers, docker, networking, tcp, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/network/port-publishing/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Trace traffic to a published container port

A service is listening inside a Docker container but is unreachable through its published host port. Describe the traffic path and your debugging order.

## Answer guide

- A published Docker port maps a host address and port to a container port through Docker's networking rules; it does not make an application reachable if it only listens on loopback inside the container or on a different port.
- First prove the process and its bind address from the container namespace. Then inspect the published mapping (`docker port`/inspect), its host IP binding, and whether the container is attached to the expected network.
- Test in order from the container, the host, and a remote client. The first failed boundary distinguishes application binding from port publishing, host firewall/routing, or an external load-balancer/DNS path.
- Publishing to `0.0.0.0` can expose a service beyond the intended interface. Docker Engine networking behavior and firewall integration vary by platform/version, so confirm generated rules rather than assuming a particular iptables/nftables implementation.

## References

- [Docker Docs: Port publishing and mapping](https://docs.docker.com/engine/network/port-publishing/)
- Further reading (blog): [Docker: Hardening container networking](https://www.docker.com/blog/docker-engine-28-hardening-container-networking-by-default/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker networking tutorial](https://docs.docker.com/network/tutorials/)
