---
title: Govern global traffic failover for web endpoints
theme: web-servers
difficulty: staff
type: scenario
tags: [availability, dns, traffic-management, incident-management]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc2308
    source_type: standard
    verified_on: 2026-08-06
---

# Govern global traffic failover for web endpoints

How do you design a global failover process for public web traffic that balances speed, correctness and operator safety?

## Answer guide

- Define health signals that represent user success, eligible target capacity, routing ownership, maximum failover rate, rollback criteria and communication paths. Exercise the exact DNS, CDN or global-load-balancer mechanism with game days, including partial region failure and recovery while one region remains degraded.
- Account for DNS TTL and negative caching, resolver behavior, connection reuse, data locality, authentication dependencies and certificate consistency. Maintain sufficient warm capacity and configuration parity, and expose routing decisions and target health to the incident commander.
- Failing over faster than dependencies can handle may create a second outage. A green TCP probe cannot prove the application, authorization or database path works. Do not assume a short TTL means immediate universal convergence, and do not route write traffic across regions without explicit consistency and ownership semantics.

## References

- [RFC 2308: DNS negative caching](https://www.rfc-editor.org/rfc/rfc2308)
- Further reading (personal blog): [Marc Brooker on resilient systems](https://brooker.co.za/blog/)

## What to learn next

- Official documentation: [AWS Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- Manual or specification: [RFC 2308](https://www.rfc-editor.org/rfc/rfc2308)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [Cloudflare traffic management](https://blog.cloudflare.com/)
- Hands-on guide: [Google SRE disaster recovery](https://sre.google/workbook/disaster-recovery/)
