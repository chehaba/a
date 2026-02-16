# Value-First Message Assets

Docs, instructions, scripts, and AI prompts for the 10 value-first outbound messages.

---

## No Analysis Required — Use These Docs Directly

| Message | Doc | When to use |
|---------|-----|-------------|
| #3 IT Director — Ownership checklist | [templates/01 Systems Ownership Checklist.md](templates/01%20Systems%20Ownership%20Checklist.md) | Send as-is or attach |
| #4 IT Director — Drift audit template | [templates/02 Drift Audit Template.md](templates/02%20Drift%20Audit%20Template.md) | Send as-is or attach |
| #5 Director — Decision latency worksheet | [templates/03 Decision Latency Worksheet.md](templates/03%20Decision%20Latency%20Worksheet.md) | Send as-is or attach |
| #6 Marketing VP — Spend reallocation | [templates/04 Spend Reallocation Framework.md](templates/04%20Spend%20Reallocation%20Framework.md) | Send as-is or attach |
| #7 Finance Director — System ownership map | [templates/05 System Ownership Map.md](templates/05%20System%20Ownership%20Map.md) | Send as-is or attach |
| #8 IT Director — Backlog prioritization | [templates/06 Backlog Prioritization Matrix.md](templates/06%20Backlog%20Prioritization%20Matrix.md) | Send as-is or attach |
| #10 C-level/VP — KPI latency snapshot | [templates/07 KPI Latency Snapshot.md](templates/07%20KPI%20Latency%20Snapshot.md) | Send as-is or attach |
| Conversion leak checklist | [templates/08 Conversion Leak Checklist.md](templates/08%20Conversion%20Leak%20Checklist.md) | Campaign 01, 09 |
| Trust signal placement | [templates/09 Trust Signal Placement Checklist.md](templates/09%20Trust%20Signal%20Placement%20Checklist.md) | Campaign 01 |
| Landing page CTA audit | [templates/10 Landing Page CTA Audit Criteria.md](templates/10%20Landing%20Page%20CTA%20Audit%20Criteria.md) | Campaign 01, 09 |
| Channel scoring framework | [templates/11 Channel Scoring Framework.md](templates/11%20Channel%20Scoring%20Framework.md) | Campaign 01, 02 |
| Orphan system red flags | [templates/12 Orphan System Red Flag Checklist.md](templates/12%20Orphan%20System%20Red%20Flag%20Checklist.md) | Campaign 03, 04 |
| UTM parameter template | [templates/13 UTM Parameter Template.md](templates/13%20UTM%20Parameter%20Template.md) | Campaign 01, 02 |

---

## Analysis Required — Instructions + Script + AI Prompt

| Message | Instructions | Script | AI Prompt |
|---------|---------------|--------|-----------|
| #1 Conversion teardown | [analysis/Conversion Teardown Instructions.md](analysis/Conversion%20Teardown%20Instructions.md) | `python3 scripts/run_conversion_teardown.py "URL"` | In that doc |
| #2 Attribution snapshot | [analysis/Attribution Snapshot Instructions.md](analysis/Attribution%20Snapshot%20Instructions.md) | `python3 scripts/run_attribution_check.py "URL"` | In that doc |
| #9 3 fixes one-pager | Same as #1 | Same script | Same AI prompt |

---

## Scripts (run from repo root)

```bash
# Conversion teardown / 3 fixes
python3 scripts/run_conversion_teardown.py "https://prospect-website.com/landing-page"

# Attribution check
python3 scripts/run_attribution_check.py "https://prospect-website.com"
```

Scripts output structure/checklist; you add the narrative or use the AI prompt to generate it.
