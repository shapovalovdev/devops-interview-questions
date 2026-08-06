---
title: Trace an intermittent DNS resolution failure on Linux
theme: linux-troubleshooting
difficulty: junior
type: troubleshooting
tags: [linux, dns, resolver, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man5/resolv.conf.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Trace an intermittent DNS resolution failure on Linux

## Answer guide

- Test the exact name, record type, and resolver path from the affected host; distinguish NXDOMAIN, timeout, stale cache, search-domain expansion, and application-level caching.
- Inspect effective resolver configuration and query the configured server directly with a bounded tool such as `dig`. Compare UDP and TCP behavior where truncation, firewalls, or MTU problems are plausible.
- Avoid changing `/etc/resolv.conf` blindly because NetworkManager, systemd-resolved, DHCP, or a container runtime may own it. Validate the fix from the application identity and monitor resolution latency and error rate.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
