#!/usr/bin/env bash
# Build one clean commit, render the Helm-owned overlay, and smoke it in k3d.
# Namespace cleanup is guarded by the UID returned by this run's create call.
set -euo pipefail

context=k3d-proto
cluster=proto
# k3s resolves unqualified names to Docker Hub, so use the same canonical name
# that containerd records after k3d imports it.
image=docker.io/library/devops-questions-content-api
node=k3d-${cluster}-server-0

for required_command in curl docker git helm k3d kubectl kustomize perl python3; do
  if ! command -v "$required_command" >/dev/null; then
    echo "missing required command: $required_command" >&2
    exit 1
  fi
done

root=$(git rev-parse --show-toplevel)
cd "$root"
if (( $# > 1 )); then
  echo "usage: $0 [commit]" >&2
  exit 2
fi
requested_commit=${1:-HEAD}
source_commit=$(git rev-parse --verify "${requested_commit}^{commit}")
head_commit=$(git rev-parse --verify HEAD)
if ! [[ "$source_commit" == "$head_commit" ]]; then
  echo "refusing to label the checked-out $head_commit build as $source_commit" >&2
  exit 1
fi
worktree_status=$(git status --porcelain=v1 --untracked-files=all)
if [[ -n "$worktree_status" ]]; then
  echo "refusing to build a dirty or untracked Docker context:" >&2
  printf '%s\n' "$worktree_status" >&2
  exit 1
fi

build_timestamp=$(git show -s --format=%cI "$source_commit")
namespace="content-api-216-${source_commit:0:8}-$(date +%s)-$$"
release=$namespace
namespace_created=false
namespace_uid=
overlay=
port_forward=

cleanup() {
  local status=$?
  local cleanup_status=0
  local current_uid=
  trap - EXIT
  set +e

  if [[ -n "$port_forward" ]]; then
    kill "$port_forward" 2>/dev/null
    wait "$port_forward" 2>/dev/null
  fi
  if [[ "$namespace_created" == true ]]; then
    if (( status != 0 )); then
      kubectl --context "$context" -n "$namespace" get pods 2>/dev/null || true
      kubectl --context "$context" -n "$namespace" describe pods 2>/dev/null || true
      kubectl --context "$context" -n "$namespace" logs "deployment/$release" --all-containers=true --prefix 2>/dev/null || true
    fi
    current_uid=$(kubectl --context "$context" get namespace "$namespace" -o jsonpath='{.metadata.uid}' 2>/dev/null)
    if [[ -n "$namespace_uid" && -n "$current_uid" && "$current_uid" == "$namespace_uid" ]]; then
      if kubectl --context "$context" delete namespace "$namespace" --wait=true; then
        echo "cleanup_namespace=$namespace"
      else
        echo "failed to delete owned namespace $namespace" >&2
        cleanup_status=1
      fi
    else
      echo "refusing to delete namespace $namespace: UID is not the one this run created" >&2
      cleanup_status=1
    fi
  fi
  if [[ -n "$overlay" ]]; then
    rm -rf "$overlay"
  fi
  if (( status == 0 && cleanup_status != 0 )); then
    status=$cleanup_status
  fi
  exit "$status"
}
trap cleanup EXIT
trap 'exit 130' INT TERM

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
mkdir -p "$overlay/kustomize"
cp -R deploy "$overlay/deploy"
cp -R kustomize/k3d "$overlay/kustomize/k3d"
# Render an isolated instance with the commit tag without changing tracked files.
perl -0pi -e "s/content-api-k3d/$release/g" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s#newName: devops-questions-content-api#newName: $image#; s/newTag: local/newTag: $source_commit/" "$overlay/kustomize/k3d/kustomization.yaml"
perl -0pi -e "s#repository: devops-questions-content-api#repository: $image#" "$overlay/kustomize/k3d/values.yaml"
perl -0pi -e "s/tag: local/tag: $source_commit/" "$overlay/kustomize/k3d/values.yaml"

rendered=$overlay/rendered.yaml
kustomize build --enable-helm --load-restrictor LoadRestrictionsNone "$overlay/kustomize/k3d" > "$rendered"
if kubectl --context "$context" get namespace "$namespace" >/dev/null 2>&1; then
  echo "refusing to use pre-existing namespace $namespace" >&2
  exit 1
fi
if namespace_uid=$(kubectl --context "$context" create namespace "$namespace" -o jsonpath='{.metadata.uid}'); then
  namespace_created=true
else
  echo "failed to create unique namespace $namespace" >&2
  exit 1
fi
if [[ -z "$namespace_uid" ]]; then
  echo "created namespace $namespace without receiving its UID" >&2
  exit 1
fi

kubectl --context "$context" -n "$namespace" apply -f "$rendered"
kubectl --context "$context" -n "$namespace" rollout status "deployment/$release" --timeout=180s

port_forward_log=$overlay/port-forward.log
kubectl --context "$context" -n "$namespace" port-forward --address 127.0.0.1 "service/$release" :8000 >"$port_forward_log" 2>&1 &
port_forward=$!
local_port=
for ((attempt = 1; attempt <= 30; attempt++)); do
  while IFS= read -r line; do
    if [[ $line =~ 127\.0\.0\.1:([0-9]+) ]]; then
      local_port=${BASH_REMATCH[1]}
      break
    fi
  done < "$port_forward_log"
  if [[ -n "$local_port" ]]; then
    break
  fi
  if ! kill -0 "$port_forward" 2>/dev/null; then
    cat "$port_forward_log" >&2
    exit 1
  fi
  sleep 1
done
if [[ -z "$local_port" ]]; then
  cat "$port_forward_log" >&2
  echo "kubectl did not report a local port" >&2
  exit 1
fi

base_url=http://127.0.0.1:$local_port
health_response=$overlay/health.json
health_ready=false
for ((attempt = 1; attempt <= 30; attempt++)); do
  if curl --fail --silent "$base_url/api/v1/health" > "$health_response"; then
    health_ready=true
    break
  fi
  sleep 1
done
if [[ "$health_ready" != true ]]; then
  cat "$port_forward_log" >&2
  echo "Content API health did not become reachable through the Service" >&2
  exit 1
fi

meta_response=$overlay/meta.json
meta_headers=$overlay/meta.headers
curl --fail --silent --show-error --dump-header "$meta_headers" --output "$meta_response" "$base_url/api/v1/meta"
content_digest=$(python3 - "$meta_response" "$meta_headers" "$source_commit" <<'PY'
import json
import re
import sys
from pathlib import Path

meta_path, header_path, expected_commit = sys.argv[1:]
meta = json.loads(Path(meta_path).read_text(encoding="utf-8"))
if not isinstance(meta, dict):
    raise SystemExit("/api/v1/meta did not return an object")
if meta.get("source_commit") != expected_commit:
    raise SystemExit(
        f"meta.source_commit={meta.get('source_commit')!r}, built commit={expected_commit!r}"
    )
content_digest = meta.get("content_digest")
if not isinstance(content_digest, str) or re.fullmatch(r"[0-9a-f]{64}", content_digest) is None:
    raise SystemExit(f"meta.content_digest is not a sha256 digest: {content_digest!r}")
headers = {}
for line in Path(header_path).read_text(encoding="utf-8").splitlines():
    name, separator, value = line.partition(":")
    if separator:
        headers[name.lower()] = value.strip()
if headers.get("x-content-snapshot") != content_digest:
    raise SystemExit(
        f"X-Content-Snapshot={headers.get('x-content-snapshot')!r}, "
        f"meta.content_digest={content_digest!r}"
    )
print(content_digest)
PY
)

assert_no_restarts() {
  local counts
  local count
  local restart_count=0
  counts=$(kubectl --context "$context" -n "$namespace" get pods \
    -l "app.kubernetes.io/instance=$release" \
    -o jsonpath='{range .items[*].status.containerStatuses[*]}{.restartCount}{"\n"}{end}')
  if [[ -z "$counts" ]]; then
    echo "no running workload container status found" >&2
    return 1
  fi
  while IFS= read -r count; do
    [[ -z "$count" ]] && continue
    if ! [[ "$count" =~ ^[0-9]+$ ]]; then
      echo "invalid restart count from Kubernetes: $count" >&2
      return 1
    fi
    restart_count=$((restart_count + count))
  done <<< "$counts"
  echo "restart_count=$restart_count"
  if (( restart_count != 0 )); then
    echo "Content API restarted during normal startup" >&2
    return 1
  fi
}

health=$(<"$health_response")
printf 'source_commit=%s\n' "$source_commit"
printf 'content_digest=%s\n' "$content_digest"
printf 'snapshot_header=%s\n' "$content_digest"
printf 'health=%s\n' "$health"
printf 'namespace=%s\n' "$namespace"
kubectl --context "$context" -n "$namespace" get pods -o wide
assert_no_restarts
