---
title: How do you investigate high CPU steal time on a virtual machine?
theme: systems-performance
difficulty: senior
type: troubleshooting
tags: [cloud, cpu, virtualization, performance]
sources:
  - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you investigate high CPU steal time on a virtual machine?

## Answer guide

- CPU steal time means the guest was ready to run but the hypervisor scheduled another workload. Verify the guest metric, provider instance telemetry, host class, burst-credit state where applicable, and correlation with latency.
- Separate provider contention from application CPU saturation, quota throttling, and noisy network or storage symptoms. Compare another instance family, availability zone, or dedicated capacity using the same workload and observation window.
- Escalate evidence to the provider if a controlled comparison supports host contention. A resize may change cost, NUMA layout, or CPU model; it can relieve a symptom while masking inefficient application concurrency.

## References

- [Amazon EC2 monitoring](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html)
- [Linux procfs documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Further reading (blog): [Brendan Gregg — Linux CPU Utilization](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)

## What to learn next

- Official documentation: [Amazon EC2 metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- Manual or specification: [procfs documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Maintainer or personal blog: [Brendan Gregg — CPU utilization](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [CloudWatch metrics guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
