# Linux Foundation Certified System Administrator (LFCS) coverage map

This study map aligns original, public practice Questions with the Linux
Foundation's public [Linux Foundation Certified System Administrator (LFCS)
domains and competencies](https://training.linuxfoundation.org/certification/LFCS/).
The program page was reviewed on 2026-08-06. It is a learning index, not an
exam reconstruction, leaked material, a prediction of scored tasks, or a
guarantee of an exam result. The official program describes a
distribution-agnostic, performance-based examination; each Question below is
therefore written as an original operational prompt and calls out
distribution-specific commands where that matters.

Questions remain in their canonical Theme folders. The `lfcs` certification tag
is a cross-cutting filter, not a separate duplicated Question collection.

## Official domain mapping

| Official public domain | Weight | Representative canonical original practice Questions | Mapping status |
| --- | ---: | --- | --- |
| Operations and Deployment | 25% | [Tune kernel updates and rollbacks](../../questions/linux/kernel-upgrade-rollback.md); [diagnose systemd service failure](../../questions/linux/systemd-service-failure.md); [choose cron or systemd timers](../../questions/linux/cron-versus-systemd-timers.md); [recover a failed filesystem check](../../questions/linux/filesystem-check-failure.md); [manage a libvirt VM change](../../questions/linux/manage-libvirt-virtual-machines.md); [maintain package repositories](../../questions/linux/maintain-package-repositories.md); [debug an SELinux permission denial](../../questions/linux-troubleshooting/debug-permission-denied.md); [operate container runtime and image boundaries](../../questions/containers/container-image-and-runtime.md) | Covered, including the explicit libvirt, package/repository, and SELinux objectives. |
| Networking | 25% | [Configure a DNS resolver](../../questions/linux-networking/dns-resolver-configuration.md); [inspect host interfaces and addresses](../../questions/linux-networking/interface-state-and-addresses.md); [debug routing with route-get](../../questions/linux-networking/route-get-debugging.md); [validate bonding failover](../../questions/linux-networking/bond-failover-validation.md); [triage firewall path](../../questions/linux-networking/firewall-path-triage.md); [investigate packet loss](../../questions/linux-troubleshooting/triage-network-packet-loss.md); [deploy a reverse-proxy certificate](../../questions/web-servers/tls-certificate-deployment.md) | Covered through canonical host-network and web-server Questions. |
| Storage | 20% | [Configure LVM storage](../../questions/linux/configure-lvm-storage.md); [mount persistent storage](../../questions/storage/mount-persistent-storage.md); [troubleshoot filesystem corruption](../../questions/storage/diagnose-filesystem-corruption.md); [operate NFS shared storage](../../questions/storage/operate-nfs-shared-storage.md); [configure filesystem automounts](../../questions/linux/configure-filesystem-automounts.md); [respond to swap activity](../../questions/linux-performance/swap-activity-response.md); [investigate storage latency](../../questions/storage/investigate-storage-latency.md) | Covered, including the explicit LVM and automounter objectives. |
| Essential Commands | 20% | [Inspect process states](../../questions/linux/process-states.md); [debug deleted-open files](../../questions/linux/deleted-open-files.md); [interpret load average](../../questions/linux/load-average-interpretation.md); [debug service environment](../../questions/linux/service-environment-debugging.md); [investigate file-descriptor exhaustion](../../questions/linux/file-descriptor-exhaustion.md); [diagnose a failed mount](../../questions/linux-troubleshooting/debug-failed-mount.md); [manage TLS certificate deployment](../../questions/web-servers/tls-certificate-deployment.md) | Covered; source Questions emphasize observing effective state before changing it. |
| Users and Groups | 10% | [Manage permissions and umask](../../questions/linux/permissions-and-umask.md); [apply least-privilege Linux capabilities](../../questions/linux/linux-capabilities-least-privilege.md); [debug permission denied](../../questions/linux-troubleshooting/debug-permission-denied.md); [integrate LDAP users through SSSD](../../questions/linux/integrate-ldap-users-with-sssd.md); [set process resource limits](../../questions/processes/resource-limits.md) | Covered, including the explicit directory-account objective. |

## Completed original gap Questions

The LFCS public objectives name five capabilities that were not previously
addressed with sufficient direct configuration depth. These original Questions
fill those gaps. They use official upstream or official distribution
documentation as factual authority and separately label a complementary blog
post for learning context.

1. [**Configure LVM storage for a growing service.**](../../questions/linux/configure-lvm-storage.md)
   Covers physical volumes, volume groups, logical volumes, filesystem growth,
   backup/snapshot limits, and post-change verification.
2. [**Configure filesystem automounts without hiding a dependency failure.**](../../questions/linux/configure-filesystem-automounts.md)
   Covers autofs maps, access-triggered mounts, expiry, optional-dependency
   semantics, and unavailable-server behavior.
3. [**Integrate LDAP users through SSSD safely.**](../../questions/linux/integrate-ldap-users-with-sssd.md)
   Covers NSS/PAM integration, TLS and bind controls, cache boundaries,
   revocation expectations, and local break-glass access.
4. [**Manage a libvirt virtual machine change safely.**](../../questions/linux/manage-libvirt-virtual-machines.md)
   Covers persistent versus live domain state, explicit change scope, capacity,
   and rollback.
5. [**Maintain package repositories without breaking fleet updates.**](../../questions/linux/maintain-package-repositories.md)
   Covers repository failure diagnosis, metadata/signature verification,
   distribution qualifiers, staging, and supply-chain incident response.

## Central publication handoff

The following shared-file changes intentionally remain with the coordinator so
that catalog and validator state changes happen atomically:

1. Add `lfcs` under `## Certifications` in `TAGS.md`.
2. Add `{"tag": "lfcs", "map": "docs/certifications/lfcs.md", "minimum_questions": 25}` to the `certifications` array in `config/content-manifest.json`.
3. Set the `linux` Theme state to `in-progress` during the additive
   certification integration, because it will contain its 25-question core plus
   these five LFCS-specific gap Questions; do not discard valid coverage merely
   to retain an artificial exact-count cap.
4. Add `lfcs` to the front-matter tags of the 30 mapped Questions in the table
   above (25 pre-existing mappings plus the five gap Questions), and regenerate
   `assets/questions.js` so each Markdown path has exactly one website record.
5. Extend `tests/validate_questions.py` only through the existing manifest
   contract: the new manifest entry already makes it check that the map exists,
   that `lfcs` is in `TAGS.md`, and that at least 25 mapped Questions carry the
   tag. No LFCS-specific hard-coded validator branch is needed.

## Publication gate

Do not expose an LFCS filter until the five central changes above are integrated
together and `python3 tests/validate_questions.py`, `python3 tests/site_check.py`,
and the GitHub Actions validation workflow pass. This prevents a visible
certification label from overstating the published coverage.
