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

Method before metrics: why a baseline precedes tuning, the USE method applied
to a real resource, and utilization versus saturation, since together they
decide which question to ask next. CPU leads the resources — the safe first
pass on unexpected consumption, context-switch rates, steal time on a virtual
machine, proving lock contention — then memory: use versus pressure, page-cache
effects on filesystem measurements, pressure stall information, and the
OOM-killer investigation that refuses to treat the kill as the root cause.
Storage and network follow with the disk-latency breakdown, TCP
retransmissions, and NUMA locality, and the tail-latency incident with a normal
average ties the resource chapters into one case. Tools arrive late on purpose
— ftrace event selection, sampling profilers that do not distort production,
eBPF safeguards — because they assume you know what you are looking for.
Benchmark validity and capacity-model governance decide whether measurements
become decisions, and the closing three — performance budgets in architecture
governance, leading a cross-layer incident, and the observability programme —
are staff-level because they spend the whole method.
