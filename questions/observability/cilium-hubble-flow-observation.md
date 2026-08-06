---
title: Investigate a failed request with Cilium Hubble
theme: observability
difficulty: middle
type: troubleshooting
tags: [observability, kubernetes, networking, troubleshooting, debugging, cca]
sources:
  - url: https://docs.cilium.io/en/stable/gettingstarted/hubble_setup/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a failed request with Cilium Hubble

A Pod can resolve a Service name but its HTTP request times out. How would you use Hubble without treating it as the only source of truth?

## Answer guide

- Confirm that Hubble is enabled and reachable, then filter flows by namespace, source, destination, protocol, verdict, and time window to correlate the failed request.
- Use identity, DNS, L4/L7 metadata, and policy verdicts to distinguish name resolution, routing, policy denial, reset, and no-response symptoms.
- Corroborate the candidate cause with Service endpoints, workload readiness, application logs, and a controlled request from the same identity.
- Flow visibility has deployment, retention, sampling, and protocol limits. Sensitive metadata also needs access control; avoid concluding that an unseen flow proves no traffic occurred or changing policy before verifying the path.

## References

- [Cilium Hubble setup](https://docs.cilium.io/en/stable/gettingstarted/hubble_setup/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
