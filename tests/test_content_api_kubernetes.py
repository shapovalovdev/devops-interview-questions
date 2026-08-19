"""Render gates for the Helm-owned Content API Kubernetes contract."""

from __future__ import annotations

import shutil
import subprocess
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / "deploy" / "content-api"
OVERLAY = ROOT / "kustomize" / "k3d"
SMOKE_SCRIPT = ROOT / "scripts" / "smoke_k3d_content_api.sh"


def render_helm() -> list[dict[str, object]]:
    output = subprocess.run(
        [
            "helm", "template", "content-api-test", str(CHART),
            "--set", "image.repository=registry.example/content-api",
            "--set", "image.tag=abcdef0123456789",
        ],
        check=True,
        text=True,
        capture_output=True,
    ).stdout
    return [document for document in yaml.safe_load_all(output) if document]


class ContentApiKubernetesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if shutil.which("helm") is None or shutil.which("kustomize") is None:
            raise unittest.SkipTest("helm and kustomize are required for Kubernetes render tests")
        cls.documents = render_helm()
        output = subprocess.run(
            ["kustomize", "build", "--enable-helm", "--load-restrictor", "LoadRestrictionsNone", str(OVERLAY)],
            check=True,
            text=True,
            capture_output=True,
        ).stdout
        cls.overlay_documents = [document for document in yaml.safe_load_all(output) if document]

    def test_chart_owns_the_only_workload_and_service(self) -> None:
        self.assertEqual({document["kind"] for document in self.documents}, {"Deployment", "Service", "ServiceAccount"})
        self.assertEqual({document["kind"] for document in self.overlay_documents}, {"Deployment", "Service", "ServiceAccount"})

    def test_deployment_is_restricted_and_only_sqlite_is_writable(self) -> None:
        deployment = next(document for document in self.documents if document["kind"] == "Deployment")
        pod = deployment["spec"]["template"]["spec"]
        container = pod["containers"][0]
        self.assertFalse(pod["automountServiceAccountToken"])
        self.assertEqual(pod["securityContext"]["runAsUser"], 10001)
        self.assertEqual(pod["securityContext"]["fsGroup"], 10001)
        self.assertEqual(pod["securityContext"]["seccompProfile"]["type"], "RuntimeDefault")
        self.assertTrue(container["securityContext"]["readOnlyRootFilesystem"])
        self.assertFalse(container["securityContext"]["allowPrivilegeEscalation"])
        self.assertEqual(container["securityContext"]["capabilities"]["drop"], ["ALL"])
        self.assertEqual(container["volumeMounts"], [{"name": "content-store", "mountPath": "/srv/data"}])
        init = pod["initContainers"][0]
        self.assertEqual(init["command"], ["cp", "/srv/data/content.db", "/work/content.db"])
        self.assertTrue(init["securityContext"]["readOnlyRootFilesystem"])
        self.assertFalse(init["securityContext"]["allowPrivilegeEscalation"])
        self.assertEqual(init["securityContext"]["capabilities"]["drop"], ["ALL"])
        self.assertEqual(container["readinessProbe"]["httpGet"]["path"], "/api/v1/health")
        self.assertEqual(container["livenessProbe"]["httpGet"]["path"], "/api/v1/health")
        self.assertEqual(container["resources"]["requests"], {"cpu": "100m", "memory": "128Mi"})
        self.assertEqual(container["resources"]["limits"], {"cpu": "500m", "memory": "256Mi"})

    def test_chart_rejects_latest_outside_local_overlay(self) -> None:
        result = subprocess.run(
            ["helm", "template", "content-api-test", str(CHART), "--set", "image.repository=registry.example/content-api", "--set", "image.tag=latest"],
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not be latest", result.stderr)

    def test_k3d_smoke_verifies_the_default_import_reaches_containerd(self) -> None:
        script = SMOKE_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('k3d image import "$image:$source_commit" -c "$cluster"', script)
        self.assertNotIn("--mode direct", script)
        self.assertIn("--provenance=false", script)
        self.assertIn("image=docker.io/library/devops-questions-content-api", script)
        self.assertIn('ctr -n k8s.io images list -q', script)
        self.assertIn('grep -Eq "(^|/)${image}:${source_commit}$"', script)
        self.assertIn("--dump-header - --output /dev/null", script)
        self.assertNotIn("--head", script)
        self.assertIn("for attempt in $(seq 1 30); do", script)


if __name__ == "__main__":
    unittest.main()
