#!/usr/bin/env python3
"""
Convert an Xray manual-test JSON export into grouped Gherkin .feature files.

Driven by a config JSON that the calling skill builds via Q&A with the user.

Usage:
    python xray_to_gherkin.py --config path/to/config.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ---------- Config ----------


@dataclass
class Config:
    input_json: Path
    output_dir: Path
    prefix_routing: dict[str, str]  # "[Home]" -> "home"
    visual_keywords: list[str]
    firebase_keywords: list[str]
    external_keywords: list[str]
    feature_titles: dict[str, str] = field(default_factory=dict)  # slug -> "Feature: Home"
    default_bucket: str | None = None  # slug for tests with no/unmapped prefix; None = fail loudly

    @classmethod
    def load(cls, path: Path) -> "Config":
        data = json.loads(path.read_text())
        return cls(
            input_json=Path(data["input_json"]).expanduser(),
            output_dir=Path(data["output_dir"]).expanduser(),
            prefix_routing=data["prefix_routing"],
            visual_keywords=data.get("visual_keywords", []),
            firebase_keywords=data.get("firebase_keywords", []),
            external_keywords=data.get("external_keywords", []),
            feature_titles=data.get("feature_titles", {}),
            default_bucket=data.get("default_bucket"),
        )


# ---------- Xray test model ----------


@dataclass
class XrayTest:
    key: str
    summary: str
    labels: list[str]
    description_text: str
    description_urls: list[str]
    steps: list[dict[str, str]]

    @classmethod
    def from_raw(cls, raw: dict[str, Any]) -> "XrayTest":
        desc_text, desc_urls = _extract_description(raw.get("description"))
        steps = [
            {
                "action": (s.get("action") or "").strip(),
                "data": (s.get("data") or "").strip(),
                "result": (s.get("result") or "").strip(),
            }
            for s in (raw.get("steps") or [])
        ]
        return cls(
            key=raw["key"],
            summary=(raw.get("summary") or "").strip(),
            labels=raw.get("labels") or [],
            description_text=desc_text,
            description_urls=desc_urls,
            steps=steps,
        )


def _extract_description(desc: Any) -> tuple[str, list[str]]:
    """Extract plain text and URLs from Atlassian Document Format."""
    if not isinstance(desc, dict):
        return "", []
    text_parts: list[str] = []
    urls: list[str] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            ntype = node.get("type")
            if ntype == "text" and "text" in node:
                text_parts.append(node["text"])
            elif ntype == "inlineCard":
                url = (node.get("attrs") or {}).get("url")
                if url:
                    urls.append(url)
            for child in node.get("content", []) or []:
                walk(child)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(desc)
    return " ".join(text_parts).strip(), urls


# ---------- Routing ----------

PREFIX_RE = re.compile(r"^\s*(\[[^\]]+\])")


def extract_prefix(summary: str) -> str | None:
    m = PREFIX_RE.match(summary)
    return m.group(1) if m else None


def strip_prefix(summary: str) -> str:
    return PREFIX_RE.sub("", summary).strip()


# ---------- Tag detection ----------


def detect_tags(test: XrayTest, cfg: Config) -> list[str]:
    tags = [f"@{test.key}"]
    if "Regression" in test.labels:
        tags.append("@regression")

    haystack = " ".join(
        [test.summary, test.description_text]
        + [s["action"] + " " + s["result"] for s in test.steps]
    ).lower()

    def matches(keywords: list[str]) -> bool:
        return any(kw.lower() in haystack for kw in keywords)

    if matches(cfg.visual_keywords):
        tags.append("@visual")
    if matches(cfg.firebase_keywords):
        tags.append("@firebase")
    if matches(cfg.external_keywords):
        tags.append("@external")
    return tags


# ---------- Placeholder handling ----------

PLACEHOLDER_RE = re.compile(r"\$\{([^}]+)\}")


def find_placeholders(test: XrayTest) -> list[str]:
    seen: list[str] = []
    for step in test.steps:
        for field_val in (step["action"], step["data"], step["result"]):
            for m in PLACEHOLDER_RE.finditer(field_val):
                name = m.group(1)
                if name not in seen:
                    seen.append(name)
    return seen


def rewrite_placeholders(text: str) -> str:
    return PLACEHOLDER_RE.sub(lambda m: f"<{m.group(1)}>", text)


# ---------- Convertibility ----------


def is_unconvertible(test: XrayTest) -> str | None:
    """Return a reason string if the test cannot be converted, else None."""
    if not test.steps:
        return "no steps and summary alone is not actionable"
    if all(not s["action"] for s in test.steps):
        return "all step actions are empty"
    return None


# ---------- Gherkin emission ----------


def render_scenario(test: XrayTest, cfg: Config) -> str:
    tags = detect_tags(test, cfg)
    placeholders = find_placeholders(test)
    is_outline = bool(placeholders)

    lines: list[str] = []

    # Context comments
    if test.description_urls:
        for url in test.description_urls:
            lines.append(f"  # ref: {url}")
    desc = test.description_text.strip()
    if desc and desc.lower() != strip_prefix(test.summary).lower():
        # collapse newlines
        clean = " ".join(desc.split())
        if len(clean) > 200:
            clean = clean[:197] + "..."
        lines.append(f"  # context: {clean}")
    if placeholders:
        lines.append(
            f"  # TODO: fill from Xray {test.key} — placeholders were not expanded in source"
        )

    # Tags
    lines.append("  " + " ".join(tags))

    # Header
    scenario_name = strip_prefix(test.summary) or test.key
    header = "Scenario Outline" if is_outline else "Scenario"
    lines.append(f"  {header}: {scenario_name}")

    # Default Given
    lines.append("    Given the app is launched")

    # Steps
    first_when = True
    first_then = True
    for step in test.steps:
        action = rewrite_placeholders(step["action"]).strip()
        result = rewrite_placeholders(step["result"]).strip()
        data = rewrite_placeholders(step["data"]).strip()
        if action:
            keyword = "When" if first_when else "And"
            first_when = False
            lines.append(f"    {keyword} {action}")
            if data:
                lines.append(f"      # data: {data}")
        if result:
            keyword = "Then" if first_then else "And"
            first_then = False
            lines.append(f"    {keyword} {result}")

    # Examples table for outlines
    if is_outline:
        lines.append("")
        lines.append("    Examples:")
        header_row = " | ".join(placeholders)
        lines.append(f"      | {header_row} |")
        # empty row so the table is syntactically valid
        empty = " | ".join(["" for _ in placeholders])
        lines.append(f"      | {empty} |")

    return "\n".join(lines)


def render_feature_file(slug: str, scenarios: list[str], cfg: Config) -> str:
    title = cfg.feature_titles.get(slug, slug.replace("_", " ").title())
    out = [f"Feature: {title}", ""]
    out.append("\n\n".join(scenarios))
    out.append("")
    return "\n".join(out)


# ---------- Main pipeline ----------


def run(cfg: Config) -> int:
    raw_tests = json.loads(cfg.input_json.read_text())
    if not isinstance(raw_tests, list):
        print("ERROR: input JSON must be a list of tests", file=sys.stderr)
        return 2

    tests = [XrayTest.from_raw(t) for t in raw_tests]

    # Validate all prefixes are routed (unless default_bucket is set)
    if cfg.default_bucket is None:
        unmapped: set[str] = set()
        for t in tests:
            prefix = extract_prefix(t.summary)
            if prefix is None:
                unmapped.add(f"(no prefix on {t.key})")
            elif prefix not in cfg.prefix_routing:
                unmapped.add(prefix)
        if unmapped:
            print("ERROR: unmapped prefixes in input:", file=sys.stderr)
            for p in sorted(unmapped):
                print(f"  {p}", file=sys.stderr)
            return 3

    # Bucket
    buckets: dict[str, list[XrayTest]] = {}
    skipped: list[tuple[XrayTest, str]] = []

    for t in tests:
        reason = is_unconvertible(t)
        if reason:
            skipped.append((t, reason))
            continue
        prefix = extract_prefix(t.summary)
        slug = cfg.prefix_routing.get(prefix) if prefix else None
        if slug is None:
            slug = cfg.default_bucket  # guaranteed non-None here if we got past validation
        buckets.setdefault(slug, []).append(t)

    # Stable order: by Xray key within each bucket
    for slug in buckets:
        buckets[slug].sort(key=lambda t: t.key)
    skipped.sort(key=lambda x: x[0].key)

    # Write feature files
    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    features_dir = cfg.output_dir
    written: list[str] = []
    for slug, bucket in sorted(buckets.items()):
        scenarios = [render_scenario(t, cfg) for t in bucket]
        content = render_feature_file(slug, scenarios, cfg)
        out_path = features_dir / f"{slug}.feature"
        out_path.write_text(content)
        written.append(f"{slug}.feature ({len(bucket)} scenarios)")

    # Write skipped.md
    skipped_path = cfg.output_dir.parent / "skipped.md"
    if skipped:
        lines = ["# Skipped Xray tests", ""]
        for t, reason in skipped:
            lines.append(f"- {t.key} — {t.summary} — reason: {reason}")
        skipped_path.write_text("\n".join(lines) + "\n")
    elif skipped_path.exists():
        skipped_path.unlink()

    # Account check
    total = len(tests)
    converted = sum(len(b) for b in buckets.values())
    if converted + len(skipped) != total:
        print(
            f"ERROR: accounting mismatch — input {total}, converted {converted}, skipped {len(skipped)}",
            file=sys.stderr,
        )
        return 4

    # Report
    print(f"Input tests: {total}")
    print(f"Converted:   {converted}")
    print(f"Skipped:     {len(skipped)} (see {skipped_path if skipped else 'no skipped.md'})")
    print("Feature files written:")
    for w in written:
        print(f"  {w}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", required=True, type=Path, help="Path to config JSON")
    args = p.parse_args()
    cfg = Config.load(args.config)
    return run(cfg)


if __name__ == "__main__":
    sys.exit(main())
