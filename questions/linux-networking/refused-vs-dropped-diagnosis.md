---
title: Distinguish connection refused from a firewall drop
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, security, troubleshooting, tcp]
sources:
  - url: https://netfilter.org/projects/nftables/manpage.html
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains
    source_type: official-docs
    verified_on: 2026-08-16
---

# Distinguish connection refused from a firewall drop

A client cannot reach a service: one attempt fails fast with "connection refused", another just times out. How do you tell a dead listener from a firewall drop?

## Answer guide

- The TCP semantics differ: "connection refused" means something answered with a TCP RST, so the packet reached a host with no listener on that port — a drop means silence, typically a firewall discarding packets or a return-path failure, and the SYN never completes.
- Inspect the packet path on the server with `nft list ruleset` (check the input chain policy and rules) and read per-rule counters after a controlled test connection: a drop-rule counter climbing proves the firewall ate the packet, while untouched counters point somewhere else.
- Capture on both sides with tcpdump to localize the layer — if the SYN arrives on the server interface but no SYN-ACK leaves, the drop is local firewall policy; if it never arrives, an intermediate firewall, routing, or cloud security group is responsible; a RST captured from the server means the listener itself is down.

## References

- [nft(8) man page](https://netfilter.org/projects/nftables/manpage.html)
- [nftables wiki: Configuring chains](https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains)
- Further reading (blog): [Red Hat — network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)

## What to learn next

- Official documentation: [netfilter.org nftables project](https://netfilter.org/projects/nftables/index.html)
- Manual or specification: [nft(8) man page](https://netfilter.org/projects/nftables/manpage.html)
- Maintainer or personal blog: [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [nftables wiki: a simple ruleset for a server](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)
