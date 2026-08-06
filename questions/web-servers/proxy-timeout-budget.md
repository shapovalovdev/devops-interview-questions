---
title: Set reverse-proxy timeouts from a request budget
theme: web-servers
difficulty: middle
type: scenario
tags: [nginx, http, latency, reliability]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set reverse-proxy timeouts from a request budget

How should proxy connect, send and read timeouts relate to an end-to-end service objective?

## Answer guide

- Derive a deadline from the caller’s end-to-end latency budget and allocate bounded time for connection, request transmission, upstream processing and response transfer. Configure the proxy explicitly, propagate a deadline where the application supports it, and make upstream cancellation observable.
- A connect timeout protects the wait for a socket; read timeout normally limits idle time between upstream reads, not necessarily total response duration. Measure percentiles and timeout reasons before tuning, because buffering, streaming responses and HTTP protocol behavior change the relevant metric.
- A proxy timeout shorter than the downstream deadline produces avoidable 504 responses; a much longer one holds workers and connections during overload. Retrying at several layers multiplies load. Treat a timeout as an uncertain outcome for non-idempotent operations and use a bounded retry policy.

## References

- [NGINX proxy module timeouts](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- Further reading (personal blog): [Marc Brooker on timeouts](https://brooker.co.za/blog/)

## What to learn next

- Official documentation: [Envoy timeouts](https://www.envoyproxy.io/docs/envoy/latest/faq/configuration/timeouts)
- Manual or specification: [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS on timeouts and retries](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- Hands-on guide: [NGINX proxy configuration](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
