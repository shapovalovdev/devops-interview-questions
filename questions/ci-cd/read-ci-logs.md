---
title: Triage a failed CI job from its logs
theme: ci-cd
difficulty: junior
type: troubleshooting
tags: [ci-cd, debugging, troubleshooting, automation]
sources:
  - url: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a failed CI job from its logs

How do you turn a failed CI job into a safe, actionable diagnosis?

## Answer guide

- Identify the first failing command, its exit code, runner image, commit, inputs, and preceding warnings; later failures are often consequences.
- Reproduce with the same lockfiles, tool versions, environment variables, and service dependencies where possible. Compare a passing run rather than guessing from one log line.
- Redact secrets before sharing logs and preserve logs/artifacts long enough for investigation. Do not solve a flaky or environmental failure by blindly rerunning it: classify it and add a deterministic check or owned remediation.

## References

- [GitHub Docs: Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Further reading: GitHub Docs—storing workflow data as artifacts](https://docs.github.com/en/actions/how-tos/store-and-share-data)
