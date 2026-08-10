---
title: How would you govern a capacity model for a multi-tenant platform?
theme: systems-performance
difficulty: staff
type: scenario
tags: [capacity-planning, performance, cloud, governance]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How would you govern a capacity model for a multi-tenant platform?

## Answer guide

- Model demand by tenant class, workload shape, growth, and seasonal risk, then map it to the limiting resources and user latency objectives. Include headroom for failures, maintenance, retries, and deployment overlap.
- Review forecasts against measured utilization, saturation, error budgets, and cost. Assign owners for input quality, purchase or reservation lead time, quota management, and explicit escalation thresholds.
- Use load tests and controlled production experiments to calibrate the model. Averages hide tenant skew and burstiness; overprovisioning alone is costly, while aggressive utilization targets can turn one failure into a cascading incident.

## References

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/)
- [Google SRE Workbook](https://sre.google/workbook/)
- Further reading (blog): [Brendan Gregg — Capacity Planning](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [Google SRE workbook](https://sre.google/workbook/)
- Manual or specification: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Maintainer or personal blog: [Brendan Gregg — methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Kubernetes resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
