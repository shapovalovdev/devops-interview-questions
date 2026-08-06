---
title: Execute a shell script with an explicit interpreter
theme: shell-scripting
difficulty: junior
type: theory
tags: [bash, shell, scripting, automation]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Execute a shell script with an explicit interpreter

Why does a script's shebang matter, and when should an automation job call `bash script.sh` explicitly?

## Answer guide

- The shebang tells the kernel which interpreter to use when an executable script is invoked by path. `#!/usr/bin/env bash` finds Bash through `PATH`; `#!/bin/sh` promises only that system's POSIX shell interface.
- Invoke `bash script.sh` when the program intentionally uses Bash features and the caller must not depend on executable mode or shebang resolution. Keep the interpreter choice consistent with the syntax used.
- `/bin/sh` is not necessarily Bash and can reject arrays, `[[ ... ]]`, and process substitution. Conversely, an `env` shebang depends on a trustworthy, predictable `PATH`.
- Test the script with its production interpreter in a minimal environment. A developer's interactive Bash profile can hide a non-portable dependency.

## References

- [GNU Bash manual: Invoking Bash](https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html)
- Further reading (blog): [Red Hat: A practical introduction to Bash scripting](https://www.redhat.com/en/blog/bash-scripting)
