#!/usr/bin/env python3
"""
Analyze ATX leads from data/Inbound/atx leads/ for Modern Workplace and Marketing Services.
Output: Best leads report at reports/ATX Leads Best to Target.md
"""
import pandas as pd
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ATX_DIR = BASE / "data" / "Inbound" / "atx leads"
OUT = BASE / "reports" / "ATX Leads Best to Target.md"

# Modern Workplace: IT infrastructure, SharePoint, M365, cloud migration decision makers
MW_TITLE_PATTERNS = [
    (r"\b(director|vp|vice\s*president)\s+.*\b(it|technology|information\s*systems|infrastructure|cybersecurity)\b", 3),
    (r"\b(cio|cto|chief\s*information)\b", 3),
    (r"\b(director|manager)\s+.*\b(digital\s*systems|business\s*systems|information\s*technology)\b", 3),
    (r"\bhead\s*of\s*business\s*systems\b", 3),
    (r"\b(director|vp).*cloud\b|\bcloud\s*platform\b|\bdelivery\s*engineering\s*director\b", 3),
    (r"\bservicenow\b.*(director|engineering)\b|(director|engineering).*\bservicenow\b", 3),
    (r"\b(director|manager)\s+.*\b(engineering|it)\b.*\b(campus|systems|automation)\b", 2),
    (r"\btechnology\s*director\b|\bmanager.*information\s*technology\b", 3),
    (r"\bmanager.*business\s*applications\b|\bmanager.*campus\s*engineering\b", 2),
    (r"\b(director|vp).*finance\b", 1),  # Sometimes owns systems
]

# Marketing Services: Marketing decision makers
MKT_TITLE_PATTERNS = [
    (r"\b(vp|vice\s*president|director)\s+.*\b(marketing|brand|communications)\b", 3),
    (r"\b(director|manager)\s+.*\b(marketing|brand|digital\s*marketing|product\s*marketing)\b", 3),
    (r"\bhead\s*of\s*(marketing|brand)\b", 3),
    (r"\bchief\s*marketing\s*officer\b|\bcmo\b", 3),
    (r"\bmanager.*(communications|content|social\s*media)\b", 2),
    (r"\b(senior\s*director|director)\s+.*\b(content|social|marketing)\b", 3),
    (r"\bart\s*director\b|\bbrand\s*manager\b", 2),
]

# Industries with better Modern Workplace win rates (from Oops.csv)
MW_STRONG_INDUSTRIES = {"healthcare", "health", "hospital", "medical", "manufacturing", "construction", "energy", "utilities", "government", "education", "non-profit", "finance", "credit union", "bank", "insurance"}

MKT_STRONG_INDUSTRIES = {"retail", "consumer", "software", "tech", "manufacturing", "healthcare", "professional services"}


def is_gatekeeper(title: str) -> bool:
    """Exclude EAs, admins, coordinators — not decision makers."""
    t = str(title or "").lower()
    return bool(re.search(r"\b(executive\s*assistant|admin\s*to|assistant\s*to\s*(the|chief)|chief\s*of\s*staff)\b", t))


def mw_score(title: str, company: str) -> int:
    """Score 0–5 for Modern Workplace fit."""
    if is_gatekeeper(title):
        return 0
    t = str(title or "").lower()
    c = str(company or "").lower()
    score = 0
    for pat, pts in MW_TITLE_PATTERNS:
        if re.search(pat, t, re.I):
            score = max(score, pts)
    if any(ind in c for ind in MW_STRONG_INDUSTRIES):
        score = min(5, score + 1)
    # Downrank pure "Director, Engineering" (software dev) unless other signals
    if re.search(r"\bdirector,?\s*engineering\b", t) and score < 2:
        score = 0
    return score


def mkt_score(title: str, company: str) -> int:
    """Score 0–5 for Marketing Services fit."""
    t = str(title or "").lower()
    c = str(company or "").lower()
    score = 0
    for pat, pts in MKT_TITLE_PATTERNS:
        if re.search(pat, t, re.I):
            score = max(score, pts)
    if any(ind in c for ind in MKT_STRONG_INDUSTRIES):
        score = min(5, score + 1)
    return score


def main():
    # Try both paths: local atx leads or extracted from commit
    local_leads = ATX_DIR / "My Open Leads 2-14-2026 12-04-24 PM.xlsx"
    local_dirs = ATX_DIR / "Directors, Finance and Marketing 2-14-2026 11-55-55 AM.xlsx"
    if not local_leads.exists():
        # Fallback: use /tmp if extracted
        local_leads = Path("/tmp/atx_leads.xlsx")
        local_dirs = Path("/tmp/atx_directors.xlsx")

    leads_df = pd.read_excel(local_leads, sheet_name="My Open Leads")
    directors_df = pd.read_excel(local_dirs, sheet_name=0)

    # Combine
    def row_to_rec(df, col_map, source):
        records = []
        for _, r in df.iterrows():
            name = r.get(col_map.get("name", " Name")) or f"{r.get('First Name','')} {r.get('Last Name','')}".strip()
            records.append({
                "Name": name,
                "Job Title": r.get(col_map.get("title", "Job Title"), ""),
                "Company": r.get(col_map.get("company", "Company Name"), ""),
                "Email": r.get("Email", ""),
            })
            records[-1]["Source"] = source
        return records

    lead_cols = {"name": " Name", "title": "Job Title", "company": "Company Name"}
    dir_cols = {"name": " Name", "title": "Job Title", "company": "Company Name"}
    all_rows = row_to_rec(leads_df, lead_cols, "Open Leads") + row_to_rec(directors_df, dir_cols, "Directors")

    # Dedupe by email
    seen = set()
    unique = []
    for r in all_rows:
        e = (r.get("Email") or "").strip().lower()
        if e and e not in seen:
            seen.add(e)
            unique.append(r)

    # Score
    for r in unique:
        r["MW_Score"] = mw_score(r["Job Title"], r["Company"])
        r["Mkt_Score"] = mkt_score(r["Job Title"], r["Company"])

    mw_best = sorted([r for r in unique if r["MW_Score"] >= 2], key=lambda x: (-x["MW_Score"], x["Company"]))
    mkt_best = sorted([r for r in unique if r["Mkt_Score"] >= 2], key=lambda x: (-x["Mkt_Score"], x["Company"]))

    # Build markdown
    lines = [
        "# ATX Leads — Best to Target",
        "",
        "**Source:** [data/Inbound/atx leads/](https://github.com/chehaba/prospecting/tree/2b4da6298189aedac0adc1a3776c0303955ab45b/data/Inbound/atx%20leads) (Open Leads + Directors, Finance and Marketing)",
        "",
        "**Data:** My Open Leads (1,342 Austin contacts) + Directors, Finance and Marketing (368)",
        "",
        "---",
        "",
        "## Modern Workplace / Cloud Migration (SharePoint, M365)",
        "",
        "Top contacts by title fit: IT Director+, infrastructure, cloud, ServiceNow, business systems.",
        "",
        "### Tier 1 — Contact First",
        "",
        "| # | Name | Company | Title | Email | Why |",
        "|---|-----|---------|------|-------|-----|",
    ]
    for i, r in enumerate(mw_best[:25], 1):
        why = "IT/infrastructure ownership" if r["MW_Score"] >= 3 else "Influencer, execution focus"
        lines.append(f"| {i} | **{r['Name']}** | {r['Company']} | {r['Job Title']} | {r['Email']} | {why} |")

    lines.extend([
        "",
        "### Tier 2 — Strong Influencers",
        "",
        "| Name | Company | Title | Email |",
        "|------|---------|------|-------|",
    ])
    for r in mw_best[25:50]:
        lines.append(f"| {r['Name']} | {r['Company']} | {r['Job Title']} | {r['Email']} |")

    lines.extend([
        "",
        "---",
        "",
        "## Marketing Services (Demand Gen, PPC, HubSpot, Creative)",
        "",
        "Top contacts by title fit: Marketing Director+, Brand, Communications, Content.",
        "",
        "### Tier 1 — Contact First",
        "",
        "| # | Name | Company | Title | Email | Why |",
        "|---|-----|---------|------|-------|-----|",
    ])
    for i, r in enumerate(mkt_best[:25], 1):
        why = "Budget owner for marketing" if r["Mkt_Score"] >= 3 else "Influencer"
        lines.append(f"| {i} | **{r['Name']}** | {r['Company']} | {r['Job Title']} | {r['Email']} | {why} |")

    lines.extend([
        "",
        "### Tier 2 — Strong Influencers",
        "",
        "| Name | Company | Title | Email |",
        "|------|---------|------|-------|",
    ])
    for r in mkt_best[25:50]:
        lines.append(f"| {r['Name']} | {r['Company']} | {r['Job Title']} | {r['Email']} |")

    lines.extend([
        "",
        "---",
        "",
        "## Messaging",
        "",
        "**Modern Workplace:** Use 03 IT Director Ownership or 04 IT Director Drift. Hook: \"Most waste comes from 'nobody owns this system anymore.'\" CTA: \"Worth a 15-min check if you have any orphan systems or drift right now?\"",
        "",
        "**Marketing Services:** Use Marketing Creative or Attribution campaign. Hook: conversion leaks, attribution clarity, creative performance.",
        "",
        "**Channel:** Email first, then LinkedIn. Austin-based angle: \"Austin consulting firm\" for local coffee/call.",
        "",
    ])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Modern Workplace: {len(mw_best)} | Marketing Services: {len(mkt_best)}")


if __name__ == "__main__":
    main()
