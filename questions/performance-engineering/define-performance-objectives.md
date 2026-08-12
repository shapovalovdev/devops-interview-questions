---
title: What makes a performance objective actionable?
theme: performance-engineering
difficulty: junior
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# What makes a performance objective actionable?

Someone proposes "the site should be fast" as the performance objective. Rewrite it so an on-call engineer can act on it, and say what each part has to pin down.

## Answer guide

- An actionable objective names five things: the indicator and where it is measured, the population of requests it covers, the aggregation, the target with its window, and the consequence of missing it. "99 percent of authenticated GET /cart requests complete within 300 ms measured at the load balancer over a rolling 28-day window" can be acted on; "the site should be fast" cannot. The threshold itself should come from user behaviour or business evidence, not from whatever the service happens to do today.
- The indicator has to be a ratio of good events to valid events, which forces two definitions: good (under the latency threshold and not an error) and valid (excluding health checks, synthetic probes, bots, and traffic the service was never meant to serve). The percentile decides who is protected — a p50 target protects nobody at the tail, while a p99.9 target on an endpoint serving a few hundred requests an hour is statistically meaningless. Measure at the boundary nearest the user that you can still attribute, since a handler-side timer omits accept-queue, TLS, and network time.
- Target and window together define an error budget: 99 percent over 28 days permits roughly 6.7 hours of badness, and that budget is the consequence mechanism deciding when feature work yields to reliability work. Set the target deliberately below 100 percent, keep the internal objective stricter than any external SLA so there is room to react before a contractual breach, and write separate objectives per request class — one target spanning a 5 ms cache read and a two-second report cannot be enforced against either.
- Objectives derived from current performance ratify whatever the service already does and can never be missed; objectives derived from an aspiration nobody funds are ignored within a quarter. An objective with no owner and no consequence is a dashboard. And the denominator quietly breaks the number: counting each retry as a separate event, or scoring a client-abandoned request as a success, makes the indicator move for reasons that have nothing to do with the user experience.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
