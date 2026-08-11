---
title: Inject packet loss and network partitions
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, fault-injection, packet-loss, networking]
sources:
  - url: https://man7.org/linux/man-pages/man8/tc-netem.8.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Inject packet loss and network partitions

What changes when you drop packets or partition the network rather than adding delay?

## Answer guide

- Packet loss is not slow success. TCP hides moderate loss behind retransmission, so a few per cent of drops appears to the application as sudden latency spikes and a collapsed congestion window rather than errors; heavy loss produces connection resets and timeouts. The netem queueing discipline models loss, duplication, corruption, and reordering with an optional correlation factor, which matters because real loss arrives in bursts, not uniformly at random.
- A partition is different again: both sides stay healthy and both believe the other has died. That is what exposes split-brain in leader election, dual writes to a replicated store, stale caches serving confidently, and clients that fail over to a replica that is also accepting writes. Choose the direction deliberately — a one-way partition, where A reaches B but B cannot reply, breaks far more assumptions than a symmetric cut.
- Material constraints: apply the fault at a boundary you can reverse without network access to the far side, because you may not be able to reach the isolated host to clean up. Keep control-plane, SSH, and telemetry paths outside the fault or accept that you will lose visibility. Duration must exceed the relevant timeouts, heartbeat intervals, and lease durations, or nothing interesting happens.
- Failure modes: partitioning a quorum member and losing write availability for the whole cluster, cutting off a node the orchestrator then evicts and reschedules elsewhere, a lease that expires and triggers a real failover you have to unwind, and conntrack or connection-pool state that stays broken after the fault is removed so recovery needs an explicit reset.

## References

- [tc-netem(8) — network emulator queueing discipline](https://man7.org/linux/man-pages/man8/tc-netem.8.html)
- Further reading (blog): [Cloudflare blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Chaos Mesh — simulate network chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)
- Manual or specification: [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
- Maintainer or personal blog: [Mikolaj Pawlikowski — chaos engineering writing](https://mikolajpawlikowski.com/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [tc-netem(8) manual page](https://man7.org/linux/man-pages/man8/tc-netem.8.html)
