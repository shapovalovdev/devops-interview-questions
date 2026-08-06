---
title: Explain a web server request lifecycle
theme: web-servers
difficulty: junior
type: theory
tags: [http, web-server, nginx]
sources:
  - url: https://nginx.org/en/docs/http/request_processing.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a web server request lifecycle

What does a web server do after it accepts an HTTP request?

## Answer guide

- The server accepts a TCP or TLS connection, parses the HTTP request, chooses a virtual server from the local address and Host header, then applies location or route rules. It either returns a static response, generates one through a module, or proxies the request to an upstream application.
- Request processing is configuration and protocol dependent. TLS negotiation happens before HTTP routing; HTTP/2 streams can share one connection; and an invalid Host, malformed header, or unmatched route needs an explicit safe response. Log the selected server, route, status, upstream and timing fields.
- Do not assume a reachable listener proves the application is healthy. DNS may point to a different endpoint, a load balancer may terminate TLS, and an upstream timeout or bad response can fail after routing. Preserve request identifiers so those layers can be correlated.

## References

- [NGINX: how request processing works](https://nginx.org/en/docs/http/request_processing.html)
- Further reading (personal blog): [Mark Nottingham's HTTP writing](https://www.mnot.net/blog/)

## What to learn next

- Official documentation: [NGINX HTTP core module](https://nginx.org/en/docs/http/ngx_http_core_module.html)
- Manual or specification: [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Mark Nottingham's blog](https://www.mnot.net/blog/)
- Technical blog: [NGINX engineering blog](https://www.nginx.com/blog/)
- Hands-on guide: [NGINX beginner's guide](https://nginx.org/en/docs/beginners_guide.html)
