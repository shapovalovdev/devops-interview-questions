---
title: Establish data governance architecture
theme: backend-architecture
difficulty: staff
type: scenario
tags: [security, governance, databases]
sources:
  - url: https://www.nist.gov/privacy-framework
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish data governance architecture

What architecture decisions make data handling auditable and safe as a backend grows?

## Answer guide

- Inventory data classes, owners, purpose, retention, residency, access paths, and deletion requirements before selecting storage. Make classification and lifecycle enforcement part of service interfaces, event schemas, backups, analytics, and operational tooling.
- Apply least privilege, encryption where appropriate, audit trails, and regular access review, while making the data subject or business lifecycle executable. Define governance metrics and an incident process for exposure, deletion failure, and incorrect retention.
- A policy document alone does not remove data from replicas, queues, logs, or backups. Over-collecting identifiers complicates every future migration; test a deletion and access-revocation request end to end across all copies.

## References

- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- Further reading (blog): [GitHub: data privacy engineering](https://github.blog/security/privacy/)

## What to learn next

- Official documentation: [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- Manual or specification: [NIST SP 800-53 Rev. 5 security and privacy controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [GitHub Security Lab](https://github.blog/security/)
- Hands-on guide: [OWASP data protection cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
