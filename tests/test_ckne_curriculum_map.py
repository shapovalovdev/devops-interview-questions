"""Keep the public CKNE curriculum map explicit while the program is developing."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "ckne.md"


def main() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/kubernetes-network-engineer-program/",
        "reviewed on 2026-08-06",
        "still in development",
        "not** a reproduction of exam questions",
        "Core Infrastructure and CNI | 15%",
        "Service Networking and DNS | 25%",
        "Advanced Traffic Management | 20%",
        "Network Security and Policy | 25%",
        "Observability | 15%",
        "multi-interface Pod configuration Question is required",
        "LLM-traffic routing Question is required",
        "Multus CNI documentation",
        "Gateway API Inference Extension documentation",
        "`ckne`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"CKNE curriculum map is missing: {', '.join(missing)}"
    print("Validated public CKNE curriculum map and explicit gap policy.")


if __name__ == "__main__":
    main()
