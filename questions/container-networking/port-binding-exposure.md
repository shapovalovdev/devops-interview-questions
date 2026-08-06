---
title: Restrict published-port exposure
theme: container-networking
difficulty: middle
type: scenario
tags: [containers, docker, networking, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/network/port-publishing/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Restrict published-port exposure

How would you publish an administrative container endpoint without unintentionally exposing it to the network?

## Answer guide

- Bind the published port to a deliberately selected host address, commonly loopback when a local reverse proxy or operator is the only intended client. Avoid a wildcard host binding unless public reachability is the requirement.
- Separate management and user-facing endpoints into explicit exposure rules. Record the owning firewall, proxy, and authentication control rather than relying on a hidden host-port convention.
- Verify the effective mapping with Docker inspection and a connection test from both an allowed and disallowed network location.
- Docker's firewall integration and defaults can vary by release and platform; review the engine's current behavior after upgrades and do not assume a published port is private.

## References

- [Docker Docs: Port publishing and mapping](https://docs.docker.com/engine/network/port-publishing/)
- Further reading (blog): [Docker: Hardening container networking by default](https://www.docker.com/blog/docker-engine-28-hardening-container-networking-by-default/)
