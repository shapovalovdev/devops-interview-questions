---
title: Apply web-server rate limits without harming clients
theme: web-servers
difficulty: middle
type: scenario
tags: [nginx, security, availability, traffic-management]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_limit_req_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply web-server rate limits without harming clients

How do you design a request-rate limit for a public login endpoint?

## Answer guide

- Choose an identity key that cannot be trivially forged, such as a normalized authenticated principal or trusted client address, and set a documented rate and bounded burst based on downstream capacity and user behavior. Return a clear status and retry guidance, and measure allowed, delayed and rejected requests.
- Scope limits per sensitive route and combine them with application controls, account lockout policy and abuse detection. Validate behavior through trusted proxies, NATed enterprise users, IPv6, distributed deployments and deployment restarts; local in-memory limits may not be globally consistent.
- A global limit can let one attacker deny service to everyone, while an unlimited burst only moves overload to the application. Do not trust client-supplied forwarding headers. Rate limiting is not authorization, bot detection, or a substitute for capacity planning and incident response.

## References

- [NGINX request-limit module](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html)
- Further reading (personal blog): [Troy Hunt on abuse and security](https://www.troyhunt.com/)

## What to learn next

- Official documentation: [NGINX connection limits](https://nginx.org/en/docs/http/ngx_http_limit_conn_module.html)
- Manual or specification: [RFC 6585: 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [Cloudflare rate limiting docs](https://developers.cloudflare.com/waf/rate-limiting-rules/)
- Hands-on guide: [NGINX limiting guide](https://docs.nginx.com/nginx/admin-guide/security-controls/controlling-access-proxied-http/)
