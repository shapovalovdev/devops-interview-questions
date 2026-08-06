---
title: Prevent a reverse-proxy cache from serving the wrong response
theme: web-servers
difficulty: middle
type: troubleshooting
tags: [http, nginx, performance, security]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent a reverse-proxy cache from serving the wrong response

A user sees another user’s data after a cache rollout. What do you investigate and change?

## Answer guide

- Disable or bypass the affected cache safely, identify the effective cache key and response cacheability rules, and inspect whether cookies, authorization, method, query parameters, Host, locale or content negotiation were omitted. Purge only after preserving evidence and confirming the scope of exposure.
- Cache shared responses only with an explicit public contract, honor origin cache controls, use `Vary` where representations differ, and make personalized or authorization-dependent responses private or uncacheable. Test with independent accounts and request variants in CI and at the edge.
- A cache key that ignores Host can mix tenants; ignoring Authorization or Cookie can expose data. Blindly purging does not fix a bad key, and adding every header destroys hit rate. Treat the event as a security incident when another principal’s response was delivered.

## References

- [NGINX proxy cache controls](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- Further reading (personal blog): [Mark Nottingham on HTTP caching](https://www.mnot.net/blog/)

## What to learn next

- Official documentation: [NGINX caching guide](https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/)
- Manual or specification: [RFC 9111: HTTP caching](https://www.rfc-editor.org/rfc/rfc9111)
- Maintainer or personal blog: [Mark Nottingham's blog](https://www.mnot.net/blog/)
- Technical blog: [Cloudflare cache docs](https://developers.cloudflare.com/cache/)
- Hands-on guide: [NGINX source and build instructions](https://github.com/nginx/nginx)
