---
title: Design an API rate-limiting policy
theme: backend-architecture
difficulty: middle
type: scenario
tags: [http, availability, security]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc6585
    source_type: standard
    verified_on: 2026-08-06
---

# Design an API rate-limiting policy

How should a public API protect shared capacity without making failures opaque?

## Answer guide

- Define a named resource budget and a key such as API credential, tenant, route, or source identity; choose a documented algorithm such as token bucket. Apply limits at a trustworthy point and return a clear 429 response with safe retry guidance.
- Separate sustained rate, burst allowance, expensive-operation quota, and emergency protection. Instrument allowed, limited, and error requests by tenant and route, and provide a reviewed override process for legitimate high-volume integrations.
- A limit keyed only by source IP harms users behind NAT, while globally coordinated counters can become a dependency outage. Do not retry 429s immediately; test abusive traffic, distributed limiter failure, and fairness under one noisy tenant.

## References

- [RFC 6585: 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585)
- Further reading (blog): [Stripe: rate limiters](https://stripe.com/blog/rate-limiters)

## What to learn next

- Official documentation: [Envoy local rate limit](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/local_rate_limit_filter)
- Manual or specification: [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [Envoy rate limiting sandbox](https://www.envoyproxy.io/docs/envoy/latest/start/sandboxes/ratelimit)
