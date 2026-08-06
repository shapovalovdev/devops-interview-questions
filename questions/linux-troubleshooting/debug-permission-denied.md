---
title: Debug a Linux `Permission denied` failure for a service
theme: linux-troubleshooting
difficulty: junior
type: troubleshooting
tags: [linux, permissions, selinux, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man2/open.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a Linux `Permission denied` failure for a service

## Answer guide

- Identify the exact process, path, operation, and effective credentials from the service logs or tracing. Check every parent directory's execute permission, ownership, ACLs, mount options, and the target file mode.
- Account for mandatory access control such as SELinux or AppArmor and for service sandboxing. A successful interactive shell test may differ from a systemd unit's user, capability set, namespace, or security policy.
- Apply the smallest durable ownership, ACL, label, or policy change and retest as the service account. Do not solve the incident with world-writable permissions or by permanently disabling a mandatory access-control system.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man2/open.2.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
