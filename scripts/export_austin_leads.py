#!/usr/bin/env python3
"""
Scrape Austin Chamber registry and export leads to a printable markdown document.
Uses scrape_austin_chamber.py internally. Output goes to reports/Austin Registry Leads.md.

Usage:
  python3 scripts/export_austin_leads.py                    # Use existing directory.json
  python3 scripts/export_austin_leads.py --refresh           # Re-scrape, then export
  python3 scripts/export_austin_leads.py --categories 328 323 # Scrape specific categories
  python3 scripts/export_austin_leads.py --out reports/MyLeads.md
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIRECTORY_JSON = REPO_ROOT / "data" / "austin-chamber" / "directory.json"
DEFAULT_OUT = REPO_ROOT / "reports" / "Austin Registry Leads.md"


def load_directory(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else []


def run_scrape(categories: list[int] | None = None, no_filter: bool = False) -> bool:
    """Run scrape_austin_chamber.py. Returns True on success."""
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "scrape_austin_chamber.py")]
    if no_filter:
        cmd.append("--no-filter")
    elif categories:
        cmd.extend(["--categories"] + [str(c) for c in categories])
    else:
        # Default: Health Care (328) + IT (323) for lead gen
        cmd.extend(["--categories", "328", "323"])
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    return result.returncode == 0


def export_markdown(leads: list[dict], out_path: Path, source: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Austin Registry Leads",
        "",
        f"**Source:** {source}",
        f"**Total:** {len(leads)} organizations",
        "",
        "---",
        "",
        "## Lead List",
        "",
        "| # | Company | Website | Categories | Tier | LinkedIn |",
        "|---|---------|---------|------------|------|----------|",
    ]

    for i, org in enumerate(leads, 1):
        title = (org.get("title") or "").replace("|", "\\|")
        web = org.get("webUrl") or ""
        if web:
            label = web.replace("https://", "").replace("http://", "")[:35]
            if len(web) > 35:
                label += "..."
            web_cell = f"[{label}]({web})"
        else:
            web_cell = "—"
        cats = (org.get("categories") or "").replace("|", ", ")[:40]
        tier = org.get("tier") or "—"
        linkedin = org.get("linkedin") or "—"
        lines.append(f"| {i} | {title} | {web_cell} | {cats} | {tier} | {linkedin} |")

    lines.extend([
        "",
        "---",
        "",
        "## Regenerate",
        "",
        "```bash",
        "# Use existing data",
        "python3 scripts/export_austin_leads.py",
        "",
        "# Re-scrape then export",
        "python3 scripts/export_austin_leads.py --refresh",
        "",
        "# Scrape specific categories (328=Health Care, 323=IT & Technology)",
        "python3 scripts/export_austin_leads.py --refresh --categories 328 323",
        "```",
        "",
    ])

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Export Austin Chamber leads to markdown")
    ap.add_argument("--refresh", action="store_true", help="Re-scrape before exporting")
    ap.add_argument("--no-filter", action="store_true", help="When refreshing: fetch all categories")
    ap.add_argument("--categories", type=int, nargs="*", help="When refreshing: category IDs (default: 328, 323)")
    ap.add_argument("--out", type=str, default=None, help=f"Output path (default: {DEFAULT_OUT})")
    args = ap.parse_args()

    out_path = Path(args.out) if args.out else DEFAULT_OUT

    if args.refresh:
        if not run_scrape(args.categories, no_filter=args.no_filter):
            print("ERROR: Scrape failed.", file=sys.stderr)
            sys.exit(1)
        source = "Austin Chamber API (refreshed)"
    else:
        if not DIRECTORY_JSON.exists():
            print("No directory.json found. Run with --refresh first.", file=sys.stderr)
            sys.exit(1)
        source = "data/austin-chamber/directory.json"

    leads = load_directory(DIRECTORY_JSON)
    if not leads:
        print("No leads to export.", file=sys.stderr)
        sys.exit(1)

    export_markdown(leads, out_path, source)
    print(f"Exported {len(leads)} leads to {out_path}")


if __name__ == "__main__":
    main()
