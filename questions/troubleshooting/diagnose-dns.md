---
title: Diagnose DNS failure from client to authoritative data
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, dns, networking, resolver, monitoring]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034
    source_type: standard
    verified_on: 2026-08-06
---
# Diagnose DNS failure from client to authoritative data
## Answer guide
- Separate name syntax, client resolver configuration, cache, recursive resolver, delegation, authoritative response, and transport. Capture the queried name, record type, response code, server, and timeout rather than saying simply “DNS is down.”
- Query a known resolver and authoritative servers where permitted, then compare TTL, CNAME chain, DNSSEC status, IPv4/IPv6 reachability, and split-horizon views. Cache propagation means a correct new record need not be visible everywhere immediately.
- Correct the owning zone or resolver configuration and verify from affected networks. Avoid flushing every cache or replacing nameservers without evidence; that can hide a delegation error and create a larger outage.
## References
- [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
- Further reading (blog): [Cloudflare — DNS](https://blog.cloudflare.com/tag/dns/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Standard: [IANA DNS parameters](https://www.iana.org/domains/root/db)
- Official guide: [BIND documentation](https://bind9.readthedocs.io/)
- Personal technical blog: [Bert Hubert](https://berthub.eu/)
- Technical blog: [Cloudflare DNS](https://blog.cloudflare.com/tag/dns/)
