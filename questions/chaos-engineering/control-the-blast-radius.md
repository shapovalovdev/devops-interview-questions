---
title: Control the blast radius of an experiment
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, blast-radius, fault-injection, availability]
sources:
  - url: https://chaos-mesh.org/docs/define-chaos-experiment-scope/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Control the blast radius of an experiment

How do you bound the damage an experiment can do, and how do you widen it responsibly?

## Answer guide

- Blast radius is the set of users, requests, and components a fault can reach. Bound it along every axis you have: selector scope (one namespace, one label, one instance, one availability zone), traffic share (a percentage of requests or a header-matched cohort), duration, and time of day. Chaos Mesh scopes by namespace, label and annotation selectors with an explicit mode and value; AWS Fault Injection Service bounds it with resource tags, filters, and a selection count.
- Prefer architectural isolation over hope. Cells, shuffle-sharded partitions, and per-tenant capacity limits mean the fault physically cannot reach beyond a known fraction of users, which is a stronger guarantee than a tool configuration that a typo could widen. Run in a canary cell first, and make the cell boundary the same one your production traffic routing already respects.
- Widen in planned steps, not in one jump: one instance, then one shard, then one zone, then a full-region drill, re-running the smaller scope after every change and only escalating when the previous step is boring. Each step needs its own abort condition, because the threshold that is safe for one per cent of traffic is far too loose for fifty.
- Failure modes: selectors that match more than intended because a label is shared, a fault type with inherently global reach such as DNS or a shared database, hidden coupling through a common cache or queue, retry amplification carrying the failure outside the scoped set, and a "small" experiment that happens to hit the one instance holding a leader lease.

## References

- [Chaos Mesh — define the scope of a chaos experiment](https://chaos-mesh.org/docs/define-chaos-experiment-scope/)
- Further reading (blog): [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [Chaos Mesh — define the scope of a chaos experiment](https://chaos-mesh.org/docs/define-chaos-experiment-scope/)
- Manual or specification: [AWS Fault Injection Service targets and selection modes](https://docs.aws.amazon.com/fis/latest/userguide/targets.html)
- Maintainer or personal blog: [Adrian Cockcroft — architecture and resilience writing](https://adrianco.medium.com/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Builders' Library — workload isolation using shuffle sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/)
