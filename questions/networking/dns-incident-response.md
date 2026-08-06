---
title: Lead a DNS incident response
theme: networking
difficulty: senior
type: scenario
tags: [dns, networking, incident-response, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc2308.html
    source_type: standard
    verified_on: 2026-08-06
---

# Lead a DNS incident response

A production name was changed to a bad target. How do you restore service while accounting for caches?

## Answer guide

- Establish the authoritative desired record and correct it at the zone owner first. Preserve evidence of the old/new values, TTLs, and change time; changing many unrelated records makes cache diagnosis harder.
- Query authoritative servers and several independent recursive resolvers for the exact type/name. Positive and negative DNS answers can remain cached until TTL expiry, so authoritative correction does not make every client switch immediately.
- Keep the former target healthy or provide a compatible response for the measured propagation window where practical. Monitor request volume, resolver error codes, and address-family split; communicate a realistic recovery window rather than claiming DNS has "propagated."
- After recovery, improve change controls: preflight query checks, staged records, TTL reduction before risky moves, and an explicit rollback target. DNS rollback is also cache-sensitive, so rehearse it.

## References

- [RFC 1034: DNS concepts and caching](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 2308: Negative caching](https://www.rfc-editor.org/rfc/rfc2308.html)
- [ICANN: DNS security and stability](https://www.icann.org/en/stability-security)
