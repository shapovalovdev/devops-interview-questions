---
title: Choose an upstream load-balancing policy
theme: web-servers
difficulty: middle
type: scenario
tags: [nginx, web-server, traffic-management, availability]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_upstream_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose an upstream load-balancing policy

How do you choose and operate a policy for balancing requests across application instances?

## Answer guide

- Start with an explicit upstream pool, health signal and failure behavior. Round robin is a reasonable baseline for similar stateless instances; least-connections can help when request duration differs; consistent hashing is appropriate only when the application needs affinity and its failure behavior is understood.
- Set connect, read and response timeouts separately, observe per-upstream latency, errors and active connections, and remove instances through a graceful drain. A web-server passive failure setting detects request failures; it is not a complete replacement for application-aware readiness checks.
- Session affinity can create hot instances and makes replacement harder. Retrying a failed request may duplicate non-idempotent work, and marking a slow but healthy instance down can amplify a capacity incident. Test a node drain, network partition and uneven request-cost distribution before production.

## References

- [NGINX upstream module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html)
- Further reading (personal blog): [Marc Brooker on load balancing](https://brooker.co.za/blog/)

## What to learn next

- Official documentation: [NGINX upstream module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html)
- Manual or specification: [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [NGINX load balancing guide](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
