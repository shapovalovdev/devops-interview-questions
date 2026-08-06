---
title: Explain a container network namespace
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, linux, namespaces, networking, process-isolation]
sources:
  - url: https://man7.org/linux/man-pages/man7/network_namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a container network namespace

What resources are isolated by a Linux network namespace, and what does it not secure?

## Answer guide

- A network namespace isolates network devices, addresses, routing tables, firewall rules, sockets, and related networking state. A runtime usually connects it to the host through a virtual Ethernet pair.
- Sharing a network namespace deliberately makes processes share localhost and ports, which is useful for Pod-style sidecars but changes the trust and failure boundary.
- Namespace separation is not network authorization. Apply ingress and egress policy, protect the runtime API, and avoid host networking unless its performance or integration value outweighs lost isolation.

## References

- [Linux man-pages: network namespaces](https://man7.org/linux/man-pages/man7/network_namespaces.7.html)
- Further reading (blog): [Docker: networking overview](https://www.docker.com/blog/docker-networking-tutorial/)
