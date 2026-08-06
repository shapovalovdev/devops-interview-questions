---
title: Make upstream retries safe at a proxy
theme: web-servers
difficulty: senior
type: scenario
tags: [http, nginx, reliability, availability]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Make upstream retries safe at a proxy

When may a reverse proxy retry an upstream request, and when must it not?

## Answer guide

- Retry only operations whose effect is known to be safe to repeat, or where the application implements an idempotency key and replay contract. Bound attempt count and total deadline, select a different healthy upstream when appropriate, and record original attempt, retry reason and final result.
- Separate connection failure before request transmission from a timeout after an upstream may have processed the request. Follow documented proxy behavior for request buffering and partial responses, and coordinate the proxy policy with client SDKs, service meshes and job queues to avoid stacked retries.
- Retrying a payment, mutation or email after a response timeout can duplicate side effects. Aggressive retries turn partial dependency failure into overload; retrying every status hides application bugs. Never claim a failed response means the upstream did nothing without evidence or reconciliation.

## References

- [NGINX proxy retry settings](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- Further reading (personal blog): [Brandur Leach on idempotency](https://brandur.org/)

## What to learn next

- Official documentation: [Envoy retry architecture](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_routing#retry-policy)
- Manual or specification: [RFC 9110 idempotent methods](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Brandur Leach's writing](https://brandur.org/)
- Technical blog: [AWS retries and backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- Hands-on guide: [NGINX reverse proxy guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
