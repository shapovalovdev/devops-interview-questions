"""Regression evidence for permanent link repairs from hosted run 31374633603."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCOPES = [
    ROOT / "questions" / theme
    for theme in ("network-storage", "version-control", "distributed-systems", "logging", "troubleshooting", "web-servers", "ci-cd", "processes", "shell-scripting", "container-networking")
]
STALE_URL_FRAGMENTS = (
    "implementing-the-saga-pattern-with-aws-lambda-and-amazon-step-functions",
    "consensus-and-coordination",
    "dns-what-is-it-and-how-does-it-work",
    "cassandra.apache.org/doc/latest/cassandra/operating/",
    "docs.ceph.com/en/latest/rbd/rbd/",
    "docs.ceph.com/en/latest/start/quick-rgw/",
    "docs.kernel.org/admin-guide/nvme-fabrics.html",
    "docs.temporal.io/develop/java/saga",
    "git-database-internals-i-packed-object-store",
    "jvns.ca/blog/2021/12/15/dns-doesn-t-propagate",
    "jvns.ca/blog/2022/10/17/what-is-cryptography",
    "jvns.ca/blog/2024/02/15/git-worktrees",
    "jvns.ca/blog/2024/03/20/git-objects",
    "jvns.ca/blog/2024/06/21/git-tips",
    "slsa.dev/spec/v1.0/build-requirements",
    "techcommunity.microsoft.com/category/windowsserver/blog/storageatmsft",
    "wiki.linux-nfs.org/wiki/index.php/Main_Page",
    "www.confluent.io/blog/stream-data-processing-using-apache-flink",
    "www.redhat.com/en/blog/channel/storage",
    "aws.amazon.com/blogs/mt/control-log-retention-in-aws-accounts",
    "aws.amazon.com/blogs/storage/how-to-protect-data-using-amazon-s3-object-lock",
    "blog.cloudflare.com/tag/postmortem",
    "blog.mozilla.org/en/internet-culture/privacy-security",
    "pagerduty.com/resources/learn/",
    "pagerduty.com/resources/learn/incident-command-system",
    "sre.google/sre-book/capacity-planning",
    "sre.google/workbook/disaster-recovery",
    "docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/caching-dependencies-to-speed-up-workflows",
    "docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-variations-of-jobs-in-a-workflow",
    "docs.github.com/en/actions/security-for-github-actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds",
    "docs.github.com/en/actions/tutorials/security-hardening-your-deployments",
    "docs.github.com/en/repositories/working-with-files/managing-files/working-with-submodules",
    "kubernetes.io/docs/tasks/run-application/rollout/",
    "grafana.com/blog/2020/04/21/how-labels-in-loki-can-make-log-queries-faster-and-more-efficient",
    "grafana.com/blog/2021/01/20/how-to-run-grafana-loki-as-a-multi-tenant-log-aggregation-system",
    "grafana.com/blog/2023/10/10/how-to-control-logging-costs-with-grafana-loki",
    "grafana.com/blog/author/ed-welch",
    "grafana.com/blog/tags/loki",
    "grafana.com/docs/loki/latest/operations/storage/migrate-to-tsdb",
    "opentelemetry.io/docs/collector/monitoring/",
    "elastic.co/docs/reference/ecs/migrate",
    "honeycomb.io/blog/how-trace-context-works",
    "phusionpassenger.com/library/indepth/docker/",
    "redhat.com/en/blog/channel/enable-sysadmin",
    "redhat.com/en/blog/linux-signals",
    "docs.cilium.io/en/stable/network/bgp-control-plane/)",
    "charity.wtf/2019/02/05/logs-vs-structured-events/",
    "techcommunity.microsoft.com/category/windowsserver/blog/windowsserver",
)


def test_hosted_run_31374633603_permanent_links_are_not_reintroduced() -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for scope in SCOPES for path in scope.glob("*.md"))
    text += (ROOT / "docs/related-materials/network-storage.md").read_text(encoding="utf-8")
    for fragment in STALE_URL_FRAGMENTS:
        assert fragment not in text, f"stale link reintroduced: {fragment}"


def test_journald_question_uses_the_live_systemd_manual() -> None:
    """Keep this single-file #65 repair independent while other process slices land."""
    text = (ROOT / "questions" / "processes" / "journald-process-diagnostics.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/automation/what-is-systemd" not in text
    assert "https://www.freedesktop.org/software/systemd/man/latest/systemd.html" in text


def test_systemd_service_lifecycle_uses_the_live_systemd_manual() -> None:
    text = (ROOT / "questions" / "processes" / "systemd-service-lifecycle.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/automation/what-is-systemd" not in text
    assert "https://www.freedesktop.org/software/systemd/man/latest/systemd.html" in text


def test_process_tree_supervision_uses_the_live_systemd_manual() -> None:
    text = (ROOT / "questions" / "processes" / "process-tree-supervision.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/automation/what-is-systemd" not in text
    assert "https://www.freedesktop.org/software/systemd/man/latest/systemd.html" in text


def test_program_vs_process_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "program-vs-process.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_pid_and_parent_process_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "pid-and-parent-process.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_fork_exec_wait_lifecycle_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "fork-exec-wait-lifecycle.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_resource_limits_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "resource-limits.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_file_descriptor_inheritance_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "file-descriptor-inheritance.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_read_process_status_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "read-process-status.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_process_identity_and_pid_reuse_uses_live_kernel_process_documentation() -> None:
    text = (ROOT / "questions" / "processes" / "process-identity-and-pid-reuse.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_debug_error_budget_uses_live_error_budget_guidance() -> None:
    text = (ROOT / "questions" / "troubleshooting" / "debug-error-budget.md").read_text(encoding="utf-8")
    assert "https://www.nobl9.com/blog" not in text
    assert "https://sre.google/workbook/error-budget-policy/" in text


def test_processes_materials_use_live_kernel_process_documentation() -> None:
    text = (ROOT / "docs" / "related-materials" / "processes.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/topics/linux/what-is-a-linux-process" not in text
    assert "https://docs.kernel.org/filesystems/proc.html" in text


def test_exit_statuses_uses_live_enable_sysadmin_source() -> None:
    text = (ROOT / "questions" / "shell-scripting" / "use-exit-statuses.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/blog/channel/enable-sysadmin" not in text
    assert "https://www.redhat.com/en/blog/welcome" in text


def test_host_networking_tradeoffs_uses_live_docker_networking_tutorial() -> None:
    text = (ROOT / "questions" / "container-networking" / "host-networking-tradeoffs.md").read_text(encoding="utf-8")
    assert "https://docs.docker.com/network/tutorials/" not in text
    assert "https://docs.docker.com/engine/network/tutorials/standalone/" in text


def test_deployment_rollout_check_uses_live_kubernetes_blog() -> None:
    text = (ROOT / "questions" / "certification-last-minute-review" / "deployment-rollout-check.md").read_text(encoding="utf-8")
    assert "https://learnk8s.io/kubernetes-deployments" not in text
    assert "https://kubernetes.io/blog/" in text


def test_incident_change_freeze_uses_live_sre_incident_response_workbook() -> None:
    text = (ROOT / "questions" / "ci-cd" / "incident-change-freeze.md").read_text(encoding="utf-8")
    assert "https://sre.google/workbook/managing-incidents/" not in text
    assert "https://sre.google/workbook/incident-response/" in text


def test_ingress_gateway_routing_uses_live_maintainer_source() -> None:
    text = (ROOT / "questions" / "certification-last-minute-review" / "ingress-gateway-routing.md").read_text(encoding="utf-8")
    assert "https://technosophos.com/2023/05/25/gateway-api.html" not in text
    assert "https://technosophos.com/" in text


def test_configmap_secret_boundaries_uses_live_liz_rice_source() -> None:
    text = (ROOT / "questions" / "certification-last-minute-review" / "configmap-secret-boundaries.md").read_text(encoding="utf-8")
    assert "https://www.aquasec.com/blog/kubernetes-secrets-management/" not in text
    assert "https://www.lizrice.com/" in text


def test_configuration_management_materials_use_live_ansible_blog() -> None:
    text = (ROOT / "docs" / "related-materials" / "configuration-management.md").read_text(encoding="utf-8")
    assert "https://www.redhat.com/en/blog/channel/ansible" not in text
    assert "https://www.ansible.com/blog" in text


def test_pod_disruption_budget_uses_live_scylladb_blog() -> None:
    text = (ROOT / "questions" / "certification-last-minute-review" / "pod-disruption-budget.md").read_text(encoding="utf-8")
    assert "https://www.scylladb.com/2022/08/18/kubernetes-pod-disruption-budgets/" not in text
    assert "https://www.scylladb.com/blog/" in text


def test_container_network_security_architecture_uses_live_docker_tutorial() -> None:
    text = (ROOT / "questions" / "container-networking" / "container-network-security-architecture.md").read_text(encoding="utf-8")
    assert "https://docs.docker.com/network/tutorials/" not in text
    assert "https://docs.docker.com/engine/network/tutorials/standalone/" in text
