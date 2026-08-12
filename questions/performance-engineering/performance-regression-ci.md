---
title: What should a performance regression check in CI actually prove?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# What should a performance regression check in CI actually prove?

A CI job runs a 60-second benchmark on every pull request and fails the build when p95 exceeds the previous run by ten percent. Why does that gate fail the team, and what should it assert instead?

## Answer guide

- Comparing against the immediately preceding run on shared CI hardware measures the runner, not the change. Noise on shared runners routinely exceeds ten percent, so the gate emits false failures, the team learns to re-run until green, and it then catches nothing real. A gate worth keeping compares against a rolling baseline distribution with a threshold derived from that distribution's own variance, builds and runs candidate and baseline in the same job on the same machine, and requires the failure to reproduce before it blocks a merge.
- Shift what CI asserts toward things that are deterministic in a noisy environment: allocation counts, SQL statements executed per request (which is how you catch an N+1 before production), number of downstream calls, bytes transferred, response or bundle size, and scaling behaviour across a growing input. These are counts, not times, so they are stable on a busy runner. Wall-clock throughput and tail latency need quiet pinned hardware and long runs, which belongs in a nightly or pre-release job, with a production canary as the final check.
- A 60-second run barely clears warm-up on a JIT runtime or a cold page cache, so much of what it measures is startup. Fix what you can — pinned instance type, dedicated host, CPU pinning, no concurrent jobs — and report a distribution across repetitions instead of one number. Version the benchmark's dataset alongside the benchmark itself, or a fixture change will present as a code regression and consume a day of investigation.
- A flaky gate is worse than no gate, because it teaches an entire team to dismiss performance signals. A microbenchmark gate can stay green while the service regresses, since it excludes I/O, serialization, and contention. The subtler failure is automatic baseline ratcheting after every merge: twenty consecutive two-percent regressions compound to roughly forty percent without a single build ever failing, so keep an absolute budget tied to the user-facing objective next to the relative comparison.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
