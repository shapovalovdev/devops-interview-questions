#!/usr/bin/env python3
"""Gate the vendor-honesty contract for cloud, databases, and infrastructure-as-code.

Issue #110 distinguishes Themes whose single source is the rightful authority
from Themes where one product silently stands in for a category.  These three
Themes teach portable concepts through one vendor, so their honesty contract is:

* every vendor-neutral Question's answer guide names a concrete equivalent in
  another implementation — a construct, never a gesture at "other providers";
* the genuinely branded Questions keep their framing;
* each Theme's related-materials page states the vendor bias plainly;
* the mapped implementations are backed by additional primary sources from
  distinct hosts, not by swapped citations.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
MATERIALS = ROOT / "docs" / "related-materials"

# Cloud Questions that are legitimately about AWS-branded behaviour and keep
# their framing: CloudTrail, CloudWatch, AWS IAM, the AWS VPC, multi-account
# boundaries, and AWS incident response.
AWS_BRANDED_CLOUD_QUESTIONS = {
    "cloudtrail-audit-evidence.md",
    "cloudwatch-alarm-design.md",
    "iam-policy-evaluation.md",
    "vpc-network-foundations.md",
    "multi-account-boundaries.md",
    "cloud-incident-response.md",
}

CLOUD_MARKERS = ("azure", "google cloud", "gcp", "microsoft entra", "finops", "nist")
DATABASES_MARKERS = (
    "mysql",
    "mariadb",
    "sql server",
    "innodb",
    "binlog",
    "gtid",
    "always on",
    "query store",
    "tempdb",
)
IAC_MARKERS = (
    "opentofu",
    "cloudformation",
    "pulumi",
    "bicep",
    "open policy agent",
    "rego",
    "sentinel",
    "terratest",
)

INCUMBENT_HOSTS = {
    "cloud": "docs.aws.amazon.com",
    "databases": "www.postgresql.org",
    "infrastructure-as-code": "developer.hashicorp.com",
}
MINIMUM_ADDITIONAL_SOURCE_HOSTS = {"cloud": 3, "databases": 2, "infrastructure-as-code": 3}


def answer_guide(text: str) -> str:
    guide = text.split("## Answer guide", 1)[1].split("## References", 1)[0]
    return guide.lower()


def source_urls(text: str) -> list[str]:
    block = re.search(r"^sources:\n([\s\S]*?)(?=^[A-Za-z][\w-]*:|^---$)", text, re.MULTILINE)
    assert block, "missing sources block"
    return re.findall(r"^  - url: (https://[^\s]+)$", block.group(1), re.MULTILINE)


def theme_questions(theme: str) -> list[Path]:
    return sorted((QUESTIONS / theme).glob("*.md"))


def test_cloud_questions_name_other_providers() -> None:
    missing = [
        path.name
        for path in theme_questions("cloud")
        if path.name not in AWS_BRANDED_CLOUD_QUESTIONS
        and not any(marker in answer_guide(path.read_text(encoding="utf-8")) for marker in CLOUD_MARKERS)
    ]
    assert not missing, f"cloud Questions without a concrete Azure/Google/etc. mapping: {missing}"


def test_aws_branded_cloud_questions_keep_their_framing() -> None:
    branded_titles = {
        "cloudtrail-audit-evidence.md": "CloudTrail",
        "cloudwatch-alarm-design.md": "CloudWatch",
        "iam-policy-evaluation.md": "AWS IAM",
        "vpc-network-foundations.md": "AWS VPC",
        "multi-account-boundaries.md": "AWS multi-account",
        "cloud-incident-response.md": "AWS workload incident response",
    }
    assert set(branded_titles) == AWS_BRANDED_CLOUD_QUESTIONS, "the branded set must stay deliberate"
    for name, marker in branded_titles.items():
        text = (QUESTIONS / "cloud" / name).read_text(encoding="utf-8")
        title = re.search(r"^title: (.+)$", text, re.MULTILINE).group(1)
        assert marker.lower() in title.lower(), f"cloud/{name}: expected AWS-branded title, got {title}"


def test_databases_questions_name_other_engines() -> None:
    missing = [
        path.name
        for path in theme_questions("databases")
        if not any(marker in answer_guide(path.read_text(encoding="utf-8")) for marker in DATABASES_MARKERS)
    ]
    assert not missing, f"databases Questions without a concrete other-engine mapping: {missing}"


def test_iac_questions_name_other_tools() -> None:
    missing = [
        path.name
        for path in theme_questions("infrastructure-as-code")
        if not any(marker in answer_guide(path.read_text(encoding="utf-8")) for marker in IAC_MARKERS)
    ]
    assert not missing, f"infrastructure-as-code Questions without a concrete other-tool mapping: {missing}"


def test_related_materials_state_the_vendor_bias() -> None:
    for theme in INCUMBENT_HOSTS:
        page = (MATERIALS / f"{theme}.md").read_text(encoding="utf-8")
        assert "Vendor scope, stated plainly" in page, f"{theme}: related materials must state the vendor bias plainly"


def test_additional_primary_sources_come_from_distinct_hosts() -> None:
    for theme, incumbent in INCUMBENT_HOSTS.items():
        hosts = Counter()
        for path in theme_questions(theme):
            for url in source_urls(path.read_text(encoding="utf-8")):
                host = re.sub(r"^https://", "", url).split("/", 1)[0]
                if host != incumbent:
                    hosts[host] += 1
        minimum = MINIMUM_ADDITIONAL_SOURCE_HOSTS[theme]
        assert len(hosts) >= minimum, (
            f"{theme}: expected at least {minimum} distinct non-{incumbent} primary-source hosts, "
            f"got {sorted(hosts)}"
        )


def main() -> None:
    test_cloud_questions_name_other_providers()
    test_aws_branded_cloud_questions_keep_their_framing()
    test_databases_questions_name_other_engines()
    test_iac_questions_name_other_tools()
    test_related_materials_state_the_vendor_bias()
    test_additional_primary_sources_come_from_distinct_hosts()
    print(
        "Validated vendor-honesty mappings across cloud, databases, and infrastructure-as-code."
    )


if __name__ == "__main__":
    main()
