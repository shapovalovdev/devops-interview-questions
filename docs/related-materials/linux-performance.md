# Linux performance related materials

These resources complement the Linux-performance Theme. Start with a workload
baseline, and use production tracing only with an explicit overhead and data
handling plan.

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [proc(5) manual](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)

## Suggested study order

Work this Theme as a resource tour, one subsystem at a time, before any
governance question. The cheap first passes come first — vmstat, CPU
utilization read correctly, the growing run queue, load average interpreted
honestly — because their job is to point at the next tool. CPU continues with
excess context switching, perf profiling, and cgroup throttling; memory follows
with free versus available, the OOM analysis, page-cache reclaim, pressure
stall information, and sustained swap. The I/O and network group closes the
technical half: iowait without blaming storage, the full filesystem with
free-looking space, file-descriptor exhaustion, TCP retransmissions, softirq
saturation. Take NUMA locality, kernel samepage merging, noisy-neighbour
policy, and observability overhead once single-host diagnosis is reliable. The
programme questions — the baseline programme, the capacity model, leading a
performance incident — finish the set by making the tools an organizational
habit instead of personal heroics.
