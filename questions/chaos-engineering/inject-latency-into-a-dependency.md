---
title: Inject latency into a single dependency
theme: chaos-engineering
difficulty: junior
type: scenario
tags: [chaos-engineering, fault-injection, latency, networking]
sources:
  - url: https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Inject latency into a single dependency

How do you add latency to one downstream call, and what should you watch while it is applied?

## Answer guide

- Decide where the delay is applied before choosing a tool. Network-level injection with a traffic-control queueing discipline, as Chaos Mesh NetworkChaos and the Linux tc netem module do, delays packets on the wire and therefore affects every call over that path. Application-level injection through a proxy or service-mesh fault filter delays a chosen route or a percentage of requests and leaves health checks and control-plane traffic alone.
- Scope the fault by direction, target, and share of traffic: one client deployment, one destination service and port, and a fraction of requests rather than all of them. Start with a delay a little below the client's configured timeout to observe queueing and retries, then exceed the timeout in a second run to observe the failure path itself. Correlated jitter is more realistic than a fixed delay.
- Watch the caller, not the callee. Client-side p50, p95 and p99 latency, timeout and retry counts, connection-pool saturation, thread or goroutine counts, queue depth, and the success rate of the user journey are what falsify the hypothesis. Also check the callers of your caller, because a slow dependency propagates upward faster than most teams expect.
- Failure modes: delaying liveness or readiness probes so the orchestrator restarts healthy pods, injecting on a shared node and hitting unrelated workloads, forgetting that a retry with no jitter turns added latency into a load spike, and leaving a queueing discipline attached to an interface after the experiment because the cleanup step ran on the wrong host.

## References

- [Chaos Mesh — simulate network chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Chaos Mesh — simulate network chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)
- Manual or specification: [tc-netem(8) — network emulator queueing discipline](https://man7.org/linux/man-pages/man8/tc-netem.8.html)
- Maintainer or personal blog: [Mikolaj Pawlikowski — chaos engineering writing](https://mikolajpawlikowski.com/)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [AWS Builders' Library — timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
