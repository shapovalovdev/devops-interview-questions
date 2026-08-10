---
title: Diagnose reverse-path filtering drops
theme: linux-networking
difficulty: senior
type: troubleshooting
tags: [linux, networking, security, troubleshooting]
sources:
  - url: https://docs.kernel.org/networking/ip-sysctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose reverse-path filtering drops

Why can reverse-path filtering break a multi-homed Linux host, and what is the safe response?

## Answer guide

- Reverse-path filtering checks whether the source address of an arriving packet has an acceptable reverse route. It helps resist spoofed-source traffic, but strict behavior can reject valid asymmetric or policy-routed flows.
- Inspect the interface and global `rp_filter` settings, `ip rule` and route tables, and packet evidence for the affected source. Test the actual reverse lookup in the same namespace and mark context rather than assuming the main table describes it.
- Do not globally disable source validation as a quick fix. Correct unintended asymmetry where possible, select a policy appropriate to the documented topology, and constrain exposure with ingress filtering and firewall rules. Re-test failover and VPN paths because they often change routing symmetry.

## References

- [Linux kernel: IP sysctl reverse-path filtering settings](https://docs.kernel.org/networking/ip-sysctl.html)
- Further reading (blog): [Red Hat: configuring IP networking with ip commands](https://www.redhat.com/en/blog/configuring-ip-networking-with-ip-commands)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
