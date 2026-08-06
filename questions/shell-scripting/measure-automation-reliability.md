---
title: Measure shell-automation reliability
theme: shell-scripting
difficulty: staff
type: scenario
tags: [bash, shell, scripting, observability, reliability, governance]
sources:
  - url: https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Measure shell-automation reliability

How would you know whether an organization’s operational scripts are becoming safer?

## Answer guide

- Measure outcomes: completion rate by operation and version, retries, duration, rollback rate, unsafe manual intervention, and incidents attributable to automation. Segment by blast radius and criticality.
- Establish SLOs for important automation, instrument start/end and target-level results, and preserve a correlation ID from request to effect.
- Use metrics to prioritize platform improvements such as safer libraries or API migration, not to punish teams for reporting failures.
- Avoid a vanity metric such as script count or raw success rate; a job that silently ignores errors can look healthy while causing drift.

## References

- [GNU Bash manual: Exit status](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html)
- Further reading (blog): [Red Hat: Improve automation with observability](https://www.redhat.com/en/blog/automation-observability)
