---
title: What must stay controlled when you compare two performance runs?
theme: performance-engineering
difficulty: junior
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.brendangregg.com/methodology.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# What must stay controlled when you compare two performance runs?

Run A of the current build reports 12,000 requests per second and run B of the next commit reports 11,400. What must have been held constant before you can call that a five percent regression?

## Answer guide

- A comparison means something only when exactly one thing differs. Hold the build flags and runtime version, the dataset and its size and key distribution, warm-up state, the arrival model and concurrency, the run duration, and the hardware — same instance type, same CPU generation, ideally the same host. Then interleave the arms as ABAB rather than running all of A and then all of B, so environmental drift is shared by both instead of being charged entirely to the second one.
- Run-to-run variance is frequently larger than the effect under test. Cloud instances of one type ship several CPU models, burst credits on T-family instances and gp2 volumes deplete mid-run, co-tenants change, and turbo and thermal behaviour differ between hosts. Report a distribution over at least five repetitions with an explicit spread — median plus interquartile range, or a confidence interval — and treat any difference smaller than the measured run-to-run noise as no result rather than a small one.
- Record the variables you cannot control so the number can be re-interpreted later: kernel version, CPU model from `/proc/cpuinfo`, speculative-execution mitigation settings, container CPU quota and cgroup version, NUMA placement, filesystem and storage class, whether the generator was in the same availability zone, and the generator's own version and host. Warm-up is the most commonly skipped control — a JVM needs C2 compilation, the page cache needs filling, connection pools need establishing, and autoscaling needs to settle before the first measured request.
- Running on a shared CI runner produces noise that will never resolve into a signal no matter how many repetitions you add. Reusing state across arms breaks the comparison silently: a cache warmed by A, a table grown by A, a queue backlog left behind by A. Comparing peak throughput rather than throughput at a fixed latency target hides the case where B is faster only at latencies nobody would ship. And if the error rate differs between arms the throughput figures are not comparable at all, because failed requests complete cheaply.

## References

- [Brendan Gregg: Performance methodologies](https://www.brendangregg.com/methodology.html)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
