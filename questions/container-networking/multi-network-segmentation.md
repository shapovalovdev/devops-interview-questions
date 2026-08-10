---
title: Segment a multi-tier application with Docker networks
theme: container-networking
difficulty: middle
type: scenario
tags: [containers, docker, networking, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/network/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Segment a multi-tier application with Docker networks

How would you use Docker networks to limit reachability in a web, API, and database stack?

## Answer guide

- Attach the web and API workloads to a frontend network, and attach the API and database to a separate backend network. Do not attach the web workload to the backend merely for convenience.
- Publish only the externally required frontend port. Internal peers should communicate by scoped service names on their shared network rather than through host-published ports.
- Network segmentation reduces accidental reachability but does not supply application authentication, database authorization, or encryption; retain those controls.
- Review every dual-homed workload because it bridges two reachability zones. Its image, logging, and egress behavior deserve additional scrutiny.

## References

- [Docker Docs: Container networking](https://docs.docker.com/engine/network/)
- Further reading (blog): [Docker: Docker networking drivers](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker networking tutorial](https://docs.docker.com/network/tutorials/)
