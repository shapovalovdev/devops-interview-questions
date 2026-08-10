---
title: Explain Docker network drivers
theme: container-networking
difficulty: junior
type: theory
tags: [containers, docker, networking, reliability]
sources:
  - url: https://docs.docker.com/engine/network/drivers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Docker network drivers

What problem does a Docker network driver solve, and when would you choose bridge, host, overlay, or none?

## Answer guide

- A network driver supplies the connectivity model for containers: address allocation, reachability, and (where applicable) name resolution and isolation. Pick the driver for the workload boundary, not simply because it is Docker's default.
- Bridge is the normal single-host choice; host removes network-namespace isolation and shares the host stack; overlay connects workload endpoints across participating hosts; none deliberately gives a container no network connectivity.
- Host networking can create port conflicts and reduces isolation. Overlay networking has cluster and control-plane prerequisites, while bridge traffic remains local to its host unless another component forwards it.
- Confirm the engine mode, driver capabilities, and the expected exposure path before troubleshooting. Do not assume a driver makes traffic encrypted, routable across every environment, or protected by policy by itself.

## References

- [Docker Docs: Network drivers](https://docs.docker.com/engine/network/drivers/)
- Further reading (blog): [Docker: Hardening container networking by default](https://www.docker.com/blog/docker-engine-28-hardening-container-networking-by-default/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
