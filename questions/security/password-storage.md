---
title: Store application passwords safely
theme: security
difficulty: junior
type: theory
tags: [security, least-privilege]
sources:
  - url: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Store application passwords safely

How should an application store user passwords, and why is encryption alone not the answer?

## Answer guide

- Store a password verifier produced by a purpose-built, salted, adaptive password-hashing function; do not store the plaintext or a fast general hash.
- A one-way verifier lets the service check a login without needing the original password. A unique salt prevents one precomputed attack from serving every account, while cost settings make guesses expensive.
- Choose parameters appropriate for the service and revisit them as hardware changes; migrate a verifier on the next successful login when parameters change.
- Reversible encryption creates a key-management problem and exposes every password if that key is recovered. Rate-limit authentication and protect reset flows because a strong hash does not stop online guessing.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST SP 800-63B: Authentication](https://pages.nist.gov/800-63-3/sp800-63b.html)
