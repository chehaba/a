#!/usr/bin/env python3
"""
Enrich lead list with detected tech stack from company websites.
Reads directory.json, fetches each webUrl, runs tech detection, outputs markdown.

Usage:
  python3 scripts/enrich_leads_with_tech.py                      # First 20 URLs (sanity limit)
  python3 scripts/enrich_leads_with_tech.py --limit 5             # Quick test
  python3 scripts/enrich_leads_with_tech.py --no-limit             # All (slow)
  python3 scripts/enrich_leads_with_tech.py --input data/austin-chamber/directory.json
"""

import argparse
import json
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "data" / "austin-chamber" / "directory.json"
DEFAULT_OUT = REPO_ROOT / "reports" / "Austin Leads With Tech Stack.md"


def load_leads(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else []


def detect_tech(url: str) -> dict:
    """Run detect_tech_stack.py and parse JSON output."""
    import subprocess
    script = REPO_ROOT / "scripts" / "detect_tech_stack.py"
    result = subprocess.run(
        [sys.executable, str(script), url, "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {"technologies": [], "evidence": {}, "error": "fetch failed"}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"technologies": [], "evidence": {}, "error": "parse failed"}


def main():
    ap = argparse.ArgumentParser(description="Enrich leads with tech stack from website HTML")
    ap.add_argument("--input", type=str, default=str(DEFAULT_INPUT), help="Input directory.json path")
    ap.add_argument("--out", type=str, default=None, help=f"Output path (default: {DEFAULT_OUT})")
    ap.add_argument("--limit", type=int, default=20, help="Max URLs to scan (0 = no limit)")
    ap.add_argument("--no-limit", action="store_true", help="Scan all URLs")
    ap.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    args = ap.parse_args()

    limit = None if args.no_limit else (args.limit or 20)
    in_path = Path(args.input)
    out_path = Path(args.out) if args.out else DEFAULT_OUT

    if not in_path.exists():
        print(f"ERROR: Input not found: {in_path}", file=sys.stderr)
        sys.exit(1)

    leads = load_leads(in_path)
    # Filter to those with webUrl
    with_url = [l for l in leads if l.get("webUrl") and l["webUrl"].startswith("http")]
    to_scan = with_url[:limit] if limit else with_url

    print(f"Scanning {len(to_scan)} URLs (of {len(with_url)} with URLs)...")

    results = []
    for i, org in enumerate(to_scan):
        url = org["webUrl"]
        print(f"  [{i+1}/{len(to_scan)}] {org.get('title', '')} ...", end=" ", flush=True)
        tech = detect_tech(url)
        tech_list = tech.get("technologies") or []
        if tech.get("error"):
            print(f"FAIL: {tech['error']}")
        else:
            print(", ".join(tech_list) or "(none)")
        results.append({
            "title": org.get("title"),
            "url": url,
            "categories": org.get("categories"),
            "technologies": tech_list,
            "evidence": tech.get("evidence", {}),
        })
        if i < len(to_scan) - 1:
            time.sleep(args.delay)

    # Write markdown
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Austin Leads — Tech Stack Detected",
        "",
        f"**Source:** {in_path}",
        f"**Scanned:** {len(results)} URLs",
        "",
        "---",
        "",
        "| Company | Website | Tech Stack | Categories |",
        "|---------|---------|------------|------------|",
    ]
    for r in results:
        title = (r["title"] or "").replace("|", "\\|")
        url = r["url"]
        tech_str = ", ".join(r["technologies"]) if r["technologies"] else "—"
        cats = (r.get("categories") or "")[:30]
        lines.append(f"| {title} | [link]({url}) | {tech_str} | {cats} |")

    lines.extend([
        "",
        "---",
        "",
        "**Regenerate:** `python3 scripts/enrich_leads_with_tech.py`",
        "",
    ])

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
