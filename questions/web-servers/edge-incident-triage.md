---
title: Lead an edge-web-server incident triage
theme: web-servers
difficulty: senior
type: troubleshooting
tags: [incident-response, troubleshooting, nginx, observability]
sources:
  - url: https://docs.nginx.com/nginx/admin-guide/monitoring/logging/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Lead an edge-web-server incident triage

Requests are failing intermittently at the edge. What evidence and sequence guide the first thirty minutes?

## Answer guide

- Establish scope by hostname, region, protocol, status class, client population and start time. Correlate load-balancer, web-server and upstream metrics with deploys, certificate changes, DNS, capacity and dependency health; preserve a sample of request IDs, logs and configuration versions before changing them.
- Mitigate the narrowest proven failing layer: shift traffic, drain an unhealthy pool, roll back a bad edge configuration, or protect an overloaded dependency. Assign explicit incident roles and update stakeholders with impact, current hypothesis, mitigation and next evidence checkpoint.
- Do not restart every proxy or purge every cache without a hypothesis; that can erase useful state and spread a configuration defect. A 5xx aggregate hides 499s, resets and client-specific failures. After recovery, verify delayed queues, certificate propagation and error budgets before declaring resolution.

## References

- [NGINX logging guide](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
- Further reading (personal blog): [John Allspaw on incident response](https://www.kitchensoap.com/)

## What to learn next

- Official documentation: [NGINX monitoring guide](https://docs.nginx.com/nginx/admin-guide/monitoring/)
- Manual or specification: [Google SRE incident response](https://sre.google/sre-book/managing-incidents/)
- Maintainer or personal blog: [John Allspaw's blog](https://www.kitchensoap.com/)
- Technical blog: [Cloudflare outage posts](https://blog.cloudflare.com/)
- Hands-on guide: [NGINX logging guide](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
