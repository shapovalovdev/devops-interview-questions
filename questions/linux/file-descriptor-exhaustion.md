---
title: Diagnose too many open files in a Linux service
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, debugging, troubleshooting]
---

# Diagnose too many open files in a Linux service

An application reports “too many open files.” How do you find the leaking resource and choose a safe remedy?

## Answer guide

- Inspect the process file-descriptor count and the configured per-process limit.
- Categorize descriptors: files, sockets, pipes, or deleted files held open.
- Fix the application leak or connection lifecycle before raising limits; validate under sustained load.
