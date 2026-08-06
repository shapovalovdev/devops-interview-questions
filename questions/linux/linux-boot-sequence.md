---
title: Explain the Linux boot sequence
theme: linux
difficulty: middle
type: theory
tags: [linux, troubleshooting]
---

# Explain the Linux boot sequence

Starting when firmware hands off control, explain the major stages that bring a Linux host to a usable state.

## Answer guide

- Firmware starts a bootloader, which loads the kernel and usually an initramfs.
- The kernel initializes hardware and mounts an initial root filesystem.
- An init system such as `systemd` becomes PID 1, starts units, and reaches a target state.

## Follow-ups

- What evidence would you inspect if a host stops at the initramfs prompt?
