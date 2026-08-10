---
title: Scope a CDN cache key correctly
theme: caching
difficulty: middle
type: scenario
tags: [caching, cdn, http, security]
sources:
  - url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-key-understand-cache-policy.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://www.rfc-editor.org/rfc/rfc9111.html
    source_type: standard
    verified_on: 2026-08-10
---

# Scope a CDN cache key correctly

You are putting a CDN in front of an API that varies its responses by locale, plan tier, and authenticated user. How do you define the cache key?

## Answer guide

- Start from the rule that the cache key must contain every input the response actually depends on. The default key on most CDNs is the host and path only; every query parameter, header, or cookie that changes the response must be added explicitly, or two different responses collapse onto one entry and users receive each other's content.
- Add only what genuinely varies the response. Every element added to the key multiplies the number of stored variants and divides the hit ratio: including a cookie that carries a per-user session identifier gives every user a private entry and reduces the CDN to a very expensive pass-through. Normalise instead — map a long list of accepted locales to a handful of buckets, and strip analytics and campaign parameters that never reach the application.
- Use the HTTP mechanisms rather than only vendor settings. `Cache-Control: private` marks a response as storable by a browser but not by a shared cache, `no-store` forbids storage entirely, and `Vary` tells a shared cache which request headers were used for content negotiation. Responses to authenticated requests must be marked correctly at the origin so that a CDN misconfiguration is not the only thing standing between two customers.
- Decide the authenticated case deliberately. The usual answers are to keep per-user responses out of the shared cache entirely, to cache only the shared fragments and compose per-user content elsewhere, or to move the authorization decision to the edge so identity becomes part of the key. Each has a different failure mode when the CDN configuration drifts.
- Failure modes to name: a `Vary: *` or an accidental `Vary: Cookie` destroying the hit ratio; a header added to the key at the CDN but not reflected in `Vary`, so intermediate caches still collapse variants; unkeyed inputs such as `X-Forwarded-Host` being reflected into the response and enabling cache poisoning; and a key change deployed without a purge, leaving both old and new entries live simultaneously.

## References

- [Amazon CloudFront cache key and cache policy documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-key-understand-cache-policy.html)
- [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Further reading (blog): [Fastly blog](https://www.fastly.com/blog)

## What to learn next

- Official documentation: [Amazon CloudFront cache key and cache policy documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-key-understand-cache-policy.html)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Julia Evans — HTTP and networking explainers](https://jvns.ca/)
- Technical blog: [Fastly blog](https://www.fastly.com/blog)
- Hands-on guide: [MDN Vary header reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary)
