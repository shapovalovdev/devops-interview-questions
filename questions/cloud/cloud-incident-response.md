---
title: Lead an AWS workload incident response
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, incident-response, observability, reliability]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Lead an AWS workload incident response

How do you contain a suspected compromised cloud workload while preserving evidence and service recovery options?

## Answer guide

- Declare an incident, establish roles and a communication channel, then use the smallest safe containment action: restrict identity or network access, isolate the workload, and preserve the original state where evidence is needed.
- Collect authoritative evidence from CloudTrail, service logs, metrics, configuration history, and relevant snapshots before destructive remediation. Record timestamps, account, region, principal, and actions taken.
- Rotate exposed credentials, remove persistence, rebuild from known-good artifacts, and validate monitoring before returning traffic. Treat a replacement instance as remediation only after the root access path is understood.
- Avoid deleting the compromised resource first: it can destroy evidence and prevent scope analysis. Conversely, delaying containment for perfect forensics can allow continued harm; balance both through a rehearsed runbook.

## References

- [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html)
- [Further reading: AWS CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
