---
title: Prevent overlapping scheduled script runs
theme: shell-scripting
difficulty: senior
type: scenario
tags: [bash, shell, scripting, automation, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Redirections.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent overlapping scheduled script runs

A scheduled reconciliation sometimes overlaps with itself. What locking design would you use?

## Answer guide

- Use an operating-system lock with a lifetime tied to an open file descriptor, such as `flock`, and make contention an explicit, observable outcome. Hold it only around the mutually exclusive critical section.
- Put lock location and ownership under controlled permissions; include a run ID and start time in diagnostics, not a hand-maintained PID file as the source of truth.
- A stale PID can be reused and a process can die without cleanup. Prefer kernel-managed release on descriptor close and design recovery for host failure.
- Decide whether a second run should wait, skip, or fail based on correctness and freshness objectives. Test cancellation and an unexpectedly terminated owner.

## References

- [GNU Bash manual: Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- Further reading (blog): [Red Hat: Prevent concurrent Bash script runs](https://www.redhat.com/en/blog/prevent-concurrent-bash-scripts)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
