# Storage: related materials

Use the kernel and Linux manual pages referenced by each Question as authority.

## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)

## Suggested study order

The shape question comes first because block, file, or object decides every
later answer, and the close is platform scope.

1. [Choose between block, file, and object storage](../../questions/storage/block-file-object-storage.html)
    — Block, file, or object comes first because it decides every later answer.
2. [Mount persistent storage safely on Linux](../../questions/storage/mount-persistent-storage.html)
    — Mounting persistent storage safely is the hands-on first step.
3. [Operate NFS shared storage safely](../../questions/storage/operate-nfs-shared-storage.html)
    — NFS as the first real workload teaches shared storage's surprises early.
4. [Choose block-volume performance for a workload](../../questions/storage/choose-volume-performance.html)
    — The performance and protection pairing opens with choosing block-volume
    performance for the workload.
5. [Create an application-consistent volume snapshot](../../questions/storage/design-consistent-snapshot.html)
    — Application-consistent snapshots capture state that is actually
    restorable.
6. [Plan for performance when restoring a volume from a snapshot](../../questions/storage/handle-snapshot-restore-latency.html)
    — Restore-from-snapshot planning prices the latency the snapshot hid.
7. [Distinguish backups from storage snapshots](../../questions/storage/distinguish-backups-and-snapshots.html)
    — The distinction is stated before the exercise that proves it.
8. [Run a meaningful backup restore exercise](../../questions/storage/restore-backup-exercise.html)
    — The restore exercise is what a backup claim is finally worth.
9. [Diagnose a full filesystem when free space remains](../../questions/storage/inode-exhaustion.html)
    — The incident set opens with the full filesystem that still shows free
    space.
10. [Recover storage held by deleted open files](../../questions/storage/diagnose-deleted-open-files.html)
    — Space held by deleted open files is the storage incident everyone meets
    once.
11. [Respond to suspected filesystem corruption](../../questions/storage/diagnose-filesystem-corruption.html)
    — Suspected corruption is responded to, not blindly repaired.
12. [Explain RAID redundancy and its limits](../../questions/storage/explain-raid-redundancy.html)
    — RAID limits sit between the incidents and the rebuild that actually kills
    arrays.
13. [Plan a degraded RAID rebuild without compounding risk](../../questions/storage/plan-raid-rebuild-risk.html)
    — The degraded rebuild is planned because a rebuild is when an array dies.
14. [Investigate a storage latency incident](../../questions/storage/investigate-storage-latency.html)
    — The storage latency incident closes the incident set.
15. [Design database point-in-time recovery](../../questions/storage/database-point-in-time-recovery.html)
    — The resilience tier opens with database point-in-time recovery as its
    strictest form.
16. [Design cross-region storage recovery](../../questions/storage/design-cross-region-recovery.html)
    — Cross-region recovery spends the resilience tier at distance.
17. [Design immutable recovery copies against ransomware](../../questions/storage/design-immutable-recovery.html)
    — Immutable copies assume the ransomware reached everything else first.
18. [Design an object-storage lifecycle policy](../../questions/storage/manage-object-lifecycle.html)
    — The object lifecycle policy automates what retention demands of objects.
19. [Govern data retention and deletion across storage systems](../../questions/storage/govern-data-retention.html)
    — Retention governance closes the resilience tier with deletion as a duty.
20. [Set storage SLOs for a platform](../../questions/storage/set-storage-slos.html)
    — Platform scope opens with SLOs the storage platform will defend.
21. [Use storage quotas without surprising tenants](../../questions/storage/control-storage-quotas.html)
    — Quotas allocate the platform's storage without surprising the tenants who
    hit them.
22. [Migrate stateful storage with controlled downtime](../../questions/storage/migrate-stateful-storage.html)
    — Stateful migration moves live data with controlled downtime.
23. [Manage storage cost and capacity as a portfolio](../../questions/storage/manage-storage-cost-and-capacity.html)
    — Cost and capacity as a portfolio prices the whole estate together.
24. [Lead an organization-wide storage disaster-recovery strategy](../../questions/storage/lead-storage-disaster-recovery.html)
    — The organization-wide disaster-recovery strategy is storage's staff-level
    close.
25. [Build a self-service storage platform with guardrails](../../questions/storage/build-self-service-storage-platform.html)
    — The self-service platform wraps the whole subject in guardrails.
