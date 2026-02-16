#!/usr/bin/env python3
"""
Scrape Austin Chamber of Commerce Member Directory.
Uses public API: https://www.austinchamber.com/api/v1/directory

Usage:
  python3 scripts/scrape_austin_chamber.py                    # all categories
  python3 scripts/scrape_austin_chamber.py --categories 328   # Health Care only
  python3 scripts/scrape_austin_chamber.py --categories 323  # Computers, IT & Technology
  python3 scripts/scrape_austin_chamber.py --categories 328 323  # multiple
"""

import argparse
import json
import time
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

BASE_URL = "https://www.austinchamber.com/api/v1/directory"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "austin-chamber"


def fetch_page(categories: list[int], page: int = 1, per_page: int = 50) -> dict:
    if requests is None:
        raise RuntimeError("Install requests: pip install requests")
    params = {"page": page, "perPage": per_page}
    if categories:
        params["categories"] = ",".join(map(str, categories))
    r = requests.get(BASE_URL, params=params, timeout=30, headers={"Accept": "application/json"})
    r.raise_for_status()
    return r.json()


def parse_org(item: dict) -> dict:
    addr = item.get("address") or {}
    cats = item.get("category") or []
    tier = item.get("tier") or {}
    return {
        "id": item.get("id"),
        "title": item.get("title"),
        "slug": item.get("slug"),
        "tier": tier.get("name", ""),
        "description": (item.get("directoryDescription") or "").strip() or None,
        "street1": addr.get("street1"),
        "street2": addr.get("street2"),
        "city": addr.get("city"),
        "state": addr.get("state"),
        "zip": addr.get("zip"),
        "phone": item.get("phone"),
        "webUrl": item.get("webUrl"),
        "linkedin": (item.get("social") or {}).get("linkedin"),
        "categories": ", ".join(c.get("title", "") for c in cats if c.get("title")),
        "category_ids": ", ".join(str(c.get("id", "")) for c in cats),
    }


def scrape(categories: list[int], max_pages: int | None = None, delay: float = 0.15, filter_category: bool = True) -> list[dict]:
    all_items = []
    page = 1
    cat_set = set(str(c) for c in categories) if categories else None
    while True:
        data = fetch_page(categories, page=page)
        items = data.get("data") or []
        for item in items:
            parsed = parse_org(item)
            if cat_set and filter_category:
                ids = (parsed.get("category_ids") or "").replace(" ", "").split(",")
                if not any(cid.strip() in cat_set for cid in ids if cid.strip()):
                    continue
            all_items.append(parsed)
        links = data.get("links") or {}
        last = links.get("last") or {}
        href = last.get("href", "") if isinstance(last, dict) else str(last)
        if not href or "page=" not in href:
            break
        try:
            last_page = int(href.split("page=")[-1].split("&")[0])
        except (IndexError, ValueError):
            last_page = page
        if page >= last_page:
            break
        if max_pages and page >= max_pages:
            break
        page += 1
        time.sleep(delay)
    return all_items


def main():
    ap = argparse.ArgumentParser(description="Scrape Austin Chamber directory")
    ap.add_argument("--categories", type=int, nargs="*", default=[328],
                    help="Category IDs to filter (default 328=Health Care). 323=IT & Technology. Empty = no filter.")
    ap.add_argument("--no-filter", action="store_true", help="Fetch all; ignore category filter")
    ap.add_argument("--max-pages", type=int, default=None, help="Limit pages (for testing)")
    ap.add_argument("--out", type=str, default=None, help="Output path (default: data/austin-chamber/)")
    args = ap.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else OUTPUT_DIR / "directory.json"

    use_filter = not args.no_filter and args.categories
    print(f"Fetching categories: {args.categories if use_filter else 'all (no filter)'}")
    items = scrape(args.categories if use_filter else [], max_pages=args.max_pages, filter_category=use_filter)
    print(f"Collected {len(items)} organizations")

    out_path.write_text(json.dumps(items, indent=2), encoding="utf-8")
    print(f"Saved to {out_path}")

    # Also CSV for easy use
    if items:
        import csv
        csv_path = out_path.with_suffix(".csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=items[0].keys(), extrasaction="ignore")
            w.writeheader()
            w.writerows(items)
        print(f"CSV saved to {csv_path}")


if __name__ == "__main__":
    main()
