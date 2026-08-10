---
title: Use a user-defined bridge for service discovery
theme: container-networking
difficulty: junior
type: theory
tags: [containers, docker, networking, dns]
sources:
  - url: https://docs.docker.com/engine/network/drivers/bridge/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use a user-defined bridge for service discovery

Why is a user-defined bridge normally preferable to Docker's default bridge for collaborating containers?

## Answer guide

- A user-defined bridge provides a scoped application network and Docker-managed DNS so peers can resolve a container name or network alias. That avoids hard-coding an address that may change after recreation.
- The default bridge does not provide the same automatic name resolution between containers; its legacy linking approach is not a replacement for an explicit network design.
- Attach only the services that need to communicate. A broad shared bridge increases lateral-reachability and makes a name collision or accidental dependency more likely.
- DNS only locates the peer; it does not prove the process is listening, the protocol is correct, or an application authorization rule permits the request. Test those boundaries separately.

## References

- [Docker Docs: Bridge network driver](https://docs.docker.com/engine/network/drivers/bridge/)
- Further reading (blog): [Docker: Understanding Docker networking](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
