#!/usr/bin/env python3
"""
Conversion teardown helper. Fetches a URL, extracts structure (forms, CTAs, headings),
outputs a checklist. You add the 3 fixes and one-pager copy.
Usage: python3 run_conversion_teardown.py "https://example.com/landing-page"
"""

import sys
import re
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import re as re_module

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"


def fetch_url(url):
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=10) as r:
            return r.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, OSError) as e:
        return None


def count_fields(html):
    """Count form fields."""
    inp = re_module.findall(r'<input[^>]+type="?(?:text|email|tel|hidden)"?', html, re_module.I)
    return len(inp)


def run_teardown(url):
    html = fetch_url(url)
    if not html:
        print("ERROR: Could not fetch URL. Check URL and network.")
        return

    # Extract via regex
    title_m = re_module.search(r"<title[^>]*>([^<]+)</title>", html, re_module.I | re_module.DOTALL)
    title = (title_m.group(1).strip()[:60] + "...") if title_m else "N/A"
    n_fields = count_fields(html)
    has_form = "<form" in html.lower()
    cta_keywords = ["sign", "join", "get", "start", "try", "demo", "contact", "submit", "download", "request"]
    cta_count = sum(1 for _ in re_module.finditer(r'<a[^>]+>[^<]*(' + "|".join(cta_keywords) + r')', html, re_module.I))
    cta_count += len(re_module.findall(r'<button[^>]*>', html, re_module.I))
    cta_count += len(re_module.findall(r'<input[^>]+type="?(?:submit|button)"?', html, re_module.I))
    speed_note = "Check PageSpeed Insights: https://pagespeed.web.dev/"

    print("=" * 60)
    print("CONVERSION TEARDOWN — Structure Extract")
    print(f"URL: {url}")
    print("=" * 60)
    print()
    print("CHECKLIST (review and add Pass/Fail)")
    print("-" * 40)
    print(f"  [ ] Clear value prop (title): {title}")
    print(f"  [ ] Single primary CTA: {cta_count} CTA-like elements found")
    print(f"  [ ] Form present: {'Yes' if has_form else 'No'}")
    print(f"  [ ] Form fields (3-5 ideal): {n_fields} visible inputs")
    print(f"  [ ] Page speed: {speed_note}")
    print()
    print("NEXT STEPS")
    print("-" * 40)
    print("1. Manually review the page for: headline match, trust signals, mobile.")
    print("2. Pick the 3 biggest leaks from your checklist.")
    print("3. Use docs/analysis/Conversion Teardown Instructions.md to write the one-pager.")
    print("4. Or paste this URL into the AI prompt in that doc.")
    print()


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url.startswith("http"):
        print("Usage: python3 run_conversion_teardown.py 'https://example.com/landing-page'")
        sys.exit(1)
    run_teardown(url)
