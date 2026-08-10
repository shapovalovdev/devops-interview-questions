---
title: Govern a shared cache platform
theme: caching
difficulty: staff
type: scenario
tags: [caching, platform-engineering, governance, reliability, cost-optimization]
sources:
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/security/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://redis.io/docs/latest/operate/oss_and_stack/management/config/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Govern a shared cache platform

Forty services share one cache cluster. One team's change now regularly evicts another team's data. How do you govern the platform?

## Answer guide

- Name the structural problem: a single shared memory pool with no isolation makes every tenant's capacity a function of every other tenant's behaviour, and eviction is the mechanism by which one team's incident becomes another's. Governance documents cannot fix that; the isolation boundary has to be real.
- Choose the isolation model deliberately, and price each option. Dedicated clusters per critical service give the strongest blast-radius containment at the highest cost and operational surface; shard groups or separate databases per tenant give partial separation; and a single pool with per-tenant quotas gives the least isolation but the best utilisation. Reserve dedicated capacity for the tenants whose failure would be user-visible and pool the rest, rather than applying one rule to everything.
- Enforce the contract in the client library, not in a wiki. A platform-owned client that mandates key prefixes, caps value and key sizes, requires a TTL on every write, applies sane timeouts, coalesces refreshes, and fails open to the origin removes whole classes of incident and gives the platform team a place to ship fixes once. Access control with per-tenant credentials and command restrictions keeps one tenant from running an expensive or destructive command against the whole instance.
- Make consumption observable and attributable before you make it chargeable. Per-prefix memory, request rate, hit ratio, eviction share, and error rate, broken down by tenant, turn arguments into data and let capacity be planned rather than negotiated. Showback usually changes behaviour on its own; chargeback is only worth the friction once the numbers are trusted.
- Run it as a product with an operating contract: an onboarding review that asks for the staleness budget and the cache-unavailable behaviour, a stated SLO for the platform itself, a documented degraded mode, quotas with alerting before they bite, and a deprecation path for abandoned key spaces. The most common long-run failure is not a technical one — it is an unowned key family from a deleted service that nobody dares remove.

## References

- [Redis security documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Redis configuration reference](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
- Further reading (blog): [Redis blog](https://redis.io/blog/)

## What to learn next

- Official documentation: [Redis security documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- Manual or specification: [Redis configuration reference](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
- Maintainer or personal blog: [Will Larson — engineering and platform strategy writing](https://lethain.com/)
- Technical blog: [Scaling Memcache at Facebook, NSDI 2013](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala)
- Hands-on guide: [Google SRE book — table of contents](https://sre.google/sre-book/table-of-contents/)
