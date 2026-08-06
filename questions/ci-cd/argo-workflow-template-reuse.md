---
title: Reuse Argo Workflow templates without losing control
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-workflows, capa, automation]
sources:
  - url: https://argo-workflows.readthedocs.io/en/latest/workflow-templates/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reuse Argo Workflow templates without losing control

How should a platform team offer a shared Argo Workflow step for building and scanning images?

## Answer guide

- Publish a versioned WorkflowTemplate or ClusterWorkflowTemplate with explicit parameters and a narrow, documented output contract. Teams can reference it instead of copying YAML, while the platform keeps the implementation in a reviewed location.
- Keep tenant-specific values such as image names, source revisions, and destinations as validated parameters; bind service accounts and namespace permissions according to the caller’s trust boundary.
- Pin or promote template versions rather than changing a shared template unexpectedly. A cluster-scoped template increases blast radius, so test compatibility, preserve rollback options, and audit who can update it.

## References

- [Argo Workflows: WorkflowTemplates](https://argo-workflows.readthedocs.io/en/latest/workflow-templates/)
- Further reading (blog): [GitHub Blog: Reusable workflows](https://github.blog/changelog/2021-10-18-github-actions-reusable-workflows/)
