---
title: Monitor discovered entities with Zabbix low-level discovery
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, zabbix, automation]
sources:
  - url: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.zabbix.com/documentation/current/en/manual/config/items
    source_type: official-docs
    verified_on: 2026-08-17
---

# Monitor discovered entities with Zabbix low-level discovery

A fleet of hypervisors each exposes a different set of network interfaces, mounted filesystems, and virtual machines. Explain how Zabbix low-level discovery (LLD) turns one template into per-entity items and triggers without hand-adding them.

## Answer guide

- An LLD rule runs a discovery item (a built-in key such as `net.if.discovery` or `vfs.fs.discovery`, an SNMP walk, or a script returning JSON) that emits one record per real entity, each carrying discovery macros like `{#IFNAME}` or `{#FSNAME}` plus any custom attributes you add.
- Attached to the rule are prototypes — item, trigger, and graph prototypes — written once with the macros embedded; Zabbix instantiates a real item, trigger, and graph per discovered entity, and keeps them in sync: a filesystem that disappears is removed after the rule stops reporting it (with a keep-lost-resources period to absorb flapping).
- Guard the generated surface with discovery filters and user-macro contexts so a churning entity (ephemeral containers, loopback interfaces) cannot spawn thousands of short-lived items; every prototype inherits the same interval and history/trend policy as a normal item, so unfiltered discovery multiplies load on the server, proxy, and database alike.
- Treat LLD as the mechanism that keeps the template honest: the out-of-the-box templates rely on it for filesystems, network interfaces, CPUs, and VMware entities, and overrides (per-discovery-condition changes to interval, severity, or disabled state) let one template serve heterogeneous hosts without forking it per host class.

## References

- [Low-level discovery](https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery)
- [Items](https://www.zabbix.com/documentation/current/en/manual/config/items)
- Further reading (blog): [Zabbix blog — getting started with hosts, items, and triggers](https://blog.zabbix.com/getting-started-with-zabbix-hosts-items-and-triggers/30190/)

## What to learn next

- Official documentation: [Low-level discovery](https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery)
- Manual or specification: [Custom LLD rules](https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery#custom-lld-rules)
- Maintainer or personal blog: [Zabbix blog](https://blog.zabbix.com/)
- Technical blog: [Getting started with Zabbix hosts, items, and triggers](https://blog.zabbix.com/getting-started-with-zabbix-hosts-items-and-triggers/30190/)
- Hands-on guide: [Configuring a template](https://www.zabbix.com/documentation/current/en/manual/config/templates/template)
