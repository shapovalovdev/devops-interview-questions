---
title: Read arbitrary input lines safely in Bash
theme: shell-scripting
difficulty: junior
type: scenario
tags: [bash, shell, scripting, filesystem, automation]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Read arbitrary input lines safely in Bash

How do you iterate over a newline-delimited file without corrupting backslashes or losing its final unterminated line?

## Answer guide

- Use `while IFS= read -r line || [[ -n $line ]]; do ...; done < file`. An empty `IFS` prevents trimming and `-r` prevents `read` from treating backslashes as escapes.
- Keep the loop input redirection on the loop, not a pipeline, when the body must update variables in the current shell. Validate that the input format is actually newline-delimited.
- Newline is valid in Unix filenames, so line-oriented parsing is not safe for arbitrary filenames. Prefer a NUL-delimited producer and `read -d ''` where the producer supports it.
- Do not use `for line in $(cat file)`: command substitution splits on whitespace and expands globs. Such corruption can direct a destructive operation at the wrong path.

## References

- [GNU Bash manual: Bash builtins (`read`)](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html)
- Further reading (blog): [Red Hat: How to read files in Bash](https://www.redhat.com/en/blog/reading-file-bash)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
