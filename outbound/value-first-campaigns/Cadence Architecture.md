# Value-First Campaign Cadence Architecture

31-day free-value cadence for each persona. Every touch offers something free. Folder names use Title Case (no hyphens or underscores).

---

## Structure

| Element | Description |
|---------|-------------|
| **Campaign** | One per value-first message (10 total) |
| **Folder names** | Title Case with spaces (e.g., "01 Marketing Creative Conversion") |
| **Days** | 1–31, one template per day |
| **Channel** | Email (primary), LinkedIn (Days 3, 7, 14, 21, 28) |
| **Format** | Subject, Body, Free Value, ATTACH (doc path), CTA |
| **Free value** | Unique doc, checklist, or framework per day |
| **CTA** | Days 5, 10, 15, 20, 25, 30: soft offer for 15-min call. Other days: no ask |

---

## Cadence Phases

| Days | Phase | Goal |
|------|-------|------|
| 1–7 | Intro + light value | Establish pattern: free resource, no ask |
| 8–14 | Deeper value | More substantive frameworks, checklists |
| 15–21 | Operational tools | Templates they can use immediately |
| 22–28 | Cadence & process | Review agendas, planning, governance |
| 29–31 | Close loop | Year-end, monthly, strategic review tools |

---

## Campaigns

| # | Campaign | Persona | Free Value Theme |
|---|----------|----------|------------------|
| 01 | Marketing Director × Creative — Conversion | Marketing Director, VP, Manager | Conversion leaks, landing pages, CTAs |
| 02 | Marketing Director × Creative — Attribution | Marketing Director, VP | Attribution, spend allocation, channels |
| 03 | IT Director — Ownership & Checklist | IT Director, CIO | Systems ownership, drift, governance |
| 04 | IT Director — Drift Audit | IT Director, Infrastructure | Drift, orphan systems, documentation |
| 05 | Director — Decision Latency | Director, VP (Ops, Finance, IT) | Time-to-answer, KPI reporting |
| 06 | Marketing VP — Spend Reallocation | Marketing VP, CMO | Spend efficiency, channel mix |
| 07 | Finance Director — System Ownership | Finance Director, VP Finance | Critical systems, ownership maps |
| 08 | IT Director — Backlog Prioritization | IT Director, Dev lead | Backlog, prioritization, partners |
| 09 | Marketing Manager × Creative — 3 Fixes | Marketing Manager | Quick fixes, ads, landing pages |
| 10 | C-level / VP — KPI Latency | C-level, VP | Decision latency, exec KPIs |

---

## Attachment Mapping

Each template has an **ATTACH** field: path to doc or instructions to create. Docs in `docs/templates/`:

| Doc | Campaigns / Days |
|-----|------------------|
| 01 Systems Ownership Checklist | 03 (Day 1), 04 |
| 02 Drift Audit Template | 03 (Day 2), 04 |
| 03 Decision Latency Worksheet | 05 (Day 1) |
| 04 Spend Reallocation Framework | 06 (Day 1) |
| 05 System Ownership Map | 07 (Day 1) |
| 06 Backlog Prioritization Matrix | 08 (Day 11) |
| 07 KPI Latency Snapshot | 05 (Day 2), 10 (Day 1) |
| 08 Conversion Leak Checklist | 01 (Day 1), 09 |
| 09 Trust Signal Placement Checklist | 01 (Day 5) |
| 10 Landing Page CTA Audit Criteria | 01 (Day 2), 09 |
| 11 Channel Scoring Framework | 01, 02 (Day 14) |
| 12 Orphan System Red Flag Checklist | 03, 04 (Day 5) |
| 13 UTM Parameter Template | 01, 02 (Day 23) |

**Other days:** Create from the FREE VALUE description, or use `scripts/run_conversion_teardown.py` / `scripts/run_attribution_check.py` for campaigns 01, 02, 09.

---

## Usage

1. Pick campaign by persona.
2. Start at Day 1 or Day 7 (depending on prior touch).
3. Send one template per day (or every 2–3 days if cadence is slower).
4. Attach the doc referenced in FREE VALUE.
5. If they reply, exit cadence and respond; optional soft offer for a call.
6. If no reply by Day 31, pause 30 days and restart or mark as nurture.

---

## Regenerate Templates

```bash
python3 scripts/generate_cadence_templates.py
```
