#!/usr/bin/env python3
"""
Infer company type from email domain + description.
Build Company Type × Ask × Service → Target Matrix for outbound messaging.
Output: Which company types to target with which service-specific copy.

Usage:
  python3 scripts/company_target_matrix.py                    # uses data/Inbound/Inbound.xlsx
  python3 scripts/company_target_matrix.py path/to/leads.xlsx # custom file (include Email column)

To enable domain-based company inference: Export inbound leads from CRM with Email column.
Domain patterns: .gov→Government, .edu→Education, *health*→Healthcare, etc.
"""

import pandas as pd
import sys
import re
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path(__file__).resolve().parent.parent
INBOUND_PATH = BASE / "data" / "Inbound" / "Inbound.xlsx"

# ----- Ask → Affirma Service mapping (for messaging) -----
ASK_TO_SERVICE = {
    "SharePoint Migration": "Modern Workplace",
    "SharePoint General": "Modern Workplace",
    "SharePoint Restructure": "Modern Workplace",
    "Intranet Build": "Modern Workplace",
    "Power BI": "Data & Analytics",
    "Dashboard/Reporting": "Data & Analytics",
    "Dynamics/CRM": "CRM",
    "HubSpot": "Marketing Services",
    "SEO": "Marketing Services",
    "AI/Copilot": "AI / Automation",
    "Power Automate/Flows": "Modern Workplace",
    "Power Apps": "Modern Workplace",
    "BPO/Helpdesk": "Infrastructure / BPO",
    "Google to M365 Migration": "Infrastructure",
    "Tenant/M365 Migration": "Infrastructure",
    "Exchange Migration": "Infrastructure",
    "Compliance/Purview": "Modern Workplace",
    "Guidance/Consulting": "Modern Workplace",  # broad
    "Training": "Modern Workplace",
    "Ongoing Support": "Infrastructure",
    "Migration (general)": "Infrastructure",
    "RFP/Quote": "—",  # depends
    "Other": "—",
}


# ----- Domain → Company Type (when Email available) -----
def domain_to_company_type(domain):
    """Infer company type from email domain. Returns None if unknown."""
    if pd.isna(domain) or not str(domain).strip():
        return None
    d = str(domain).lower().strip()
    # TLD-based
    if d.endswith(".gov") or d.endswith(".gov.au") or ".gov." in d:
        return "Government"
    if d.endswith(".edu") or ".edu." in d:
        return "Education"
    if d.endswith(".mil"):
        return "Government"
    if d.endswith(".org"):
        return "Non-Profit"  # heuristic; some .org are for-profit
    # Domain name patterns (company part before TLD)
    base = d.split("/")[0].split(".")[0] if "." in d else d
    patterns = [
        (r"health|medical|hospital|clinic|care|patient|physician|healthcare", "Healthcare"),
        (r"city|county|state|town|borough|municipal|gov", "Government"),
        (r"school|univ|college|edu|district", "Education"),
        (r"bank|financial|capital|insurance|fmo|imo", "Financial Services"),
        (r"law|legal|attorney|counsel", "Legal"),
        (r"construction|contractor|build|realty|realestate", "Construction"),
        (r"mfg|manufacturing|industrial", "Manufacturing"),
        (r"msp|managedservice|tekhero", "MSP"),
    ]
    for pat, ctype in patterns:
        if re.search(pat, base):
            return ctype
    return "Commercial"  # generic for .com when no pattern matches


def extract_domain(email):
    """Extract domain from email address."""
    if pd.isna(email) or "@" not in str(email):
        return None
    return str(email).strip().split("@")[-1].lower()


# ----- Industry from description (fallback when no Email) -----
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


def extract_industry_from_desc(text):
    if pd.isna(text):
        return None
    t = str(text).lower()
    for pattern, label in INDUSTRY_PATTERNS:
        if re.search(pattern, t, re.I):
            return label
    return None


# ----- Ask extraction (simplified, reuse deep_parse logic) -----
CATEGORY_PATTERNS = [
    ("SharePoint Migration", r"\b(?:migrat|moving|move)\b.*\b(?:sharepoint|sp\s*online|file\s*server|box|google\s*drive)\b|\b(?:sharepoint|sp)\b.*\b(?:migrat|on[\s\-]?prem|2016|2019)\b"),
    ("Intranet Build", r"\b(?:intranet|hub\s*site|landing\s*page)\b.*\b(?:build|create|design)\b|\b(?:build|create)\b.*\b(?:intranet|sharepoint\s*site)\b"),
    ("SharePoint Restructure", r"\b(?:restructur|reorganiz|optimiz|refresh|moderniz)\b.*\b(?:sharepoint|intranet)\b"),
    ("SharePoint General", r"\b(?:sharepoint|sp\s*online|spo)\b"),
    ("Power BI", r"\b(?:power\s*bi|powerbi)\b"),
    ("Power Automate/Flows", r"\b(?:power\s*automate|flows?|workflow)\b"),
    ("Power Apps", r"\b(?:power\s*apps?|power\s*pages?)\b"),
    ("Dynamics/CRM", r"\b(?:dynamics\s*365|d365|business\s*central|bc\s*365|crm\b|salesforce)\b"),
    ("AI/Copilot", r"\b(?:copilot|ai\s+(?:strategy|consultant|solution|roadmap)|chatgpt|generative\s+ai)\b"),
    ("Google to M365 Migration", r"\b(?:google\s*workspace|g\s*suite|gmail)\b.*\b(?:microsoft|m365|office\s*365)\b"),
    ("Tenant/M365 Migration", r"\b(?:tenant|tenant[\s\-]?to[\s\-]?tenant|t2t|merge\s*tenant)\b"),
    ("Exchange Migration", r"\b(?:exchange\s*(?:migration|migrat)|intermedia)\b"),
    ("HubSpot", r"\b(?:hubspot|hub\s*spot)\b"),
    ("BPO/Helpdesk", r"\b(?:helpdesk|help\s*desk|call\s*center|outsourc.*(?:support|customer)|24/7|noc|soc)\b"),
    ("Compliance/Purview", r"\b(?:purview|cmmc|hipaa|pii|dlp|compliance)\b"),
    ("Training", r"\b(?:training|new\s*hire)\b"),
    ("Ongoing Support", r"\b(?:ongoing|maintain|maintenance|managed\s*service)\b"),
    ("RFP/Quote", r"\b(?:rfp|quote|proposal|bid)\b"),
    ("SEO", r"\b(?:seo|search\s*engine)\b"),
    ("Migration (general)", r"\b(?:migrat|migration)\b"),
    ("Dashboard/Reporting", r"\b(?:dashboard|report(?:ing)?|kpi|analytics)\b"),
    ("Guidance/Consulting", r"\b(?:guidance|consulting|partner|assessment)\b"),
]


def get_ask(text):
    if pd.isna(text):
        return "Other"
    t = str(text).lower()
    for name, pattern in CATEGORY_PATTERNS:
        if re.search(pattern, t, re.I):
            return name
    return "Other"


# ----- Service-specific phrase (replace "this investment") -----
SERVICE_PHRASES = {
    "Modern Workplace": "this SharePoint migration",  # or "this intranet build", "this M365 optimization"
    "Data & Analytics": "this Power BI deployment",
    "CRM": "this Dynamics implementation",
    "Marketing Services": "this HubSpot setup",
    "AI / Automation": "this AI rollout",
    "Infrastructure": "this migration",
    "Infrastructure / BPO": "this helpdesk outsourcing",
}


def main():
    path = INBOUND_PATH
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return
    # Support both Excel and CSV
    if str(path).lower().endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path, sheet_name="Inbound For Help")
    n = len(df)

    # Add columns
    df["Ask"] = df["Description"].apply(get_ask)
    df["Service"] = df["Ask"].map(ASK_TO_SERVICE)
    df["Industry_Desc"] = df["Description"].apply(extract_industry_from_desc)

    # Company type: from Email domain if present, else from description
    has_email = "Email" in df.columns
    if has_email:
        df["Domain"] = df["Email"].apply(extract_domain)
        df["Company_Type"] = df["Domain"].apply(domain_to_company_type)
    else:
        df["Company_Type"] = df["Industry_Desc"]

    # Fallback: use Industry_Desc when Company_Type from domain is Commercial/None
    if has_email:
        mask = (df["Company_Type"].isna()) | (df["Company_Type"] == "Commercial")
        df.loc[mask, "Company_Type"] = df.loc[mask, "Industry_Desc"]
    df["Company_Type"] = df["Company_Type"].fillna("Unknown")

    # ----- Output -----
    lines = []
    lines.append("=" * 70)
    lines.append("COMPANY TYPE × ASK × SERVICE — Target Matrix")
    lines.append("=" * 70)
    lines.append(f"\nData: {path.name} ({n} leads)")
    lines.append(f"Email column: {'Yes — using domain inference' if has_email else 'No — using Industry from description only'}")
    lines.append("")

    # 1. Company Type × Ask (counts)
    ct_ask = df[df["Company_Type"] != "Unknown"].groupby(["Company_Type", "Ask"]).size().reset_index(name="Count")
    ct_ask = ct_ask.sort_values(["Company_Type", "Count"], ascending=[True, False])
    lines.append("\n--- Company Type × Ask (use for targeting) ---")
    for ct in ct_ask["Company_Type"].unique():
        sub = ct_ask[ct_ask["Company_Type"] == ct]
        total = sub["Count"].sum()
        lines.append(f"\n  {ct} (n={total}):")
        for _, row in sub.head(5).iterrows():
            svc = ASK_TO_SERVICE.get(row["Ask"], "—")
            lines.append(f"    - {row['Ask']:30} → {svc:25} ({row['Count']})")

    # 2. Target recommendations: Company Type → Service → Message phrase
    lines.append("\n" + "=" * 70)
    lines.append("TARGET RECOMMENDATIONS — Which companies get which service message")
    lines.append("=" * 70)
    for ct in sorted(ct_ask["Company_Type"].unique()):
        sub = df[df["Company_Type"] == ct]
        top_asks = sub["Ask"].value_counts().head(3)
        services = [ASK_TO_SERVICE.get(a, "—") for a in top_asks.index if ASK_TO_SERVICE.get(a) != "—"]
        services = list(dict.fromkeys(services))[:2]  # unique, max 2
        phrases = [SERVICE_PHRASES.get(s, f"this {s.lower()} engagement") for s in services if s in SERVICE_PHRASES]
        lines.append(f"\n  Target {ct}:")
        lines.append(f"    Top asks: {', '.join(top_asks.index[:3].tolist())}")
        lines.append(f"    Services to message: {', '.join(services) if services else '—'}")
        lines.append(f"    Say \"{phrases[0]}\" not \"this investment\"" if phrases else "    (Use generic financial lever)")

    # 3. Ask → Service phrase table
    lines.append("\n" + "=" * 70)
    lines.append("SERVICE-SPECIFIC PHRASES — Replace 'this investment' in copy")
    lines.append("=" * 70)
    for ask, svc in sorted(ASK_TO_SERVICE.items(), key=lambda x: (x[1], x[0])):
        if svc == "—":
            continue
        phrase = SERVICE_PHRASES.get(svc, f"this {svc.lower()} engagement")
        lines.append(f"  {ask:35} → \"{phrase}\"")

    result = "\n".join(lines)
    print(result)
    return result


if __name__ == "__main__":
    main()
