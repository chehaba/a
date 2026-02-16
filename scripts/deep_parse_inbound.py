#!/usr/bin/env python3
"""
Deep parse of data/Inbound/Inbound.xlsx — granular categories, titles, industries, pain points.
Feeds reports/Inbound What They Want.md
"""

import pandas as pd
import re
from pathlib import Path
from collections import Counter, defaultdict

INBOUND_PATH = Path(__file__).resolve().parent.parent / "data" / "Inbound" / "Inbound.xlsx"


# ----- Granular "What They Want" categories (priority order) -----
CATEGORY_PATTERNS = [
    ("SharePoint Migration", r"\b(?:migrat|moving|move)\b.*\b(?:sharepoint|sp\s*online|spo|file\s*server|box|google\s*drive|onedrive)\b|\b(?:sharepoint|sp)\b.*\b(?:migrat|on[\s\-]?prem|2016|2019)\b", None),
    ("Intranet Build", r"\b(?:intranet|hub\s*site|landing\s*page|homesite)\b.*\b(?:build|create|design|implement|develop)\b|\b(?:build|create|design)\b.*\b(?:intranet|sharepoint\s*site)\b", None),
    ("SharePoint Restructure", r"\b(?:restructur|reorganiz|optimiz|refresh|moderniz|cleanup)\b.*\b(?:sharepoint|intranet)\b|\b(?:sharepoint)\b.*\b(?:restructur|permission|governance)\b", None),
    ("SharePoint General", r"\b(?:sharepoint|sp\s*online|spo)\b", None),
    ("Power BI", r"\b(?:power\s*bi|powerbi)\b", None),
    ("Power Automate/Flows", r"\b(?:power\s*automate|power\s*automation|flows?|workflow)\b", None),
    ("Power Apps", r"\b(?:power\s*apps?|power\s*pages?)\b", None),
    ("Dynamics/CRM", r"\b(?:dynamics\s*(?:365|365\s*ce|365\s*f&o)?|d365|business\s*central|bc\s*365|crm\b|salesforce)\b", None),
    ("AI/Copilot", r"\b(?:copilot|ai\s+(?:strategy|consultant|solution|roadmap|implementation)|artificial\s+intelligence|chatgpt|generative\s+ai)\b", None),
    ("Google to M365 Migration", r"\b(?:google\s*workspace|g\s*suite|gmail|google\s*drive)\b.*\b(?:microsoft|m365|office\s*365|o365)\b|\b(?:migrat|move)\b.*\b(?:google|gmail)\b.*\b(?:microsoft|365)\b", None),
    ("Tenant/M365 Migration", r"\b(?:tenant|tenant[\s\-]?to[\s\-]?tenant|t2t|merge\s*tenant)\b", None),
    ("Exchange Migration", r"\b(?:exchange\s*(?:migration|migrat)|intermedia|email\s*migration)\b", None),
    ("HubSpot", r"\b(?:hubspot|hub\s*spot)\b", None),
    ("BPO/Helpdesk", r"\b(?:helpdesk|help\s*desk|call\s*center|customer\s*service\s*(?:outsourc|support)|outsourc(?:e|ing).*(?:support|customer|it\s*support)|level\s*[12]\s*(?:support|helpdesk)|24/7|noc|soc|bp[o]?)\b", None),
    ("Compliance/Purview", r"\b(?:purview|cmmc|hipaa|pii|sensitivity\s*label|dlp|compliance|data\s*governance)\b", None),
    ("Training", r"\b(?:training|train\s*the\s*trainer|new\s*hire)\b", None),
    ("Ongoing Support", r"\b(?:ongoing|maintain|maintenance|support\s*(?:contract|ongoing)|managed\s*service)\b", None),
    ("RFP/Quote", r"\b(?:rfp|quote|proposal|bid|solicit)\b", None),
    ("SEO", r"\b(?:seo|search\s*engine)\b", None),
    ("Migration (general)", r"\b(?:migrat|migration|migrating)\b", None),
    ("Dashboard/Reporting", r"\b(?:dashboard|report(?:ing)?|kpi|analytics)\b", None),
    ("Guidance/Consulting", r"\b(?:guidance|consulting|consultant|partner|assessment|discovery)\b", None),
]


def get_primary_category(text):
    """Return first matching category, else Other."""
    if pd.isna(text):
        return "Other"
    t = str(text).lower()
    for name, pattern, _ in CATEGORY_PATTERNS:
        if re.search(pattern, t, re.I):
            return name
    return "Other"


# ----- Title extraction from description -----
TITLE_PATTERNS = [
    (r"\b(?:it\s*)?director\b", "Director"),
    (r"\bdirector\s+of\s+(?:it|technology|operations|business\s*intelligence)\b", "Director"),
    (r"\b(?:it\s*)?manager\b", "Manager"),
    (r"\bmarketing\s*manager\b", "Marketing Manager"),
    (r"\bhr\s*(?:and\s*)?ops?\s*manager\b", "HR/Ops Manager"),
    (r"\bconsultant\b", "Consultant"),
    (r"\bowner\b", "Owner"),
    (r"\bcto\b", "CTO"),
    (r"\bceo\b", "CEO"),
    (r"\bcfo\b", "CFO"),
    (r"\bsoftware\s*developer\b", "Software Developer"),
    (r"\bproject\s*manager\b", "Project Manager"),
    (r"\bprogram\s*manager\b", "Program Manager"),
    (r"\boperations\s*coordinator\b", "Operations Coordinator"),
    (r"\b(?:chief\s*)?of\s*staff\b", "Chief of Staff"),
    (r"\barchitect\b", "Architect"),
    (r"\bengineer\b", "Engineer"),
]


def extract_title(text):
    """Extract first matching title from description."""
    if pd.isna(text):
        return None
    t = str(text)
    for pattern, label in TITLE_PATTERNS:
        m = re.search(pattern, t, re.I)
        if m:
            return label
    return None


# ----- Industry/vertical hints (from description) -----
INDUSTRY_PATTERNS = [
    (r"\b(?:healthcare|hospital|medical|patient|clinical|physician)\b", "Healthcare"),
    (r"\b(?:non[\s\-]?profit|501c3|ngo)\b", "Non-Profit"),
    (r"\b(?:government|municipal|city\s+of|county|federal)\b", "Government"),
    (r"\b(?:financial\s*services|bank|insurance|fmo|imo)\b", "Financial Services"),
    (r"\b(?:manufacturing|manufacturer)\b", "Manufacturing"),
    (r"\b(?:construction|contractor|general\s*contractor)\b", "Construction"),
    (r"\b(?:legal|law\s*firm|attorney)\b", "Legal"),
    (r"\b(?:education|school|university|district)\b", "Education"),
    (r"\b(?:real\s*estate|property)\b", "Real Estate"),
    (r"\b(?:msp|managed\s*service)\b", "MSP"),
]


def extract_industry(text):
    if pd.isna(text):
        return None
    t = str(text).lower()
    for pattern, label in INDUSTRY_PATTERNS:
        if re.search(pattern, t, re.I):
            return label
    return None


# ----- Pain point / urgency language -----
PAIN_PHRASES = [
    r"\b(?:information\s*overload|so\s*many\s*options)\b",
    r"\b(?:messy|cluttered|out\s*of\s*control|chaos)\b",
    r"\b(?:no\s*one\s*owns|nobody\s*owns|orphaned)\b",
    r"\b(?:lost\s*(?:our|the)\s*expert|expert\s*left)\b",
    r"\b(?:lean\s*team|limited\s*resources|no\s*internal\s*it)\b",
    r"\b(?:end\s*of\s*life|eol|sunset)\b",
    r"\b(?:asap|urgent|immediately)\b",
    r"\b(?:inherited\s*(?:a|an)\s*mess)\b",
    r"\b(?:doesn'?t\s*work|not\s*working|broken)\b",
    r"\b(?:struggl|challenge|difficult)\b",
]


def extract_pain_flags(text):
    if pd.isna(text):
        return []
    t = str(text).lower()
    flags = []
    labels = [
        "information overload", "messy/cluttered", "no owner", "expert left",
        "lean team", "end of life", "urgent", "inherited mess", "broken", "struggling"
    ]
    for i, pat in enumerate(PAIN_PHRASES):
        if re.search(pat, t, re.I) and i < len(labels):
            flags.append(labels[i])
    return flags


def main():
    if not INBOUND_PATH.exists():
        print(f"Inbound file not found: {INBOUND_PATH}")
        return

    df = pd.read_excel(INBOUND_PATH, sheet_name="Inbound For Help")
    n = len(df)

    # Apply categorizations
    df["Ask"] = df["Description"].apply(get_primary_category)
    df["Title"] = df["Description"].apply(extract_title)
    df["Industry"] = df["Description"].apply(extract_industry)
    df["PainFlags"] = df["Description"].apply(extract_pain_flags)

    # ----- Output sections -----
    lines = []

    lines.append("=" * 70)
    lines.append("DEEP PARSE — Inbound What They Want")
    lines.append("=" * 70)
    lines.append(f"\nTotal: {n} qualified leads\n")

    # 1. Granular Ask distribution
    ask_counts = df["Ask"].value_counts()
    lines.append("\n--- Ask Distribution (granular) ---")
    for ask, cnt in ask_counts.items():
        pct = 100 * cnt / n
        lines.append(f"  {cnt:4} ({pct:5.1f}%) | {ask}")

    # 2. Title × Ask cross-tab (only where title extracted)
    titled = df[df["Title"].notna()]
    if len(titled) > 0:
        lines.append("\n--- Title × Ask (n={}) ---".format(len(titled)))
        tab = titled.groupby(["Title", "Ask"]).size().reset_index(name="Count")
        tab = tab.sort_values(["Title", "Count"], ascending=[True, False])
        for _, row in tab.iterrows():
            lines.append(f"  {row['Title']:25} | {row['Ask']:30} | {row['Count']}")

    # 3. Industry × Ask (where industry extracted)
    industry_df = df[df["Industry"].notna()]
    if len(industry_df) > 0:
        lines.append("\n--- Industry × Ask (n={}) ---".format(len(industry_df)))
        ind_ask = industry_df.groupby(["Industry", "Ask"]).size().reset_index(name="Count")
        ind_ask = ind_ask.sort_values(["Industry", "Count"], ascending=[True, False])
        for _, row in ind_ask.iterrows():
            lines.append(f"  {row['Industry']:20} | {row['Ask']:30} | {row['Count']}")

    # 4. Source Campaign × Top Asks
    lines.append("\n--- Source Campaign × Top Ask ---")
    for src in df["Source Campaign"].dropna().unique()[:8]:
        sub = df[df["Source Campaign"] == src]
        top = sub["Ask"].value_counts().head(3)
        lines.append(f"  {src}:")
        for ask, cnt in top.items():
            lines.append(f"    - {ask}: {cnt}")

    # 5. Pain point frequency
    all_pains = []
    for flags in df["PainFlags"]:
        all_pains.extend(flags)
    if all_pains:
        lines.append("\n--- Pain Point Language (frequency) ---")
        for pain, cnt in Counter(all_pains).most_common(12):
            lines.append(f"  {cnt:4} | {pain}")

    # 6. Employee size bands (if available)
    if "No. of Employees" in df.columns:
        emp = df["No. of Employees"].dropna()
        emp = pd.to_numeric(emp, errors="coerce").dropna()
        if len(emp) > 0:
            bands = pd.cut(emp, bins=[0, 50, 200, 500, 5000, float("inf")],
                           labels=["1–50", "51–200", "201–500", "501–5K", "5K+"])
            lines.append("\n--- Employee Size Band (where available) ---")
            for band, cnt in bands.value_counts().sort_index().items():
                pct = 100 * cnt / len(emp)
                lines.append(f"  {cnt:4} ({pct:5.1f}%) | {band}")

    # 7. Ask pairs (multiple categories per lead — secondary)
    lines.append("\n--- Secondary Ask Signals (Power BI + Migration, etc.) ---")
    pbi_mig = df["Description"].str.contains(r"power\s*bi|powerbi", case=False, na=False) & \
              df["Description"].str.contains(r"migrat|tableau|sap\s*business\s*object", case=False, na=False)
    lines.append(f"  Power BI + migration/legacy replacement: {pbi_mig.sum()}")
    sp_ai = df["Description"].str.contains(r"sharepoint|intranet", case=False, na=False) & \
            df["Description"].str.contains(r"copilot|ai\s", case=False, na=False)
    lines.append(f"  SharePoint + AI/Copilot: {sp_ai.sum()}")

    result = "\n".join(lines)
    print(result)
    return result, df


if __name__ == "__main__":
    main()
