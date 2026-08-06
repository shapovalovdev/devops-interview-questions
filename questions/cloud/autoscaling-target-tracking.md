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
---

# Configure target-tracking autoscaling safely

How would you scale an EC2 service from demand without causing oscillation or overload?

## Answer guide

- Choose a metric that represents work or saturation, such as request count per target or CPU utilization when it correlates with capacity. Target tracking adjusts group capacity to keep the metric near the selected target.
- Set minimum capacity for baseline availability and maximum capacity for cost and downstream protection. Confirm the launch template, registration, warm-up, and load balancer health checks make new capacity useful.
- Observe scale-out latency, queue depth, error rate, and downstream limits during a load test. Scaling compute cannot fix a database, quota, or external API bottleneck.
- Avoid combining policies that fight over the same signal without understanding their precedence. A low target or noisy metric can flap capacity and create a self-inflicted incident.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [EC2 Auto Scaling target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Further reading: Auto Scaling health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)
