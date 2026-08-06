---
title: Trace a DNS lookup from an application to an answer
theme: networking
difficulty: middle
type: theory
tags: [dns, networking, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc2308.html
    source_type: standard
    verified_on: 2026-08-06
---

# Trace a DNS lookup from an application to an answer

What happens when an application resolves a hostname, and where can you investigate when resolution fails?

## Answer guide

- A stub resolver in the host or runtime first applies its local name-service configuration (for example hosts-file and search-domain rules) and may use a local cache. It sends an iterative-resolution request to a configured recursive resolver rather than normally contacting every authoritative server itself.
- The recursive resolver answers from cache when the relevant positive or negative TTL is still valid. On a miss it follows DNS delegations from a root server through the relevant TLD and authoritative zone, then returns the requested resource record or a negative response.
- Diagnose by separating layers: inspect the exact name and record type the application asks for, resolver/search configuration, cache age, recursive resolver response, and reachability to the resolver. Querying an authoritative server can distinguish bad zone data from stale recursive cache.
- Do not assume every failure is DNS. A successful A/AAAA lookup does not prove the destination is routable or listening; conversely an application can retain its own cache after DNS is corrected. Negative responses are cacheable too, so a recently created name may remain unavailable until its negative TTL expires.

## References

- [RFC 1034: Domain names — concepts and facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 2308: DNS negative caching](https://www.rfc-editor.org/rfc/rfc2308.html)
- [Cloudflare learning: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
