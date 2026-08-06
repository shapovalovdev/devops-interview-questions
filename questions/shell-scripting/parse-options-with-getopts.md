---
title: Parse command-line options with getopts
theme: shell-scripting
difficulty: middle
type: scenario
tags: [bash, shell, scripting, automation]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Parse command-line options with getopts

How do you give a deployment script a safe, predictable short-option interface?

## Answer guide

- Define a small option grammar with `getopts`, validate each value, and shift by `OPTIND - 1` before processing remaining positional arguments. Print usage and return non-zero for malformed input.
- Keep option parsing separate from actions so `--dry-run`, target selection, and confirmation checks are visible before any mutation occurs.
- `getopts` handles short options; do not assume GNU `getopt` behavior is portable. If long options are required, document the selected parser and test the target runtime.
- Treat values beginning with `-` and missing arguments explicitly. Ambiguous parsing can make a target name be interpreted as an option or bypass safeguards.

## References

- [GNU Bash manual: Bourne shell builtins (`getopts`)](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)
- Further reading (blog): [Red Hat: Parse Bash command-line arguments](https://www.redhat.com/en/blog/arguments-bash-scripts)
