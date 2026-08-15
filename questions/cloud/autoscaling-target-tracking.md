---
title: Configure target-tracking autoscaling safely
theme: cloud
difficulty: middle
type: scenario
tags: [aws, cloud, capacity-planning, monitoring, reliability]
sources:
  - url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-overview
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/compute/docs/autoscaler
    source_type: official-docs
    verified_on: 2026-08-16
---

# Configure target-tracking autoscaling safely

How would you scale an EC2 service from demand without causing oscillation or overload?

## Answer guide

- Choose a metric that represents work or saturation, such as request count per target or CPU utilization when it correlates with capacity. Target tracking adjusts group capacity to keep the metric near the selected target.
- Set minimum capacity for baseline availability and maximum capacity for cost and downstream protection. Confirm the launch template, registration, warm-up, and load balancer health checks make new capacity useful.
- Observe scale-out latency, queue depth, error rate, and downstream limits during a load test. Scaling compute cannot fix a database, quota, or external API bottleneck.
- Avoid combining policies that fight over the same signal without understanding their precedence. A low target or noisy metric can flap capacity and create a self-inflicted incident.
- Target tracking has named equivalents: an Azure Monitor autoscale rule scales to hold a metric near a target, and a Google Cloud autoscaler resizes a managed instance group on utilization or balancing load, so the transferable content is the metric-to-capacity rule and its flapping risks, not an EC2 feature.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [EC2 Auto Scaling target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Further reading: Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)
- [Azure Monitor — autoscale overview](https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-overview)
- [Google Cloud — autoscaler](https://cloud.google.com/compute/docs/autoscaler)

## What to learn next

- Official documentation: [EC2 Auto Scaling target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- Manual or specification: [EC2 Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Compute Blog — Faster target tracking](https://aws.amazon.com/blogs/compute/faster-scaling-with-amazon-ec2-auto-scaling-target-tracking/)
- Hands-on guide: [AWS Workshops](https://workshops.aws/)
