---
title: Rightsize overprovisioned compute
theme: finops
difficulty: middle
type: scenario
tags: [finops, rightsizing, cost-optimization, capacity-planning]
sources:
  - url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances
    source_type: official-docs
    verified_on: 2026-08-11
---

# Rightsize overprovisioned compute

A fleet of virtual machines averages 8 percent CPU utilisation. How do you rightsize it without causing an incident?

## Answer guide

- Average CPU is not sufficient evidence. Pull a utilisation profile over at least a full business cycle — several weeks, covering month-end, marketing events, and batch windows — and look at high percentiles, not the mean. A workload at 8 percent average and 95 percent at the daily peak is not overprovisioned on CPU at all.
- Check every dimension the instance is actually sized on: CPU, memory, network throughput, disk IOPS and throughput, and any per-instance connection or file-descriptor ceiling. Rightsizing tools such as AWS Compute Optimizer and Google Cloud machine type recommendations infer from collected metrics, and memory is frequently missing unless an agent is installed, so a recommendation may be based on CPU alone.
- The mechanism of a safe change is incremental and reversible: change one instance family or size at a time, in one availability zone or one canary group, keep the old configuration ready, and watch latency percentiles and error rates rather than just CPU. Prefer moving to a newer generation or a different family ratio over simply shrinking, since a better price-performance family often saves more with less risk.
- Material constraints: burstable families accumulate and spend credits, so a small instance that looks fine for a week can fall off a cliff when credits run out; some instance changes require a stop and start with an address or local-storage implication; and commitment coverage bought for the old family may no longer apply after the move, turning a compute saving into a discount loss.
- Failure modes: rightsizing away the headroom that absorbed a failover, sizing to steady state and losing the capacity that handled a retry storm, applying a recommendation generated during a quiet period, and shrinking a node group until the scheduler can no longer place the largest pod.

## References

- [AWS Compute Optimizer user guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- [Apply Google Cloud machine type recommendations](https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances)
- Further reading (blog): [AWS Compute blog](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Compute Optimizer user guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- Manual or specification: [AWS Well-Architected cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Apply Google Cloud machine type recommendations](https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances)
