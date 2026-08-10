---
title: Select DNS record types and TTLs
theme: networking
difficulty: middle
type: scenario
tags: [dns, networking, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc2181.html
    source_type: standard
    verified_on: 2026-08-06
---

# Select DNS record types and TTLs

How do A, AAAA, CNAME, and TTL choices affect a service migration?

## Answer guide

- A and AAAA records map a name to IPv4 and IPv6 addresses. A CNAME aliases one domain name to another canonical name; DNS rules constrain where CNAME may coexist with other data at the same owner name.
- TTL is a cache-control value supplied with a record set. Lower it before a planned move only after accounting for existing caches, resolver behaviour, and negative caching; it cannot retroactively shorten entries already cached with an older TTL.
- For a migration, publish and test the target under a separate name, lower TTL in advance, monitor both destinations, then change the intended record. Retain the old endpoint for a rollback window sized for observed caches and client behaviour.
- DNS is not a strong instant failover mechanism: clients and recursive resolvers cache independently, and dual-stack clients can choose A or AAAA differently. Pair DNS changes with health checks and explicit rollback criteria.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 1034: DNS resource records and aliases](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 2181: Clarifications to the DNS specification](https://www.rfc-editor.org/rfc/rfc2181.html)
- [Cloudflare learning: What is a DNS TTL?](https://www.cloudflare.com/learning/dns/dns-records/dns-ttl/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
