---
title: How are throughput, concurrency, and latency related during a load test?
theme: performance-engineering
difficulty: junior
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How are throughput, concurrency, and latency related during a load test?

A load test at 50 virtual users reports 500 requests per second at 100 ms; raising it to 100 virtual users reports 520 requests per second at 190 ms. What does that pair of results tell you, and which figure is the service's capacity?

## Answer guide

- Little's law, concurrency = throughput x latency, ties the two runs together: 50 users at 100 ms is consistent with 500 requests per second, and the second run added concurrency that turned almost entirely into queue time rather than completed work. That is the knee. Capacity is roughly the 500 per second at which latency was still flat, not the 520 the tool printed at twice the latency.
- The plateau is partly an artifact of the generator's model. A closed-loop test with a fixed number of virtual users is self-limiting, because each user waits for a response before sending again, so offered load falls as the service slows and throughput flattens instead of collapsing. An open-loop model with a fixed arrival rate (k6 `constant-arrival-rate`, Vegeta) keeps arriving regardless, and past the knee the backlog and latency grow without bound — which is what real traffic does.
- Little's law needs a stable observation window with arrivals matching departures and no growing backlog, and it relates averages only; substituting p99 for mean latency gives a meaningless number. The queueing consequence is the practical one: response time scales roughly as 1/(1 - utilization), so the step from 80 to 90 percent utilization costs far more latency than the step from 0 to 80. Planning to run a latency-sensitive service near full utilization is planning an incident.
- Read throughput as successful responses only. Failed and timed-out requests complete quickly and inflate the number, so a service that starts fast-failing looks faster on the throughput chart while getting worse for users. Closed-loop tests additionally under-sample the slow period through coordinated omission. And before concluding the server is the ceiling, check the generator: a single-threaded tool, a saturated test host, or ephemeral port exhaustion on the client produces the same flat throughput curve.

## References

- [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
