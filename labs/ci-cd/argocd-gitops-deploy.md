---
title: "ArgoCD: деплой Helm-чарта из Git вместо ручного helm upgrade"
theme: "ci-cd"
difficulty: "middle"
question_ref: "ci-cd/gitops-pull-versus-push-delivery.md"
tags: [ci-cd, kubernetes, argo-cd, gitops, deployment, git, delivery]
why: "ArgoCD is a hard requirement in efin A-tier vacancies and GitOps is a frequent senior interview topic. This lab teaches pull-based deployment and drift thinking rather than mere tool installation, closing the gap between running helm upgrade by hand and declarative delivery where Git is the single source of truth."
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

# Lab: ArgoCD — деплой Helm-чарта из Git вместо ручного helm upgrade

В этой лабораторной вы переводите существующий Helm-чарт (orders-devops) с ручного `helm upgrade` на GitOps-модель: кластер сам подтягивает желаемое состояние из Git через ArgoCD. Лабораторная парная к материалу 12 пака Metalogiya.

## Prerequisites

*   Кластер Kubernetes: ваш k3s-кластер или кubeadm-кластер из лабораторной по CNI (`kubectl get nodes` отвечает `Ready`).
*   Helm-чарт `orders-devops`, выложенный в Git-репозиторий (GitHub/GitLab, доступный с кластера по https).
*   Установленные локально `kubectl` и `helm`; доступ к nodes через SSH.
*   Storage-class, на который ссылается чарт (Local Path Provisioner в k3s подходит).

Ключевая документация: https://argo-cd.readthedocs.io/en/stable/ и https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/

## Exercise 1: установка ArgoCD и доступ к UI/API

1. Создайте namespace и примените официальный манифест:
    ```bash
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```
2. Дождитесь, пока все поды `argocd-*` станут `Running`:
    ```bash
    kubectl get pods -n argocd -w
    ```
3. Получите initial admin password (в k3s secret типа `Opaque`, пароль — поле `admin.password`):
    ```bash
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo
    ```
4. Откройте UI через port-forward (локально, без exposure наружу):
    ```bash
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```
5. Войдите в UI (admin / пароль) и проверьте API тем же паролем:
    ```bash
    argocd login localhost:8080 --username admin --insecure
    argocd app list
    ```

## Exercise 2: подключение репозитория и Application с auto-sync

1. Зарегистрируйте репозиторий с чартом (публичный репозиторий; для приватного — HTTPS-credentials или deploy key):
    ```bash
    argocd repo add https://github.com/<you>/orders-devops.git --type git
    argocd repo list
    ```
2. Создайте Application из Helm-чарта. Сохраните манифест в Git (это тоже часть источника истины), затем примените:
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
        server: https://<cluster-api>  # внутри кластера это стандартный адрес kubernetes.default.svc
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
3. Добейтесь статуса `Healthy` и `Synced`; проверьте, что ресурсы появились:
    ```bash
    kubectl get all -n orders
    ```
4. Ответьте себе: где здесь desired state, а где live state? Что делает `prune: true`?

## Exercise 3: изменение в Git → автодеплой → проверка в кластере

1. Не запуская `helm upgrade`, внесите изменение в Git: например, поднимите `replicaCount` или смените тег образа в `values.yaml`, закоммитьте и запушьте.
2. Понаблюдайте, как ArgoCD замечает новый коммит (polling или webhooks):
    ```bash
    argocd app get orders-devops --watch
    ```
3. Проверьте, что изменение применилось в кластере:
    ```bash
    kubectl get deploy -n orders -o wide
    kubectl rollout status deploy/<chart-deployment> -n orders
    ```
4. Зафиксируйте время от push до применения — это ваш delivery latency без единого ручного шага.

## Exercise 4: drift — ручное изменение и возврат состояния

1. Сломайте желаемое состояние руками:
    ```bash
    kubectl scale deploy/<chart-deployment> -n orders --replicas=1
    ```
2. Посмотрите diff и дождитесь, пока `selfHeal: true` вернёт реплики:
    ```bash
    argocd app diff orders-devops
    kubectl get deploy -n orders -w
    ```
3. Удалите ресурс (например, Service) и убедитесь, что ArgoCD пересоздал его.
4. Теперь критическая часть — когда auto-heal это плохо:
    *   Во время инцидента оператор применил экстренный фикс `kubectl edit`/`kubectl patch` в кластере. Что произойдёт с этим фиксом при `selfHeal: true`, и как правильно сделать экстренный фикс durable? (Правильный ответ: немедленно закоммитить то же изменение в Git.)
    *   Включите `manual` sync: уберите блок `automated` из Application, повторите ручное изменение и убедитесь, что ArgoCD показывает `OutOfSync`, но ничего не откатывает.
    *   Сформулируйте политику: для каких окружений (prod/stage/dev) вы бы оставили auto-sync, а для каких — manual и почему. Сверьтесь с https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/

## Exercise 5: sync-waves и pre-sync hooks

1. Добавьте в шаблон чарта Job миграции БД с hook-аннотациями:
    ```yaml
    metadata:
      annotations:
        argocd.argoproj.io/hook: PreSync
        argocd.argoproj.io/hook-delete-policy: HookSucceeded
    ```
2. Аннотируйте остальные ресурсы волнами: `argocd.argoproj.io/sync-wave: "0"` для Namespace/CRD, `"1"` для Deployment/Service, `"2"` для тестового Job.
3. Сделайте коммит, запустите sync и проверьте порядок выполнения:
    ```bash
    argocd app sync orders-devops
    kubectl get jobs -n orders
    ```
4. Проверьте в UI (Sync window / resource view), что миграция выполнилась до Deployment.

## Exercise 6: контрольные вопросы (без подглядывания)

1. **App-of-apps:** что это за паттерн, как выглядит корневое Application, указывающее на папку с другими Application, и какую проблему централизованного управления это решает? (Справка: https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/)
2. **Pull vs push:** чем GitOps-pull (ArgoCD) отличается от CI-push (helm upgrade из pipeline)? Кто держит credentials кластера в каждой модели?
3. **Источник истины:** почему в GitOps-модели нельзя считать источником истины вывод `kubectl get`? К чему приводит ручной `kubectl apply` поверх GitOps-приложения?
4. **Rollback:** почему в GitOps откат релиза — это `git revert`, а не `kubectl rollout undo`? Что произойдёт с `rollout undo` при `selfHeal: true`?

## Что должно получиться

*   Работающее приложение, развернутое без единого `helm upgrade` после настройки.
*   Демонстрация drift-detection и self-heal на живом кластере.
*   Pre-sync hook с миграцией, выполняющийся до основного Deployment.
*   Устные ответы на четыре вопроса Exercise 6 — по формату собеседования (efin A-tier спрашивает ArgoCD обязательно).
