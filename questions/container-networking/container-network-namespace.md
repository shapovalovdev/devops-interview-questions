---
title: Explain a container network namespace
theme: container-networking
difficulty: junior
type: theory
tags: [containers, docker, networking, linux]
sources:
  - url: https://docs.docker.com/engine/network/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a container network namespace

What does a container network namespace isolate, and what remains shared with the host?

## Answer guide

- In Docker's normal networking modes, a container has its own network namespace: interfaces, addresses, routes, and sockets are distinct from the host namespace. Docker connects that namespace according to the selected network driver.
- The container still uses the host kernel, so namespace isolation is not a separate kernel or an absolute security boundary. Host networking intentionally bypasses this separation.
- Inspect from the correct namespace when debugging; a listener or route seen on the host may not exist in the container, and vice versa.
- Do not treat a namespace as a firewall policy. Exposure can still result from published ports, host routing, privileged configuration, or another attached network.

## References

- [Docker Docs: Container networking](https://docs.docker.com/engine/network/)
- Further reading (blog): [Docker: Networking basics](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)

## What to learn next

- Official documentation: [Docker networking](https://docs.docker.com/engine/network/)
- Manual or specification: [network_namespaces(7)](https://man7.org/linux/man-pages/man7/network_namespaces.7.html)
- Maintainer or personal blog: [Julia Evans: Linux networking writing](https://jvns.ca/)
- Technical blog: [Docker networking drivers](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
- Hands-on guide: [Docker networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
