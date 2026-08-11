---
title: How should an engineer choose latency histogram buckets?
theme: performance-engineering
difficulty: middle
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://prometheus.io/docs/practices/histograms/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How should an engineer choose latency histogram buckets?

You are adding an `http_request_duration_seconds` histogram to a service whose objective is a 300 ms p99. How do you choose bucket boundaries, and what does the choice cost?

## Answer guide

- Put a boundary exactly on the value you make decisions about. With a 300 ms objective, `0.3` must be an edge, because then the SLO compliance ratio is a plain division of two bucket counters and needs no interpolation at all. Around that anchor, space edges roughly geometrically (say 5 ms to 10 s at a factor near two) so relative resolution is constant across the range; Prometheus `DefBuckets` is a generic 5 ms-to-10 s ladder and is almost never the right ladder for a specific endpoint.
- A classic histogram is a set of cumulative `le` counters, and `histogram_quantile` interpolates linearly inside whichever bucket holds the quantile. Accuracy therefore depends entirely on how fine the buckets are near the quantile you query, not on how many buckets you have overall, so extra edges out at 30 s buy nothing while extra edges between 200 ms and 500 ms buy a usable p99.
- Every bucket is a separate time series, multiplied by every label combination: twelve buckets on a metric with 3 labels of 20 values each is roughly 720 series per instance before you count `_sum` and `_count`. Boundaries are also a compatibility contract — changing them makes old and new series non-mergeable and breaks any comparison spanning the change, and `le` values must be formatted identically across services or the aggregation silently splits. Native histograms (Prometheus 2.40 and later, still experimental) replace the choice with a resolution factor but need a matching exposition and query stack.
- Two failure modes dominate. Buckets set below real latency dump nearly everything into `+Inf`, and the p99 pins to the highest finite edge and stops responding to regressions. Buckets too coarse around the objective make the quantile jump between two edges as a few requests cross over, which shows up as an alert that flaps between fine and firing without the service changing. Both look like a broken service and are actually a broken metric, so verify the bucket population once under real traffic before wiring an alert to it.

## References

- [Prometheus: Histograms and summaries](https://prometheus.io/docs/practices/histograms/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
