---
title: Explain shell quoting and variable expansion
theme: shell-scripting
difficulty: junior
type: theory
tags: [bash, shell, scripting, troubleshooting]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Quoting.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain shell quoting and variable expansion

How do unquoted, single-quoted, and double-quoted values differ in a shell command, and why does that matter for automation?

## Answer guide

- Unquoted expansion can be split into multiple words and undergo pathname expansion. Single quotes preserve literal text; double quotes retain argument boundaries while allowing parameter and command expansion.
- Quote parameter expansions by default: `"$value"` passes one argument even when it contains spaces or glob characters. Use arrays and `"${items[@]}"` for an argument list rather than building a command string.
- Quoting prevents accidental interpretation by the current shell; it does not make arbitrary input safe to pass to another interpreter. Do not use `eval` to repair quoting.
- Test with empty values, whitespace, glob characters, and newlines. A script that succeeds for a simple hostname can split a filename or expand an unintended wildcard in production.

## References

- [GNU Bash manual: Quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html)
- Further reading (blog): [Red Hat: Bash parameters and expansions](https://www.redhat.com/en/blog/guide-bash-parameters-expansions)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
