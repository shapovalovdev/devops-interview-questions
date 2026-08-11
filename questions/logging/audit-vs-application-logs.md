---
title: Distinguish audit logs from application logs
theme: logging
difficulty: middle
type: theory
tags: [logging, security, governance, incident-response]
sources:
  - url: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish audit logs from application logs

Why should audit events not be treated as ordinary application diagnostics?

## Answer guide

- Audit logs answer who performed a security- or business-relevant action, on which object, when, from where, and whether it succeeded. Application logs primarily explain runtime behavior. Both may share transport, but audit semantics, integrity, access, and retention requirements are usually stricter.
- Define audit event schemas and failure behavior before implementation. Include authenticated principal and authorization decision without recording credentials, use server-side time and actor attribution, and avoid allowing a caller to supply the authoritative audit identity.
- Protect the pipeline from alteration and make missing events detectable. Restricted query access, append-oriented storage, separate administrative duties, and monitoring of collectors help; they do not make an audit log automatically tamper-proof, especially across compromised systems.

## References

- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Further reading (blog): [Google Cloud: audit logs](https://cloud.google.com/logging/docs/audit)

## What to learn next

- Official documentation: [Kubernetes audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- Manual or specification: [NIST SP 800-92 Rev. 1 (initial public draft) — guide to computer security log management](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [Google Cloud audit logs](https://cloud.google.com/logging/docs/audit)
- Hands-on guide: [AWS CloudTrail user guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
