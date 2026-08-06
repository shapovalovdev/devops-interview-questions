---
title: Verify signed commits and release tags
theme: version-control
difficulty: senior
type: scenario
tags: [git, version-control, security, delivery, supply-chain]
sources:
  - url: https://git-scm.com/docs/git-verify-commit
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/git-verify-tag
    source_type: official-docs
    verified_on: 2026-08-06
---

# Verify signed commits and release tags

How would you use signed Git objects in a release process, and what do they prove or not prove?

## Answer guide

- Signed commits and annotated tags let Git verify that a trusted signing key made the signature over that object. Configure trust and key distribution deliberately, then verify the release tag and the commit it identifies in CI or release automation.
- Bind release approval to a protected tag, immutable commit ID, build provenance, and artifact digest. Rotate or revoke keys through an auditable process and investigate failed or unknown signatures before release.
- A valid signature proves control of a signing key at signing time, not that the change is safe, reviewed, non-malicious, or reproducibly built. It must complement code review, CI, branch protection, and artifact verification.
- Avoid accepting any cryptographically valid key without identity and authorization policy. Compromised keys or broad trust settings turn signature checks into false assurance.

## References

- [Git documentation: git-verify-commit](https://git-scm.com/docs/git-verify-commit)
- [Git documentation: git-verify-tag](https://git-scm.com/docs/git-verify-tag)
- Further reading (blog): [GitHub Docs — commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)

## What to learn next

- Official documentation: [Git: git-verify-commit](https://git-scm.com/docs/git-verify-commit)
- Manual or specification: [Pro Git: signing your work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
- Maintainer or personal blog: [Julia Evans — cryptography](https://jvns.ca/blog/2022/10/17/what-is-cryptography/)
- Technical blog: [GitHub Docs — verified signatures](https://docs.github.com/en/authentication/managing-commit-signature-verification)
- Hands-on guide: [Git: git-tag signing](https://git-scm.com/docs/git-tag#Documentation/git-tag.txt--s)
