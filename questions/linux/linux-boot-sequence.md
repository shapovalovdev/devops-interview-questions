---
title: Explain the Linux boot sequence
theme: linux
difficulty: middle
type: theory
tags: [linux, troubleshooting]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/bootup.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the Linux boot sequence

Starting when firmware hands off control, explain the major stages that bring a Linux host to a usable state.

## Answer guide

- Firmware initializes enough hardware to select and start a bootloader. The bootloader loads a kernel and, where configured, an initramfs; its configuration and the distribution decide the exact files and hand-off details.
- The kernel initializes drivers and memory management, uses the initramfs to locate or prepare the real root filesystem when necessary, then starts the configured init program as PID 1.
- On systemd hosts, PID 1 activates units according to dependencies until the selected target is reached. A boot that reaches a login prompt can still have failed services, so inspect failed units and the journal rather than treating the target as proof of application health.
- At an initramfs shell, first identify whether the root device, storage driver, crypt/RAID assembly, or root mount option is missing. Preserve the exact kernel and initramfs error before changing bootloader configuration.

## References

- [systemd bootup sequence](https://www.freedesktop.org/software/systemd/man/latest/bootup.html)
- Further reading: [systemd special targets](https://www.freedesktop.org/software/systemd/man/latest/systemd.special.html)
