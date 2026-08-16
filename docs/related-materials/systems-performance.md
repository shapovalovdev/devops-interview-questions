# Systems performance related materials

These materials support safe systems-performance investigation: establish a
baseline, quantify overhead, and avoid collecting sensitive production data
without a review. *Systems Performance* itself is commercially published, so
this page links only lawful public material rather than copies of that book.

## What to learn next

- Official documentation: [Linux kernel performance events](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Manual or specification: [perf(1) manual](https://man7.org/linux/man-pages/man1/perf.1.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Datadog Engineering](https://www.datadoghq.com/blog/engineering/)
- Hands-on guide: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)

## Legal free books

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) is freely published by Google and is useful for service-level, capacity, and incident context.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) is freely published companion material with practical exercises and implementation guidance.

## Suggested study order

Method before metrics, resources before tools, tools before benchmark validity —
the staff tier spends the whole method.

1. [Why establish a baseline before performance tuning?](../../questions/systems-performance/baseline-before-tuning.html)
    — A baseline is why tuning can be judged at all, so method comes before
    metrics.
2. [How do you apply the USE method to a production resource?](../../questions/systems-performance/use-method-basics.html)
    — The USE method turns checking everything into a directed question.
3. [What is the difference between CPU utilization and CPU saturation?](../../questions/systems-performance/cpu-utilization-and-saturation.html)
    — Utilization versus saturation decides which question to ask next of a
    resource.
4. [What is a safe first pass for investigating unexpected CPU consumption?](../../questions/systems-performance/cpu-profiling-first-pass.html)
    — CPU leads the resources with a safe first pass on unexpected consumption.
5. [When are high context-switch rates a performance concern?](../../questions/systems-performance/context-switch-investigation.html)
    — Context-switch rates matter only against a threshold worth the name.
6. [How do you investigate high CPU steal time on a virtual machine?](../../questions/systems-performance/cpu-steal-time-cloud.html)
    — Steal time is somebody else's saturation billed to your virtual machine.
7. [How do you prove lock contention is causing an application latency regression?](../../questions/systems-performance/lock-contention-analysis.html)
    — Proving lock contention closes the CPU chapter where the application meets
    the scheduler.
8. [Which signals distinguish memory use from memory pressure on Linux?](../../questions/systems-performance/memory-pressure-signals.html)
    — Memory opens with use versus pressure, the distinction everything leans
    on.
9. [How does the Linux page cache affect filesystem performance measurements?](../../questions/systems-performance/filesystem-cache-behavior.html)
    — The page cache explains the filesystem measurements that confused
    everyone.
10. [What does Linux pressure stall information add to resource monitoring?](../../questions/systems-performance/pressure-stall-information.html)
    — PSI quantifies the stall the pressure signals could only infer.
11. [How do you investigate an OOM-killer incident without treating the kill as the root cause?](../../questions/systems-performance/oom-killer-incident.html)
    — The OOM investigation refuses to treat the kill itself as the root cause.
12. [How do you break down elevated disk I/O latency?](../../questions/systems-performance/disk-latency-breakdown.html)
    — Storage follows the memory chapter with a structured disk-latency
    breakdown.
13. [How do TCP retransmissions inform a latency investigation?](../../questions/systems-performance/network-retransmission-triage.html)
    — TCP retransmissions inform the latency investigation from the network
    side.
14. [How can NUMA locality cause a performance regression on a large host?](../../questions/systems-performance/numa-locality-performance.html)
    — NUMA locality is the topology regression large hosts quietly hide.
15. [How do you investigate a tail-latency incident when average latency is normal?](../../questions/systems-performance/tail-latency-incident.html)
    — The tail-latency incident with a normal average ties the resource chapters
    into one case.
16. [How do you select ftrace events for a latency investigation?](../../questions/systems-performance/ftrace-event-selection.html)
    — Tools arrive late on purpose, because they assume you know what you are
    looking for.
17. [How do you use sampling profilers without distorting production performance?](../../questions/systems-performance/perf-sampling-and-overhead.html)
    — Sampling profilers are used without distorting the production being
    measured.
18. [What safeguards are needed when using eBPF for production observability?](../../questions/systems-performance/ebpf-observability-safety.html)
    — eBPF carries safeguards because it is powerful in exactly the wrong
    places.
19. [How do you review whether a benchmark result is valid for a production decision?](../../questions/systems-performance/benchmark-validity-review.html)
    — Benchmark validity decides whether measurements ever become decisions.
20. [How would you govern a capacity model for a multi-tenant platform?](../../questions/systems-performance/capacity-model-governance.html)
    — The capacity model is governed, not worshipped, once it drives decisions.
21. [How do you use performance budgets in architecture governance?](../../questions/systems-performance/performance-budget-architecture.html)
    — The closing three open with performance budgets in architecture
    governance.
22. [How should a staff engineer lead a cross-layer performance incident?](../../questions/systems-performance/performance-incident-command.html)
    — Leading a cross-layer incident spends the whole method under pressure.
23. [How would you design a systems-performance observability program across teams?](../../questions/systems-performance/performance-observability-program.html)
    — The observability program is the staff-level synthesis of everything
    above.
