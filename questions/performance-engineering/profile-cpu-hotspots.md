---
title: How do you investigate a CPU hotspot without optimizing the wrong code?
theme: performance-engineering
difficulty: middle
type: troubleshooting
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.brendangregg.com/perf.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you investigate a CPU hotspot without optimizing the wrong code?

A service is using 70 percent of its CPU budget and the flame graph shows `memcpy` as the widest leaf frame. How do you profile it so that the fix targets the real cost?

## Answer guide

- A leaf like `memcpy`, `malloc`, or a serialization routine is a symptom; the actionable unit is the call path that reaches it, so read a flame graph by the width of the ancestor frames rather than the top row. Collect with `perf record -F 99 -g` or the runtime's sampling profiler over the workload you actually care about, then fold to a flame graph. Sampling at 99 Hz instead of 100 Hz avoids lock-stepping with periodic timer work and the aliasing that produces.
- On-CPU profiling can only ever explain CPU time. If the service is slow but not CPU-saturated, the latency is off-CPU — blocked on a lock, on I/O, or waiting for the scheduler — and no amount of extra on-CPU profiling will reveal it; that needs off-CPU sampling such as `offcputime` or scheduler tracing. Decide which regime you are in from the utilization-versus-latency correlation before you profile, or you will optimise code that is not where the delay lives.
- The profile is only as good as the stacks. Builds compiled with `-fomit-frame-pointer` truncate stacks to one frame, so either build with frame pointers, pay for `--call-graph dwarf`, or use LBR. Symbolisation needs debug info, JIT runtimes (JVM, Node, .NET) need a perf map agent, and profiling inside a container needs the symbols visible in the profiler's mount namespace. Permission is the other common wall: `perf` needs `perf_event_paranoid` relaxed or `CAP_PERFMON`, which is usually why profiling a pod silently returns nothing.
- A profile captured while the service is idle, warming up, or driven by a synthetic harness attributes cost to startup or to the harness. Percentages are relative, so a frame worth 40 percent of CPU is worth nothing if the service is I/O-bound. Amdahl's law bounds the payoff: halving the cost of a path that is 20 percent of CPU returns 10 percent. Confirm the fix by re-measuring end-to-end latency, throughput, and cost, not by confirming that the frame in the flame graph got narrower.

## References

- [Brendan Gregg: perf tools](https://www.brendangregg.com/perf.html)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
