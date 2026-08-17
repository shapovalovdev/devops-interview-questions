---
title: Decide when to deploy a Zabbix proxy
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, zabbix, distributed-systems, networking, resilience]
sources:
  - url: https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://www.zabbix.com/documentation/current/en/manual/appendix/items/activepassive
    source_type: official-docs
    verified_on: 2026-08-16
---

# Decide when to deploy a Zabbix proxy

Your fleet spans several data centers and a set of remote clusters with unreliable links to the central Zabbix server. When does a Zabbix proxy earn its place, and what trade-offs does it add?

## Answer guide

- A proxy is a local collection tier: hosts in a remote site report to the proxy, and only the proxy talks to the central server, cutting cross-WAN agent chatter and server load to one stream per site.
- It buys survivable buffering — the proxy queues collected values on disk or in memory when the uplink or the server is down, then replays them, so a transient link failure no longer becomes a gap in graphs or a storm of unreachable alerts.
- Active-mode proxies also solve reachability where the central server cannot initiate connections into a firewalled cluster; the proxy dials out instead.
- The trade-offs are a second component to deploy, patch, and monitor per site, configuration-sync delay before new hosts appear centrally, and a fault domain: proxy failure blinds every host behind it, so proxy health itself needs alerting and spare capacity.
- Reasonable rule: one proxy per data center or remote cluster, sized for that site's metrics per second; avoid proxies for a single LAN where the server hears agents directly.

## References

- Further reading (blog): [Zabbix blog — hidden benefits of Zabbix proxy](https://blog.zabbix.com/hidden-benefits-of-zabbix-proxy/9359/)
- [Zabbix documentation — distributed monitoring with proxies](https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies)
- [Zabbix documentation — active and passive agent checks](https://www.zabbix.com/documentation/current/en/manual/appendix/items/activepassive)

## What to learn next

- Official documentation: [Zabbix proxies](https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies)
- Manual or specification: [Active and passive checks](https://www.zabbix.com/documentation/current/en/manual/appendix/items/activepassive)
- Maintainer or personal blog: [Zabbix blog — installing and configuring the Zabbix proxy](https://blog.zabbix.com/installing-and-configuring-the-zabbix-proxy/13319/)
- Technical blog: [Robust Perception monitoring blog](https://www.robustperception.io/blog/)
- Hands-on guide: [Zabbix server and proxy containers](https://github.com/zabbix/zabbix-docker)
