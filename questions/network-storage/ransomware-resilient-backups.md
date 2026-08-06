---
title: Build ransomware-resilient storage backups
theme: network-storage
difficulty: senior
type: scenario
tags: [storage, security, reliability, monitoring, governance]
sources:
  - url: https://www.cisa.gov/stopransomware/ransomware-guide
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build ransomware-resilient storage backups

How would you make backups resilient to both production compromise and operator error?

## Answer guide

- Separate backup credentials, administration planes, and retention controls from production identities. Keep recoverable copies in a distinct failure domain and protect them with immutable or write-once controls where the selected platform supports them.
- Define recovery point and recovery time objectives, data classification, key-management recovery, restore order, and authority to release retention. Exercise isolated restores regularly and record evidence that data, permissions, application consistency, and dependencies are usable.
- Replication of a corrupted or encrypted dataset is not a backup. A backup that cannot be located, decrypted, authorized, or restored at scale during an incident creates false confidence; monitor jobs, age, capacity, and restore-test success.

## References

- [CISA: ransomware guide](https://www.cisa.gov/stopransomware/ransomware-guide)
- Further reading (blog): [Google Cloud Blog: ransomware protection](https://cloud.google.com/blog/topics/threat-intelligence)

## What to learn next

- Official documentation: [CISA ransomware resources](https://www.cisa.gov/stopransomware)
- Manual or specification: [NIST SP 800-34 contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/final)
- Maintainer or personal blog: [Troy Hunt blog](https://www.troyhunt.com/)
- Technical blog: [Google Cloud threat intelligence](https://cloud.google.com/blog/topics/threat-intelligence)
- Hands-on guide: [CISA ransomware guide](https://www.cisa.gov/stopransomware/ransomware-guide)
