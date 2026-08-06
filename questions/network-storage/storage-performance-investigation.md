---
title: Investigate network-storage latency
theme: network-storage
difficulty: senior
type: troubleshooting
tags: [storage, networking, performance, monitoring, troubleshooting]
sources:
  - url: https://docs.kernel.org/block/index.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate network-storage latency

How do you isolate whether high storage latency originates in an application, client, network, or storage service?

## Answer guide

- Start from the affected operation and time window: collect application request latency, filesystem and block-device latency, client CPU and queueing, network loss or retransmissions, and server or array latency. Correlate by host, volume, path, operation size, and percentile rather than only averages.
- Form hypotheses and change one variable at a time. Compare an unaffected workload, a local-disk control, and a direct service measurement where safe; inspect saturation, errors, queue depth, throttling, and recent configuration or topology changes.
- Do not tune queue depth or cache settings as a first response. A client symptom can be caused by a congested switch, degraded disk, backend recovery, DNS delay, or application burst; changing settings without a baseline can conceal the cause and worsen tail latency.

## References

- [Linux kernel: block layer documentation](https://docs.kernel.org/block/index.html)
- Further reading (blog): [Brendan Gregg: Linux performance analysis](https://www.brendangregg.com/blog/)

## What to learn next

- Official documentation: [Linux block layer documentation](https://docs.kernel.org/block/index.html)
- Manual or specification: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Maintainer or personal blog: [Brendan Gregg blog](https://www.brendangregg.com/blog/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [Brendan Gregg performance tools](https://www.brendangregg.com/linuxperf.html)
