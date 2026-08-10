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

## What to learn next

- Official documentation: [Cilium Hubble network observability](https://docs.cilium.io/en/stable/observability/hubble/)
- Manual or specification: [eBPF reference — what is eBPF?](https://ebpf.io/what-is-ebpf/)
- Maintainer or personal blog: [Brendan Gregg — eBPF tracing resources](https://www.brendangregg.com/ebpf.html)
- Technical blog: [Cilium project blog](https://cilium.io/blog/)
- Hands-on guide: [Layer 7 flow visibility with hubble observe](https://docs.cilium.io/en/stable/observability/visibility/)
