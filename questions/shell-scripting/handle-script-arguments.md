---
title: Handle shell-script arguments without losing boundaries
theme: shell-scripting
difficulty: junior
type: theory
tags: [bash, shell, scripting, automation]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle shell-script arguments without losing boundaries

How should a Bash script accept and forward user-supplied arguments?

## Answer guide

- Positional parameters hold the caller's arguments. Use `"$@"` to forward each original argument as a separate word; use `$#` to validate count and `shift` only after consuming a documented parameter.
- Parse options deliberately, using `getopts` for short options or a tested parser for a larger interface. Reject unknown, missing, and ambiguous inputs before changing state.
- `"$*"` joins arguments into one word when quoted, while unquoted `$@` and `$*` permit splitting. Do not reconstruct a command with a string and `eval`.
- Cover empty arguments, values beginning with `-`, spaces, and `--`. Failing to preserve boundaries can turn an input value into an extra option or a different command.

## References

- [GNU Bash manual: Shell parameters](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html)
- Further reading (blog): [Red Hat: Arguments in Bash scripts](https://www.redhat.com/en/blog/arguments-bash-scripts)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
