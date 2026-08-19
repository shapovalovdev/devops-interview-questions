#!/usr/bin/env bash
# Build a provenance-labelled image, render the Helm-owned overlay, and smoke it
# in k3d. The trap deletes only the namespace this script creates.
set -euo pipefail

context=k3d-proto
cluster=proto
namespace=content-api-206
release=content-api-206
image=devops-questions-content-api
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
  --build-arg SOURCE_COMMIT="$source_commit" \
  --build-arg BUILD_TIMESTAMP="$build_timestamp" \
  -t "$image:$source_commit" .
# Direct import keeps the Docker image tag visible to the k3s containerd store.
k3d image import "$image:$source_commit" -c "$cluster" --mode direct

overlay=$(mktemp -d)
trap 'rm -rf "$overlay"; cleanup' EXIT
mkdir -p "$overlay/kustomize"
cp -R deploy "$overlay/deploy"
cp -R kustomize/k3d "$overlay/kustomize/k3d"
# Render an isolated instance with the commit tag without changing tracked files.
perl -0pi -e "s/content-api-k3d/$release/g" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s/content-api-k3d/$namespace/g" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s/newTag: local/newTag: $source_commit/" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s/tag: local/tag: $source_commit/" "$overlay/kustomize/k3d/values.yaml"
kubectl --context "$context" create namespace "$namespace"
(cd "$overlay/kustomize/k3d" && kustomize build --enable-helm --load-restrictor LoadRestrictionsNone) | kubectl --context "$context" -n "$namespace" apply -f -
kubectl --context "$context" -n "$namespace" rollout status "deployment/$release" --timeout=120s
kubectl --context "$context" -n "$namespace" port-forward "service/$release" 18000:8000 >/tmp/content-api-206-port-forward.log 2>&1 &
port_forward=$!
trap 'kill "$port_forward" 2>/dev/null || true; rm -rf "$overlay"; cleanup' EXIT
sleep 2
curl --fail --show-error http://127.0.0.1:18000/api/v1/health
curl --fail --show-error http://127.0.0.1:18000/api/v1/meta
curl --fail --show-error --head http://127.0.0.1:18000/api/v1/health | grep -i '^x-content-snapshot:'
