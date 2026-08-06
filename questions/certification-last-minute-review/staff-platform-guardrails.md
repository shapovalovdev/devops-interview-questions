---
title: Design platform guardrails that retain team autonomy
theme: certification-last-minute-review
difficulty: staff
type: theory
tags: [kubernetes, platform-engineering, security, governance, reliability, cks]
sources:
  - url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design platform guardrails that retain team autonomy

Which Kubernetes controls should become platform defaults rather than review comments?

## Answer guide

- Make the safe path easy: provide namespace templates, scoped identities, resource defaults, network policy patterns, observability, and documented deployment interfaces. Defaults reduce repeated decisions without removing application ownership.
- Enforce only high-confidence, broadly applicable boundaries through admission policy, for example prohibited privileged settings or required labels. Roll out in audit or warn mode first and maintain an exception process with expiry and accountable approval.
- Measure both risk reduction and developer experience. A guardrail that causes opaque deployment failure encourages bypasses; surface an actionable message, a remediation example, and an escalation route.

## References

- [Kubernetes: Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- Further reading (blog): [Niels de Graaf — platform engineering](https://niels-degraaf.com/2023/01/11/platform-engineering.html)

## What to learn next

- Official documentation: [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- Manual or specification: [Kubernetes admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
- Maintainer or personal blog: [Niels de Graaf — platform engineering](https://niels-degraaf.com/2023/01/11/platform-engineering.html)
- Technical blog: [CNCF — platform engineering](https://www.cncf.io/blog/2023/08/30/platform-engineering-what-is-it-and-why-is-it-important/)
- Hands-on guide: [Kubernetes ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
