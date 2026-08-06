---
title: Respond to a BGP route leak risk
theme: networking
difficulty: senior
type: scenario
tags: [networking, security, incident-response, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc4271.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc8212.html
    source_type: standard
    verified_on: 2026-08-06
---

# Respond to a BGP route leak risk

What controls reduce the chance that your edge advertises or accepts unintended Internet routes?

## Answer guide

- BGP distributes reachability between autonomous systems; a route leak is a propagation or advertisement that violates intended policy and can redirect traffic or create instability. Do not treat BGP adjacency as a trust boundary by itself.
- Apply explicit inbound and outbound prefix/AS-path policy, maximum-prefix limits, and only advertise owned/authorized prefixes. RFC 8212 recommends that eBGP implementations require explicit import and export policy rather than accepting and advertising everything by default.
- Use route-origin validation and provider coordination where available, but understand that validation is one signal, not a complete guarantee of correct propagation policy. Monitor announced prefixes, paths, and reachability from independent vantage points.
- Have a tested withdrawal/escalation runbook and protect management access. A hurried broad filter can cause a larger outage than the original bad route, so changes need peer review and rollback.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 4271: Border Gateway Protocol 4](https://www.rfc-editor.org/rfc/rfc4271.html)
- [RFC 8212: Default External BGP Route Propagation Behavior](https://www.rfc-editor.org/rfc/rfc8212.html)
- [MANRS routing security actions](https://www.manrs.org/)
