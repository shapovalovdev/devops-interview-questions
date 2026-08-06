---
title: Apply HTTP caching safely
theme: backend-architecture
difficulty: junior
type: theory
tags: [http, performance, availability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9111
    source_type: standard
    verified_on: 2026-08-06
---

# Apply HTTP caching safely

How do HTTP cache directives affect a backend API design?

## Answer guide

- HTTP caching lets a client or shared cache reuse a response according to explicit response controls. Set Cache-Control, validators such as ETag, and variation rules based on the resource’s freshness, privacy, and authorization semantics.
- Identify which responses are public, private, immutable, or must be revalidated. Include cache behavior in API documentation and measure cache hit rate, origin load, and stale-response behavior as part of capacity planning.
- A shared cache can leak data if responses vary by credentials without correct directives. Incorrect invalidation or a long freshness lifetime can serve obsolete state; test authenticated responses, deployments, and updates through the actual CDN or proxy.

## References

- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111)
- Further reading (blog): [Cloudflare: HTTP caching](https://blog.cloudflare.com/sometimes-i-cache/)

## What to learn next

- Official documentation: [MDN: HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- Manual or specification: [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111)
- Maintainer or personal blog: [Mark Nottingham's blog](https://www.mnot.net/blog/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [Varnish tutorial](https://www.varnish-software.com/developers/tutorials/)
