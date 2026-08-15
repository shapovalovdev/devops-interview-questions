# Linux troubleshooting: related materials

Use these curated materials after completing the Theme Questions. They are learning context; the primary evidence for each answer remains in its front matter and References.

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

## Suggested study order

Start with the failures that stop a host being useful at all — the boot that
fails after a configuration change, the mount that blocks startup, the
interrupted package transaction — because every later diagnosis presumes a
booted machine. Then the service tier: Permission denied, the service failing
after a restart, the unit that starts before its dependency is usable, and the
app that works in a shell but not as a service. Resource exhaustion comes third
— the full filesystem, too many open files, OOM kills on a cgroup-aware host,
memory pressure without immediately adding RAM, zombies, and the D-state hung
task — with high load but low CPU as the bridge out of pure CPU thinking and
into storage I/O latency. The network set — intermittent DNS,
connection-tracking exhaustion, packet loss to a critical dependency, the
NFS-stalled application, clock skew breaking authentication — assumes you can
already read process state and logs. Keep the kernel panic last among
diagnostics, since it is pure evidence-preservation discipline. The final
questions — the runbook programme, fleet observability, capacity and saturation
risk, the cross-team major incident — govern a fleet rather than a host, and
only read after the diagnostics they organize.
