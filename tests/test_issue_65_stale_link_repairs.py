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
