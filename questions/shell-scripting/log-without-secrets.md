---
title: Make shell-script logs useful without leaking secrets
theme: shell-scripting
difficulty: middle
type: scenario
tags: [bash, shell, scripting, logging, security, troubleshooting]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Make shell-script logs useful without leaking secrets

How do you add diagnostic logging to a deployment script while protecting credentials?

## Answer guide

- Emit timestamped, structured context to stderr: action, safe identifiers, and outcome. Keep primary results on stdout only when another tool consumes them.
- Do not enable `set -x` around tokens, signed URLs, or secret-bearing commands; Bash traces expanded arguments. Disable tracing around secret acquisition and redact known sensitive fields.
- Give operators a debug mode that is explicit, short-lived, and safe by default. Record a correlation ID rather than copying credentials into an incident channel.
- Review failure logs and CI artifacts as attackers can. A single leaked token can turn otherwise correct diagnostics into an account compromise.

## References

- [GNU Bash manual: The `set` builtin (`xtrace`)](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)
- Further reading (blog): [Red Hat: Debug Bash scripts](https://www.redhat.com/en/blog/debug-bash-scripts)
