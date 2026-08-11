---
title: Set a staleness budget with stale-while-revalidate
theme: caching
difficulty: senior
type: scenario
tags: [caching, http, reliability, availability, latency]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc5861.html
    source_type: standard
    verified_on: 2026-08-10
  - url: https://www.rfc-editor.org/rfc/rfc9111.html
    source_type: standard
    verified_on: 2026-08-10
---

# Set a staleness budget with stale-while-revalidate

Your origin cannot survive the refresh load a short TTL creates, but the product wants fresh data. How do you use a staleness budget to satisfy both?

## Answer guide

- Split freshness into two numbers instead of one. `max-age` is how long the copy is considered fresh; `stale-while-revalidate` is how long past that a cache may serve the stale copy immediately while it refreshes in the background. Requests during that window get a fast response from cache and the origin sees one refresh instead of a wall of blocked clients.
- Add the second half of the budget for failure: `stale-if-error` lets a cache keep serving the expired copy when the origin returns a 5xx, times out, or cannot be reached. That converts a total origin outage into a degradation whose duration you chose in advance, which is usually the single highest-value caching change an availability review can make.
- Write the numbers down as a product decision, not a config value. State the maximum acceptable staleness in normal operation and the maximum during an origin incident, and derive `max-age`, `stale-while-revalidate`, and `stale-if-error` from them. Different resources deserve different budgets — a pricing page and an availability count are not the same risk.
- Know the caveats. RFC 5861 defines these as extensions and RFC 9111 permits a cache to serve stale responses only when it is not forbidden — for instance by `must-revalidate` or `no-cache` — so support varies by CDN, reverse proxy, and browser, and an unsupported directive is silently ignored. Verify behaviour per hop rather than assuming, and expose the served age so you can prove it later. `nginx` expresses the same idea through `proxy_cache_use_stale` with `updating` and `error` rather than through the HTTP directives.
- Failure modes to name: a long `stale-if-error` masking an origin that has been broken for hours because nobody alerts on served age; background revalidation that itself stampedes because it is not coalesced; a stale error response being stored and then re-served; and stacked layers each adding their own staleness so the true worst case is the sum across hops.

## References

- [RFC 5861 — HTTP Cache-Control extensions for stale content](https://www.rfc-editor.org/rfc/rfc5861.html)
- [RFC 9111 — HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- Further reading (blog): [Fastly blog](https://www.fastly.com/blog)

## What to learn next

- Official documentation: [MDN Cache-Control header reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
- Manual or specification: [RFC 5861 — HTTP Cache-Control extensions for stale content](https://www.rfc-editor.org/rfc/rfc5861.html)
- Maintainer or personal blog: [Marc Brooker — caches, modes, and unstable systems](https://brooker.co.za/blog/2021/08/27/caches.html)
- Technical blog: [Fastly blog](https://www.fastly.com/blog)
- Hands-on guide: [nginx proxy_cache_use_stale directive reference](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_use_stale)
