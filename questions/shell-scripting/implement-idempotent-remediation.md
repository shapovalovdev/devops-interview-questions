---
title: Make a remediation script idempotent
theme: shell-scripting
difficulty: senior
type: scenario
tags: [bash, shell, scripting, automation, reliability]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Make a remediation script idempotent

How do you design a script that can be retried safely after a partial failure?

## Answer guide

- Discover the current state, compare it to a declared desired state, and make only the necessary change. Verify the postcondition rather than assuming a command's success means convergence.
- Make writes atomic where possible and record stable identifiers for created resources. Pair create and delete operations with ownership checks.
- External APIs can time out after applying a request, so retrying blindly can duplicate work. Prefer provider idempotency keys or re-query before retry.
- Add a dry-run and an interrupt/retry test. Idempotence is not a slogan: prove it with repeated execution against realistic partial state.

## References

- [GNU Bash manual: Conditional constructs](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)
- Further reading (blog): [Red Hat: Write idempotent Bash scripts](https://www.redhat.com/en/blog/idempotent-bash-scripts)

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)
