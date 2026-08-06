---
title: Use storage quotas without surprising tenants
theme: storage
difficulty: junior
type: scenario
tags: [storage, linux, capacity-planning, reliability]
sources:
  - url: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_file_systems/limiting-storage-space-usage-on-xfs-with-quotas_managing-file-systems
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use storage quotas without surprising tenants

How would you introduce filesystem quotas for shared build or application storage?

## Answer guide

- Identify the accounting unit—user, group, or project—and baseline current consumption before setting soft and hard limits that match the service contract.
- Enable the filesystem's supported quota mechanism, report usage and grace periods to owners, and test the failure behavior in a non-production environment.
- Pair quotas with cleanup ownership, capacity alerts, an exception process, and audit records so a noisy tenant cannot consume all shared capacity.
- A hard limit can fail an application at the worst time; a quota without alerting turns an avoidable capacity decision into an outage. Do not assume quota behavior is portable across filesystems.

## References

- [Red Hat: XFS quotas](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_file_systems/limiting-storage-space-usage-on-xfs-with-quotas_managing-file-systems)
- Further reading (blog): [Red Hat: storage administration](https://www.redhat.com/en/blog/managing-storage-linux)
