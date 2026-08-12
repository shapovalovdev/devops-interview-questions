---
title: Explain the four GitOps principles
theme: ci-cd
difficulty: junior
type: theory
tags: [ci-cd, git, kubernetes, deployment, delivery, automation]
sources:
  - url: https://opengitops.dev/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md
    source_type: standard
    verified_on: 2026-08-12
---

# Explain the four GitOps principles

Name the four principles that OpenGitOps v1.0.0 uses to define a GitOps-managed system, and say what a team is still missing if it satisfies only some of them.

## Answer guide

- The four principles are: the desired state is **declarative**; that desired state is stored **versioned and immutable**, with a complete version history; software agents **pull** the desired state automatically; and those agents **continuously reconcile** the actual system toward it. Together they describe a managed software system, not a product you buy.
- Mechanically, the declarative description says what the outcome should be rather than the steps to reach it, so the same description can be applied repeatedly. Immutable versioning gives every state a retrievable identifier, which is what makes rollback "apply an earlier version" instead of "run a compensating script". Pulling moves the credentials and the decision to apply into the agent, and continuous reconciliation means correctness is restored on a loop rather than only at the moment of a deploy.
- Constraints worth stating: v1.0.0 says *state store*, not Git, and says nothing about Kubernetes, so an OCI registry-backed store or a non-Kubernetes target can still be GitOps. The principles also say nothing about how the desired state is produced — continuous integration, testing, image building, and review policy all remain separate concerns — and they grant no authorization or secret-handling model on their own.
- Common partial adoptions and what each still costs: a pipeline that runs `kubectl apply` from CI is declarative and versioned but not pulled, so CI holds production credentials and nothing corrects drift between runs; a repository whose environment files are edited in place loses immutability, so the deployed version is not reproducible; and an agent with automatic synchronization switched off detects drift but never closes it, leaving a cluster that silently diverges while the dashboard still shows the intended commit.

## References

- [OpenGitOps: GitOps principles and the GitOps Working Group](https://opengitops.dev/)
- [OpenGitOps: GitOps Principles v1.0.0](https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md)
- Further reading (blog): [GitLab — what GitOps is and where it fits](https://about.gitlab.com/topics/gitops/)

## What to learn next

- Official documentation: [OpenGitOps project site](https://opengitops.dev/)
- Manual or specification: [OpenGitOps glossary of terms](https://github.com/open-gitops/documents/blob/main/GLOSSARY.md)
- Maintainer or personal blog: [Argo project maintainers' blog](https://blog.argoproj.io/)
- Technical blog: [GitLab — GitOps topic guide](https://about.gitlab.com/topics/gitops/)
- Hands-on guide: [Flux: get started](https://fluxcd.io/flux/get-started/)
