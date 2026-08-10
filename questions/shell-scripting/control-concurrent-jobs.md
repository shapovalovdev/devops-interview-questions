---
title: Control concurrent jobs in a Bash worker
theme: shell-scripting
difficulty: senior
type: scenario
tags: [bash, shell, scripting, automation, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control concurrent jobs in a Bash worker

How would you add bounded parallelism to a script that operates on many targets?

## Answer guide

- Start no more than a defined number of background jobs, retain each PID and target identity, and use `wait` to collect all outcomes before declaring success.
- Bound concurrency to the dependency's capacity and apply timeouts, retry policy, and rate limiting per operation. More parallel processes can amplify an outage.
- Background jobs do not automatically propagate their failures to the parent. Aggregate statuses and emit a target-level summary suitable for a rerun.
- Avoid sharing writable temporary files or mutable global state between jobs. Test partial failure, cancellation, and a hung child before using concurrency in a release path.

## References

- [GNU Bash manual: Job-control builtins](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html)
- Further reading (blog): [Red Hat: Run tasks in parallel with Bash](https://www.redhat.com/en/blog/parallel-shell-scripts)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
