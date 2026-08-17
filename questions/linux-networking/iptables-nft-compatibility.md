---
title: Explain iptables-nft compatibility on modern distros
theme: linux-networking
difficulty: middle
type: theory
tags: [linux, networking, security, migration]
sources:
  - url: https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://wiki.debian.org/nftables
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://netfilter.org/projects/iptables/index.html
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain iptables-nft compatibility on modern distros

Ubuntu and Debian systems still ship `iptables` commands, yet their firewall is nftables-based. What actually runs when a legacy iptables script executes?

## Answer guide

- Modern distributions install iptables as the `iptables-nft` variant: the same command-line tool parses the classic syntax, but translates the rules into an nftables kernel ruleset through the nft compatibility layer, so `iptables -L` output reflects rules living in nftables tables you can also see with `nft list ruleset`.
- The legacy `iptables-legacy` variant still talks to the old xtables kernel interface, and mixing the two backends on one host creates two independently-evaluated rule sets — a classic cause of rules that appear present yet never match — so `iptables --version` (or the `update-alternatives` selection on Debian/Ubuntu) must be checked before debugging.
- Practical consequences: legacy scripts and tools like older Docker or failover tooling can keep working untranslated, but translation is not always lossless (some extensions behave differently or are unsupported), so teams should treat `iptables-translate` as the migration path to native nftables syntax rather than freezing iptables habits forever.

## References

- [nftables wiki: Moving from iptables to nftables](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables)
- [Debian wiki: nftables](https://wiki.debian.org/nftables)
- [netfilter.org: iptables project page](https://netfilter.org/projects/iptables/index.html)
- Further reading (blog): [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)

## What to learn next

- Official documentation: [netfilter.org nftables project](https://netfilter.org/projects/nftables/index.html)
- Manual or specification: [nft(8) man page](https://netfilter.org/projects/nftables/manpage.html)
- Maintainer or personal blog: [Julia Evans — iptables basics](https://jvns.ca/blog/2017/06/07/iptables-basics/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [nftables wiki: a simple ruleset for a server](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)
