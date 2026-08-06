---
title: Establish Kubernetes admission policy guardrails
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, governance, automation]
sources:
  - url: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish Kubernetes admission policy guardrails

How would you prevent unsafe workload manifests without making every delivery change a platform-team ticket?

## Answer guide

- Admission control runs after authentication and authorization and can validate, mutate, or reject API requests before persistence.
- Start with clear, testable requirements such as disallowing privileged containers, requiring resource controls, or restricting registries; publish exceptions and ownership.
- Use Kubernetes-supported admission mechanisms and stage policies in audit or warn modes when available before enforcing them, with CI checks to give developers fast feedback.
- A broken or unavailable webhook can affect the API path according to its failure policy; make the policy service highly available and avoid non-deterministic external dependencies.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
- [Kubernetes: Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
