# Opportunity Segmentation Analysis Report

**Data:** Oops.csv (562 opportunities)  
**Date:** 2026-02-13

---

## Overall

| Metric | Value |
|--------|-------|
| Total opportunities | 562 |
| Won | 199 |
| Lost | 363 |
| Win rate | 35.4% |

---

## By Service

| Service | Won | Lost | Total | Win% |
|---------|-----|-----|-------|------|
| Modern Workplace | 74 | 102 | 176 | 42.0 |
| Custom Dev | 37 | 74 | 111 | 41.6 |
| Marketing Services | 31 | 45 | 76 | 40.8 |
| Data & Analytics | 11 | 49 | 60 | 18.3 |
| Infrastructure | 20 | 30 | 50 | 40.0 |
| Creative | 15 | 20 | 35 | 42.9 |
| CRM | 14 | 17 | 31 | 45.2 |

**Best performers:** CRM (45.2%), Creative (42.9%), Modern Workplace (42.0%)  
**Weakest:** Data & Analytics (18.3%)

---

## By Industry

| Industry | Won | Lost | Total | Win% |
|----------|-----|-----|-------|------|
| Non-Profit | 10 | 2 | 12 | 83.3 |
| Healthcare | 23 | 25 | 48 | 47.9 |
| Energy, Utilities, Waste Treatment | 9 | 10 | 19 | 47.4 |
| Business Services | 25 | 29 | 54 | 46.3 |
| Government | 7 | 5 | 12 | 58.3 |
| Construction | 9 | 13 | 22 | 40.9 |
| Education | 13 | 18 | 31 | 41.9 |
| Software | 27 | 106 | 133 | 20.3 |

**Best performers:** Non-Profit (83.3%), Government (58.3%), Healthcare (47.9%)  
**Weakest:** Transportation (10.0%), Organizations (13.3%), Software (20.3%)

---

## By Source Campaign

| Source | Won | Lost | Total | Win% |
|--------|-----|-----|-------|------|
| Marketing - Web Visitor | 6 | 1 | 7 | 85.7 |
| Direct Sales Campaign | 5 | 1 | 6 | 83.3 |
| Account Management Campaign | 29 | 17 | 46 | 63.0 |
| Direct Sales - Personal Network | 9 | 9 | 18 | 50.0 |
| Marketing - SEO | 30 | 36 | 66 | 45.5 |
| Marketing – PPC | 73 | 97 | 170 | 42.9 |
| Direct Sales - LinkedIn | 23 | 96 | 119 | 19.3 |

**Best performers:** Web Visitor (85.7%), Direct Sales Campaign (83.3%), Account Management (63.0%)  
**Weakest:** CEM - Existing Customer New Service (5.9%)

---

## Segment Attractiveness Score

Formula: w₁(Revenue Potential) + w₂(Win Rate) + w₃(Urgency) + w₄(Strategic Fit)  
Weights: 0.25, 0.35, 0.20, 0.20

**Top 10 segments (Title × Service):**

1. Director of Finance × Modern Workplace — 11/11 (100%) — Score 66.1
2. Insitu IT Department × Infrastructure — 4/4 (100%) — Score 57.8
3. Senior Reimbursement Account Manager × Custom Dev — 5/5 (100%) — Score 55.0
4. Director of Marketing Operations × Infrastructure — 4/4 (100%) — Score 55.0
5. IT Director × Custom Dev — 4/4 (100%) — Score 55.0
6. IS Program Manager × Modern Workplace — 5/5 (100%) — Score 55.0
7. Owner × Custom Dev — 2/2 (100%) — Score 55.0
8. CIO × Modern Workplace — 3/4 (75%) — Score 51.8
9. Product Marketing Manager × Creative — 2/3 (66.7%) — Score 46.1
10. Director of Marketing × Marketing Services — 2/3 (66.7%) — Score 46.1

---

## Industry × Service (Best Win Rates)

| Industry | Service | Won | Total | Win% |
|----------|---------|-----|-------|------|
| Business Services | Infrastructure | 8 | 10 | 80.0 |
| Healthcare | Modern Workplace | 15 | 27 | 55.6 |
| Business Services | Modern Workplace | 7 | 14 | 50.0 |
| Manufacturing | Modern Workplace | 7 | 15 | 46.7 |
| Finance | Modern Workplace | 9 | 20 | 45.0 |

---

## Multi-Opportunity Accounts

| Metric | Value |
|--------|-------|
| Multi-opp opportunities | 156 |
| Won | 38 |
| Win rate | 24.4% |

Multi-opp accounts underperform single-opp (24.4% vs ~40%+ for strong sources).

---

## Takeaways

1. **Non-Profit + Healthcare:** Highest industry win rates — double down.
2. **Account Management + Web Visitor:** Best source performance — nurture inbounds and existing accounts.
3. **LinkedIn volume, low win rate:** 119 engaged, 19.3% win — qualify better or shift mix.
4. **Software:** 133 opportunities, 20.3% win — segment harder; focus on titles/accounts that convert.
5. **Director of Finance × Modern Workplace:** Top segment — ideal ICP for Modern Workplace plays.
6. **CRM:** Smallest service volume with strongest win rate — consider scaling.

---

Run `python3 scripts/run_analysis.py` from repo root to regenerate.


