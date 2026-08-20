#!/usr/bin/env bash
# Build a provenance-labelled image, render the Helm-owned overlay, and smoke it
# in k3d. The trap deletes only the namespace this script creates.
set -euo pipefail

context=k3d-proto
cluster=proto
unique_id=$(LC_ALL=C tr -dc 'a-z0-9' </dev/urandom | head -c 8 || date +%s)
namespace="content-api-${unique_id}"
release="content-api-${unique_id}"
# k3s resolves unqualified names to Docker Hub, so use the same canonical name
# that containerd records after k3d imports it.
image=docker.io/library/devops-questions-content-api
node=k3d-${cluster}-server-0
source_commit=$(git rev-parse HEAD)
build_timestamp=$(git show -s --format=%cI HEAD)
created_namespace=false

if [ -n "$(git status --porcelain)" ]; then
  echo "error: working tree is dirty; smoke requires a clean git working tree for reproducible provenance" >&2
  exit 1
fi

for command in docker k3d kubectl kustomize; do
  command -v "$command" >/dev/null || { echo "missing required command: $command" >&2; exit 1; }
done

cleanup() {
  if [ "$created_namespace" = "true" ]; then
    kubectl --context "$context" -n "$namespace" get pods 2>/dev/null || true
    kubectl --context "$context" -n "$namespace" describe pods 2>/dev/null || true
    kubectl --context "$context" -n "$namespace" logs "deployment/$release" --all-containers=true --prefix 2>/dev/null || true
    kubectl --context "$context" delete namespace "$namespace" --ignore-not-found --wait=true
  fi
}
trap cleanup EXIT

docker build -f Dockerfile.api \
  --provenance=false \
  --build-arg SOURCE_COMMIT="$source_commit" \
  --build-arg BUILD_TIMESTAMP="$build_timestamp" \
  -t "$image:$source_commit" .
# k3d's default import mode is the reliable path into this cluster's containerd.
k3d image import "$image:$source_commit" -c "$cluster"
docker exec "$node" ctr -n k8s.io images list -q \
  | grep -Eq "(^|/)${image}:${source_commit}$" \
  || { echo "imported image is not visible to k3s containerd" >&2; exit 1; }

overlay=$(mktemp -d)
trap 'rm -rf "$overlay"; cleanup' EXIT
mkdir -p "$overlay/kustomize/k3d"
cp -R deploy "$overlay/deploy"

# Write isolated Kustomize + Helm values without mutating tracked files or relying on regex.
cat > "$overlay/kustomize/k3d/values.yaml" <<EOF
image:
  repository: ${image}
  tag: ${source_commit}
  local: true
  pullPolicy: IfNotPresent
EOF

cat > "$overlay/kustomize/k3d/kustomization.yaml" <<EOF
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: ${namespace}
helmGlobals:
  chartHome: ../../deploy
helmCharts:
  - name: content-api
    releaseName: ${release}
    namespace: ${namespace}
    valuesFile: ../../deploy/content-api/values.yaml
    additionalValuesFiles:
      - values.yaml
    includeCRDs: false
EOF

kubectl --context "$context" create namespace "$namespace"
created_namespace=true

(cd "$overlay/kustomize/k3d" && kustomize build --enable-helm --load-restrictor LoadRestrictionsNone) | kubectl --context "$context" -n "$namespace" apply -f -
kubectl --context "$context" -n "$namespace" rollout status "deployment/$release" --timeout=120s

# Verify no container restarts occurred during cold start
restarts=$(kubectl --context "$context" -n "$namespace" get pods -l "app.kubernetes.io/name=content-api,app.kubernetes.io/instance=${release}" -o jsonpath='{.items[0].status.containerStatuses[0].restartCount}' 2>/dev/null || echo "0")
if [ "${restarts:-0}" -gt 0 ]; then
  echo "error: container restarted ${restarts} times during startup; cold start probe failed" >&2
  exit 1
fi

kubectl --context "$context" -n "$namespace" port-forward "service/$release" 18000:8000 >/tmp/content-api-port-forward.log 2>&1 &
port_forward=$!
trap 'kill "$port_forward" 2>/dev/null || true; rm -rf "$overlay"; cleanup' EXIT

for attempt in $(seq 1 30); do
  if curl --fail --silent http://127.0.0.1:18000/api/v1/health >/dev/null; then
    break
  fi
  if [ "$attempt" = 30 ]; then
    cat /tmp/content-api-port-forward.log >&2
    exit 1
  fi
  sleep 1
done

curl --fail --show-error http://127.0.0.1:18000/api/v1/health
meta_output=$(curl --fail --show-error --silent http://127.0.0.1:18000/api/v1/meta)
echo "$meta_output"

meta_commit=$(python3 -c "import json,sys; print(json.loads(sys.argv[1]).get('source_commit',''))" "$meta_output")
meta_digest=$(python3 -c "import json,sys; print(json.loads(sys.argv[1]).get('content_digest',''))" "$meta_output")

if [ "$meta_commit" != "$source_commit" ]; then
  echo "error: meta.source_commit ($meta_commit) != built source_commit ($source_commit)" >&2
  exit 1
fi

header_snapshot=$(curl --fail --show-error --silent --dump-header - --output /dev/null http://127.0.0.1:18000/api/v1/health | grep -i '^x-content-snapshot:' | awk '{print $2}' | tr -d '\r\n')
if [ "$header_snapshot" != "$meta_digest" ]; then
  echo "error: X-Content-Snapshot header ($header_snapshot) != meta.content_digest ($meta_digest)" >&2
  exit 1
fi

