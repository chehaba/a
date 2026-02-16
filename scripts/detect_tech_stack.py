#!/usr/bin/env python3
"""
Detect technology stack from a website by inspecting HTML.
Fetches URL, parses HTML for meta tags, script src, link href, and known patterns.
Outputs JSON with observed technologies (no guessing—only reported evidence).

Usage:
  python3 scripts/detect_tech_stack.py "https://example.com"
  python3 scripts/detect_tech_stack.py "https://example.com" --json
"""

import argparse
import json
import re
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"

# Patterns: (identifier, list of regex or literal strings that indicate presence)
# Evidence must appear in HTML. No guessing.
TECH_PATTERNS = [
    # Microsoft
    ("SharePoint", [r"/_layouts/", r"/_catalogs/", r"SharePoint", r"sharepoint\.com", r"spoprod-"]),
    ("M365/Microsoft 365", [r"microsoft\.com/.*365", r"office\.com", r"login\.microsoftonline", r"O365", r"Microsoft 365"]),
    ("Azure", [r"azure\.com", r"azurewebsites\.net", r"azurestaticapps"]),
    ("Power BI", [r"powerbi\.com", r"app\.powerbi", r"PowerBIEmbed"]),
    ("Dynamics", [r"dynamics", r"dynamics365", r"crm\.dynamics"]),
    # CMS
    ("WordPress", [r"wp-content", r"wp-includes", r"wordpress", r"/wp-json/"]),
    ("Drupal", [r"Drupal", r"drupal\.org"]),
    ("Sitefinity", [r"Sitefinity", r"sitefinity"]),
    # CRM/Marketing
    ("Salesforce", [r"salesforce", r"force\.com", r"sfdc\.net"]),
    ("HubSpot", [r"hubspot", r"hs-scripts", r"hsforms"]),
    ("Marketo", [r"marketo", r"munchkin"]),
    # E-commerce
    ("Shopify", [r"shopify", r"cdn\.shopify"]),
    # Analytics/Tagging
    ("Google Analytics", [r"google-analytics", r"googletagmanager", r"gtag", r"ga\s*\("]),
    ("Google Tag Manager", [r"googletagmanager\.com/gtm"]),
    # Cloud/CDN
    ("AWS", [r"amazonaws", r"cloudfront\.net"]),
    ("Cloudflare", [r"cloudflare", r"cf-ray"]),
    ("Akamai", [r"akamai"]),
    # Front-end / Meta
    ("React", [r"react\.js", r"react-dom", r"__NEXT_DATA__", r"reactjs"]),
    ("Vue", [r"vue\.js", r"vuejs", r"__nuxt"]),
    ("Angular", [r"angular\.js", r"ng-version", r"ng-app"]),
]


def fetch_html(url: str) -> str | None:
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, OSError) as e:
        return None


def detect_tech(html: str, url: str) -> dict:
    """Inspect HTML and return only observed technologies with evidence."""
    html_lower = html.lower()
    result = {
        "url": url,
        "technologies": [],
        "evidence": {},
        "meta_generator": None,
        "meta_application": None,
    }

    # Meta generator (e.g., WordPress 6.x)
    gen = re.search(r'<meta\s+name=["\']generator["\']\s+content=["\']([^"\']+)["\']', html, re.I)
    if gen:
        result["meta_generator"] = gen.group(1).strip()

    # Meta application-name
    app = re.search(r'<meta\s+name=["\']application-name["\']\s+content=["\']([^"\']+)["\']', html, re.I)
    if app:
        result["meta_application"] = app.group(1).strip()

    for tech_name, patterns in TECH_PATTERNS:
        for pat in patterns:
            if isinstance(pat, str) and re.search(pat, html, re.I):
                if tech_name not in result["technologies"]:
                    result["technologies"].append(tech_name)
                if tech_name not in result["evidence"]:
                    result["evidence"][tech_name] = []
                result["evidence"][tech_name].append(f"matched: {pat[:50]}...")
                break

    # Also check meta generator for known tech
    if result["meta_generator"]:
        gen_val = result["meta_generator"].lower()
        for tech_name, _ in TECH_PATTERNS:
            if tech_name.lower().replace("/", " ").replace("-", " ") in gen_val:
                if tech_name not in result["technologies"]:
                    result["technologies"].append(tech_name)
                result["evidence"][tech_name] = [f"meta generator: {result['meta_generator']}"]

    return result


def main():
    ap = argparse.ArgumentParser(description="Detect tech stack from website HTML")
    ap.add_argument("url", help="URL to inspect")
    ap.add_argument("--json", action="store_true", help="Output JSON only")
    args = ap.parse_args()

    url = args.url
    if not url.startswith("http"):
        url = "https://" + url

    html = fetch_html(url)
    if not html:
        print("ERROR: Could not fetch URL. (Check network, SSL, or try a different URL.)", file=sys.stderr)
        sys.exit(1)

    result = detect_tech(html, url)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print("=" * 60)
    print("TECH STACK DETECTION (Evidence from HTML)")
    print(f"URL: {url}")
    print("=" * 60)
    if result["meta_generator"]:
        print(f"\nMeta generator: {result['meta_generator']}")
    if result["meta_application"]:
        print(f"Meta application: {result['meta_application']}")
    print("\nOBSERVED TECHNOLOGIES")
    print("-" * 40)
    for t in result["technologies"]:
        ev = result["evidence"].get(t, ["—"])
        print(f"  • {t}")
        for e in ev[:2]:
            print(f"    {e}")
    if not result["technologies"]:
        print("  (None detected from inspected HTML)")
    print()


if __name__ == "__main__":
    main()
