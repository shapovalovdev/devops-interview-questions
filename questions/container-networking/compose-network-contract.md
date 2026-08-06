---
title: Define a Compose network contract
theme: container-networking
difficulty: middle
type: scenario
tags: [containers, docker, networking, deployment, reliability]
sources:
  - url: https://docs.docker.com/reference/compose-file/networks/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define a Compose network contract

What should a production-minded Compose file state explicitly about networking?

## Answer guide

- Name the required networks and attach each service only where it must communicate. Compose creates an application network by default, but explicit topology makes reachability and reviews clearer.
- Declare published ports separately from internal service ports, and document any external pre-existing network with `external` rather than silently creating a look-alike network.
- Treat service names and aliases as API contracts for peer workloads. Test startup order and retry behavior because network creation does not guarantee the destination application is ready.
- Do not copy a development Compose topology into production unchanged; proxying, secrets, firewall ownership, and multi-host routing may differ materially.

## References

- [Docker Compose reference: networks](https://docs.docker.com/reference/compose-file/networks/)
- Further reading (blog): [Docker: Understanding Docker networking](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
