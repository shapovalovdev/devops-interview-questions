---
title: Diagnose Linux policy routing rules
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip-rule.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose Linux policy routing rules

Why can a route exist in the main table while a Linux connection still takes another path?

## Answer guide

- Linux policy routing evaluates rules that can choose route tables based on selectors such as source address, firewall mark, input interface, and UID. The main table is only one table and may not be consulted for a particular packet.
- Inspect `ip rule show`, every referenced `ip route show table <id>`, and a matching `ip route get` query. Trace where marks originate if rules match them; a NAT, firewall, VPN, or workload network namespace may set them.
- Preserve symmetry for stateful protocols and management access. Adding a broad source or mark rule can redirect unrelated traffic, bypass intended segmentation, or create return-path failures. Make the smallest owned change, test the defined flows, and persist it through the host network manager.

## References

- [ip-rule(8): routing-policy database management](https://man7.org/linux/man-pages/man8/ip-rule.8.html)
- Further reading (blog): [Red Hat: configuring IP networking with ip commands](https://www.redhat.com/en/blog/configuring-ip-networking-with-ip-commands)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
