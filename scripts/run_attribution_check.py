#!/usr/bin/env python3
"""
Attribution check helper. Fetches a URL, looks for UTM params, forms, landing structure.
Outputs a short report. You add the narrative.
Usage: python3 run_attribution_check.py "https://example.com"
"""

import sys
import re
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"


def fetch_url(url):
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=10) as r:
            return r.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, OSError):
        return None


def run_check(url):
    html = fetch_url(url)
    if not html:
        print("ERROR: Could not fetch URL.")
        return

    # Find links with href
    links = re.findall(r'href=["\']([^"\']+)["\']', html, re.I)
    utm_links = [l for l in links if "utm_" in l.lower()]
    has_utm = len(utm_links) > 0
    form_count = len(re.findall(r"<form[^>]*>", html, re.I))
    has_hidden_source = bool(re.search(r'name=["\'](?:source|utm_source|referrer|how_did_you_hear)["\']', html, re.I))
    distinct_destinations = set()
    for l in links:
        if l.startswith("http") or l.startswith("/"):
            distinct_destinations.add(l.split("?")[0][:80])
    n_dest = len(distinct_destinations)

    print("=" * 60)
    print("ATTRIBUTION CHECK — Structure Extract")
    print(f"URL: {url}")
    print("=" * 60)
    print()
    print("OBSERVED")
    print("-" * 40)
    print(f"  UTM params in links: {'Yes' if has_utm else 'No'} ({len(utm_links)} links with UTM)")
    print(f"  Forms: {form_count}")
    print(f"  Form captures source/hidden field: {'Possible' if has_hidden_source else 'Not found'}")
    print(f"  Distinct link destinations (approx): {min(n_dest, 20)}")
    print()
    print("COMMON GAPS (add those that apply)")
    print("-" * 40)
    if not has_utm:
        print("  • No UTM in links — paid/organic traffic not tagged")
    if form_count > 0 and not has_hidden_source:
        print("  • Forms may not capture lead source")
    print("  • Last-click-only attribution (assume unless told otherwise)")
    print("  • Homepage as ad destination vs dedicated landing pages")
    print()
    print("NEXT STEPS")
    print("-" * 40)
    print("1. Use docs/analysis/Attribution Snapshot Instructions.md to write the snapshot.")
    print("2. Or paste this URL into the AI prompt in that doc.")
    print()


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url.startswith("http"):
        print("Usage: python3 run_attribution_check.py 'https://example.com'")
        sys.exit(1)
    run_check(url)
