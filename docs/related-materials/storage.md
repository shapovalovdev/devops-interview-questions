# Storage: related materials

Use the kernel and Linux manual pages referenced by each Question as authority.

## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)

## Suggested study order

The shape question comes first — block, file, or object — because it decides
every later answer; then mount persistent storage safely and run NFS shared
storage as the first real workload. Performance and protection pair up next:
block-volume performance, application-consistent snapshots, and
restore-from-snapshot planning on one side, the backup-versus-snapshot
distinction and a restore exercise that proves it on the other. The incident
set follows — the full filesystem with free space remaining, space held by
deleted open files, suspected corruption, the storage latency incident — with
RAID limits and the degraded-rebuild plan between them, since a rebuild is when
an array actually dies. The resilience tier comes after: database point-in-time
recovery, cross-region recovery, immutable copies against ransomware, retention
and lifecycle policy. Finish at platform scope — SLOs, quotas that do not
surprise tenants, stateful migration with controlled downtime, cost and
capacity as a portfolio, the organization-wide disaster-recovery strategy, and
the self-service platform that wraps the whole subject in guardrails.
