# Linux related materials

These resources complement the Linux Theme's Question-level references. They
are a curated starting point for process inspection, filesystems, systemd, and
host operations; review their applicability to the distribution and kernel in
use.

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance analysis](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)

## Legal free books

No general Linux book is linked here. This avoids pointing learners to
unauthorized copies of commercial titles; the upstream manuals and
project-maintainer resources above are free to read and are the appropriate
primary study material.

## Suggested study order

Boot, process states, and load average open the Theme because half its incidents
are misread without that trio, and the close is fleet scope.

1. [Explain the Linux boot sequence](../../questions/linux/linux-boot-sequence.html)
    — The boot sequence opens the Theme because half its incidents are misread
    without it.
2. [Explain Linux process states during an incident](../../questions/linux/process-states.html)
    — Process states are the smallest unit of host evidence the Theme ever
    reads.
3. [Interpret a high Linux load average](../../questions/linux/load-average-interpretation.html)
    — Load average counts uninterruptible sleep, so it is only honest after
    process states.
4. [Diagnose a systemd service that repeatedly fails](../../questions/linux/systemd-service-failure.html)
    — The repeatedly failing unit is the first host object an operator actually
    touches.
5. [Design a graceful Linux service shutdown](../../questions/linux/signals-and-graceful-shutdown.html)
    — The graceful-shutdown contract resolves the restart-amplification trap the
    failing unit exposed.
6. [Use strace safely to investigate a hung Linux process](../../questions/linux/strace-production-safely.html)
    — strace covers the cases systemd hides, used safely on a production host.
7. [Debug process visibility across PID namespaces](../../questions/linux/pid-namespaces-debugging.html)
    — PID-namespace visibility completes the debugging pair for container-era
    hosts.
8. [Explain mounts and filesystem types on Linux](../../questions/linux/mounts-and-filesystem-types.html)
    — Storage opens with what is mounted where, and as what filesystem.
9. [Configure LVM storage for a growing service](../../questions/linux/configure-lvm-storage.html)
    — LVM grows the storage story beyond a single device.
10. [Explain Linux permissions and umask](../../questions/linux/permissions-and-umask.html)
    — Permissions and umask decide who may read what the mounts exposed.
11. [Respond to a filesystem mounted read-only after errors](../../questions/linux/filesystem-check-failure.html)
    — The filesystem mounted read-only after errors is the storage tier's own
    failure mode.
12. [Recover disk space held by deleted open files](../../questions/linux/deleted-open-files.html)
    — Space held by deleted open files is the storage tier's most famous
    surprise.
13. [Investigate a Linux out-of-memory kill](../../questions/linux/oom-killer-investigation.html)
    — Memory opens with the kernel's own kill decision, interpretable with
    process state in hand.
14. [Diagnose a cgroup resource limit problem](../../questions/linux/cgroups-resource-isolation.html)
    — The cgroup limit problem is memory pressure with a named owner.
15. [Diagnose too many open files in a Linux service](../../questions/linux/file-descriptor-exhaustion.html)
    — File-descriptor exhaustion comes last so its usage-versus-limit alerting
    lesson follows two different exhaustion shapes.
16. [Maintain package repositories without breaking fleet updates](../../questions/linux/maintain-package-repositories.html)
    — The change tier opens with where the fleet's software actually comes from.
17. [Plan a production Linux kernel upgrade and rollback](../../questions/linux/kernel-upgrade-rollback.html)
    — The kernel upgrade with rollback is the change tier's highest-stakes
    routine.
18. [Choose between cron and systemd timers](../../questions/linux/cron-versus-systemd-timers.html)
    — Cron versus systemd timers is the scheduling decision the change tier
    makes daily.
19. [Integrate LDAP users through SSSD safely](../../questions/linux/integrate-ldap-users-with-sssd.html)
    — SSSD brings external identity onto the host the Theme has been changing.
20. [Manage a libvirt virtual machine change safely](../../questions/linux/manage-libvirt-virtual-machines.html)
    — A libvirt change is the host learning it runs someone else's workload.
21. [Investigate a failure that occurred only during the previous boot](../../questions/linux/previous-boot-log-analysis.html)
    — The failure that happened only during the previous boot is change
    diagnosis with cold evidence.
22. [Define SLOs for a Linux host platform](../../questions/linux/linux-platform-slo.html)
    — Fleet scope opens by promising what the host platform will deliver.
23. [Govern a Linux security baseline without blocking delivery](../../questions/linux/linux-security-baseline.html)
    — The security baseline governs every host the SLO just made a promise
    about.
24. [Design a Linux incident evidence and forensics policy](../../questions/linux/linux-incident-forensics-policy.html)
    — The forensics policy decides what evidence the fleet preserves when
    promises break.
25. [Establish Linux fleet capacity governance](../../questions/linux/fleet-capacity-governance.html)
    — Capacity governance prices the fleet the baseline standardized.
26. [Define a Linux fleet lifecycle standard](../../questions/linux/fleet-os-lifecycle.html)
    — The fleet lifecycle standard closes the Theme at the same altitude the
    platform path reaches.
