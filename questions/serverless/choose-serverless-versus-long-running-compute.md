---
title: Decide between managed functions and long-running compute
theme: serverless
difficulty: staff
type: scenario
tags: [cloud, architecture, cost-optimization, governance, capacity-planning]
sources:
  - url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Decide between managed functions and long-running compute

An organization is arguing about whether new services should default to functions or to long-running containers. How do you decide, and how do you make the decision reviewable?

## Answer guide

- Make it a workload-shaped decision with written criteria rather than a platform preference. The variables that actually decide it are traffic shape and duty cycle, latency budget including the tolerance for cold starts, request duration against the platform's maximum, statefulness and connection cost, packaging weight, and how much of the team's time currently goes to capacity and patching work that a managed platform would absorb.
- Functions win where load is spiky or unpredictable, the unit of work is short and independent, integration with managed event sources is the point, and the team is small enough that not owning scaling and patching is a real saving. Long-running compute wins where utilisation is high and steady, latency budgets are tight enough that any cold start is unacceptable, the process must hold expensive state such as large caches or connection pools, or the workload needs specialised hardware and long execution.
- Quantify rather than assert. Compare fully loaded cost at realistic percentiles—not just compute, but request charges, log ingestion, NAT and gateway data, and the tracing backend—against instances plus their idle capacity, control-plane, and operational headcount. Include the migration and dual-run cost, and state the traffic level at which the answer flips, because that crossover is the durable output of the analysis.
- Treat portability honestly. Managed event sources and identity integrations are where lock-in really lives, not the handler code. Keep business logic behind an interface you own, and record the decision as an ADR with its assumptions and review trigger so the organization can revisit it when traffic, pricing, or platform limits change rather than relitigating it per team.
- Failure modes to expect: a hybrid built by default that pays both operational bills, a strategic mandate issued without a paved road so teams reinvent identity and delivery, cost models that ignore log and network charges and then surprise finance, and a "temporary" migration that stalls halfway and leaves two production topologies to be operated for years.

## References

- [AWS Well-Architected Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
- Further reading (blog): [AWS Architecture Blog — compute selection articles](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [AWS Well-Architected Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
- Manual or specification: [Microservices on AWS whitepaper](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
- Maintainer or personal blog: [Marc Brooker — on the economics and internals of serverless](https://brooker.co.za/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [KEDA event-driven autoscaling concepts](https://keda.sh/docs/latest/concepts/)
