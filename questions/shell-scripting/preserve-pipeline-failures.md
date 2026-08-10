---
title: Preserve the failed command in a pipeline
theme: shell-scripting
difficulty: middle
type: troubleshooting
tags: [bash, shell, scripting, debugging, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Preserve the failed command in a pipeline

A pipeline appears successful although its producer failed. How do you diagnose and fix it?

## Answer guide

- By default a pipeline returns the status of its last command. Enable `set -o pipefail` when the pipeline should fail if any component fails, then inspect `PIPESTATUS` promptly when individual statuses matter.
- Keep a consumer from masking a failed producer; for example, a formatter can successfully process empty input after a failed API request.
- Some commands intentionally receive SIGPIPE when a downstream consumer exits early. Classify that behavior before turning every non-zero pipeline status into an incident.
- Capture stderr and test the error case in CI. Retrying the final consumer cannot repair a producer whose output was never generated.

## References

- [GNU Bash manual: Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html)
- Further reading (blog): [Red Hat: Bash error handling](https://www.redhat.com/en/blog/bash-error-handling)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
