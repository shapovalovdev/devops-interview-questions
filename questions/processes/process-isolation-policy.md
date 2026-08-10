---
title: Govern process isolation and privilege policy
theme: processes
difficulty: staff
type: scenario
tags: [linux, processes, security, least-privilege, namespaces, capabilities]
sources:
  - url: https://man7.org/linux/man-pages/man7/capabilities.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern process isolation and privilege policy

How would you define a practical process-isolation policy for shared Linux infrastructure?

## Answer guide

- Start from threat and tenancy boundaries, then select controls appropriate to the workload: distinct service identities, filesystem permissions, capabilities, seccomp, namespaces, cgroups, and service-manager sandboxing. Containers complement rather than replace a host patching and identity policy.
- Establish a default-deny baseline with tested exceptions. Every exception should identify the needed capability or host access, risk owner, expiry, and compensating monitoring; broad root access or privileged containers make policy compliance meaningless.
- Validate both workload compatibility and observability. Restrictions can break DNS, certificate reload, temporary files, debugging, or crash collection; provide supported diagnostic paths so responders are not pressured to disable controls wholesale.
- Measure adoption and outcomes: privileged-process inventory, exception age, sandbox violations, security incidents, and delivery lead time. Reassess controls with kernel, runtime, and threat-model changes rather than treating a one-time hardening guide as permanent.

## References

- [capabilities(7): partition Linux privilege](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- [namespaces(7): Linux isolation namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- [systemd.exec: execution sandbox settings](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html)
- Free book: [Linux Security HOWTO](https://tldp.org/HOWTO/Security-HOWTO/)
- Further reading (blog): [Liz Rice: Containers from scratch](https://www.lizrice.com/)

## What to learn next

- Official documentation: [man7 capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- Manual or specification: [man7 namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- Maintainer or personal blog: [Liz Rice — Containers from Scratch](https://www.lizrice.com/)
- Technical blog: [Red Hat — Linux security](https://www.redhat.com/en/topics/security)
- Hands-on guide: [Linux Security HOWTO](https://tldp.org/HOWTO/Security-HOWTO/)
