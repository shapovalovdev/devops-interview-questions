---
title: Explain why nftables replaces iptables
theme: linux-networking
difficulty: junior
type: theory
tags: [linux, networking, security]
sources:
  - url: https://netfilter.org/projects/nftables/index.html
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain why nftables replaces iptables

The classic iptables command line is being phased out on major distributions. What problems does nftables solve that iptables could not?

## Answer guide

- nftables extends the netfilter kernel subsystem with generic set and map data structures, so one rule can match thousands of addresses or ports; with plain iptables that required a chain per purpose or an iptables-ipset sidecar, and rule evaluation scaled badly.
- The whole nftables ruleset is expressed in one syntax and applied in a single atomic transaction with `nft -f`, so a reload cannot leave the host half-protected between two commands; iptables applied rules one by one, and `iptables-restore` was a partial workaround.
- One nftables framework covers IPv4 and IPv6 (plus ARP and bridge) in a unified ruleset, removing the duplicated `iptables`/`ip6tables` configurations that drifted apart in practice, and the kernel can batch ruleset updates efficiently instead of invoking per-rule userspace transitions.

## References

- [netfilter.org: nftables project page](https://netfilter.org/projects/nftables/index.html)
- [nftables wiki: Moving from iptables to nftables](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables)
- Further reading (blog): [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)

## What to learn next

- Official documentation: [netfilter.org nftables project](https://netfilter.org/projects/nftables/index.html)
- Manual or specification: [nft(8) man page](https://netfilter.org/projects/nftables/manpage.html)
- Maintainer or personal blog: [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [nftables wiki: a simple ruleset for a server](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)
