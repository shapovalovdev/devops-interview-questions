---
title: Use command substitution without hiding failures
theme: shell-scripting
difficulty: middle
type: troubleshooting
tags: [bash, shell, scripting, debugging, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use command substitution without hiding failures

Why can `value=$(command)` make an automation failure difficult to see, and how should it be handled?

## Answer guide

- Command substitution captures standard output and removes trailing newlines. Assign only data that the command is expected to produce, then check its status in an explicit error-handling path.
- Quote `"$value"` when using the captured result. Capture diagnostics separately on stderr rather than mixing human logs into a value consumed by later commands.
- Bash's `errexit` behavior has context-sensitive exceptions, including commands in substitutions and functions. Do not infer safety merely because `set -e` is enabled.
- Test empty output, non-zero status, and malformed output. Otherwise a failed lookup can silently become an empty target or a dangerous default.

## References

- [GNU Bash manual: Command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html)
- Further reading (blog): [Red Hat: Bash parameters and expansions](https://www.redhat.com/en/blog/guide-bash-parameters-expansions)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
