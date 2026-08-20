"""Dedicated API tests for /api/v1/learning-paths and /api/v1/learning-paths/{slug}."""

from __future__ import annotations

import pytest


def test_list_learning_paths_returns_all_tracks(corpus_client):
    response = corpus_client.get("/api/v1/learning-paths")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    slugs = {item["slug"] for item in data["items"]}
    assert {"devops-foundations", "kubernetes-operations", "sre-telemetry", "linux-sysadmin"}.issubset(slugs)

    # Check response headers
    assert "X-Content-Snapshot" in response.headers


def test_get_learning_path_devops_foundations_dag(corpus_client):
    response = corpus_client.get("/api/v1/learning-paths/devops-foundations")
    assert response.status_code == 200
    data = response.json()

    assert data["slug"] == "devops-foundations"
    assert data["title"] == "Full DevOps Career Pathway"
    assert data["icon"] == "🌐"
    assert data["color"] == "#38bdf8"
    assert "CKA" in data["certifications"]
    assert len(data["steps"]) >= 10

    first_step = data["steps"][0]
    assert first_step["step_id"] == "step-linux-proc"
    assert first_step["skill_id"] == "linux-proc"
    assert first_step["question_id"] == "linux/process-states"
    assert "Process Lifecycle" in first_step["concepts"]
    assert first_step["prerequisites"] == []

    # Check second step dependency
    second_step = data["steps"][1]
    assert "step-linux-proc" in second_step["prerequisites"]


def test_get_learning_path_kubernetes_operations_dag(corpus_client):
    response = corpus_client.get("/api/v1/learning-paths/kubernetes-operations")
    assert response.status_code == 200
    data = response.json()

    assert data["slug"] == "kubernetes-operations"
    assert data["icon"] == "☸️"
    assert data["color"] == "#326ce5"
    assert "CKA" in data["certifications"]
    assert any(step["question_id"] == "kubernetes/kubeadm-cluster-lifecycle" for step in data["steps"])


def test_get_learning_path_sre_telemetry_dag(corpus_client):
    response = corpus_client.get("/api/v1/learning-paths/sre-telemetry")
    assert response.status_code == 200
    data = response.json()

    assert data["slug"] == "sre-telemetry"
    assert data["icon"] == "📊"
    assert "observability/define-an-sli-and-slo" in [s["question_id"] for s in data["steps"]]


def test_get_learning_path_linux_sysadmin_dag(corpus_client):
    response = corpus_client.get("/api/v1/learning-paths/linux-sysadmin")
    assert response.status_code == 200
    data = response.json()

    assert data["slug"] == "linux-sysadmin"
    assert data["icon"] == "🐧"
    assert "RHCSA" in data["certifications"]


def test_get_learning_path_conditional_etag(corpus_client):
    res1 = corpus_client.get("/api/v1/learning-paths/devops-foundations")
    etag = res1.headers.get("ETag")
    assert etag is not None

    res2 = corpus_client.get("/api/v1/learning-paths/devops-foundations", headers={"If-None-Match": etag})
    assert res2.status_code == 304


def test_get_learning_path_404_problem_details(corpus_client):
    res = corpus_client.get("/api/v1/learning-paths/non-existent-track")
    assert res.status_code == 404
    data = res.json()
    assert data["status"] == 404
    assert "not found" in data["title"].lower() or "not found" in data["detail"].lower()
