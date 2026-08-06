---
title: Explain container lifecycle states and restart policy
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, reliability]
sources:
  - url: https://docs.docker.com/engine/containers/start-containers-automatically/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain container lifecycle states and restart policy

What happens when a container's main process exits, and how should you choose a Docker restart policy?

## Answer guide

- A container runs while its configured main process runs; when that process exits, the container stops and records an exit status. A successful-looking container state does not prove the service was ever ready.
- Restart policies let Docker restart eligible containers after exits or daemon restarts. Choose `no`, `on-failure`, `always`, or `unless-stopped` based on the workload's intended recovery behavior.
- A restart policy is local process recovery, not application orchestration: it does not correct a bad configuration, unavailable dependency, or corrupted data.
- Avoid restart loops that hide repeated failures. Capture exit reason and logs, add health checks where appropriate, and let an orchestrator own availability when more than one host or replica is required.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Start containers automatically](https://docs.docker.com/engine/containers/start-containers-automatically/)
- [Further reading: Docker Docs on container lifecycle](https://docs.docker.com/engine/containers/run/)
