# Linux troubleshooting: related materials

Use these curated materials after completing the Theme Questions. They are learning context; the primary evidence for each answer remains in its front matter and References.

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

## Suggested study order

Booting failures first, because every later diagnosis presumes a booted machine;
diagnostics before the fleet programmes that organize them.

1. [Recover safely from a Linux boot failure after a configuration change](../../questions/linux-troubleshooting/repair-boot-failure.html)
    — The boot that fails after a change comes first because everything later
    presumes a booted machine.
2. [Debug a failed network or local mount at boot](../../questions/linux-troubleshooting/debug-failed-mount.html)
    — The mount that blocks startup is the boot's most common hostage.
3. [Recover from an interrupted Linux package transaction safely](../../questions/linux-troubleshooting/recover-package-manager.html)
    — The interrupted package transaction leaves the host between states,
    recovered before services arrive.
4. [Debug a Linux `Permission denied` failure for a service](../../questions/linux-troubleshooting/debug-permission-denied.html)
    — The service tier opens with the filesystem saying no to a service.
5. [Inspect a Linux service that is failing after a restart](../../questions/linux-troubleshooting/inspect-service-logs.html)
    — The service failing after a restart is read from its logs before anything
    is touched.
6. [Diagnose a systemd service that starts before its dependency is usable](../../questions/linux-troubleshooting/diagnose-systemd-dependency.html)
    — The unit that starts before its dependency is an ordering problem, and it
    reads only with unit literacy.
7. [Diagnose a Linux filesystem reported as full](../../questions/linux-troubleshooting/diagnose-full-filesystem.html)
    — Resource exhaustion opens with the full filesystem and its several
    different causes.
8. [Investigate a service that reports too many open files](../../questions/linux-troubleshooting/investigate-file-descriptors.html)
    — Too many open files is exhaustion with a per-process culprit to find.
9. [Diagnose an OOM-killed service in a cgroup-aware host](../../questions/linux-troubleshooting/diagnose-oom-kill.html)
    — The OOM kill on a cgroup-aware host needs the cgroup boundaries named.
10. [Investigate Linux memory pressure without immediately adding RAM](../../questions/linux-troubleshooting/investigate-memory-pressure.html)
    — Memory pressure investigated without immediately adding RAM is the
    disciplined sequel to the kill.
11. [Investigate accumulating zombie processes on Linux](../../questions/linux-troubleshooting/investigate-zombie-processes.html)
    — Zombies accumulate when a parent forgets, harmless right up until they are
    not.
12. [Investigate a Linux hung-task warning or D-state process](../../questions/linux-troubleshooting/investigate-hung-task.html)
    — The D-state hung task is where process-state knowledge pays for itself.
13. [Analyze a host with a high load average but low CPU utilization](../../questions/linux-troubleshooting/analyze-load-average.html)
    — High load with low CPU bridges pure CPU thinking into storage I/O latency.
14. [Perform first-pass storage I/O latency triage on Linux](../../questions/linux-troubleshooting/perform-storage-io-triage.html)
    — First-pass storage I/O triage follows the bridge that pointed here.
15. [Trace an intermittent DNS resolution failure on Linux](../../questions/linux-troubleshooting/trace-dns-failure.html)
    — The network set opens with intermittent DNS, the flakiest dependency of
    all.
16. [Trace suspected connection-tracking exhaustion on a Linux node](../../questions/linux-troubleshooting/trace-conntrack-exhaustion.html)
    — Connection-tracking exhaustion fails new connections while the old ones
    keep living.
17. [Triage packet loss from a Linux host to a critical dependency](../../questions/linux-troubleshooting/triage-network-packet-loss.html)
    — Packet loss to a critical dependency is measured rather than assumed.
18. [Diagnose an application stalled on an NFS mount](../../questions/linux-troubleshooting/diagnose-nfs-stall.html)
    — The NFS-stalled application shows local symptoms with remote causes.
19. [Resolve clock skew that is breaking Linux service authentication](../../questions/linux-troubleshooting/resolve-clock-skew.html)
    — Clock skew breaking authentication is time, the quietest dependency on the
    host.
20. [Lead evidence-preserving triage after a Linux kernel panic](../../questions/linux-troubleshooting/debug-kernel-panic.html)
    — The kernel panic is kept last among diagnostics because it is pure
    evidence-preservation discipline.
21. [Design an evidence-driven Linux troubleshooting runbook program](../../questions/linux-troubleshooting/design-linux-troubleshooting-runbooks.html)
    — The fleet tier opens by making the diagnostics above a runbook programme.
22. [Architect Linux fleet observability for rapid fault isolation](../../questions/linux-troubleshooting/architect-linux-observability.html)
    — Fleet observability finds the faults before the runbooks ever fire.
23. [Lead capacity and saturation risk management for a Linux platform](../../questions/linux-troubleshooting/lead-linux-capacity-risk.html)
    — Capacity and saturation risk management governs the fleet's future
    failures.
24. [Coordinate a cross-team major incident rooted in Linux host failures](../../questions/linux-troubleshooting/coordinate-linux-major-incident.html)
    — The cross-team major incident closes the Theme at the scale the runbooks
    organize.
