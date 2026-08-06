---
title: Interpret process state and load average
theme: processes
difficulty: middle
type: troubleshooting
tags: [linux, processes, load, performance, debugging]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc_loadavg.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Interpret process state and load average

How do process states contribute to Linux load average, and how would you investigate a high value?

## Answer guide

- Linux load average represents runnable tasks and tasks in uninterruptible sleep, averaged over one, five, and fifteen minutes; it is not CPU utilization. A high number can arise from CPU demand, storage waits, or other uninterruptible waits, so comparing it directly with core count is only a starting hypothesis.
- Sample task states and run-queue pressure repeatedly with `ps`, `/proc`, scheduler metrics, and PSI. Identify whether the population is runnable (`R`), I/O-waiting (`D`), or a transient burst; then correlate with CPU saturation, latency, device errors, filesystem stalls, and deployment timing.
- Do not kill `D`-state tasks reflexively. They are often waiting in kernel I/O paths and may not respond until the underlying operation returns. Escalate based on service impact, preserve diagnostics, and repair the blocking storage, network filesystem, or driver path.
- Set alerts on user impact and resource saturation, not an isolated load threshold. Baselines vary by hardware, workload, cgroup limits, and batch scheduling; document the interpretation in the service runbook.

## References

- [proc_loadavg(5): load-average fields](https://man7.org/linux/man-pages/man5/proc_loadavg.5.html)
- [proc(5): process state information](https://man7.org/linux/man-pages/man5/proc.5.html)
- [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Free book: [Linux kernel scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/)
- Further reading (blog): [Brendan Gregg: Linux load averages](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

## What to learn next

- Official documentation: [man7 proc_loadavg(5)](https://man7.org/linux/man-pages/man5/proc_loadavg.5.html)
- Manual or specification: [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Maintainer or personal blog: [Brendan Gregg — Linux load averages](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)
- Technical blog: [Red Hat — Linux performance](https://www.redhat.com/en/topics/linux/what-is-linux)
- Hands-on guide: [Linux Journey — processes](https://linuxjourney.com/lesson/processes)
