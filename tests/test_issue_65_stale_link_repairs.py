"""Regression evidence for permanent link repairs from hosted run 31374633603."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCOPES = [ROOT / "questions" / theme for theme in ("network-storage", "version-control", "distributed-systems")]
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
)


def test_hosted_run_31374633603_permanent_links_are_not_reintroduced() -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for scope in SCOPES for path in scope.glob("*.md"))
    text += (ROOT / "docs/related-materials/network-storage.md").read_text(encoding="utf-8")
    for fragment in STALE_URL_FRAGMENTS:
        assert fragment not in text, f"stale link reintroduced: {fragment}"
