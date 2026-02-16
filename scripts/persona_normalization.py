#!/usr/bin/env python3
"""
Persona normalization: Job_Title → Function × Seniority
Produces target lists and copy variants for the 3 segment packs.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

_BASE = Path(__file__).resolve().parent.parent
CSV_PATH = _BASE / "data" / "opportunities" / "Oops.csv"

# Seniority rules (order matters: check more specific first)
SENIORITY_PATTERNS = [
    (r"\bCEO\b|\bCIO\b|\bCFO\b|\bCOO\b|\bCTO\b|\bC-Level\b|\bChief\s", "C-level"),
    (r"\bVP\b|\bVice President\b|\bV\.?P\.?", "VP"),
    (r"\bDirector\b|\bSr\.?\s*Director\b|\bSenior Director\b", "Director"),
    (r"\bManager\b|\bSr\.?\s*Manager\b|\bSenior Manager\b|\bHead of\b|\bLead\b", "Manager"),
    (r"\bPrincipal\b|\bEngineer\b|\bDeveloper\b|\bAnalyst\b|\bSpecialist\b|\bAdmin\b|\bCoordinator\b|\bProgram Manager\b|\bProduct Manager\b", "IC"),
]

# Function rules
FUNCTION_PATTERNS = [
    (r"\bMarketing\b|\bCMO\b|\bBrand\b|\bCommunications\b|\bContent\b|\bDigital Marketing\b", "Marketing"),
    (r"\bIT\b|\bInformation Technology\b|\bCIO\b|\bCTO\b|\bInfrastructure\b|\bSystems\b|\bDeveloper\b|\bEngineer\b|\bDevOps\b|\bSharePoint\b", "IT/Tech"),
    (r"\bFinance\b|\bCFO\b|\bAccountant\b|\bController\b|\bTreasury\b", "Finance"),
    (r"\bOperations\b|\bOps\b|\bProcurement\b|\bSupply\b", "Other"),  # could be separate, lumping for simplicity
]

def classify_seniority(title):
    t = (title or "").strip()
    for pat, level in SENIORITY_PATTERNS:
        if re.search(pat, t, re.I):
            return level
    return "Other"

def classify_function(title):
    t = (title or "").strip()
    for pat, func in FUNCTION_PATTERNS:
        if re.search(pat, t, re.I):
            return func
    return "Other"

def wilson_ci(won, total, z=1.96):
    if total == 0:
        return (0, 0)
    p = won / total
    denom = 1 + z**2 / total
    center = (p + z**2 / (2 * total)) / denom
    margin = z * (p * (1 - p) / total + z**2 / (4 * total**2)) ** 0.5 / denom
    low = max(0, (center - margin) * 100)
    high = min(100, (center + margin) * 100)
    return (round(low, 1), round(high, 1))

def load_and_tag():
    rows = []
    with open(str(CSV_PATH), newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f, skipinitialspace=True)
        for row in r:
            row = {k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
            if row.get("Status") not in ("Won", "Lost"):
                continue
            title = row.get("Job_Title", "") or "Unknown"
            row["Function"] = classify_function(title)
            row["Seniority"] = classify_seniority(title)
            rows.append(row)
    return rows

def aggregate(rows, dims, source_filter=None, min_n=1):
    """dims = list of column names, e.g. ['Function','Seniority','Primary_Service']"""
    agg = defaultdict(lambda: {"won": 0, "total": 0})
    for r in rows:
        if source_filter and r.get("Source_Campaign") != source_filter:
            continue
        key = tuple(r.get(d, "").strip() or "Unknown" for d in dims)
        agg[key]["total"] += 1
        if r["Status"] == "Won":
            agg[key]["won"] += 1

    out = []
    for k, v in agg.items():
        if v["total"] >= min_n:
            wr = 100 * v["won"] / v["total"] if v["total"] else 0
            ci = wilson_ci(v["won"], v["total"])
            out.append((k, v["won"], v["total"], round(wr, 1), ci))
    return out

def main():
    rows = load_and_tag()

    # Output 1: Persona normalization
    print("=" * 80)
    print("OUTPUT 1 — PERSONA NORMALIZATION (Function × Seniority)")
    print("=" * 80)
    print("Overall win rate: 35.4% (199/562)")
    print()
    fs = aggregate(rows, ["Function", "Seniority"], min_n=15)
    fs.sort(key=lambda x: (-x[3], -x[2]))  # win rate desc, then n
    print(f"{'Function':<15} {'Seniority':<12} {'n':<6} {'Win%':<10} {'Lift (pp)':<10}")
    print("-" * 55)
    for (f, s), won, n, wr, _ in fs:
        lift = wr - 35.4
        print(f"{f:<15} {s:<12} {n:<6} {wr:<10.1f} {lift:+.1f}")

    # Output 2: LinkedIn segments
    print()
    print("=" * 80)
    print("OUTPUT 2 — LINKEDIN CHANNEL FIT (Direct Sales - LinkedIn, n=119)")
    print("=" * 80)
    li = [r for r in rows if r.get("Source_Campaign") == "Direct Sales - LinkedIn"]
    li_agg = aggregate(li, ["Function", "Primary_Service"], min_n=10)
    li_agg.sort(key=lambda x: -x[3])
    print(f"{'Function':<12} {'Service':<22} {'n':<6} {'Win%':<10} {'95% Wilson CI':<20} {'Rec'}")
    print("-" * 85)
    for (f, svc), won, n, wr, ci in li_agg:
        ci_str = f"{ci[0]:.1f}–{ci[1]:.1f}"
        if wr >= 40:
            rec = "RUN"
        elif wr >= 20:
            rec = "TEST"
        else:
            rec = "DON'T RUN"
        print(f"{f:<12} {svc:<22} {n:<6} {wr:<10.1f} {ci_str:<20} {rec}")

    # Target lists for segments A, B, C
    print()
    print("=" * 80)
    print("TARGET LISTS (Function × Seniority × Service × Industry)")
    print("=" * 80)

    # Segment A: Marketing × Creative (LinkedIn)
    seg_a = aggregate(
        [r for r in li if r["Function"] == "Marketing" and r["Primary_Service"] == "Creative"],
        ["Function", "Seniority", "Primary_Service", "Industry"],
        source_filter="Direct Sales - LinkedIn",
        min_n=1
    )
    print()
    print("SEGMENT A: LinkedIn → Marketing × Creative")
    print("-" * 60)
    for (f, s, svc, ind), won, n, wr, ci in sorted(seg_a, key=lambda x: (-x[3], -x[2]))[:15]:
        print(f"  {f} | {s} | {svc} | {ind[:25]:<25}  n={n:3}  win={wr:.1f}%  CI=[{ci[0]:.1f}–{ci[1]:.1f}]")

    # Segment B: IT/Tech × Director
    seg_b = aggregate(
        [r for r in rows if r["Function"] == "IT/Tech" and r["Seniority"] == "Director"],
        ["Function", "Seniority", "Primary_Service", "Industry"],
        min_n=2
    )
    print()
    print("SEGMENT B: Outbound → IT/Tech × Director")
    print("-" * 60)
    for (f, s, svc, ind), won, n, wr, ci in sorted(seg_b, key=lambda x: (-x[3], -x[2]))[:15]:
        print(f"  {f} | {s} | {svc} | {ind[:25]:<25}  n={n:3}  win={wr:.1f}%  CI=[{ci[0]:.1f}–{ci[1]:.1f}]")

    # Segment C: Data & Analytics, Director+
    dir_plus = ["Director", "VP", "C-level"]
    seg_c = aggregate(
        [r for r in rows if r["Primary_Service"] == "Data & Analytics" and r["Seniority"] in dir_plus],
        ["Function", "Seniority", "Primary_Service", "Industry"],
        min_n=1
    )
    print()
    print("SEGMENT C: Email → Data & Analytics (Director+)")
    print("-" * 60)
    for (f, s, svc, ind), won, n, wr, ci in sorted(seg_c, key=lambda x: (-x[3], -x[2]))[:15]:
        print(f"  {f} | {s} | {svc} | {ind[:25]:<25}  n={n:3}  win={wr:.1f}%  CI=[{ci[0]:.1f}–{ci[1]:.1f}]")

    # Copy variants
    print()
    print("=" * 80)
    print("COPY VARIANTS (2 per segment)")
    print("=" * 80)

    copies = [
        ("Segment A: LinkedIn — Marketing × Creative", [
            ("Variant 1: Conversion leak teardown", "We usually spot 2–3 conversion leaks in 10 minutes. Want me to do a quick teardown and send 3 fixes?", "Want me to do a quick teardown and send 3 fixes?"),
            ("Variant 2: Attribution clarity", "We help teams see what's working vs not—and where spend leaks. Quick benchmark on your ads + landing pages.", "Want a creative performance benchmark (ads + landing pages)?")
        ]),
        ("Segment B: Email + LinkedIn — IT/Tech Director", [
            ("Variant 1: Ownership + drift", "Most waste comes from 'nobody owns this system anymore.' Worth a 15-min check if you have any orphan systems or drift right now?", "Worth a 15-min systems ownership + drift review?"),
            ("Variant 2: Time compression", "We help reduce backlog by bringing in a ready-to-run team. 2-week scoping sprint, fixed output: plan + effort bands.", "Want a 30-minute modernization scoping call?")
        ]),
        ("Segment C: Email — Data & Analytics (Director+)", [
            ("Variant 1: Decision latency", "How long does it take to answer basic performance questions? We reduce KPI reporting time and create owner-based alerts.", "Want a quick 'decision latency' audit—where answers get stuck and why?"),
            ("Variant 2: Operational control", "We fix the few reports that drive the biggest decisions. Power BI / reporting healthcheck with 5 fixes prioritized by ROI.", "Want an executive KPI latency audit?")
        ]),
    ]

    for seg_name, variants in copies:
        print()
        print(seg_name)
        print("-" * 50)
        for vname, body, cta in variants:
            print(f"  {vname}")
            print(f"    Body: {body[:80]}...")
            print(f"    CTA:  {cta}")
            print()

if __name__ == "__main__":
    main()
