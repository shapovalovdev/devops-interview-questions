---
title: Design multi-tenant isolation at the web edge
theme: web-servers
difficulty: staff
type: scenario
tags: [security, governance, web-server, availability]
sources:
  - url: https://owasp.org/www-project-application-security-verification-standard/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design multi-tenant isolation at the web edge

What controls prevent one tenant’s hostname, traffic spike, route or cache entry from affecting another tenant?

## Answer guide

- Establish tenant boundaries in hostname ownership, certificate issuance, route namespaces, upstream credentials, cache keys, log access, rate and concurrency budgets, and deployment authorization. Make the isolation properties testable with negative cases: unknown Host, cross-tenant cache key, direct origin request and exhausted tenant quota.
- Choose the isolation strength by threat model and blast radius. Some tenants require separate processes, load balancers or accounts; others can share an edge with strict policy. Keep a current inventory linking domains, DNS, certificates, configuration, owners and data classification.
- Sharing a wildcard route, default vhost or cache key can expose another tenant’s traffic. Per-tenant limits can still overwhelm shared upstreams without global protections. Migration and deletion are security events: stale DNS, certificates and routes can become takeover paths after a tenant is removed.

## References

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Further reading (personal blog): [Scott Helme on domain security](https://scotthelme.co.uk/)

## What to learn next

- Official documentation: [NGINX server names](https://nginx.org/en/docs/http/server_names.html)
- Manual or specification: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- Maintainer or personal blog: [Scott Helme's blog](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare multi-tenant security](https://blog.cloudflare.com/)
- Hands-on guide: [NGINX access control](https://docs.nginx.com/nginx/admin-guide/security-controls/controlling-access-proxied-http/)
