---
title: Use Bash arrays for command arguments
theme: shell-scripting
difficulty: middle
type: theory
tags: [bash, shell, scripting, automation]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Arrays.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use Bash arrays for command arguments

Why should a Bash script use an array rather than a space-separated command string?

## Answer guide

- An array represents distinct arguments. Build it as `args=(tool --flag "$value")` and execute with `"${args[@]}"` so each element remains one argument.
- This preserves whitespace and prevents accidental globbing or option merging without a second shell parse.
- Arrays are a Bash feature, not portable POSIX `sh`; declare Bash in the shebang or choose a POSIX-safe design when that portability is required.
- Do not execute an array with unquoted `${args[*]}` or convert it to a string for `eval`. That loses the very boundary information the array preserves.

## References

- [GNU Bash manual: Arrays](https://www.gnu.org/software/bash/manual/html_node/Arrays.html)
- Further reading (blog): [Red Hat: Working with arrays in Bash](https://www.redhat.com/en/blog/bash-arrays)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
