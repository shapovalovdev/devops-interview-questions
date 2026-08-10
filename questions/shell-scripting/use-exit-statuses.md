---
title: Use exit statuses as an automation contract
theme: shell-scripting
difficulty: junior
type: theory
tags: [bash, shell, scripting, ci-cd, troubleshooting]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use exit statuses as an automation contract

How should a shell script report success, expected absence, and failure to its caller?

## Answer guide

- Commands report an integer exit status; conventionally zero means success and non-zero signals a condition the caller must handle. End the script with a meaningful `exit` or let a checked command's status propagate.
- Reserve documented non-zero codes for expected outcomes when callers need to distinguish them, and write errors to standard error while keeping machine-readable standard output clean.
- A non-zero status is not automatically fatal in every context: an `if` test and `grep` with no match may be normal control flow. Check the status where its meaning is known.
- CI and schedulers can only act on the status they receive. Swallowing errors with `|| true` or a final successful `echo` can falsely mark a failed deployment as successful.

## References

- [GNU Bash manual: Exit status](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html)
- Further reading (blog): [Red Hat: Bash error handling](https://www.redhat.com/en/blog/bash-error-handling)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
