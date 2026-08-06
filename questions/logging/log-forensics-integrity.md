---
title: Preserve log integrity for an investigation
theme: logging
difficulty: senior
type: scenario
tags: [logging, security, incident-response, governance]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/92/final
    source_type: official-docs
    verified_on: 2026-08-06
---

# Preserve log integrity for an investigation

What controls make logs more trustworthy during a security investigation?

## Answer guide

- Separate producers from log administration, authenticate collection endpoints, encrypt transport, and restrict mutation and query permissions. Record collector and pipeline health so investigators can distinguish "no event occurred" from "the source or path was unavailable."
- Preserve source identity, event time, receive time, and transformation history where possible. Append-oriented storage, immutable retention options, signed exports, and controlled access improve evidentiary value, but none prove a compromised producer reported truthfully.
- Define a response procedure for legal hold and export: capture relevant scope, hashes and access history, minimize exposure of unrelated personal data, and document every handoff. Test the procedure before an incident; a backup that cannot be located or verified is weak evidence.

## References

- [NIST SP 800-92: log management](https://csrc.nist.gov/pubs/sp/800/92/final)
- Further reading (blog): [AWS: immutable logging](https://aws.amazon.com/blogs/storage/how-to-protect-data-using-amazon-s3-object-lock/)

## What to learn next

- Official documentation: [AWS S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- Manual or specification: [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [AWS immutable logging](https://aws.amazon.com/blogs/storage/how-to-protect-data-using-amazon-s3-object-lock/)
- Hands-on guide: [OpenSearch security](https://docs.opensearch.org/latest/security/)
