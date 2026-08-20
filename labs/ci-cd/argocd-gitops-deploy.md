---
title: "ArgoCD: deploying a Helm chart from Git instead of a hand-run helm upgrade"
theme: "ci-cd"
difficulty: "middle"
question_ref: "ci-cd/gitops-pull-versus-push-delivery.md"
tags: [ci-cd, kubernetes, argo-cd, gitops, deployment, git, delivery]
why: "ArgoCD is a hard requirement in many senior platform roles and GitOps is a frequent senior interview topic. This lab teaches pull-based deployment and drift thinking rather than mere tool installation, closing the gap between running helm upgrade by hand and declarative delivery where Git is the single source of truth."
checklist:
  - "Install ArgoCD into the cluster and reach the UI/API with the initial admin password."
  - "Connect the Git repository holding the orders-devops Helm chart as an ArgoCD repo."
  - "Create an Application from the chart with automated sync and pruning enabled."
  - "Commit a change (image tag or replicaCount) to Git and verify the cluster converges without running helm upgrade."
  - "Mutate a live resource with kubectl and watch ArgoCD restore it; then explain when auto-heal hurts."
  - "Switch the Application to a manual sync policy and back, explaining the tradeoff."
  - "Add a pre-sync hook Job (migration) and a sync-wave annotation; verify execution order."
  - "Answer the app-of-apps question and the three pull-vs-push questions without notes."
---

# Lab: ArgoCD — deploying a Helm chart from Git instead of a hand-run helm upgrade

In this lab you move an existing Helm chart (orders-devops) off a hand-run `helm upgrade` and onto a GitOps model: the cluster pulls its desired state from Git through ArgoCD.

## Prerequisites

*   A Kubernetes cluster: your k3s cluster, or the kubeadm cluster from the CNI lab (`kubectl get nodes` answers `Ready`).
*   The `orders-devops` Helm chart, published to a Git repository (GitHub/GitLab, reachable from the cluster over https).
*   `kubectl` and `helm` installed locally; SSH access to the nodes.
*   The storage class the chart refers to (the Local Path Provisioner in k3s will do).

Key documentation: https://argo-cd.readthedocs.io/en/stable/ and https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/

## Exercise 1: install ArgoCD and reach the UI/API

1. Create the namespace and apply the official manifest:
    ```bash
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```
2. Wait until every `argocd-*` pod is `Running`:
    ```bash
    kubectl get pods -n argocd -w
    ```
3. Get the initial admin password (an `Opaque` secret in k3s; the password is the `admin.password` field):
    ```bash
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo
    ```
4. Open the UI through a port-forward (locally, with nothing exposed outwards):
    ```bash
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```
5. Log in to the UI (admin / the password) and check the API with the same password:
    ```bash
    argocd login localhost:8080 --username admin --insecure
    argocd app list
    ```

## Exercise 2: connect the repository and create an Application with auto-sync

1. Register the repository holding the chart (a public repository; for a private one use HTTPS credentials or a deploy key):
    ```bash
    argocd repo add https://github.com/<you>/orders-devops.git --type git
    argocd repo list
    ```
2. Create an Application from the Helm chart. Keep the manifest in Git too — it is part of the source of truth — then apply it:
    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: orders-devops
      namespace: argocd
    spec:
      project: default
      source:
        repoURL: https://github.com/<you>/orders-devops.git
        targetRevision: main
        path: charts/orders-devops
        helm:
          valueFiles:
            - values.yaml
      destination:
        server: https://<cluster-api>  # inside the cluster this is the standard kubernetes.default.svc address
        namespace: orders
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
          - CreateNamespace=true
    ```
    ```bash
    kubectl apply -f orders-devops-app.yaml
    argocd app get orders-devops
    ```
3. Get to `Healthy` and `Synced`, then check the resources appeared:
    ```bash
    kubectl get all -n orders
    ```
4. Answer for yourself: which part here is the desired state and which is the live state? What does `prune: true` do?

## Exercise 3: a change in Git -> automatic deploy -> verification in the cluster

1. Without running `helm upgrade`, make a change in Git: raise `replicaCount`, say, or change the image tag in `values.yaml`, then commit and push.
2. Watch ArgoCD notice the new commit (by polling or by webhook):
    ```bash
    argocd app get orders-devops --watch
    ```
3. Check the change reached the cluster:
    ```bash
    kubectl get deploy -n orders -o wide
    kubectl rollout status deploy/<chart-deployment> -n orders
    ```
4. Record the time from push to applied — that is your delivery latency with not one manual step in it.

## Exercise 4: drift — a manual change, and the state returning

1. Break the desired state by hand:
    ```bash
    kubectl scale deploy/<chart-deployment> -n orders --replicas=1
    ```
2. Look at the diff and wait for `selfHeal: true` to bring the replicas back:
    ```bash
    argocd app diff orders-devops
    kubectl get deploy -n orders -w
    ```
3. Delete a resource (the Service, say) and confirm ArgoCD recreates it.
4. Now the critical part — when auto-heal is the wrong thing:
    *   During an incident an operator applies an emergency fix in the cluster with `kubectl edit`/`kubectl patch`. What happens to that fix under `selfHeal: true`, and how do you make an emergency fix durable? (The right answer: commit the same change to Git immediately.)
    *   Switch to `manual` sync: remove the `automated` block from the Application, repeat the manual change, and confirm ArgoCD reports `OutOfSync` but reverts nothing.
    *   State a policy: which environments (prod/stage/dev) you would leave on auto-sync and which on manual, and why. Check yourself against https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/

## Exercise 5: sync waves and pre-sync hooks

1. Add a database-migration Job to the chart templates, with the hook annotations:
    ```yaml
    metadata:
      annotations:
        argocd.argoproj.io/hook: PreSync
        argocd.argoproj.io/hook-delete-policy: HookSucceeded
    ```
2. Annotate the remaining resources into waves: `argocd.argoproj.io/sync-wave: "0"` for Namespace/CRD, `"1"` for Deployment/Service, `"2"` for the test Job.
3. Commit, run a sync, and check the order things ran in:
    ```bash
    argocd app sync orders-devops
    kubectl get jobs -n orders
    ```
4. Confirm in the UI (sync window / resource view) that the migration ran before the Deployment.

## Exercise 6: check questions (no peeking)

1. **App-of-apps:** what is the pattern, what does a root Application pointing at a folder of other Applications look like, and which central-management problem does it solve? (Reference: https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/)
2. **Pull vs push:** how does GitOps pull (ArgoCD) differ from CI push (a `helm upgrade` from the pipeline)? Who holds the cluster credentials in each model?
3. **Source of truth:** why can the output of `kubectl get` not be the source of truth in a GitOps model? What does a hand-run `kubectl apply` over a GitOps application lead to?
4. **Rollback:** why is rolling a release back in GitOps a `git revert` rather than a `kubectl rollout undo`? What happens to `rollout undo` under `selfHeal: true`?

## What you should end up with

*   A working application, deployed without a single `helm upgrade` after the initial setup.
*   A demonstration of drift detection and self-heal on a live cluster.
*   A pre-sync hook carrying the migration, running before the main Deployment.
*   Spoken answers to the four questions in Exercise 6, in interview format (ArgoCD is a required topic for GitOps roles).
