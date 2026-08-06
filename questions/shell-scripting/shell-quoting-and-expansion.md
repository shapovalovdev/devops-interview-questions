---
title: Explain shell quoting and variable expansion
theme: shell-scripting
difficulty: junior
type: theory
tags: [bash, shell, scripting, troubleshooting]
---

# Explain shell quoting and variable expansion

How do unquoted, single-quoted, and double-quoted values differ in a shell command, and why does that matter for automation?

## Answer guide

- Unquoted expansion can undergo word splitting and pathname expansion.
- Single quotes preserve literal characters; double quotes allow controlled parameter expansion.
- Quote variables by default to preserve arguments and prevent accidental glob expansion or command injection.
