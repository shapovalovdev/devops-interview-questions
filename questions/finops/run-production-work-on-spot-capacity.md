---
title: Run production work on spot capacity
theme: finops
difficulty: middle
type: scenario
tags: [finops, spot-instances, reliability, kubernetes]
sources:
  - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/compute/docs/instances/spot
    source_type: official-docs
    verified_on: 2026-08-11
---

# Run production work on spot capacity

Which parts of a production platform can safely run on spot or preemptible capacity, and what must be built before you move them?

## Answer guide

- The candidate set is work that is interruptible, restartable, and horizontally replaceable: stateless request handlers behind a load balancer with surplus replicas, queue consumers with at-least-once semantics, CI runners, batch and ETL jobs with checkpointing, and machine-learning training that saves state. Work that is stateful, singleton, or holds a long uninterruptible transaction is a poor fit.
- The mechanism to build first is graceful interruption handling. EC2 delivers a Spot instance interruption notice a short interval before reclamation and rebalance recommendations earlier than that; Google Cloud sends a preemption notice to Spot VMs before shutting them down. The handler must stop accepting new work, drain or cordon the node, finish or requeue in-flight work, and exit before the deadline rather than relying on a generic SIGTERM path that was never tested.
- Diversify the capacity pools. Interruption is correlated within an instance type, size, and zone, so a fleet pinned to one pool can lose most of its capacity at once. Spread across several families and zones, and keep an on-demand or committed floor sized to carry the service alone while replacements are found.
- Material constraints: spot capacity is not guaranteed and a request can simply go unfulfilled; the discount varies by pool and over time; reclamation and scarcity often correlate with the same demand surges that drive your own traffic; and some quota, licensing, or data-locality rules limit which pools you may use.
- Failure modes: relying on a fixed sleep in the shutdown hook instead of finishing work; a pod disruption budget that blocks drain until the deadline passes; autoscaling that cannot obtain replacement capacity because every configured pool is exhausted; and load tests that never exercise a mass reclamation, so the first real one is the experiment.

## References

- [Amazon EC2 Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Google Cloud Spot VMs](https://cloud.google.com/compute/docs/instances/spot)
- Further reading (blog): [AWS Compute blog](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [Amazon EC2 Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- Manual or specification: [EC2 Fleet allocation strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-configuration-strategies.html)
- Maintainer or personal blog: [Marc Brooker — on scale and system design](https://brooker.co.za/blog/2024/06/04/scale.html)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Karpenter disruption and consolidation](https://karpenter.sh/docs/concepts/disruption/)
