---
title: Set SLOs that survive a degraded cache
theme: caching
difficulty: staff
type: scenario
tags: [caching, sre, reliability, observability, monitoring]
sources:
  - url: https://prometheus.io/docs/practices/histograms/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://opentelemetry.io/docs/concepts/signals/metrics/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set SLOs that survive a degraded cache

Your latency SLO is met only because the cache is warm. How should the objectives and alerts be restructured?

## Answer guide

- Recognise the failure of the current design: an SLO satisfied by a cached fast path says nothing about the service's behaviour when the cache is cold, and the error budget is silently being spent on a dependency nobody has committed to. The objective must describe user-visible behaviour in both states, or it will be met right up until the moment it matters.
- Set the user-facing objective on the whole request, then use separate service-level indicators for the hit and miss paths so the mixture is visible. If the miss path cannot meet the objective at full traffic, that is a capacity commitment to write down, not a metric to hide — decide explicitly whether the answer is origin headroom, a stated degraded mode, or load shedding.
- Measure with the right instruments. Latency needs percentiles from histograms, and Prometheus histogram quantiles are estimates whose accuracy depends on bucket boundaries chosen for the latency you care about; averaging a quantile across instances is not meaningful. Aggregate the histograms, not the quantiles, and use exemplars or traces to connect a slow request to whether it hit or missed.
- Make hit ratio a diagnostic signal rather than an objective. Alerting on hit ratio produces pages for harmless changes and misses real ones, because the ratio moves with traffic mix. Page on user-visible symptoms — latency, error rate, origin saturation — and put hit ratio, eviction rate, entry age, and cache client error rate on the dashboard used to explain them.
- Define the degraded mode in advance and rehearse it. Write down what the service does at zero hit ratio: which features shed, what stale data may be served and for how long, what the load-shedding order is, and which SLO applies while degraded. Then run a game day that removes the cache, and treat any SLO that only survives with a warm cache as an unresolved risk rather than a passing quarter.

## References

- [Prometheus histograms and summaries documentation](https://prometheus.io/docs/practices/histograms/)
- [OpenTelemetry metrics signal documentation](https://opentelemetry.io/docs/concepts/signals/metrics/)
- Further reading (blog): [Cloudflare blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [Prometheus histograms and summaries documentation](https://prometheus.io/docs/practices/histograms/)
- Manual or specification: [OpenTelemetry metrics signal documentation](https://opentelemetry.io/docs/concepts/signals/metrics/)
- Maintainer or personal blog: [Marc Brooker — caches, modes, and unstable systems](https://brooker.co.za/blog/2021/08/27/caches.html)
- Technical blog: [Cloudflare blog](https://blog.cloudflare.com/)
- Hands-on guide: [Google SRE book — table of contents](https://sre.google/sre-book/table-of-contents/)
