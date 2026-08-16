# Processes: related materials

Use the Question-level sources for factual verification. This page is a curated learning path, not a substitute for validating production behavior against the running kernel, service manager, and runtime version.

## What to learn next

- Official documentation: [Linux man-pages: proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Manual or specification: [Linux man-pages: signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)
- Maintainer or personal blog: [Brendan Gregg’s Linux performance writing](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Linux kernel proc filesystem documentation](https://docs.kernel.org/filesystems/proc.html)
- Hands-on guide: [The Linux Documentation Project](https://tldp.org/)

## Suggested study order

The vocabulary of procfs, PIDs, states, and signals before lifecycles, and real
service lifecycles before fleet governance.

1. [Read a process status safely](../../questions/processes/read-process-status.html)
    — /proc and process status are the primary sources the Theme reads first.
2. [Explain PIDs and parent processes](../../questions/processes/pid-and-parent-process.html)
    — PIDs and parentage explain the family tree every status line belongs to.
3. [Interpret process state and load average](../../questions/processes/process-state-and-load.html)
    — Process states and load average connect kernel state to the number
    everyone quotes.
4. [Choose a signal for a running process](../../questions/processes/signal-basics.html)
    — Choosing a signal is the first act performed on a process you understand.
5. [Explain the fork exec wait lifecycle](../../questions/processes/fork-exec-wait-lifecycle.html)
    — fork, exec, and wait explain how processes come to exist and to exit.
6. [Control file descriptor inheritance across exec](../../questions/processes/file-descriptor-inheritance.html)
    — Descriptor inheritance decides what an exec'd child actually holds open.
7. [Model a service lifecycle with systemd](../../questions/processes/systemd-service-lifecycle.html)
    — Unit, cgroup, and kill semantics turn kernel primitives into real service
    lifecycles.
8. [Diagnose a per-process resource limit](../../questions/processes/resource-limits.html)
    — Per-process limits are the controls the lifecycle tier finally makes
    sensible.
9. [Define process observability without exposing secrets](../../questions/processes/process-observability-standard.html)
    — The observability standard decides what the fleet knows about its
    processes.
10. [Triage a hung process without destroying evidence](../../questions/processes/hung-process-triage.html)
    — Hung-process triage is evidence preservation under pressure, the use case
    the tier above serves.
11. [Design guardrails for automated process remediation](../../questions/processes/process-remediation-guardrails.html)
    — Organization-wide guardrails close the Theme by governing automated
    process remediation.
