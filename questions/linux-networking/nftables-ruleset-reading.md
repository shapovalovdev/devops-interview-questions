---
title: Read an nftables ruleset
theme: linux-networking
difficulty: junior
type: theory
tags: [linux, networking, security]
sources:
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server
    source_type: official-docs
    verified_on: 2026-08-16
---

# Read an nftables ruleset

A colleague hands you `nft list ruleset` output from a production host. Which structure do you follow to read it correctly?

## Answer guide

- The hierarchy is table, then chain, then rule: a table groups rules by family (ip, ip6, inet) and purpose; a chain inside it holds an ordered rule list attached to a netfilter hook such as input or forward; rules evaluate top to bottom and the first matching verdict wins.
- The chain's policy — `accept` or `drop` — decides what happens to packets that match no rule, so an input chain with policy drop and no permit for your port silently discards traffic, while policy accept passes everything not explicitly rejected.
- Packets traverse base chains by hook priority (for example filter input before a later-priority chain on the same hook), named chains are jumped to explicitly from other rules, and connection-state matches like `ct state established` explain why replies flow even under a deny-by-default policy.

## References

- [nftables wiki: Configuring chains](https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains)
- [nftables wiki: A simple ruleset for a server](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)
- Further reading (blog): [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)

## What to learn next

- Official documentation: [netfilter.org nftables project](https://netfilter.org/projects/nftables/index.html)
- Manual or specification: [nft(8) man page](https://netfilter.org/projects/nftables/manpage.html)
- Maintainer or personal blog: [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [nftables wiki: a simple ruleset for a server](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)
