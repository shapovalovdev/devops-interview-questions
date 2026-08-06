---
title: Prevent command injection in an automation script
theme: shell-scripting
difficulty: middle
type: scenario
tags: [bash, shell, scripting, security, least-privilege]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent command injection in an automation script

An operator supplies a host name and an optional path. How do you prevent it from becoming shell syntax?

## Answer guide

- Treat input as data: validate it against the required grammar, quote it at every command boundary, and pass command arguments as separate words or array elements.
- Avoid `eval`, `sh -c`, and interpolated command strings. Those introduce another parsing pass where input can become operators, substitutions, or redirections.
- Apply least privilege and a narrow allowlist even after quoting. Quoting cannot make an authorized but dangerous target safe.
- Test malicious-looking values, whitespace, glob characters, and option-like strings. Log a safely rendered command context without exposing credentials.

## References

- [GNU Bash manual: Shell expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html)
- Further reading (blog): [Red Hat: Avoid common Bash scripting mistakes](https://www.redhat.com/en/blog/avoid-bash-scripting-mistakes)
