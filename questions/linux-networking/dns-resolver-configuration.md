---
title: Explain Linux DNS resolver configuration
theme: linux-networking
difficulty: junior
type: theory
tags: [linux, networking, dns, troubleshooting, lfcs]
sources:
  - url: https://man7.org/linux/man-pages/man5/resolv.conf.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Linux DNS resolver configuration

What does `/etc/resolv.conf` control, and why is editing it often not a durable fix?

## Answer guide

- The resolver configuration supplies name servers, search domains, and resolver options to applications using the system resolver. Inspect the file and the active resolver service before assuming a hostname failure is an authoritative-DNS failure.
- On many systems the file is generated or symlinked by NetworkManager, systemd-resolved, DHCP, a VPN client, or container tooling. A manual edit may work briefly and then be replaced at lease renewal or reboot.
- Test both the configured path and a specific server when diagnosing. Search-domain expansion, split DNS, caching, negative answers, and different application resolvers can produce different results. Make persistent changes in the actual network/resolver owner, then verify rollback behavior.

## References

- [resolv.conf(5): resolver configuration](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)
- Further reading (blog): [Red Hat: Linux network troubleshooting commands](https://www.redhat.com/en/blog/linux-network-troubleshooting-commands)
