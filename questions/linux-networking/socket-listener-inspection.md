---
title: Identify the process listening on a Linux port
theme: linux-networking
difficulty: junior
type: troubleshooting
tags: [linux, networking, tcp, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ss.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Identify the process listening on a Linux port

How do you determine whether the expected process is listening on TCP port 8443?

## Answer guide

- Run `ss -ltnp` with appropriate privilege and filter for `:8443`. Confirm the process, PID, protocol, local address, and listening state rather than treating an open firewall rule as evidence that an application is ready.
- Interpret the bind address. A listener on `127.0.0.1` is intentionally local-only; one on `0.0.0.0` accepts IPv4 on all eligible interfaces, and IPv6 behavior depends on the socket and `bindv6only` configuration.
- Test from the same network scope as the failing client after confirming the listener. A local success does not rule out routing, firewall, TLS, proxy, or policy failures. Avoid killing a process merely because its port is unexpected; first identify its service owner and dependencies.

## References

- [ss(8): investigate Linux sockets](https://man7.org/linux/man-pages/man8/ss.8.html)
- Further reading (blog): [Red Hat: Linux network troubleshooting commands](https://www.redhat.com/en/blog/linux-network-troubleshooting-commands)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
