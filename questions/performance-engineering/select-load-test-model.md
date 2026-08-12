---
title: How do you select a load model for a production-facing service?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://k6.io/docs/testing-guides/test-types/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you select a load model for a production-facing service?

For a checkout API you must choose between a fixed virtual-user test, a constant arrival-rate test, and a replay of yesterday's production log. Which do you pick, and on what grounds?

## Answer guide

- Pick by the question being asked. To find the capacity knee and see how the service behaves past it, use an open model with a fixed arrival rate — k6's `constant-arrival-rate` or `ramping-arrival-rate`, or Vegeta — because it keeps arriving while the service degrades, exactly as users do. To characterise a bounded set of callers such as a batch pipeline or a connection-limited internal client, the closed fixed-virtual-user model is the accurate one. To validate a change against real request mix and key distribution, replay the production log.
- The two models diverge precisely where it matters. Closed-loop load is self-limiting: each virtual user waits for its response, so offered load falls as the service slows, throughput flattens instead of collapsing, and the slow window is under-sampled by coordinated omission. Open-loop load holds the arrival rate, so the backlog grows and you observe the collapse production would actually experience. That difference is why a closed-loop test can certify a service as healthy right up to the moment it falls over under real traffic.
- The model is more than the arrival shape. Match the read-to-write ratio, the key distribution (uniform random keys defeat caches that real Zipf-shaped traffic would hit, so uniform tests understate cached performance and overstate origin load), payload size distribution, think time, session and authentication behaviour, and connection reuse — a generator that opens a fresh TCP and TLS connection per request is measuring the handshake. Dataset size belongs in the model too, because an empty database produces different plans and cache behaviour than a production-sized one.
- A replay can only contain traffic the system already received, so it cannot show the behaviour of a new feature or a retry storm, and writes in a replay need idempotency handling or a scrubbed dataset — production logs also carry personal data that has its own handling rules. Verify the generator is not the bottleneck: single-threaded event loops, saturated generator CPU, per-request DNS lookups, and ephemeral port exhaustion all produce a convincing plateau. Always report error rate beside throughput, because a model that generates 4xx responses is benchmarking the error path.

## References

- [Grafana k6: Test types](https://k6.io/docs/testing-guides/test-types/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
