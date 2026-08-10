---
title: Create and clean temporary files safely
theme: shell-scripting
difficulty: middle
type: scenario
tags: [bash, shell, scripting, security, filesystem]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create and clean temporary files safely

How would a script use temporary state without predictable-name races or leaked secrets?

## Answer guide

- Create files or directories with a secure tool such as `mktemp`, record the resulting path in a quoted variable, and set restrictive permissions before writing sensitive content.
- Register cleanup with `trap` for normal exit and relevant signals; make cleanup idempotent and limit deletion to the known temporary path.
- Never form a predictable path in a shared directory or use unquoted recursive deletion. Another principal can race, replace, or observe such a path.
- Preserve enough failure evidence to debug while avoiding secret disclosure in logs. Test interruption and disk-full paths, not only success cleanup.

## References

- [GNU Bash manual: Bourne shell builtins (`trap`)](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)
- Further reading (blog): [Red Hat: Use temporary files safely in Bash](https://www.redhat.com/en/blog/temporary-files-bash)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
