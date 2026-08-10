---
title: Defend a shared cache against poisoning
theme: caching
difficulty: senior
type: scenario
tags: [caching, security, http, cdn, availability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9111.html
    source_type: standard
    verified_on: 2026-08-10
  - url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary
    source_type: official-docs
    verified_on: 2026-08-10
---

# Defend a shared cache against poisoning

How does an attacker poison a shared cache, and what controls actually stop it?

## Answer guide

- The core condition is an unkeyed input that still influences the response. If a request header, a query parameter, or a path variant changes what the origin returns but is not part of the cache key, an attacker can send one crafted request, have the harmful response stored, and then have it served to everyone who requests the normal URL. Nothing about the attack requires compromising the origin.
- The classic vectors are all instances of that condition: headers such as `X-Forwarded-Host` or `X-Original-URL` reflected into absolute links or scripts; request smuggling or header injection that desynchronises a proxy so one client's response is stored against another client's request; and normalisation differences where the cache and the origin disagree about what a path or a parameter means.
- The defences are structural. Make the key contain every input that reaches the response, or make the origin ignore inputs that are not in the key — the second is usually safer because it fails closed. Strip untrusted hop-by-hop and forwarding headers at the trust boundary rather than passing them through. Ensure the cache and the origin share one normalisation of paths, encodings, and parameter handling.
- Use the protocol correctly as well. `Vary` tells shared caches which request headers were used to select a representation, and RFC 9111 requires them to honour it, but `Vary` only covers headers, not query parameters or a proxy's own injected values. Mark authenticated and per-user responses `private` or `no-store` at the origin so that a cache misconfiguration alone cannot expose them, and never rely on the CDN configuration as the only control.
- Failure modes and operations: an error response poisoning a hot URL and being served long after the origin recovered, so keep error responses out of the shared cache; a purge that clears one point of presence and not the rest; and no detection at all, so add alerting on sudden hit-ratio or response-size shifts per URL and rehearse a fast, authenticated, cluster-wide purge before you need it.

## References

- [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [MDN Vary header reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary)
- Further reading (blog): [Cloudflare blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [MDN Vary header reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Nelson Elhage — systems and security writing](https://blog.nelhage.com/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [Varnish VCL users guide](https://varnish-cache.org/docs/trunk/users-guide/vcl.html)
