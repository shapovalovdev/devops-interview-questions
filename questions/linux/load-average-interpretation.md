---
title: Interpret a high Linux load average
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, monitoring, troubleshooting]
---

# Interpret a high Linux load average

Why can a high load average be normal on one host and an incident on another?

## Answer guide

- Compare runnable and uninterruptible work against available CPU and workload baseline.
- Check CPU saturation, I/O wait, blocked tasks, and latency rather than treating load alone as a failure.
