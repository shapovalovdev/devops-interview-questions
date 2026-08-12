---
title: Attribute Kubernetes cluster cost to teams
theme: finops
difficulty: middle
type: scenario
tags: [finops, kubernetes, cost-allocation, platform-engineering]
sources:
  - url: https://opencost.io/docs/specification
    source_type: standard
    verified_on: 2026-08-11
  - url: https://cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations
    source_type: official-docs
    verified_on: 2026-08-11
---

# Attribute Kubernetes cluster cost to teams

Ten teams share one Kubernetes cluster and the bill arrives as a handful of node line items. How do you attribute cost to each team?

## Answer guide

- The provider bills for nodes, disks, and load balancers; it has no idea what a namespace is. Attribution therefore has to be computed inside the cluster: take each workload's resource consumption over time, convert it to a share of node cost, and roll it up by an ownership label.
- The mechanism the OpenCost specification defines is to allocate each node's hourly cost across the pods scheduled on it in proportion to the maximum of requested and used CPU and memory for each pod-hour, then attach persistent volume, load balancer, and network cost to the workloads that own them. GKE cost allocation implements the same idea natively and surfaces namespace and label dimensions in the billing export.
- Requests versus usage is the central policy decision, and it is a policy decision rather than a technical one. Charging on requests makes teams responsible for the capacity they reserve and creates pressure to right-size requests; charging on usage makes the bill match consumption but leaves reserved-but-idle capacity unattributed and paid for by the platform.
- Whatever is left — the control plane, system daemonsets, monitoring agents, the idle headroom between requested and provisioned capacity, and any node capacity no pod could use — is genuinely shared and must have an explicit rule: absorbed by the platform, spread evenly, or spread in proportion to allocated cost. Publish the rule with the report.
- Failure modes: a label taxonomy that only half the workloads carry, so the largest cost centre is "unlabelled"; charging teams for idle capacity they did not request and cannot influence; and reporting a number that changes when the platform team changes node types, which makes a team's cost look worse for reasons entirely outside its control.

## References

- [OpenCost cost allocation specification](https://opencost.io/docs/specification)
- [GKE cost allocation](https://cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations)
- Further reading (blog): [OpenCost blog](https://opencost.io/blog)

## What to learn next

- Official documentation: [OpenCost documentation](https://opencost.io/docs/)
- Manual or specification: [OpenCost cost allocation specification](https://opencost.io/docs/specification)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Install OpenCost](https://www.opencost.io/docs/installation/install)
