#!/usr/bin/env python3
"""
Scrape Affirma.com navigation pages to extract what Affirma does.
Output: data/affirma-services/affirma_what_we_do.md
"""
import re
import time
from pathlib import Path
import urllib.request
import urllib.error

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "data" / "affirma-services"
OUT_FILE = OUT_DIR / "affirma_what_we_do.md"

# Service/capability pages from navigation (exclude blog posts, case studies, images, contact, team)
SERVICE_URLS = [
    "https://www.affirma.com/",
    "https://www.affirma.com/about-affirma/",
    "https://www.affirma.com/ai/",
    "https://www.affirma.com/ai/ai-agent-development/",
    "https://www.affirma.com/ai/ai-content-creation/",
    "https://www.affirma.com/ai/generative-ai/",
    "https://www.affirma.com/ai/machine-learning/",
    "https://www.affirma.com/ai/process-automation/",
    "https://www.affirma.com/application-software-developement/",
    "https://www.affirma.com/application-software-developement/application-modernization/",
    "https://www.affirma.com/application-software-developement/cloud-applications/",
    "https://www.affirma.com/application-software-developement/mobile-applications-development/",
    "https://www.affirma.com/application-software-developement/web-applications/",
    "https://www.affirma.com/data-analytics/",
    "https://www.affirma.com/data-analytics/data-engineering/",
    "https://www.affirma.com/data-analytics/data-visualization/",
    "https://www.affirma.com/data-analytics/marketing-analytics/",
    "https://www.affirma.com/data-analytics/predictive-analytics/",
    "https://www.affirma.com/cloud/",
    "https://www.affirma.com/cloud/cloud-migrations/",
    "https://www.affirma.com/cloud/cloud-strategy-adoption/",
    "https://www.affirma.com/cloud/devops-automation/",
    "https://www.affirma.com/business-process-outsourcing/",
    "https://www.affirma.com/business-process-outsourcing/customer-service-outsourcing-services/",
    "https://www.affirma.com/business-process-outsourcing/help-desk-outsourcing/",
    "https://www.affirma.com/change-management-consulting/",
    "https://www.affirma.com/content-services/",
    "https://www.affirma.com/content-services/content-creation/",
    "https://www.affirma.com/content-services/content-optimization-editorial-support/",
    "https://www.affirma.com/content-services/content-strategy/",
    "https://www.affirma.com/design-services/",
    "https://www.affirma.com/design-services/animation/",
    "https://www.affirma.com/design-services/branding-services/",
    "https://www.affirma.com/design-services/event-design/",
    "https://www.affirma.com/design-services/ux-ui-design/",
    "https://www.affirma.com/design-services/visual-design/",
    "https://www.affirma.com/digital-marketing/",
    "https://www.affirma.com/digital-marketing/audio-video-production/",  # pragma: allowlist secret
    "https://www.affirma.com/digital-marketing/customer-engagement/",
    "https://www.affirma.com/digital-marketing/marketing-automation/",
    "https://www.affirma.com/digital-marketing/product-marketing/",
    "https://www.affirma.com/digital-marketing/social-media-marketing/",
    "https://www.affirma.com/platforms/aws/",
    "https://www.affirma.com/platforms/azure/",
    "https://www.affirma.com/platforms/dynamics-365/",
    "https://www.affirma.com/platforms/hubspot/",
    "https://www.affirma.com/platforms/microsoft-365/",
    "https://www.affirma.com/platforms/optimizely-consulting/",
    "https://www.affirma.com/platforms/power-apps/",
    "https://www.affirma.com/platforms/powerbi/",
    "https://www.affirma.com/platforms/salesforce/",
    "https://www.affirma.com/platforms/servicenow-consulting-services/",
    "https://www.affirma.com/platforms/sharepoint/",
    "https://www.affirma.com/platforms/sitefinity/",
    "https://www.affirma.com/platforms/tableau/",
    "https://www.affirma.com/platforms/wordpress/",
    "https://www.affirma.com/project-mangement-outsourcing/",
    "https://www.affirma.com/research-services/",
    "https://www.affirma.com/search-marketing/",
    "https://www.affirma.com/search-marketing/ppc-consulting-services/",
    "https://www.affirma.com/search-marketing/seo-consulting-services/",
    "https://www.affirma.com/business-marketing-transformation/",
    "https://www.affirma.com/business-marketing-transformation/go-to-market-strategy/",
    "https://www.affirma.com/business-marketing-transformation/marketing-research/",
    "https://www.affirma.com/work-with-affirma/",
]


def extract_text(html: str) -> str:
    """Extract main content from HTML: meta, JSON-LD, and elementor text."""
    parts = []

    # 1. Meta description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', html, re.I)
    if m:
        parts.append(m.group(1).strip())

    # 2. JSON-LD schema description (WebPage)
    m = re.search(r'"description"\s*:\s*"([^"]+)"', html)
    if m and m.group(1) not in ["Technology Consulting &amp; Digital Agency"]:
        desc = m.group(1).replace("\\u0026", "&").replace("&amp;", "&")
        if desc not in parts:
            parts.append(desc)

    # 3. og:description
    m = re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\']([^"\']+)["\']', html, re.I)
    if m and m.group(1) not in [p for p in parts]:
        parts.append(m.group(1).strip())

    # 4. Elementor text - look for elementor-widget-text-editor with <p> content
    for block in re.findall(r'<div[^>]*class="[^"]*elementor-widget-text-editor[^"]*"[^>]*>([\s\S]*?)</div>', html):
        stripped = re.sub(r"<script[^>]*>[\s\S]*?</script>", "", block, flags=re.I)
        stripped = re.sub(r"<[^>]+>", " ", stripped)
        stripped = re.sub(r"\s+", " ", stripped).strip()
        if len(stripped) > 30:
            parts.append(stripped)

    # 5. Any <p> with substantial text (fallback)
    if not parts:
        for p in re.findall(r"<p[^>]*>([^<]+)</p>", html):
            t = p.strip()
            if len(t) > 40 and not t.startswith("http"):
                parts.append(t)

    text = " ".join(parts)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:8000] if text else "(Page content could not be fully extracted)"


def slug_from_url(url: str) -> str:
    """Get page slug from URL."""
    path = url.rstrip("/").replace("https://www.affirma.com", "")
    return path.strip("/") or "home"


def fetch_page(url: str) -> str:
    """Fetch page HTML with polite headers."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; AffirmaScraper/1.0)"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("utf-8", errors="replace")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sections = []

    for i, url in enumerate(SERVICE_URLS):
        slug = slug_from_url(url)
        print(f"[{i+1}/{len(SERVICE_URLS)}] {slug}")
        try:
            html = fetch_page(url)
            text = extract_text(html)
            if len(text) < 50:
                text = "(Page content could not be fully extracted)"
            sections.append((slug, url, text))
            time.sleep(0.5)  # Polite delay
        except Exception as e:
            sections.append((slug, url, f"[Error: {e}]"))
            print(f"  Error: {e}")

    # Build markdown
    lines = [
        "# Affirma — What We Do (from affirma.com navigation)",
        "",
        "**Source:** Scraped from affirma.com service pages",
        "",
        "---",
        "",
    ]

    for slug, url, text in sections:
        title = slug.replace("-", " ").replace("/", " → ").title()
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"**URL:** {url}")
        lines.append("")
        lines.append(text)
        lines.append("")
        lines.append("---")
        lines.append("")

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {OUT_FILE}")


if __name__ == "__main__":
    main()
