"""
Segment Attractiveness Score
= w1(Revenue Potential) + w2(Win Rate) + w3(Urgency) + w4(Strategic Fit)
"""

# Data from Microsoft Opportunity Patterns doc (Title × Service)
# Format: (title, service, engaged, won)
SEGMENTS = [
    ("Program / Project Manager", "Custom Dev", 17, 1),
    ("Manager", "Custom Dev", 8, 0),
    ("Program / Project Manager", "Creative", 6, 1),
    ("Program / Project Manager", "Marketing Services", 6, 0),
    ("Product Manager / PMM", "Creative", 5, 2),
    ("Program / Project Manager", "BPO", 4, 0),
    ("Product Manager / PMM", "Marketing Services", 4, 1),
    ("Manager", "Marketing Services", 3, 2),
    ("Manager", "Data & Analytics", 3, 0),
    ("Manager", "Modern Workplace", 3, 0),
    ("IT", "Custom Dev", 2, 0),
    ("Director of Marketing", "Creative", 2, 1),
    ("Director (other)", "Data & Analytics", 2, 0),
    ("Marketing Manager", "Marketing Services", 2, 0),
    ("President / Owner / Principal", "Custom Dev", 2, 1),
]


def normalize(values, scale=100):
    """Normalize to 0-100 scale."""
    lo, hi = min(values), max(values)
    if hi == lo:
        return [scale / 2] * len(values)
    return [scale * (v - lo) / (hi - lo) for v in values]


def score_segments(w1, w2, w3, w4, urgency_scores=None, strategic_fit=None):
    """
    Weights reflect company strategy.
    Default: w1=0.25, w2=0.35, w3=0.20, w4=0.20 (Win Rate emphasized)
    """
    engaged = [s[2] for s in SEGMENTS]
    win_rates = [s[3] / s[2] if s[2] else 0 for s in SEGMENTS]

    revenue_potential = normalize(engaged)  # more engaged = higher potential
    win_rate_norm = [wr * 100 for wr in win_rates]  # already 0-100

    urgency = urgency_scores or [50] * len(SEGMENTS)  # default neutral
    fit = strategic_fit or [50] * len(SEGMENTS)  # default neutral

    results = []
    for i, (title, service, eng, won) in enumerate(SEGMENTS):
        score = (
            w1 * revenue_potential[i]
            + w2 * win_rate_norm[i]
            + w3 * urgency[i]
            + w4 * fit[i]
        )
        results.append({
            "title": title,
            "service": service,
            "engaged": eng,
            "won": won,
            "win_rate_pct": round(win_rates[i] * 100, 0),
            "revenue_pot": round(revenue_potential[i], 1),
            "score": round(score, 1),
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)


if __name__ == "__main__":
    # Example weights (must sum to 1)
    w1, w2, w3, w4 = 0.25, 0.35, 0.20, 0.20

    print("Segment Attractiveness Score")
    print("= w1(Revenue Potential) + w2(Win Rate) + w3(Urgency) + w4(Strategic Fit)\n")
    print(f"Weights: w1={w1}, w2={w2}, w3={w3}, w4={w4}\n")

    ranked = score_segments(w1, w2, w3, w4)

    print(f"{'Rank':<5} {'Title':<28} {'Service':<22} {'Eng':<5} {'Win%':<6} {'Score':<8}")
    print("-" * 80)
    for r, row in enumerate(ranked, 1):
        print(f"{r:<5} {row['title']:<28} {row['service']:<22} {row['engaged']:<5} {row['win_rate_pct']:<6.0f} {row['score']:<8.1f}")
