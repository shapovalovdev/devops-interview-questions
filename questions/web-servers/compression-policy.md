---
title: Design a response-compression policy
theme: web-servers
difficulty: middle
type: scenario
tags: [http, nginx, performance, security]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_gzip_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a response-compression policy

When should a web server compress responses, and what must it communicate to caches?

## Answer guide

- Compress suitable textual responses only when the client advertises a supported encoding, avoid already-compressed media, and choose a compression level within the CPU budget. Send `Vary: Accept-Encoding` so shared caches do not serve an encoded representation to an incompatible client.
- Establish thresholds and content-type allowlists, observe response size, CPU, cache hit rate and compression ratio, and test direct and cached clients. Prefer precompressed immutable assets when the build and deployment pipeline can produce and select them correctly.
- Compressing secret-bearing responses in attacker-influenced contexts can expose side-channel risk, so evaluate BREACH-style conditions rather than assuming TLS solves it. Missing Vary causes corrupt-looking content; unbounded dynamic compression can consume CPU exactly when traffic is high.

## References

- [NGINX gzip module](https://nginx.org/en/docs/http/ngx_http_gzip_module.html)
- Further reading (personal blog): [Troy Hunt on web security](https://www.troyhunt.com/)

## What to learn next

- Official documentation: [Apache mod_deflate](https://httpd.apache.org/docs/2.4/mod/mod_deflate.html)
- Manual or specification: [RFC 9110 content negotiation](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [Cloudflare compression docs](https://developers.cloudflare.com/speed/optimization/content/compression/)
- Hands-on guide: [NGINX compression guide](https://docs.nginx.com/nginx/admin-guide/web-server/compression/)
