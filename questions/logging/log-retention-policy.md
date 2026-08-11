---
title: Define a log retention policy
theme: logging
difficulty: middle
type: scenario
tags: [logging, security, governance, cost-optimization]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/92/r1/ipd
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define a log retention policy

How should a platform choose log retention periods?

## Answer guide

- Classify logs by operational value, legal or contractual requirement, privacy sensitivity, and expected incident investigation window. Define retention, access, deletion, and backup behavior per class rather than one universal period for application debug output and security audit evidence.
- Account for the full lifecycle: hot searchable storage, lower-cost archive, replicas, snapshots, and restored data. Retention is not achieved merely by deleting an index; document when data becomes inaccessible and how verified deletion works in each system.
- Revisit the policy after product, jurisdiction, or threat-model changes. Minimize sensitive data before collection, enforce access controls throughout retention, and test retrieval from archive so a cheap tier does not become unusable when an incident requires it.

## References

- [NIST SP 800-92 Rev. 1 (initial public draft) — guide to computer security log management](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
- Further reading (blog): [Google Cloud: log retention](https://cloud.google.com/logging/docs/storage)

## What to learn next

- Official documentation: [Google Cloud log retention](https://cloud.google.com/logging/docs/storage)
- Manual or specification: [NIST SP 800-92 Rev. 1 (initial public draft) — guide to computer security log management](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [AWS CloudWatch Logs data-protection practices](https://aws.amazon.com/blogs/mt/how-amazon-cloudwatch-logs-data-protection-can-help-detect-and-protect-sensitive-log-data/)
- Hands-on guide: [OpenSearch index state management](https://docs.opensearch.org/latest/im-plugin/ism/index/)
