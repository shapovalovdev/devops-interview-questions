---
title: Triage TCP connection states on Linux
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, tcp, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ss.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage TCP connection states on Linux

How do socket states help diagnose a TCP connection incident?

## Answer guide

- Use `ss -tanp` to observe listeners and established or transitional TCP sockets with local and peer addresses. Compare states and counts over time with the expected application traffic rather than treating any single state as automatically faulty.
- Many `SYN-SENT` connections suggest the client is not receiving a handshake response; persistent `SYN-RECV` can point to incomplete handshakes; growing close-related states can reveal shutdown or peer behavior. Validate these hypotheses with packet captures and service logs.
- Socket output is a point-in-time view and privileges affect PID visibility. Backlog pressure, proxies, NAT, and load balancers can move the apparent problem away from the local process, so use safe rate-limited sampling and preserve incident evidence before tuning kernel or application settings.

## References

- [ss(8): socket statistics and filtering](https://man7.org/linux/man-pages/man8/ss.8.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
