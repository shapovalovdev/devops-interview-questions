---
title: Contain the blast radius of a cache outage
theme: caching
difficulty: senior
type: troubleshooting
tags: [caching, reliability, availability, incident-response, troubleshooting]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Contain the blast radius of a cache outage

The cache tier is unreachable and the service is now failing rather than merely slowing down. What went wrong in the design, and what do you do now?

## Answer guide

- Name the design flaw plainly: the cache was an availability dependency rather than an optimisation. A cache should be able to disappear and leave a degraded but working service. If losing it produces errors, either the origin cannot serve the full request rate, or the client code treats a cache error as a fatal error instead of a miss.
- Stabilise before restoring. The immediate risk is that removing the cache multiplies origin load by roughly the inverse of the miss rate, so a tier that was absorbing 95 percent of reads hands the origin twenty times its normal traffic. Shed load deliberately: turn on request coalescing, serve stale copies from any surviving layer, enable a reverse proxy's stale-on-error path, rate-limit or queue the expensive endpoints, and disable non-critical features that read through the cache.
- Restore cold caches gradually. Sending full traffic at an empty tier produces a stampede that can knock the origin over a second time and can also overwhelm the cache itself. Ramp traffic, warm the highest-value keys first, and watch origin saturation rather than cache hit ratio as the signal for how fast to go.
- Fix the client contract afterwards. Cache calls need timeouts far shorter than the request budget, bounded retries, a circuit breaker that fails open to the origin, and error handling that distinguishes "cache says absent" from "cache did not answer". A shared client library is the practical place to enforce this so every service inherits the same behaviour.
- Follow up with the structural work: capacity-test the origin at zero hit ratio so the real headroom is known rather than assumed, add a load-shedding policy with an explicit priority order, and rehearse the failure — a scheduled game day that takes the cache away is the only reliable way to find the services that quietly cannot live without it.

## References

- [nginx HTTP proxy module reference](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- [Amazon ElastiCache developer guide overview](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [nginx HTTP proxy module reference](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- Manual or specification: [RFC 5861 — HTTP Cache-Control extensions for stale content](https://www.rfc-editor.org/rfc/rfc5861.html)
- Maintainer or personal blog: [Marc Brooker — timeouts, retries and backoff with jitter](https://brooker.co.za/blog/2022/02/28/retries.html)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — table of contents](https://sre.google/sre-book/table-of-contents/)
