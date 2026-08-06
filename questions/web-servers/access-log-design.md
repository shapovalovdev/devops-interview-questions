---
title: Design useful web-server access logs
theme: web-servers
difficulty: junior
type: scenario
tags: [logging, observability, http, web-server]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_log_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design useful web-server access logs

Which fields should an access log contain to investigate a slow or failing request?

## Answer guide

- Record timestamp, request method and target, response status and bytes, request duration, virtual host, client address as interpreted behind trusted proxies, request ID, and upstream address, status and timing where proxying is used. Use a parseable structured format and document each field.
- Keep error logs separate for server failures and choose a sampling or retention policy that preserves incident evidence without exposing unnecessary data. Correlate the request ID with application, load-balancer and trace records, and validate logging changes with representative traffic.
- Logging raw authorization headers, cookies, credentials, full query strings or unrestricted bodies creates a security and privacy incident. Missing upstream timing makes a slow endpoint look like a web-server problem; overly verbose synchronous logging can itself consume disk or increase latency.

## References

- [NGINX HTTP log module](https://nginx.org/en/docs/http/ngx_http_log_module.html)
- Further reading (personal blog): [Charity Majors on observability](https://charity.wtf/)

## What to learn next

- Official documentation: [NGINX log module variables](https://nginx.org/en/docs/varindex.html)
- Manual or specification: [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- Maintainer or personal blog: [Charity Majors' blog](https://charity.wtf/)
- Technical blog: [OpenTelemetry logging](https://opentelemetry.io/docs/zero-code/)
- Hands-on guide: [NGINX logging guide](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
