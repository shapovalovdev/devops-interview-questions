---
title: "Kubernetes break-fix: a kubeadm cluster and CNI/ingress diagnosis"
theme: "kubernetes"
difficulty: "middle"
question_ref: "kubernetes/node-not-ready-triage.md"
tags: [kubernetes, cni, networking, certificates, troubleshooting, fault-injection]
why: "Kubernetes is near-universal in infrastructure roles, and interviewers distinguish 'used k3s' from 'can repair a cluster'. This break-fix lab drills diagnosis through kubectl describe, logs, and events, plus control-plane understanding (etcd, apiserver, certificates), rather than deployment alone."
checklist:
  - "The stand is up: 1 control-plane + at least 1 worker, every node Ready, the CNI pods Running."
  - "A test application is deployed and reachable through the ingress with a working endpoint."
  - "Scenario 1 is done: the CNI failure was diagnosed through kubectl describe node plus events, and the node is back to Ready."
  - "Scenario 2 is done: the pod-cidr mismatch was found (flannel/cilium config against kubeadm), and cross-node ping/curl works again."
  - "Scenario 3 is done: the selector typo was found through kubectl describe svc/endpoints, and the ingress returns 200."
  - "Scenario 4 is done: the reason the apiserver failed after the reboot is named and fixed, and the cluster answers."
  - "Scenario 5 is done: kubeadm certs check-expiration was run, the certificates were renewed, and the cluster survives a restart."
  - "Every diagnosis is narrated aloud: the candidate talks through kubectl describe / logs / events before applying a fix."
  - "The mentor broke the stand with the break commands from the Phase 1 leashed script, and the candidate fixed it unaided (at most 1 hint per scenario)."
  - "Defence: the question 'what happens to the cluster if etcd dies or the apiserver certificate expires' is answered correctly, explaining the kubelet -> apiserver -> etcd chain."
---

# Lab: Kubernetes break-fix — a kubeadm cluster and CNI/ingress diagnosis

The format: a mentor (the "chaos master") injects a failure using the commands in "Break commands (Phase 1, leashed)", and the candidate repairs it while narrating the diagnosis aloud. One scenario = one failure = one fix. Each fix is followed by a verify step and a return to the known-good state through a restore command.

## Prerequisites

*   **Host:** VirtualBox (or another hypervisor): 1 control-plane VM (2 CPU / 2-4 GB RAM) + 1-2 worker VMs (1-2 CPU / 2 GB), Ubuntu 22.04 LTS. Nested VMs on a work laptop are fine, as are 3 VMs you already have.
*   **Network:** the VMs can reach each other by internal hostname/IP; 6443/tcp is open on the control-plane; the pod-cidr does not overlap the VM network.
*   **Software:** containerd, kubeadm/kubelet/kubectl on the same minor version (1.28-1.30), helm 3 (for ingress-nginx).
*   **Candidate skills assumed:** production Ansible/Linux yes; Kubernetes only pet-level k3s. The lab closes the "can repair a cluster" gap.

## Setup (done by the candidate, ~60-90 min)

1. On every VM: install containerd + kubeadm/kubelet/kubectl, enable `br_netfilter` and `net.ipv4.ip_forward=1`, and turn swap off.
2. On the control-plane:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=<CP_IP>
   mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   ```
3. CNI — flannel (simpler for break-fix) or cilium:
   ```bash
   kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
   ```
4. Join the worker nodes with the command from the `kubeadm init` output (or `kubeadm token create --print-join-command`).
5. Ingress + the test application:
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
6. Verify: `kubectl get nodes` — all Ready; `curl -H "Host: web.lab.local" http://<CP_IP>:<INGRESS_NODEPORT>` — 200.

## Break commands (Phase 1, leashed — run by the mentor)

> The mentor runs exactly one break before each scenario, waits for the symptom to appear, and hands the stand to the candidate. `set -e` is not needed: each block is independent.

*   **Break 1 (CNI pod down → NotReady):**
  ```bash
  kubectl -n kube-flannel scale deploy/kube-flannel --replicas=0
  ```
*   **Break 2 (pod-cidr mismatch):** on the control-plane, edit the kube-flannel DaemonSet:
  ```bash
  kubectl -n kube-flannel set env ds/kube-flannel FLANNELD_IFACE=lo   # pod traffic goes to loopback
  # alternative without patching the manifest: net-conf.json Network in cm kube-flannel-cfg cannot be
  # commented out, so option B is to narrow the cidr in ConfigMap kube-flannel-cfg to 10.244.0.0/24
  # and delete the flannel pods
  kubectl -n kube-flannel rollout restart ds/kube-flannel
  ```
*   **Break 3 (ingress with no endpoint):**
  ```bash
  kubectl patch svc web -p '{"spec":{"selector":{"app":"web-broken"}}}'
  ```
*   **Break 4 (etcd/apiserver after a reboot):** on the control-plane, swap is enabled by the bootloader and kubelet will not start:
  ```bash
  sudo swapoff -a && sudo sed -i.bak 's/^#\?\/swap/\//swap/' /etc/fstab   # (harmless; preparation)
  sudo systemctl mask etcd.service 2>/dev/null || true
  sudo systemctl stop containerd && sudo systemctl start containerd
  # the break itself: turn swap back on and reboot -- kubelet fails and the static pods (apiserver/etcd) never come up
  sudo sed -i.bak 's|^#\?/swap|/swap|' /etc/fstab && sudo swapon -a && sudo reboot
  ```
  Note: if swap is already fully off, the alternative break 4 is `sudo mv /etc/kubernetes/manifests/etcd.yaml /root/` (the apiserver loses its datastore).
*   **Break 5 (cert expiry):**
  ```bash
  # simulation: slipping in an expired ca/client cert is not free, so simulate it by back-dating:
  sudo cp -r /etc/kubernetes/pki /root/pki.bak
  sudo touch -t 202401010000 /etc/kubernetes/pki/apiserver.crt /etc/kubernetes/pki/apiserver.key
  sudo crictl rmf $(sudo crictl ps -q --name kube-apiserver) || true   # the apiserver is recreated and fails on the expired cert
  ```

## Exercises (symptom -> diagnosis -> fix -> verify)

### Scenario 1: CNI pod down -> node NotReady

*   **Symptom:** `kubectl get nodes` shows the worker(s) `NotReady`; new pods hang in `ContainerCreating`.
*   **Diagnosis (narrated):**
    1. `kubectl get nodes` -> condition `Ready=False, KubeletNotReady, runtime network not ready`.
    2. `kubectl get pods -n kube-flannel -o wide` -> the flannel pods are missing / 0 replicas.
    3. `kubectl -n kube-flannel describe deploy kube-flannel` -> `replicas: 0` (someone scaled it down).
    4. `kubectl describe node <worker> | tail -20` -> events `NetworkPluginNotReady`.
*   **Fix:** `kubectl -n kube-flannel scale deploy/kube-flannel --replicas=<the original>`.
*   **Verify:** after ~1 min the nodes are `Ready`; a test pod with a `nodeSelector` onto the worker starts; `kubectl get pods -A` shows no CrashLoop.

### Scenario 2: wrong pod-cidr / CNI config mismatch -> cross-node traffic does not flow

*   **Symptom:** curl from a pod on worker-1 to a pod on worker-2 (or to a ClusterIP service) times out; within one node it works.
*   **Diagnosis:**
    1. Start two debug pods pinned to different nodes (`kubectl run test1 --image=nginx --overrides='{"spec":{"nodeSelector":{"kubernetes.io/hostname":"<w1>"}}}'`).
    2. `kubectl get pods -o wide` -> note both pod IPs; `kubectl exec test1 -- curl -m2 <podIP2>` -> timeout.
    3. `ip route` inside the nodes: check that the route `10.244.0.0/16` (or /24 after the break) via flannel.1 is present on both.
    4. `kubectl -n kube-flannel get cm kube-flannel-cfg -o yaml | grep -A2 Network` -> the cidr does not match `--pod-network-cidr` from kubeadm (or iface=lo).
*   **Fix:** restore the correct cidr/interface in the ConfigMap/DS (`kubectl -n kube-flannel set env ds/kube-flannel FLANNELD_IFACE=<REAL_IFACE>`, or roll the cm back) and `kubectl -n kube-flannel rollout restart ds/kube-flannel`.
*   **Verify:** `kubectl exec test1 -- curl -m2 <podIP2>` -> 200; the routes on both nodes are /16 via flannel.1 again.

### Scenario 3: ingress controller with no endpoint (selector typo)

*   **Symptom:** `curl -H "Host: web.lab.local" ...` -> 503 from ingress-nginx (upstream unavailable).
*   **Diagnosis:**
    1. `kubectl get ingress web` -> the address is there and the backend is described.
    2. `kubectl describe ingress web` -> endpoints: `<none>` or empty.
    3. `kubectl get endpoints web` -> empty; `kubectl describe svc web` -> `Selector: app=web-broken`, while the pods carry `app=web` (`kubectl get pods -l app=web --show-labels`).
    4. `kubectl -n ingress-nginx logs deploy/ingress-nginx-controller | grep -i upstream` -> no endpoints available.
*   **Fix:** `kubectl patch svc web -p '{"spec":{"selector":{"app":"web"}}}'`.
*   **Verify:** `kubectl get endpoints web` lists the pod IPs; curl -> 200.

### Scenario 4: the etcd pod does not answer / the apiserver will not start after a reboot

*   **Symptom:** after the control-plane `reboot`, `kubectl get nodes` hangs or returns `connection refused` / `The connection to the server ... was refused`.
*   **Diagnosis:**
    1. `systemctl status kubelet` -> failed; `journalctl -u kubelet -e --no-pager | grep -iE 'swap|failed'` -> kubelet demands swap be off.
    2. `sudo crictl ps` -> no apiserver/etcd/controller/scheduler static pods.
    3. `free -h` -> swap is on; `/etc/kubernetes/manifests/` -> the manifests are present (so the problem is kubelet, not etcd).
    4. (for the mv etcd.yaml variant) `kubectl get cs` / `crictl logs <apiserver>` -> etcd cluster unavailable / connection refused 2379.
*   **Fix:** `sudo swapoff -a && sudo sed -i '/swap/d' /etc/fstab && sudo systemctl restart kubelet`; for the manifest variant, `sudo mv /root/etcd.yaml /etc/kubernetes/manifests/`.
*   **Verify:** the static pods are Running (`sudo crictl ps`), `kubectl get nodes` answers, and every node is Ready.

### Scenario 5: certificate expiry on the control-plane

*   **Symptom:** `kubectl` returns x509 errors (`certificate has expired or is not yet valid`); the apiserver pod is in CrashLoop or missing.
*   **Diagnosis:**
    1. `sudo kubeadm certs check-expiration` -> a list showing `RESIDUAL LIFE: 0y0m0d` / the ca dependency.
    2. `sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -dates` -> notAfter is in the past.
    3. `sudo crictl logs $(sudo crictl ps -a -q --name kube-apiserver | head -1) 2>&1 | grep -i x509`.
*   **Fix:**
    ```bash
  sudo kubeadm certs renew all
  sudo systemctl restart kubelet   # the static pods are recreated with the new certificates
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config   # the refreshed kubeconfig
    ```
    (in the lab: either restore the original timestamps from `/root/pki.bak` or simply run `renew all` — renew works either way).
*   **Verify:** `sudo kubeadm certs check-expiration` -> ~364d; `kubectl get nodes` OK; after `sudo reboot` of the control-plane the cluster comes back on its own.

## Restore (back to known-good after each scenario)

*   Break 1: scale back to the original replicas.
*   Break 2: restore the cidr/iface in the kube-flannel cm/ds, then rollout restart.
*   Break 3: patch the selector back.
*   Break 4: swapoff + fstab + restart kubelet; put etcd.yaml back into manifests for option B.
*   Break 5: `sudo rm -rf /etc/kubernetes/pki && sudo cp -r /root/pki.bak /etc/kubernetes/pki && sudo systemctl restart kubelet` (or leave the renew in place — it is a valid fix).
*   Final smoke test: `kubectl get nodes` all Ready, and curl through the ingress -> 200.

## Defence (the mentor asks the candidate)

"What happens to the cluster if (a) the single etcd instance dies on a single-master setup, and (b) the apiserver certificate expires? Describe the kubelet -> apiserver -> etcd chain, and what a kubectl user sees."

Expected: (a) the apiserver can no longer read or write state — writes fail, cached reads may partly work, running pods keep running (the data plane is alive), but any create/update/pod restart is impossible; (b) kubelet and the clients get x509 errors — control of the cluster is effectively lost while the workloads stay up; the cure is `kubeadm certs renew`.
