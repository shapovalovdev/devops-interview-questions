---
title: Debug a 502 response from a reverse proxy
theme: web-servers
difficulty: middle
type: troubleshooting
tags: [http, nginx, web-server, troubleshooting]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a 502 response from a reverse proxy

An NGINX reverse proxy returns 502 while the page itself is reachable. How do you isolate the failing layer?

## Answer guide

- A 502 means the proxy could not obtain a valid response from its configured upstream; it is different from an application response that happened to contain an error page. Start with the NGINX error log and the exact upstream address, port, protocol, and failure text it records.
- From the proxy's network namespace, verify that the upstream process is running, listening on the configured address, and reachable with the expected HTTP or TLS protocol. Correlate proxy and application logs by request ID or a tight time window.
- Then check upstream DNS resolution, certificate/SNI settings, timeout values, socket/file permissions, network policy, and health/load-balancer state. Test a direct upstream request before changing proxy configuration.
- Avoid treating every 502 as a timeout: connection refusal, DNS resolution, a TLS handshake mismatch, and a prematurely closed upstream need different fixes. Preserve the failed configuration and redact secrets before sharing diagnostics.

## References

- [NGINX documentation: proxy module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- Further reading (blog): [NGINX: troubleshooting common errors](https://www.nginx.com/blog/avoiding-top-10-nginx-configuration-mistakes/)
