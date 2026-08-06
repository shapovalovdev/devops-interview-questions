---
title: Govern a Linux security baseline without blocking delivery
theme: linux
difficulty: staff
type: scenario
tags: [linux, security, least-privilege, automation]
sources:
  - url: https://man7.org/linux/man-pages/man7/capabilities.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern a Linux security baseline without blocking delivery

How would you establish a Linux hardening baseline that teams can adopt and safely deviate from?

## Answer guide

- Define a versioned baseline for supported images: patching, service identities, SSH/access paths, least privilege, filesystem and network exposure, logging, secrets handling, and recovery. Each control needs a threat rationale, owner, measurable compliance signal, and compatibility test.
- Deliver it as reusable image/configuration modules with staged rollout and a documented exception process. Exceptions should name the risk owner, compensating controls, expiry, and review date; otherwise “temporary” workarounds become an invisible permanent attack surface.
- Test the baseline against representative workloads and incident operations. A security control that breaks boot, diagnostics, or required service behavior will be bypassed under pressure.
- Measure both risk reduction and delivery cost—compliance, exception age, rollout failures, and time-to-patch—then use the evidence to simplify controls rather than proliferating manual checklists.

## References

- [capabilities(7): partitioning privileged operations](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- Further reading: [systemd.exec security and execution controls](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html)
