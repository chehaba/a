#!/usr/bin/env python3
"""
Opportunity segmentation analysis.
Uses Oops.csv and applies Segment Attractiveness Score formula.
"""

import csv
from pathlib import Path
from collections import defaultdict

_BASE = Path(__file__).resolve().parent.parent
CSV_PATH = _BASE / "data" / "opportunities" / "Oops.csv"


def load_csv():
    rows = []
    with open(str(CSV_PATH), newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            row = {k.strip(): v.strip() if isinstance(v, str) else v for k, v in row.items()}
            if not row.get("Status") or row["Status"] not in ("Won", "Lost"):
                continue
            rows.append(row)
    return rows


def agg_by_dim(rows, dim, min_count=3):
    """Aggregate won/lost by dimension."""
    counts = defaultdict(lambda: {"won": 0, "lost": 0, "total": 0})
    for r in rows:
        val = r.get(dim, "").strip() or "Unknown"
        counts[val]["total"] += 1
        counts[val]["won" if r["Status"] == "Won" else "lost"] += 1

    out = []
    for k, v in counts.items():
        if v["total"] >= min_count:
            wr = 100 * v["won"] / v["total"] if v["total"] else 0
            out.append((k, v["won"], v["lost"], v["total"], round(wr, 1)))
    return sorted(out, key=lambda x: (-x[3], -x[4]))  # by volume, then win rate


def segment_attractiveness(rows, w1=0.25, w2=0.35, w3=0.20, w4=0.20, min_engaged=2):
    """
    Segment Attractiveness Score = w1(Revenue Potential) + w2(Win Rate) + w3(Urgency) + w4(Strategic Fit)
    Revenue Potential ~ engagement; Win Rate from data; Urgency/Strategic Fit default 50.
    """
    # Build Title × Service segments (from Job_Title + Primary_Service)
    seg = defaultdict(lambda: {"won": 0, "total": 0})
    for r in rows:
        title = r.get("Job_Title", "").strip() or "Unknown"
        svc = r.get("Primary_Service", "").strip() or "Unknown"
        key = (title, svc)
        seg[key]["total"] += 1
        if r["Status"] == "Won":
            seg[key]["won"] += 1

    segments = [(k, v["won"], v["total"]) for k, v in seg.items() if v["total"] >= min_engaged]

    if not segments:
        return []

    totals = [s[2] for s in segments]
    lo, hi = min(totals), max(totals)
    rev_pot = [100 * (t - lo) / (hi - lo) if hi > lo else 50 for t in totals]
    win_rates = [100 * s[1] / s[2] if s[2] else 0 for s in segments]
    urgency = [50] * len(segments)
    fit = [50] * len(segments)

    results = []
    for i, ((title, svc), won, total) in enumerate(segments):
        score = w1 * rev_pot[i] + w2 * win_rates[i] + w3 * urgency[i] + w4 * fit[i]
        results.append({
            "title": title[:35],
            "service": svc,
            "won": won,
            "total": total,
            "win_rate": round(win_rates[i], 1),
            "score": round(score, 1),
        })

    return sorted(results, key=lambda x: -x["score"])


def industry_service_matrix(rows, min_count=2):
    """Win rate by Industry × Service."""
    counts = defaultdict(lambda: {"won": 0, "total": 0})
    for r in rows:
        ind = r.get("Industry", "").strip() or "Unknown"
        svc = r.get("Primary_Service", "").strip() or "Unknown"
        key = (ind, svc)
        counts[key]["total"] += 1
        if r["Status"] == "Won":
            counts[key]["won"] += 1

    out = []
    for (ind, svc), v in counts.items():
        if v["total"] >= min_count:
            wr = 100 * v["won"] / v["total"] if v["total"] else 0
            out.append((ind[:30], svc, v["won"], v["total"], round(wr, 1)))
    return sorted(out, key=lambda x: (-x[3], -x[4]))


def main():
    rows = load_csv()
    total = len(rows)
    won = sum(1 for r in rows if r["Status"] == "Won")
    lost = total - won
    wr_overall = 100 * won / total if total else 0

    print("=" * 70)
    print("OPPORTUNITY SEGMENTATION ANALYSIS")
    print("=" * 70)
    print()
    print("OVERALL")
    print("-" * 40)
    print(f"Total opportunities: {total}")
    print(f"Won: {won}  |  Lost: {lost}  |  Win rate: {wr_overall:.1f}%")
    print()

    # By Service
    print("BY SERVICE (min 3 engaged)")
    print("-" * 60)
    print(f"{'Service':<22} {'Won':<6} {'Lost':<6} {'Total':<6} {'Win%':<8}")
    for name, w, l, t, wr in agg_by_dim(rows, "Primary_Service")[:15]:
        print(f"{name[:22]:<22} {w:<6} {l:<6} {t:<6} {wr:<8.1f}")
    print()

    # By Industry
    print("BY INDUSTRY (min 3 engaged)")
    print("-" * 60)
    print(f"{'Industry':<30} {'Won':<6} {'Lost':<6} {'Total':<6} {'Win%':<8}")
    for name, w, l, t, wr in agg_by_dim(rows, "Industry")[:15]:
        print(f"{name[:30]:<30} {w:<6} {l:<6} {t:<6} {wr:<8.1f}")
    print()

    # By Source
    print("BY SOURCE CAMPAIGN (min 3 engaged)")
    print("-" * 60)
    print(f"{'Source':<40} {'Won':<6} {'Lost':<6} {'Total':<6} {'Win%':<8}")
    for name, w, l, t, wr in agg_by_dim(rows, "Source_Campaign")[:12]:
        print(f"{name[:40]:<40} {w:<6} {l:<6} {t:<6} {wr:<8.1f}")
    print()

    # Segment Attractiveness Score
    print("SEGMENT ATTRACTIVENESS SCORE")
    print("= w1(Revenue Potential) + w2(Win Rate) + w3(Urgency) + w4(Strategic Fit)")
    print("Weights: w1=0.25, w2=0.35, w3=0.20, w4=0.20")
    print("-" * 70)
    print(f"{'Rank':<5} {'Title':<36} {'Service':<18} {'Won/Total':<10} {'Win%':<8} {'Score':<8}")
    ranked = segment_attractiveness(rows)[:20]
    for r, row in enumerate(ranked, 1):
        print(f"{r:<5} {row['title']:<36} {row['service']:<18} {row['won']}/{row['total']:<8} {row['win_rate']:<8.1f} {row['score']:<8.1f}")
    print()

    # Industry × Service top combos
    print("INDUSTRY × SERVICE (min 2 engaged) - Top performers")
    print("-" * 70)
    print(f"{'Industry':<28} {'Service':<18} {'Won':<5} {'Total':<6} {'Win%':<8}")
    for ind, svc, w, t, wr in industry_service_matrix(rows)[:15]:
        print(f"{ind:<28} {svc:<18} {w:<5} {t:<6} {wr:<8.1f}")
    print()

    # Multi-opp accounts
    multi = [r for r in rows if r.get("Is_Multi_Opp") == "Y"]
    multi_won = sum(1 for r in multi if r["Status"] == "Won")
    multi_total = len(multi)
    multi_wr = 100 * multi_won / multi_total if multi_total else 0
    print("MULTI-OPPORTUNITY ACCOUNTS")
    print("-" * 40)
    print(f"Multi-opp opportunities: {multi_total}  |  Won: {multi_won}  |  Win rate: {multi_wr:.1f}%")
    print()

    # Takeaways
    print("=" * 70)
    print("TAKEAWAYS")
    print("=" * 70)
    svc_best = max(agg_by_dim(rows, "Primary_Service", min_count=5), key=lambda x: x[4], default=(None, 0, 0, 0, 0))
    ind_best = max(agg_by_dim(rows, "Industry", min_count=5), key=lambda x: x[4], default=(None, 0, 0, 0, 0))
    src_best = max(agg_by_dim(rows, "Source_Campaign", min_count=5), key=lambda x: x[4], default=(None, 0, 0, 0, 0))
    if svc_best[0]:
        print(f"• Best win rate (service, 5+ engaged): {svc_best[0]} @ {svc_best[4]:.1f}%")
    if ind_best[0]:
        print(f"• Best win rate (industry, 5+ engaged): {ind_best[0]} @ {ind_best[4]:.1f}%")
    if src_best[0]:
        print(f"• Best win rate (source, 5+ engaged): {src_best[0][:50]} @ {src_best[4]:.1f}%")
    top_seg = ranked[0] if ranked else None
    if top_seg:
        print(f"• Top segment (by score): {top_seg['title']} × {top_seg['service']} (score {top_seg['score']})")
    print()


if __name__ == "__main__":
    main()
