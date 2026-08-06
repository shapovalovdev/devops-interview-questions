---
title: Profile CPU with perf safely in production
theme: linux-performance
difficulty: senior
type: scenario
tags: [linux, performance, cpu, debugging, observability]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Profile CPU with perf safely in production

What safeguards should precede `perf` sampling on a production Linux host?

## Answer guide

- Define the symptom, target process or cgroup, sampling interval, collection owner, and a rollback condition. `perf` accesses kernel performance events, so follow the host's permission and security policy and choose the least intrusive measurement that answers the question.
- Measure overhead with a short trial, preserve timestamps and build identifiers, and correlate samples with CPU, request, and latency data. Prefer a representative canary or replica if production sensitivity, customer data, or capacity makes direct profiling risky.
- Sampling can perturb a saturated system and expose symbols or workload details. Do not grant broad privileges permanently or treat a flame graph as causation; validate the suspected hot path with a controlled change and before/after evidence.

## References

- [Linux kernel: perf security considerations](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Further reading (blog): [Brendan Gregg — perf Examples](https://www.brendangregg.com/perf.html)

## What to learn next

- Official documentation: [perf_event_open(2)](https://man7.org/linux/man-pages/man2/perf_event_open.2.html)
- Manual or specification: [perf(1)](https://man7.org/linux/man-pages/man1/perf.1.html)
- Maintainer or personal blog: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [perf security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
