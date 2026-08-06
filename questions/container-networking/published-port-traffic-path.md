---
title: Trace traffic to a published container port
theme: container-networking
difficulty: middle
type: troubleshooting
tags: [containers, docker, networking, tcp, troubleshooting]
---

# Trace traffic to a published container port

A service is listening inside a Docker container but is unreachable through its published host port. Describe the traffic path and your debugging order.

## Answer guide

- Verify the process listens on the expected container address and port.
- Check port publication, host bindings, and container network attachment.
- Account for NAT or proxy rules and host firewall policy.
- Test from container, host, and remote client to isolate the broken boundary.
