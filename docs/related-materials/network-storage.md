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

Decide the access shape before the protocol: the NAS, SAN, or object question
routes you to everything that follows. Take NFS as the canonical file path —
mount an export safely, choose a protocol version, failure behaviour, cache
coherency, ownership and identity mapping, and lock recovery last, because lock
recovery is incomprehensible until coherency has already worried you. SMB
mirrors it with the share itself, then signing and encryption. The block
chapter runs iSCSI initiators and targets into multipathing validation and on
to NVMe over Fabrics, with the multi-writer corruption question standing guard
over the whole block story. Object storage brings consistency-and-retry design
and lifecycle and retention rules; Ceph follows with replication versus erasure
coding and the recovery capacity that keeps a degraded cluster alive. The last
tier is platform resilience — snapshots distinguished from backups,
cross-region design, ransomware-resilient backups, the disaster-recovery
exercise — then latency triage, service tiers, tenancy boundaries, and cost and
capacity governance.
