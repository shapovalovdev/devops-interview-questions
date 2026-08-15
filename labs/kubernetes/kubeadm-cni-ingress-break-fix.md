---
title: "Kubernetes break-fix: kubeadm-кластер и диагностика CNI/ingress"
theme: "kubernetes"
difficulty: "middle"
question_ref: "kubernetes/node-not-ready-triage.md"
tags: [kubernetes, cni, networking, certificates, troubleshooting, fault-injection]
why: "Kubernetes appears in all eight target vacancies, and interviewers distinguish 'used k3s' from 'can repair a cluster'. This break-fix lab drills diagnosis through kubectl describe, logs, and events, plus control-plane understanding (etcd, apiserver, certificates), rather than deployment alone."
checklist:
  - "Стенд поднят: 1 control-plane + минимум 1 worker, все узлы Ready, CNI-подузы Running."
  - "Тестовое приложение задеплоено и доступно через ingress с рабочим endpoint."
  - "Сценарий 1 пройден: CNI-падение диагностировано через kubectl describe node + events, узел возвращён в Ready."
  - "Сценарий 2 пройден: mismatch pod-cidr найден (flannel / cilium config vs kubeadm), cross-node ping/curl восстановлен."
  - "Сценарий 3 пройден: selector typo найден через kubectl describe svc/endpoints, ingress отдаёт 200."
  - "Сценарий 4 пройден: причина падения apiserver после ребута названа и устранена, кластер отвечает."
  - "Сценарий 5 пройден: kubeadm certs check-expiration выполнен, сертификаты продлены, кластер жив после рестарта."
  - "Каждая диагностика проговорена вслух: candidate narrates kubectl describe / logs / events до применения фикса."
  - "Ментор ломал стенд break-командами из Phase 1 leashed-скрипта, а кандидат чинил без подсказок (макс 1 подсказка на сценарий)."
  - "Защита: на вопрос 'что случится с кластером, если упадёт etcd / истечёт apiserver-сертификат' дан корректный ответ с объяснением цепочки kubelet→apiserver→etcd."
---

# Lab: Kubernetes break-fix — kubeadm-кластер и диагностика CNI/ingress

Формат: ментор («хаос-мастер») инжектит аварию break-командами из раздела «Break-команды (Phase 1, leashed)», кандидат чинит, проговаривая диагностику вслух. Один сценарий = одна авария = один фикс. После каждого фикса — verify-шаг и возврат к известному-good состоянию через restore-команду.

## Prerequisites

*   **Хост:** VirtualBox (или другой гипервизор): 1 VM control-plane (2 CPU / 2–4 GB RAM) + 1–2 VM worker (1–2 CPU / 2 GB), Ubuntu 22.04 LTS. Допустимы nested-VM на рабочем ноутбуке или 3 уже существующие VM.
*   **Сеть:** VM видят друг друга по внутреннему хостнейму/IP; на control-plane открыт 6443/tcp; pod-cidr не пересекается с сетью VM.
*   **ПО:** containerd, kubeadm/kubelet/kubectl одной минорной версии (1.28–1.30), helm 3 (для ingress-nginx).
*   **Навыки кандидата:** prod Ansible/Linux — да; K8s — pet-level k3s. Лаба закрывает gap «умеет чинить кластер».

## Setup (выполняет кандидат, ~60–90 мин)

1. На всех VM: установить containerd + kubeadm/kubelet/kubectl, включить `br_netfilter`, `net.ipv4.ip_forward=1`, выключить swap.
2. На control-plane:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=<CP_IP>
   mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   ```
3. CNI — flannel (проще для break-fix) или cilium:
   ```bash
   kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
   ```
4. Join worker-узлов командой из вывода `kubeadm init` (или `kubeadm token create --print-join-command`).
5. Ingress + тестовое приложение:
   ```bash
   helm install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
   kubectl create deployment web --image=nginx --replicas=2
   kubectl expose deployment web --port=80
   kubectl apply -f - <<'EOF'
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: web
   spec:
     ingressClassName: nginx
     rules:
     - host: web.lab.local
       http:
         paths:
         - path: /
           pathType: Prefix
           backend:
             service:
               name: web
               port:
                 number: 80
   EOF
   ```
6. Verify: `kubectl get nodes` — все Ready; `curl -H "Host: web.lab.local" http://<CP_IP>:<INGRESS_NODEPORT>` — 200.

## Break-команды (Phase 1, leashed — запускает ментор)

> Ментор выполняет ровно один break перед сценарием, дожидается проявления симптома и передаёт стенд кандидату. `set -e` не нужен: каждый блок независим.

*   **Break 1 (CNI pod down → NotReady):**
  ```bash
  kubectl -n kube-flannel scale deploy/kube-flannel --replicas=0
  ```
*   **Break 2 (pod-cidr mismatch):** на control-plane отредактировать kube-flannel DaemonSet:
  ```bash
  kubectl -n kube-flannel set env ds/kube-flannel FLANNELD_IFACE=lo   # трафик подов уходит в loopback
  # альтернатива без патча манифеста: закомментировать net-conf.json Network в cm kube-flannel-cfg нельзя,
  # поэтому вариант Б — сузить cidr в ConfigMap kube-flannel-cfg на 10.244.0.0/24 и удалить поды flannel
  kubectl -n kube-flannel rollout restart ds/kube-flannel
  ```
*   **Break 3 (ingress без endpoint):**
  ```bash
  kubectl patch svc web -p '{"spec":{"selector":{"app":"web-broken"}}}'
  ```
*   **Break 4 (etcd/apiserver после ребута):** на control-plane — swap включается загрузчиком, kubelet не стартует:
  ```bash
  sudo swapoff -a && sudo sed -i.bak 's/^#\?\/swap/\//swap/' /etc/fstab   # (не ломает; подготовка)
  sudo systemctl mask etcd.service 2>/dev/null || true
  sudo systemctl stop containerd && sudo systemctl start containerd
  # сам break: включаем swap обратно и ребутаем — kubelet падает, static pods (apiserver/etcd) не поднимаются
  sudo sed -i.bak 's|^#\?/swap|/swap|' /etc/fstab && sudo swapon -a && sudo reboot
  ```
  Примечание: если swap уже выключен полностью, альтернативный break 4 — `sudo mv /etc/kubernetes/manifests/etcd.yaml /root/` (apiserver теряет datastore).
*   **Break 5 (cert expiry):**
  ```bash
  # симуляция: подсунуть протухший ca/client-cert нельзя бесплатно, поэтому датированная симуляция:
  sudo cp -r /etc/kubernetes/pki /root/pki.bak
  sudo touch -t 202401010000 /etc/kubernetes/pki/apiserver.crt /etc/kubernetes/pki/apiserver.key
  sudo crictl rmf $(sudo crictl ps -q --name kube-apiserver) || true   # apiserver пересоздастся и упадёт на expired cert
  ```

## Exercises (симптом → диагностика → фикс → verify)

### Сценарий 1: CNI pod down → узел NotReady

*   **Symptom:** `kubectl get nodes` показывает worker(s) `NotReady`; новые поды висят в `ContainerCreating`.
*   **Diagnosis (narrated):**
    1. `kubectl get nodes` → condition `Ready=False, KubeletNotReady, runtime network not ready`.
    2. `kubectl get pods -n kube-flannel -o wide` → поды flannel отсутствуют/0 replicas.
    3. `kubectl -n kube-flannel describe deploy kube-flannel` → `replicas: 0` (кто-то отскейлил).
    4. `kubectl describe node <worker> | tail -20` → events `NetworkPluginNotReady`.
*   **Fix:** `kubectl -n kube-flannel scale deploy/kube-flannel --replicas=<было>`.
*   **Verify:** через ~1 мин узлы `Ready`; тестовый под с `nodeSelector` на worker стартует; `kubectl get pods -A` без CrashLoop.

### Сценарий 2: wrong pod-cidr / CNI config mismatch → cross-node трафик не ходит

*   **Symptom:** curl с пода на worker-1 к поду на worker-2 (или к ClusterIP svc) таймаутится; в пределах узла — работает.
*   **Diagnosis:**
    1. Запустить два debug-пода с pin к разным узлам (`kubectl run test1 --image=nginx --overrides='{"spec":{"nodeSelector":{"kubernetes.io/hostname":"<w1>"}}}'`).
    2. `kubectl get pods -o wide` → записать pod IP обоих; `kubectl exec test1 -- curl -m2 <podIP2>` → timeout.
    3. `ip route` внутри нод: проверить, что маршрут `10.244.0.0/16` (или /24 после break) через flannel.1 присутствует на обоих узлах.
    4. `kubectl -n kube-flannel get cm kube-flannel-cfg -o yaml | grep -A2 Network` → cidr не совпадает с `--pod-network-cidr` из kubeadm (или iface=lo).
*   **Fix:** вернуть корректный cidr/interface в ConfigMap/DS (`kubectl -n kube-flannel set env ds/kube-flannel FLANNELD_IFACE=<REAL_IFACE>` или откат cm) и `kubectl -n kube-flannel rollout restart ds/kube-flannel`.
*   **Verify:** `kubectl exec test1 -- curl -m2 <podIP2>` → 200; маршруты на обоих узлах снова /16 через flannel.1.

### Сценарий 3: ingress controller без endpoint (selector typo)

*   **Symptom:** `curl -H "Host: web.lab.local" ...` → 503 от ingress-nginx (upstream unavailable).
*   **Diagnosis:**
    1. `kubectl get ingress web` → адрес есть, backend описан.
    2. `kubectl describe ingress web` → endpoints: `<none>` или пусто.
    3. `kubectl get endpoints web` → пустой; `kubectl describe svc web` → `Selector: app=web-broken`, а у подов `kubectl get pods -l app=web --show-labels` лейбл `app=web`.
    4. `kubectl -n ingress-nginx logs deploy/ingress-nginx-controller | grep -i upstream` → no endpoints available.
*   **Fix:** `kubectl patch svc web -p '{"spec":{"selector":{"app":"web"}}}'`.
*   **Verify:** `kubectl get endpoints web` показывает IP подов; curl → 200.

### Сценарий 4: etcd-под не отвечает / apiserver не стартует после перезагрузки

*   **Symptom:** после `reboot` control-plane `kubectl get nodes` висит/отдаёт `connection refused` или `The connection to the server ... was refused`.
*   **Diagnosis:**
    1. `systemctl status kubelet` → failed; `journalctl -u kubelet -e --no-pager | grep -iE 'swap|failed'` → kubelet требует выключённый swap.
    2. `sudo crictl ps` → нет static pod'ов apiserver/etcd/controller/scheduler.
    3. `free -h` → swap включён; `/etc/kubernetes/manifests/` → манифесты на месте (значит проблема в kubelet, не в etcd).
    4. (вариант с mv etcd.yaml) `kubectl get cs`/`crictl logs <apiserver>` → etcd cluster unavailable / connection refused 2379.
*   **Fix:** `sudo swapoff -a && sudo sed -i '/swap/d' /etc/fstab && sudo systemctl restart kubelet`; при варианте с манифестом — `sudo mv /root/etcd.yaml /etc/kubernetes/manifests/`.
*   **Verify:** static pods Running (`sudo crictl ps`), `kubectl get nodes` отвечает, все узлы Ready.

### Сценарий 5: certificate expiry на control-plane

*   **Symptom:** `kubectl` отдаёт x509-ошибки (`certificate has expired or is not yet valid`); apiserver-под в CrashLoop/отсутствует.
*   **Diagnosis:**
    1. `sudo kubeadm certs check-expiration` → список с `RESIDUAL LIFE: 0y0m0d` / ca-dependency.
    2. `sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -dates` → notAfter в прошлом.
    3. `sudo crictl logs $(sudo crictl ps -a -q --name kube-apiserver | head -1) 2>&1 | grep -i x509`.
*   **Fix:**
    ```bash
  sudo kubeadm certs renew all
  sudo systemctl restart kubelet   # static pods пересоздадутся с новыми сертификатами
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config   # обновлённый kubeconfig
    ```
    (в лабе: сначала вернуть оригинальные времена из `/root/pki.bak` ИЛИ честно сделать `renew all` — renew работает в обоих случаях).
*   **Verify:** `sudo kubeadm certs check-expiration` → ~364d; `kubectl get nodes` OK; после `sudo reboot` control-plane кластер поднимается сам.

## Restore (известный-good после каждого сценария)

*   Break 1: scale обратно до исходных replicas.
*   Break 2: вернуть cidr/iface в kube-flannel cm/ds + rollout restart.
*   Break 3: patch selector обратно.
*   Break 4: swapoff + fstab + restart kubelet; вернуть etcd.yaml в manifests при варианте Б.
*   Break 5: `sudo rm -rf /etc/kubernetes/pki && sudo cp -r /root/pki.bak /etc/kubernetes/pki && sudo systemctl restart kubelet` (или оставить renew — это валидный фикс).
*   Финальный smoke: `kubectl get nodes` все Ready + curl ingress → 200.

## Защита (вопрос ментору к кандидату)

«Что случится с кластером, если: (а) упадёт один etcd-инстанс из одного (single-master)? (б) истечёт apiserver-сертификат? Опиши цепочку kubelet→apiserver→etcd и как это увидит пользователь kubectl.»

Ожидание: (а) apiserver не сможет читать/писать state — записи упадут, чтения из кэша могут работать частично, поды продолжают работать (data-plane жив), но любые create/update/перезапуски подов невозможны; (б) kubelet и клиенты получат x509-ошибки — по сути управление кластером потеряно при живых workload; лечится `kubeadm certs renew`.
