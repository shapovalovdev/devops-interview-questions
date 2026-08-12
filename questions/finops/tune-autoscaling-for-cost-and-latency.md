---
title: Tune autoscaling for cost and latency
theme: finops
difficulty: senior
type: scenario
tags: [finops, kubernetes, latency, capacity-planning]
sources:
  - url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Tune autoscaling for cost and latency

An autoscaled service is expensive at night and slow at the morning peak. How do you tune it so both improve?

## Answer guide

- Diagnose which of the three loops is failing before touching thresholds. Horizontal pod autoscaling reacts to a metric, the cluster autoscaler or Karpenter provisions nodes, and the application itself takes time to become ready. The morning latency is almost always the sum of the metric window, the scale-up decision interval, node provisioning, image pull, and warm-up — not an aggressive target value.
- The economics of the trade are asymmetric and should be treated that way: scale up fast and scale down slowly. Over-provisioning for a few minutes costs a few minutes of instance time; under-provisioning at peak costs latency, errors, and possibly a retry storm that makes the load worse. Set a short scale-up stabilisation window and a long scale-down one.
- Attack the lag rather than the threshold where you can. Cut container start-up time and image size, use readiness gates that reflect real warm-up, keep a small pool of pre-provisioned capacity or over-provisioning placeholder pods with low priority that the scheduler evicts to make room instantly, and scale on a leading signal — queue depth, concurrency, or requests in flight — rather than on CPU, which lags the load it is caused by.
- Use scheduled scaling for known shape. A predictable morning ramp does not need to be discovered by a reactive loop every day; a scheduled minimum that rises before the ramp and falls afterwards removes the worst of the latency and most of the night-time cost with far less tuning risk than an aggressive reactive configuration.
- Constraints and failure modes: a scale-down that is too eager causes thrashing, and each cycle pays start-up cost and disturbs connections; pod disruption budgets and long terminationGracePeriod values block consolidation, so nodes never actually go away and the saving never reaches the bill; per-node overhead means very small nodes waste a large fraction of capacity; and scaling a stateless tier while a downstream database stays fixed simply moves the bottleneck.

## References

- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Kubernetes cluster autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)
- Further reading (blog): [Kubernetes blog](https://kubernetes.io/blog/)

## What to learn next

- Official documentation: [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- Manual or specification: [Kubernetes cluster autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)
- Maintainer or personal blog: [Marc Brooker — on scale and system design](https://brooker.co.za/blog/2024/06/04/scale.html)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Karpenter NodePools](https://karpenter.sh/docs/concepts/nodepools/)
