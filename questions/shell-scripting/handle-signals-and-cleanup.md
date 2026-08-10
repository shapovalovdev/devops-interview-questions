---
title: Handle termination signals and cleanup
theme: shell-scripting
difficulty: middle
type: scenario
tags: [bash, shell, scripting, signals, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle termination signals and cleanup

How should a long-running automation script respond to cancellation?

## Answer guide

- Use `trap` to catch signals such as TERM and INT, stop accepting new work, clean up owned temporary state, and exit with a status that tells the scheduler the run was interrupted.
- Track child process IDs and wait for or terminate them deliberately. A trap in the parent does not automatically make every external command transactional.
- Keep trap handlers small and safe to run during partial initialization; avoid masking the original failure with a cleanup failure.
- SIGKILL cannot be trapped, so durable state requires atomic writes, locks with recovery, and an idempotent next run. Assume a host can disappear mid-operation.

## References

- [GNU Bash manual: Bourne shell builtins (`trap`)](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)
- Further reading (blog): [Red Hat: Handle signals in Bash scripts](https://www.redhat.com/en/blog/bash-trap-command)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
