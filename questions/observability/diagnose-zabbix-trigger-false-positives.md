---
title: Diagnose Zabbix trigger false positives
theme: observability
difficulty: senior
type: troubleshooting
tags: [observability, monitoring, zabbix, incident-response, slo]
sources:
  - url: https://www.zabbix.com/documentation/current/en/manual/config/triggers
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.zabbix.com/documentation/current/en/manual/config/triggers/dependencies
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.zabbix.com/documentation/current/en/manual/maintenance
    source_type: official-docs
    verified_on: 2026-08-17
---

# Diagnose Zabbix trigger false positives

On-call engineers complain that a host's CPU and disk triggers fire almost nightly during backup windows and patch reboots, and nobody trusts the alerts anymore. Diagnose why the triggers misfire and redesign them.

## Answer guide

- First classify the false positive from the data, not the story: pull the item history around each firing in Latest data / problem events and check whether the underlying value really breached (a real spike suppressed by policy) or the trigger logic is too eager (a single poll above threshold, `last()`-only expressions with no averaging or hysteresis).
- Harden the expression: replace single-sample functions with windowed ones (`avg(/host/cpu.util,5m)`, `min(3)` style counting over consecutive polls), and add hysteresis so the problem threshold and recovery threshold differ — a trigger that recovers the instant the value dips under the line will flap for anything oscillating near it. Also verify preprocessing (delta-per-second on counters, throttling) is not amplifying noise.
- Remove structural noise: put patch windows and backups into Zabbix maintenance periods so actions are suppressed while data keeps flowing for forensics, and set trigger dependencies (disk-full on a VM behind its hypervisor, service checks behind their host's availability trigger) so one root cause pages once instead of cascading.
- Then close the loop on trust: tag triggers so actions can route by severity and service, review the Top 100 triggers report to find the noisiest offenders, and re-tune them on a schedule — a trigger whose alerts get ignored is worse than no trigger, because it teaches the team to ignore the channel.

## References

- [Triggers](https://www.zabbix.com/documentation/current/en/manual/config/triggers)
- [Trigger dependencies](https://www.zabbix.com/documentation/current/en/manual/config/triggers/dependencies)
- [Maintenance periods](https://www.zabbix.com/documentation/current/en/manual/maintenance)
- Further reading (blog): [Zabbix blog — getting started with hosts, items, and triggers](https://blog.zabbix.com/getting-started-with-zabbix-hosts-items-and-triggers/30190/)

## What to learn next

- Official documentation: [Triggers](https://www.zabbix.com/documentation/current/en/manual/config/triggers)
- Manual or specification: [Trigger expression](https://www.zabbix.com/documentation/current/en/manual/config/triggers/expression)
- Maintainer or personal blog: [Zabbix blog](https://blog.zabbix.com/)
- Technical blog: [Getting started with Zabbix hosts, items, and triggers](https://blog.zabbix.com/getting-started-with-zabbix-hosts-items-and-triggers/30190/)
- Hands-on guide: [Event correlation](https://www.zabbix.com/documentation/current/en/manual/config/event_correlation)
