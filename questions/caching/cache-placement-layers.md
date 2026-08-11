---
title: Compare cache placement layers
theme: caching
difficulty: junior
type: theory
tags: [caching, cdn, http, architecture]
sources:
  - url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
    source_type: official-docs
    verified_on: 2026-08-10
---

# Compare cache placement layers

Where can a cache sit between a user's browser and the database, and what does each placement buy and cost?

## Answer guide

- Name the layers in order: the browser or client private cache, a shared forward or corporate proxy, the CDN or edge point of presence, a reverse proxy in front of the service, an in-process local cache inside the application, a shared remote cache such as Redis or Memcached, and finally the database's own buffer pool and query caches.
- The nearer the cache is to the user, the more latency and downstream load it removes, and the less control you have over invalidating it. A browser cache cannot be purged, only versioned out by changing the URL. A CDN can usually be purged but the purge is asynchronous across many points of presence. A shared server-side cache can be invalidated deterministically.
- Correctness scope differs by layer. A private cache may hold user-specific content; a shared cache must not, which is what `Cache-Control: private` versus `public` and the `Vary` header exist to express. Putting per-user data behind a shared layer without correct key scoping is the classic way to serve one customer another customer's page.
- Cost and blast radius differ too. Edge caching is billed on traffic and shifts risk to a third party's configuration; an in-process cache is free but multiplies memory per replica and gives every replica a different view; a shared remote cache gives one consistent view but adds a network hop and a new dependency that can fail.
- Failure modes to name: layered TTLs that stack so the effective staleness is the sum rather than the maximum, a purge at one layer that leaves a stale copy at another, and an in-process cache that makes canary comparisons meaningless because each replica warms differently.

## References

- [Amazon CloudFront developer guide introduction](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [MDN HTTP caching guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
- Further reading (blog): [Cloudflare blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Amazon CloudFront developer guide introduction](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- Manual or specification: [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Maintainer or personal blog: [Julia Evans — systems explainers and zines](https://jvns.ca/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [web.dev — the HTTP cache](https://web.dev/articles/http-cache)
