---
title: Use CloudTrail as audit evidence during a change investigation
theme: cloud
difficulty: middle
type: troubleshooting
tags: [aws, cloud, security, observability, troubleshooting]
sources:
  - url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use CloudTrail as audit evidence during a change investigation

An AWS resource changed unexpectedly. How do you use CloudTrail to establish what happened?

## Answer guide

- Start with the resource, account, Region, and time window, then find the relevant management or data event. Record the event name, request parameters, source IP, user identity, session context, and event time.
- Distinguish Event history from a trail or event data store: Event history has limited management-event visibility, while durable investigation needs logging configured for the event types and retention you require.
- Correlate the API event with configuration history, deployment records, and the affected service's logs. Confirm whether an automation role, human session, or AWS service principal made the change.
- CloudTrail cannot reveal events it was not configured to record, and a single event does not prove intent. Protect log destinations and validate trail coverage before an incident.

## References

- [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Further reading: CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
