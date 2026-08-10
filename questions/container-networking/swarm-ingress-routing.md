---
title: Choose Swarm ingress or host publishing
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, docker, networking, deployment, availability]
sources:
  - url: https://docs.docker.com/engine/swarm/ingress/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose Swarm ingress or host publishing

How do Swarm routing-mesh publishing and host-mode publishing differ operationally?

## Answer guide

- With the routing mesh, a published service port can accept traffic on swarm nodes and route it to an active task. Host-mode publishing binds on the node running the task instead of using that ingress behavior.
- Choose based on the traffic path, external load-balancer design, client source-address requirements, and scheduling model. Document which nodes are expected to accept inbound traffic.
- Validate health and failure behavior under task rescheduling and node loss. A port listener alone is not evidence that a healthy backend is available.
- Avoid combining modes without a clear ownership model; duplicate port expectations and untested load-balancer targets are common incident causes.

## References

- [Docker Docs: Swarm ingress routing mesh](https://docs.docker.com/engine/swarm/ingress/)
- Further reading (blog): [Docker: Understanding Docker networking](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
