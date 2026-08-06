---
title: Design a CloudWatch alarm that supports action
theme: cloud
difficulty: middle
type: scenario
tags: [aws, cloud, monitoring, reliability, incident-response]
sources:
  - url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a CloudWatch alarm that supports action

What makes a CloudWatch alarm useful to an on-call engineer rather than just noisy?

## Answer guide

- Alert on a symptom or actionable saturation signal tied to a service objective, with a clear owner and runbook. Set period, evaluation periods, threshold, and missing-data behavior deliberately.
- Use a warning and urgent path when the response differs. Combine an error or latency signal with traffic context so a low-volume failure and a broad outage are not treated identically.
- Include dashboard links, affected resource identifiers, recent deployment context, and an escalation destination. Test alarm delivery and the action path, not merely metric collection.
- Avoid paging on every fluctuating resource metric. Overly sensitive thresholds and unhandled missing data train responders to ignore alerts and hide the real incident.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [Amazon CloudWatch: create an alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Further reading: CloudWatch alarm evaluation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation)
