#!/usr/bin/env python3
"""
Analyze data/Inbound/Inbound.xlsx — why qualified leads come in.
Outputs messaging insights for frameworks.
"""

import pandas as pd
import re
from pathlib import Path
from collections import Counter

INBOUND_PATH = Path(__file__).resolve().parent.parent / "data" / "Inbound" / "Inbound.xlsx"


def categorize(text):
    if pd.isna(text):
        return "Other"
    t = str(text).lower()
    if re.search(r"\b(?:copilot|ai\s+solution|artificial\s+intelligence|ai\s+consultant)\b", t):
        return "AI/Copilot"
    if re.search(r"\b(?:migrat|migration|migrating)\b", t):
        return "Migration"
    if re.search(r"\b(?:power\s*bi|powerbi|power\s*automate|dynamics|d365|crm\b|flow)\b", t):
        return "Power Platform"
    if re.search(r"\b(?:intranet|sharepoint\s+(?:page|build|site|restructure))\b", t):
        return "SharePoint/Intranet"
    if re.search(r"\b(?:purview|compliance|cmmc|hipaa|pii|sensitive\s+data|dlp)\b", t):
        return "Compliance/Data"
    if re.search(r"\b(?:training|new\s+hire)\b", t):
        return "Training"
    if re.search(r"\b(?:support|ongoing|maintain)\b", t):
        return "Support/Maintenance"
    if re.search(r"\b(?:dashboard|analytics|report|visualiz)\b", t):
        return "Analytics/Dashboard"
    if re.search(r"\b(?:seo|hubspot|marketing)\b", t):
        return "Marketing/SEO"
    return "Other"


def main():
    if not INBOUND_PATH.exists():
        print(f"Inbound file not found: {INBOUND_PATH}")
        return

    df = pd.read_excel(INBOUND_PATH, sheet_name="Inbound For Help")
    df["Category"] = df["Description"].apply(categorize)

    print("=" * 60)
    print("INBOUND ANALYSIS — Why Qualified Leads Come In")
    print("=" * 60)
    print(f"\nTotal: {len(df)} qualified leads")
    print("\nCategory distribution:")
    for cat, cnt in Counter(df["Category"]).most_common():
        pct = 100 * cnt / len(df)
        print(f"  {cnt:4} ({pct:5.1f}%) | {cat}")

    print("\nSource Campaign:")
    for src, cnt in df["Source Campaign"].value_counts().head(8).items():
        print(f"  {cnt:4} | {src}")

    # Language
    phrases = []
    for d in df["Description"].fillna(""):
        d = str(d).lower()
        if "looking for" in d:
            phrases.append("looking for")
        if "need help" in d:
            phrases.append("need help")
        if "migrat" in d:
            phrases.append("migrate")
        if "partner" in d:
            phrases.append("partner")
        if "guidance" in d:
            phrases.append("guidance")
    print("\nLanguage they use:")
    for p, c in Counter(phrases).most_common(8):
        print(f"  {c:4} | {p}")
    print("\nSee reports/Inbound Analysis Report.md for full insights.")


if __name__ == "__main__":
    main()
