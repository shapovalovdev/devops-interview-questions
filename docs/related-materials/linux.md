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

Open with the boot sequence, process states, and what load average actually
counts — uninterruptible sleep included — because half this Theme's incidents
are misread without that trio. Take systemd next: the unit that repeatedly
fails, then the signals and graceful-shutdown contract, then strace and
PID-namespace visibility for the cases systemd hides. Move through storage and
permissions — mounts and filesystem types, LVM, permissions and umask, the
read-only filesystem, space held by deleted open files — then memory: the OOM
investigation, the cgroup limit problem, and file-descriptor exhaustion last,
so its usage-versus-limit alerting lesson follows two different exhaustion
shapes. The change tier comes after: package repositories, the kernel upgrade
with rollback, cron versus systemd timers, LDAP through SSSD, a libvirt change,
and the failure that happened only during the previous boot. Close at fleet
scope — SLOs for a host platform, the security baseline, evidence and forensics
policy, capacity governance, the fleet lifecycle standard — the same altitude
the platform path reaches after its own host chapters.
