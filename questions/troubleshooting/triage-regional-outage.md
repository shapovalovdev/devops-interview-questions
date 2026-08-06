---
title: Triage a regional outage with a safe traffic strategy
theme: troubleshooting
difficulty: senior
type: scenario
tags: [troubleshooting, availability, networking, incident-response, capacity-planning]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Triage a regional outage with a safe traffic strategy
## Answer guide
- Confirm regional scope using independent probes and customer telemetry, then inventory dependencies that are regional, globally shared, or capacity constrained. Treat DNS, identity, control planes, and data stores as possible shared failure domains.
- Shift traffic incrementally only to prevalidated capacity and observe latency, errors, saturation, and data consistency. Preserve a healthy reserve; moving all traffic at once can overload the remaining regions.
- Decide whether writes must be limited, queued, or made read-only according to documented consistency guarantees. Communicate the user impact and recovery criteria; fail back gradually after the failing region is demonstrably stable.
## References
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book — Load Balancing at the Frontend](https://sre.google/sre-book/load-balancing-frontend/)
- Further reading (blog): [AWS Builders’ Library](https://aws.amazon.com/builders-library/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- Official guide: [Google Cloud reliability](https://cloud.google.com/architecture/framework/reliability)
- Personal technical blog: [Marc Brooker](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders’ Library](https://aws.amazon.com/builders-library/)
