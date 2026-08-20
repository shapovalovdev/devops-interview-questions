#!/usr/bin/env bash
# Build a provenance-labelled image, render the Helm-owned overlay, and smoke it
# in k3d. The trap deletes only the namespace this script creates.
set -euo pipefail

context=k3d-proto
cluster=proto
namespace=content-api-206
release=content-api-206
# k3s resolves unqualified names to Docker Hub, so use the same canonical name
# that containerd records after k3d imports it.
image=docker.io/library/devops-questions-content-api
node=k3d-${cluster}-server-0
source_commit=$(git rev-parse HEAD)
build_timestamp=$(git show -s --format=%cI HEAD)

for command in docker k3d kubectl kustomize; do
  command -v "$command" >/dev/null || { echo "missing required command: $command" >&2; exit 1; }
done

cleanup() {
  kubectl --context "$context" -n "$namespace" get pods 2>/dev/null || true
  kubectl --context "$context" -n "$namespace" describe pods 2>/dev/null || true
  kubectl --context "$context" -n "$namespace" logs "deployment/$release" --all-containers=true --prefix 2>/dev/null || true
  kubectl --context "$context" delete namespace "$namespace" --ignore-not-found --wait=true
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
mkdir -p "$overlay/kustomize"
cp -R deploy "$overlay/deploy"
cp -R kustomize/k3d "$overlay/kustomize/k3d"
# Render an isolated instance with the commit tag without changing tracked files.
perl -0pi -e "s/content-api-k3d/$release/g" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s/content-api-k3d/$namespace/g" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s#newName: devops-questions-content-api#newName: $image#; s/newTag: local/newTag: $source_commit/" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s#repository: devops-questions-content-api#repository: $image#" "$overlay/kustomize/k3d/values.yaml"
perl -0pi -e "s/tag: local/tag: $source_commit/" "$overlay/kustomize/k3d/values.yaml"
kubectl --context "$context" create namespace "$namespace"
(cd "$overlay/kustomize/k3d" && kustomize build --enable-helm --load-restrictor LoadRestrictionsNone) | kubectl --context "$context" -n "$namespace" apply -f -
kubectl --context "$context" -n "$namespace" rollout status "deployment/$release" --timeout=120s
kubectl --context "$context" -n "$namespace" port-forward "service/$release" 18000:8000 >/tmp/content-api-206-port-forward.log 2>&1 &
port_forward=$!
trap 'kill "$port_forward" 2>/dev/null || true; rm -rf "$overlay"; cleanup' EXIT
for attempt in $(seq 1 30); do
  if curl --fail --silent http://127.0.0.1:18000/api/v1/health >/dev/null; then
    break
  fi
  if [ "$attempt" = 30 ]; then
    cat /tmp/content-api-206-port-forward.log >&2
    exit 1
  fi
  sleep 1
done
curl --fail --show-error http://127.0.0.1:18000/api/v1/health
curl --fail --show-error http://127.0.0.1:18000/api/v1/meta
curl --fail --show-error --dump-header - --output /dev/null http://127.0.0.1:18000/api/v1/health \
  | grep -i '^x-content-snapshot:'
