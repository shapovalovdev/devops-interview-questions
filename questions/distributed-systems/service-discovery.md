---
title: Design service discovery and client load balancing
theme: distributed-systems
difficulty: middle
type: theory
tags: [dns, networking, availability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034.html
    source_type: standard
    verified_on: 2026-08-06
---

# Design service discovery and client load balancing

What must a service-discovery design handle beyond resolving a name to an address?

## Answer guide

- Discovery maps a logical service to eligible endpoints and metadata such as health, zone, version, and port. Clients or a proxy then apply selection, connection reuse, deadlines, and health policy; DNS alone does not establish that an endpoint can serve the requested operation.
- Choose cache TTLs and update propagation to balance control-plane load against stale routing. Make startup and dependency loss behavior explicit, including bootstrap addresses, readiness criteria, and whether existing connections may drain safely.
- Stale records, uneven endpoint load, negative caching, and health checks that test only a listening port can send traffic to broken instances. A discovery outage must not cause every client to hot-loop or discard all known healthy endpoints simultaneously.

## References

- [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- Further reading (personal blog): [Cloudflare: how DNS works](https://www.cloudflare.com/learning/dns/what-is-dns/)

## What to learn next

- Official documentation: [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- Manual or specification: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html)
- Maintainer or personal blog: [Julia Evans: DNS](https://jvns.ca/)
- Technical blog: [Cloudflare: DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
- Hands-on guide: [CoreDNS manual](https://coredns.io/manual/toc/)
