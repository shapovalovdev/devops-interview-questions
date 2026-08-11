---
title: How should capacity economics influence performance governance?
theme: performance-engineering
difficulty: staff
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How should capacity economics influence performance governance?

Finance asks why the platform's infrastructure bill grew 60 percent while traffic grew 20 percent. How do you make capacity economics a standing input to performance decisions rather than an annual surprise?

## Answer guide

- Govern on cost per unit of business work — per order, per thousand requests, per gigabyte ingested — not on total spend. Total spend rising with traffic is expected; unit cost rising is the regression worth acting on, and it is the only version of the number a team can be held to. Publish it per service beside that service's latency objective, and attribute shared spend for the database, cache, observability stack, and egress back to the services that drive it, or the largest consumers never appear in anyone's report.
- The cost curve is not linear in load. Headroom for peak is billed at peak, so a service with a 3x peak-to-average ratio pays for peak capacity around the clock unless the work can scale or move; queue-backed asynchronous work can be deferred into troughs and run on interruptible capacity, while a synchronous request path cannot. Redundancy multiplies the base: N+1 across three zones adds cross-zone transfer that can exceed the compute it protects. Telemetry retention and cardinality grow with fleet size rather than traffic, which is why observability is routinely a top-three line.
- The queue that decouples cost from peak carries the failure mode the economics have to fund. A queue absorbs a burst only while drain rate exceeds arrival rate; once it does not, backlog grows and recovery time is the accumulated deficit, so a modest capacity shortfall becomes an hours-long backlog long after the burst ended. Governance therefore has to treat drain capacity, a maximum backlog age, backlog shedding, and separate queues per priority as funded budget items rather than implementation details left to whoever is on call.
- An efficiency programme scored in dollars saved rewards cutting headroom, and that pays for itself right up to the first real peak. A chargeback number with no lever attached produces resentment instead of change, so pair it with things the owning team actually controls: instance family, autoscaling policy, retention, sampling rate. And unit cost improved during a traffic trough is not an improvement — normalise against the driver, and keep the latency objective fixed as the constraint every cost decision has to respect.

## References

- [AWS Builders' Library: Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
