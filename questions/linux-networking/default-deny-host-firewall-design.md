---
title: Design a default-deny host firewall with nftables
theme: linux-networking
difficulty: senior
type: scenario
tags: [linux, networking, security, least-privilege, tcp]
sources:
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design a default-deny host firewall with nftables

You provision an application server that must expose only SSH from the management network and the application ports to defined clients. Design the inbound nftables policy from scratch.

## Answer guide

- Start from the failure-safe direction: an inet filter table with an input base chain whose policy is `drop`, so anything not explicitly permitted is discarded — including IPv6, which the inet family covers in the same ruleset — and decide ICMP and management access before the first lockdown, or you lock yourself out of the host.
- Permit return traffic with an early `ct state established,related accept` rule so replies to outgoing connections and negotiated protocols keep flowing, then add narrow permits: SSH only from the management prefix, each application port only from the client networks and interfaces that genuinely need it, plus the ICMP types path-MTU and neighbor discovery require.
- Ship the ruleset as a versioned, reviewable file loaded atomically with `nft -f` (or the distribution's nftables.service), include a loopback accept rule, and record a rollback path: test from a second session before closing the first, use counters or logging on the drop path to catch over-blocking during rollout, and keep the cloud security group or upstream firewall as a separate, coordinated layer rather than a substitute for host policy.

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
