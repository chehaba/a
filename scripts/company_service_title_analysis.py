#!/usr/bin/env python3
"""
Company Type × Service × Buyer Title pattern analysis.
Channel-agnostic. Focus on WHO (company, title) buys WHAT (service) + topics, descriptions, inbound language.

Output: Structured datasets for targeting — Company × Service × Title with:
  - win rate, volume
  - inbound_asks (what they say they want)
  - case_study_topics (project descriptions, pains)
  - service_notes (topics, themes)
"""

import csv
import json
import re
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).resolve().parent.parent
OPS_PATH = BASE / "data" / "opportunities" / "Oops.csv"
INBOUND_PATH = BASE / "data" / "Inbound" / "Inbound.xlsx"
ASSETS = BASE / "assets"
OUT_DIR = BASE / "data" / "patterns"

# Normalize industry to company type
INDUSTRY_TO_COMPANY_TYPE = {
    "Non-Profit": "Non-Profit",
    "Government": "Government",
    "Healthcare": "Healthcare",
    "Education": "Education",
    "Finance": "Financial Services",
    "Financial Services": "Financial Services",
    "Business Services": "Commercial",
    "Software": "Technology",
    "Manufacturing": "Manufacturing",
    "Construction": "Construction",
    "Telecommunications": "Technology",
    "Consumer Services": "Commercial",
    "Organizations": "Commercial",
    "Insurance": "Financial Services",
    "Agriculture": "Agriculture",
    "Energy, Utilities, Waste Treatment": "Energy / Utilities",
    "Hospitaity": "Hospitality",
}

# Ask (inbound) → Service
ASK_TO_SERVICE = {
    "SharePoint General": "Modern Workplace",
    "SharePoint Migration": "Modern Workplace",
    "SharePoint Restructure": "Modern Workplace",
    "Intranet Build": "Modern Workplace",
    "Power BI": "Data & Analytics",
    "Dashboard/Reporting": "Data & Analytics",
    "Dynamics/CRM": "CRM",
    "HubSpot": "Marketing",
    "AI/Copilot": "AI / Automation",
    "BPO/Helpdesk": "Infrastructure",
    "Guidance/Consulting": "Modern Workplace",
    "Power Automate/Flows": "Modern Workplace",
    "Power Apps": "Modern Workplace",
    "Migration (general)": "Infrastructure",
    "Tenant/M365 Migration": "Infrastructure",
    "Google to M365 Migration": "Infrastructure",
    "Ongoing Support": "Infrastructure",
    "Compliance/Purview": "Modern Workplace",
}


def normalize_seniority(title: str) -> str:
    t = (title or "").strip()
    if re.search(r"\b(CEO|CIO|CFO|CTO|Chief|C-Level)\b", t, re.I):
        return "C-Suite"
    if re.search(r"\b(VP|Vice President)\b", t, re.I):
        return "VP"
    if re.search(r"\b(Director|Senior Director)\b", t, re.I):
        return "Director"
    if re.search(r"\b(Manager|Head of|Lead)\b", t, re.I):
        return "Manager"
    return "IC"


def normalize_function(title: str) -> str:
    t = (title or "").strip()
    if re.search(r"\b(Marketing|CMO)\b", t, re.I):
        return "Marketing"
    if re.search(r"\b(IT|CIO|CTO|Infrastructure|Systems|Developer|Engineer)\b", t, re.I):
        return "IT/Tech"
    if re.search(r"\b(Finance|CFO|Controller)\b", t, re.I):
        return "Finance"
    if re.search(r"\b(Operations|Ops)\b", t, re.I):
        return "Operations"
    if re.search(r"\b(Product|Program)\b", t, re.I):
        return "Product/Program"
    if re.search(r"\b(Executive|GM|President|Owner)\b", t, re.I):
        return "Executive"
    return "Other"


def load_opportunities():
    rows = []
    with open(OPS_PATH, newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f, skipinitialspace=True)
        for row in r:
            row = {k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
            if row.get("Status") not in ("Won", "Lost"):
                continue
            ind = row.get("Industry", "").strip() or "Unknown"
            ct = INDUSTRY_TO_COMPANY_TYPE.get(ind, ind)
            row["Company_Type"] = ct
            row["Buyer_Function"] = normalize_function(row.get("Job_Title", ""))
            row["Buyer_Seniority"] = normalize_seniority(row.get("Job_Title", ""))
            row["Buyer_Title"] = f"{row['Buyer_Function']} / {row['Buyer_Seniority']}"
            rows.append(row)
    return rows


def load_inbound():
    try:
        import pandas as pd
        df = pd.read_excel(INBOUND_PATH)
    except Exception:
        return []
    # Get Description, infer ask and industry
    rows = []
    for _, r in df.iterrows():
        desc = str(r.get("Description", "") or "")
        if not desc or desc == "nan":
            continue
        low = desc.lower()
        ask = "Other"
        for a, svc in ASK_TO_SERVICE.items():
            if a.lower().replace("/", " ").replace(" ", "") in low.replace(" ", ""):
                ask = a
                break
        ind = "Commercial"
        for pat, ct in [
            (r"healthcare|hospital|medical|clinical", "Healthcare"),
            (r"non[\s\-]?profit|ngo", "Non-Profit"),
            (r"government|municipal|city|county", "Government"),
            (r"bank|insurance|financial", "Financial Services"),
            (r"manufacturing|manufacturer", "Manufacturing"),
            (r"construction|contractor", "Construction"),
        ]:
            if re.search(pat, low):
                ind = ct
                break
        title = "Unknown"
        for t in ["Director", "Manager", "Owner", "Consultant", "CTO", "CEO"]:
            if t.lower() in low:
                title = t
                break
        rows.append({
            "company_type": ind,
            "ask": ask,
            "service": ASK_TO_SERVICE.get(ask, "—"),
            "title_hint": title,
            "description_snippet": desc[:200],
        })
    return rows


def load_case_study_topics():
    """Extract service + company hints + topics from case study filenames and (optionally) first slide."""
    topics = defaultdict(list)
    assets_root = ASSETS / "case-studies" if (ASSETS / "case-studies").exists() else ASSETS
    for f in assets_root.rglob("*.pptx"):
        name = f.stem.lower()
        # Infer service from filename
        svc = "Other"
        if "sharepoint" in name or "m365" in name or "spo" in name or "teams" in name or "intranet" in name:
            svc = "Modern Workplace"
        elif "salesforce" in name or "dynamics" in name or "crm" in name:
            svc = "CRM"
        elif " bi " in name or "power bi" in name or "snowflake" in name:
            svc = "Data & Analytics"
        elif "marketing" in name or "hubspot" in name or "pardot" in name:
            svc = "Marketing"
        elif " ai " in name or "copilot" in name or "agent" in name:
            svc = "AI / Automation"
        elif "custom dev" in name or "mobile" in name or "portal" in name or "app" in name:
            svc = "Custom Dev"
        elif "infrastructure" in name or "mdm" in name or "intune" in name:
            svc = "Infrastructure"
        elif "creative" in name or "video" in name or "webinar" in name:
            svc = "Creative"
        # Extract topic hints from filename (e.g., "Migration", "Redesign")
        topic_hints = []
        if "migration" in name:
            topic_hints.append("migration")
        if "redesign" in name or "upgrade" in name:
            topic_hints.append("redesign/upgrade")
        if "managed service" in name:
            topic_hints.append("managed service")
        if "implementation" in name:
            topic_hints.append("implementation")
        if "integration" in name:
            topic_hints.append("integration")
        topics[svc].append({"file": f.name, "topic_hints": topic_hints})
    return dict(topics)


def main():
    opps = load_opportunities()
    inbound = load_inbound()
    case_topics = load_case_study_topics()

    # Build Company_Type × Service × Buyer_Title
    pattern_agg = defaultdict(lambda: {"won": 0, "total": 0, "accounts": set()})
    for r in opps:
        ct = r["Company_Type"]
        svc = r.get("Primary_Service", "Unknown")
        title = r["Buyer_Title"]
        key = (ct, svc, title)
        pattern_agg[key]["total"] += 1
        if r["Status"] == "Won":
            pattern_agg[key]["won"] += 1
        pattern_agg[key]["accounts"].add(r.get("Account", ""))

    patterns = []
    for (ct, svc, title), v in pattern_agg.items():
        if v["total"] < 2:
            continue
        wr = v["won"] / v["total"]
        patterns.append({
            "company_type": ct,
            "service": svc,
            "buyer_title": title,
            "n": v["total"],
            "won": v["won"],
            "win_rate": round(wr, 4),
        })
    patterns.sort(key=lambda x: (-x["win_rate"], -x["n"]))

    # Enrich with inbound asks
    inbound_by_segment = defaultdict(list)
    for r in inbound:
        if r["service"] == "—":
            continue
        key = (r["company_type"], r["service"])
        inbound_by_segment[key].append({
            "ask": r["ask"],
            "title_hint": r["title_hint"],
            "snippet": r["description_snippet"][:100],
        })

    # Merge patterns with inbound and case study topics
    enriched = []
    for p in patterns:
        key = (p["company_type"], p["service"])
        inbound_items = inbound_by_segment.get(key, [])
        asks = list(set(i["ask"] for i in inbound_items))[:5]
        snippets = [i["snippet"] for i in inbound_items[:3]]
        svc_topics = case_topics.get(p["service"], [])
        topic_hints = []
        for t in svc_topics[:10]:
            topic_hints.extend(t.get("topic_hints", []))
        topic_hints = list(set(topic_hints))[:8]
        enriched.append({
            **p,
            "inbound_asks": asks,
            "inbound_snippets": snippets,
            "case_study_topics": topic_hints,
            "service_notes": [],
        })
        # Add service notes from known mappings
        if p["service"] == "Modern Workplace":
            enriched[-1]["service_notes"] = ["SharePoint migration", "intranet build", "M365 governance", "tenant consolidation"]
        elif p["service"] == "Data & Analytics":
            enriched[-1]["service_notes"] = ["Power BI", "dashboards", "decision latency", "reporting"]
        elif p["service"] == "CRM":
            enriched[-1]["service_notes"] = ["Salesforce", "Dynamics", "pipeline", "sales enablement"]
        elif p["service"] == "AI / Automation":
            enriched[-1]["service_notes"] = ["Copilot", "agents", "automation", "manual process reduction"]
        elif p["service"] == "Custom Dev":
            enriched[-1]["service_notes"] = ["custom apps", "portals", "mobile", "backlog reduction"]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "company_service_title.json", "w") as f:
        json.dump(enriched, f, indent=2)

    # Industry × Service summary
    ind_svc = defaultdict(lambda: {"won": 0, "total": 0})
    for r in opps:
        key = (r["Company_Type"], r.get("Primary_Service", ""))
        ind_svc[key]["total"] += 1
        if r["Status"] == "Won":
            ind_svc[key]["won"] += 1
    ind_svc_list = [{"company_type": k[0], "service": k[1], "n": v["total"], "won": v["won"], "win_rate": round(v["won"]/v["total"], 4)}
                   for k, v in ind_svc.items() if v["total"] >= 2]
    ind_svc_list.sort(key=lambda x: (-x["win_rate"], -x["n"]))
    with open(OUT_DIR / "company_type_service.json", "w") as f:
        json.dump(ind_svc_list, f, indent=2)

    # Inbound language by company type + service
    inbound_summary = []
    for (ct, svc), items in inbound_by_segment.items():
        asks = list(set(i["ask"] for i in items))
        inbound_summary.append({"company_type": ct, "service": svc, "inbound_asks": asks, "n": len(items)})
    inbound_summary.sort(key=lambda x: -x["n"])
    with open(OUT_DIR / "inbound_language_by_segment.json", "w") as f:
        json.dump(inbound_summary, f, indent=2)

    # Case study topics by service
    with open(OUT_DIR / "case_study_topics_by_service.json", "w") as f:
        json.dump({k: v[:20] for k, v in case_topics.items()}, f, indent=2)

    # Write summary report
    report_lines = [
        "# Company × Service × Buyer Title — Pattern Analysis",
        "",
        "**Focus:** WHO (company type, buyer title) buys WHAT (service). Channel-agnostic.",
        "",
        "---",
        "",
        "## Top Patterns (by win rate, n≥2)",
        "",
        "| Company Type | Service | Buyer Title | n | Win Rate | Inbound Asks | Topics |",
        "|--------------|---------|-------------|---|----------|---------------|--------|",
    ]
    for p in enriched[:40]:
        asks = ", ".join(p["inbound_asks"][:3]) if p["inbound_asks"] else "—"
        topics = ", ".join(p["case_study_topics"][:3]) if p["case_study_topics"] else "—"
        report_lines.append(f"| {p['company_type']} | {p['service']} | {p['buyer_title']} | {p['n']} | {p['win_rate']:.0%} | {asks} | {topics} |")

    report_lines.extend([
        "",
        "---",
        "",
        "## Datasets (data/patterns/)",
        "",
        "| File | Description |",
        "|------|-------------|",
        "| company_service_title.json | Full patterns with inbound_asks, case_study_topics, service_notes |",
        "| company_type_service.json | Company Type × Service win rates |",
        "| inbound_language_by_segment.json | What inbound leads say they want, by segment |",
        "| case_study_topics_by_service.json | Project themes from case study filenames |",
        "",
        "**Regenerate:** `python3 scripts/company_service_title_analysis.py`",
    ])
    (BASE / "reports" / "Company Service Title Patterns.md").write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Patterns: {len(enriched)}")
    print(f"Inbound segments: {len(inbound_summary)}")
    print(f"Wrote {OUT_DIR} and reports/Company Service Title Patterns.md")


if __name__ == "__main__":
    main()
