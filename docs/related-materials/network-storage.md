# Network-storage related materials

These resources complement the Network Storage Theme's Question-level sources.
They cover the protocol, distributed-storage, and operational concerns behind
NFS, SMB, iSCSI, object storage, and resilient storage platforms. Confirm
product-specific behavior against the deployed version before using it in a
production runbook.

## What to learn next

- Official documentation: [Ceph architecture](https://docs.ceph.com/en/latest/architecture/)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog)
- Hands-on guide: [Ceph quick start](https://docs.ceph.com/en/latest/start/)

## Suggested study order

Decide the access shape before the protocol, because the NAS, SAN, or object
question routes you to everything that follows.

1. [Choose NAS, SAN, or object storage for a workload](../../questions/network-storage/nas-san-object-storage.html)
    — The NAS, SAN, or object question comes first because it routes everything
    that follows.
2. [Mount an NFS export safely](../../questions/network-storage/nfs-mount-basics.html)
    — NFS opens the file chapter by mounting an export safely.
3. [Select an NFS protocol version](../../questions/network-storage/nfs-version-selection.html)
    — The protocol version changes failure behaviour, so it is chosen before
    that behaviour is tuned.
4. [Choose NFS failure behavior](../../questions/network-storage/nfs-hard-soft-mounts.html)
    — Hard versus soft mounts decide what the client does when the server
    vanishes.
5. [Explain NFS cache coherency](../../questions/network-storage/nfs-caching-coherency.html)
    — Cache coherency explains why NFS reads can surprise the writer.
6. [Diagnose NFS ownership and identity mapping](../../questions/network-storage/nfs-identity-mapping.html)
    — Identity mapping decides whose permissions the export actually enforces.
7. [Plan NFS lock recovery](../../questions/network-storage/nfs-lock-recovery.html)
    — Lock recovery is incomprehensible until coherency has already worried you,
    so it comes last.
8. [Explain an SMB file share](../../questions/network-storage/smb-share-basics.html)
    — SMB mirrors the NFS chapter, opening with the share itself.
9. [Apply SMB signing and encryption](../../questions/network-storage/smb-signing-encryption.html)
    — Signing and encryption are SMB's security tier above the share.
10. [Explain iSCSI initiators and targets](../../questions/network-storage/iscsi-initiator-target.html)
    — The block chapter opens with the iSCSI initiator and target model.
11. [Validate iSCSI multipathing](../../questions/network-storage/iscsi-multipathing.html)
    — Multipathing validation proves the redundancy the block path claims.
12. [Design an NVMe over Fabrics deployment](../../questions/network-storage/nvmeof-fabrics-design.html)
    — NVMe over Fabrics is the block chapter's modern transport.
13. [Prevent multi-writer block-storage corruption](../../questions/network-storage/block-storage-single-writer.html)
    — The multi-writer corruption question stands guard over the whole block
    story.
14. [Design for object-storage consistency and retries](../../questions/network-storage/object-storage-consistency.html)
    — Object storage opens with consistency and retry design.
15. [Design object lifecycle and retention rules](../../questions/network-storage/object-lifecycle-retention.html)
    — Lifecycle and retention rules govern what object storage keeps and for how
    long.
16. [Choose Ceph replication or erasure coding](../../questions/network-storage/ceph-replication-vs-erasure-coding.html)
    — Ceph opens with its core durability trade, replication versus erasure
    coding.
17. [Protect Ceph recovery capacity](../../questions/network-storage/ceph-recovery-capacity.html)
    — Recovery capacity is what keeps a degraded Ceph cluster alive.
18. [Distinguish snapshots from backups](../../questions/network-storage/snapshots-versus-backups.html)
    — Platform resilience opens by distinguishing snapshots from backups.
19. [Design cross-region storage resilience](../../questions/network-storage/cross-region-storage-resilience.html)
    — Cross-region design spends the snapshot-versus-backup distinction at
    distance.
20. [Build ransomware-resilient storage backups](../../questions/network-storage/ransomware-resilient-backups.html)
    — Ransomware-resilient backups assume the adversary reaches the primary
    copy.
21. [Run a storage disaster-recovery exercise](../../questions/network-storage/storage-disaster-recovery-exercise.html)
    — The disaster-recovery exercise proves the resilience tier rather than
    describing it.
22. [Investigate network-storage latency](../../questions/network-storage/storage-performance-investigation.html)
    — Latency triage is the operations tier's daily question.
23. [Define storage platform service tiers](../../questions/network-storage/storage-platform-service-tiers.html)
    — Service tiers promise latency and capacity per class of workload.
24. [Establish storage tenancy boundaries](../../questions/network-storage/storage-security-tenancy.html)
    — Tenancy boundaries keep tenants apart on shared storage.
25. [Govern storage cost and capacity across teams](../../questions/network-storage/storage-cost-and-capacity-governance.html)
    — Cost and capacity governance closes the Theme at platform scale.
