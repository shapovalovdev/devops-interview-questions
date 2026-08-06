---
title: Run a containerized service as a non-root user
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, security, least-privilege]
---

# Run a containerized service as a non-root user

What changes are needed to run an application image without root privileges?

## Answer guide

- Create or select an unprivileged user and ensure runtime paths are writable by it.
- Avoid privileged ports and host mounts that bypass the intended boundary.
