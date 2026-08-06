---
title: Explain Kyverno policy-engine fundamentals
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, security, policy-as-code, kyverno, kca]
sources:
  - url: https://kyverno.io/docs/introduction/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Kyverno policy-engine fundamentals

What is Kyverno, where does it evaluate Kubernetes configuration, and when would you choose validation, mutation, generation, or image verification?

## Answer guide

- Kyverno is a policy engine whose policies are declarative resources. In Kubernetes it can participate in admission processing and can also evaluate configuration through its tooling and background controllers. A strong answer distinguishes an admission decision before persistence from later background processing; neither is a substitute for authentication, authorization, or a secure delivery process.
- Use validation to accept or reject nonconforming resources, mutation to apply safe defaults, generation to create or synchronize dependent resources, and image verification to enforce supply-chain requirements. Define the resource scope, expected state, owner, and policy mode before choosing one; mutation that hides an application defect or generation that creates uncontrolled cross-namespace resources is a poor default.
- Start with observable, tested policies and a narrow rollout. Admission failures can block deployments, policy scope can unexpectedly include controller-created resources, and a policy engine cannot compensate for overly broad RBAC or an unavailable control plane. Document exceptions and recovery before enforcement.

## References

- [Kyverno introduction and policy-management capabilities](https://kyverno.io/docs/introduction/)
- [Kyverno validating-policy documentation](https://kyverno.io/docs/policy-types/validating-policy/)
- [Kubernetes admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
- Further reading (blog): [Kyverno community blog](https://kyverno.io/blog/)

## What to learn next

- Official documentation: [How Kyverno works](https://kyverno.io/docs/introduction/how-kyverno-works/)
- Official documentation: [Kyverno CLI apply](https://kyverno.io/docs/kyverno-cli/reference/kyverno_apply/)
- Manual or specification: [Kubernetes dynamic admission control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
- Maintainer or personal blog: [Nirmata engineering blog — Kyverno](https://nirmata.com/blog/)
- Free learning material: [Kyverno policy library](https://kyverno.io/policies/)
