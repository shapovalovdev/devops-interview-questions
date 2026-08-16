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
governance question.

1. [Use vmstat for a first performance pass](../../questions/linux-performance/vmstat-first-pass.html)
    — vmstat is the cheap first pass whose whole job is pointing at the next
    tool.
2. [Read CPU utilization before tuning](../../questions/linux-performance/cpu-utilization-basics.html)
    — Reading CPU utilization correctly prevents tuning a number that was never
    the problem.
3. [Investigate a growing CPU run queue](../../questions/linux-performance/cpu-run-queue-triage.html)
    — The growing run queue is the saturation the utilization average hid.
4. [Interpret Linux load average correctly](../../questions/linux-performance/load-average-meaning.html)
    — Load average interpreted honestly follows the queue, since it counts
    runnable and uninterruptible work alike.
5. [Investigate excess context switching](../../questions/linux-performance/context-switch-analysis.html)
    — Excess context switching continues the CPU story at the scheduler.
6. [Profile CPU with perf safely in production](../../questions/linux-performance/perf-sampling-safety.html)
    — perf profiling goes deeper than the counters, used safely in production.
7. [Diagnose cgroup CPU throttling](../../questions/linux-performance/cpu-throttling-diagnosis.html)
    — Cgroup CPU throttling is the container-era ceiling the scheduler tier
    explains.
8. [Distinguish free memory from available memory](../../questions/linux-performance/memory-available-basics.html)
    — Memory opens with free versus available, the distinction every capacity
    claim leans on.
9. [Analyze a Linux OOM kill](../../questions/linux-performance/oom-killer-analysis.html)
    — The OOM analysis needs the pressure picture the available-memory tier
    built.
10. [Investigate page-cache reclaim and memory pressure](../../questions/linux-performance/page-cache-reclaim.html)
    — Page-cache reclaim explains memory pressure with no process to blame.
11. [Use pressure stall information to find contention](../../questions/linux-performance/pressure-stall-information.html)
    — PSI quantifies the contention the tiers above could only infer.
12. [Respond to sustained swap activity](../../questions/linux-performance/swap-activity-response.html)
    — Sustained swap is the memory tier's slow failure, responded to rather than
    feared.
13. [Interpret iowait without blaming storage immediately](../../questions/linux-performance/iowait-interpretation.html)
    — The I/O group opens with iowait read without immediately blaming storage.
14. [Diagnose a full filesystem with free-looking space](../../questions/linux-performance/disk-space-versus-inodes.html)
    — The full filesystem with free-looking space is the I/O tier's famous trap.
15. [Diagnose file-descriptor exhaustion](../../questions/linux-performance/file-descriptor-exhaustion.html)
    — Descriptor exhaustion completes the exhaustion shapes with a slow leak
    against a limit.
16. [Triage TCP retransmissions on a Linux service](../../questions/linux-performance/network-retransmission-triage.html)
    — TCP retransmissions bring the resource tour to the network interface.
17. [Diagnose network softirq saturation](../../questions/linux-performance/softirq-saturation.html)
    — Softirq saturation is the network stack's own saturation signature.
18. [Recognize NUMA locality as a performance constraint](../../questions/linux-performance/numa-locality.html)
    — NUMA locality becomes a constraint worth naming once single-host diagnosis
    is reliable.
19. [Evaluate kernel samepage merging safely](../../questions/linux-performance/kernel-samepage-merging.html)
    — KSM prices memory deduplication honestly against its own CPU cost.
20. [Design a noisy-neighbor performance policy](../../questions/linux-performance/noisy-neighbor-policy.html)
    — The noisy-neighbour policy makes co-tenancy a governed trade rather than a
    gamble.
21. [Govern performance-observability overhead](../../questions/linux-performance/observability-overhead-governance.html)
    — Observability overhead is governed rather than assumed to be free.
22. [Establish a Linux performance baseline program](../../questions/linux-performance/performance-baseline-program.html)
    — The programme tier opens by making baselines an organizational habit.
23. [Build a capacity model for a Linux service](../../questions/linux-performance/performance-capacity-model.html)
    — The capacity model turns those baselines into provisioning plans.
24. [Lead a Linux performance incident](../../questions/linux-performance/performance-incident-command.html)
    — Leading the performance incident closes the Theme with the tools as a
    method.
