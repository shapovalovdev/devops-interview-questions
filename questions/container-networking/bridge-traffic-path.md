---
title: Trace bridge-network traffic
theme: container-networking
difficulty: middle
type: troubleshooting
tags: [containers, docker, networking, tcp, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/network/drivers/bridge/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Trace bridge-network traffic

Two containers on the same bridge cannot communicate. Describe a boundary-by-boundary debugging approach.

## Answer guide

- Confirm both containers are running and attached to the same intended user-defined bridge; inspect their addresses, aliases, and routes rather than guessing from Compose names.
- Test name resolution, then the destination address and port from the source namespace. At the destination, verify the application listens on the container interface rather than only on loopback.
- Inspect any service mesh, host firewall, or application ACL after proving the local Docker path. Same-network membership is necessary but not sufficient for a successful protocol exchange.
- Do not publish a host port merely to make peer containers communicate: that changes the exposure boundary and can obscure the original bridge or listener defect.

## References

- [Docker Docs: Bridge network driver](https://docs.docker.com/engine/network/drivers/bridge/)
- Further reading (blog): [Docker: Understanding Docker networking](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)

## What to learn next

- Official documentation: [Docker bridge network driver](https://docs.docker.com/engine/network/drivers/bridge/)
- Manual or specification: [Linux network namespaces](https://man7.org/linux/man-pages/man7/network_namespaces.7.html)
- Maintainer or personal blog: [Julia Evans: networking writing](https://jvns.ca/)
- Technical blog: [Docker networking drivers](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
- Hands-on guide: [Docker network tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
