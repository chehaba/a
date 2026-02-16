# Docs — Deep Synthesis

**Purpose:** Value-first message assets, templates, analysis instructions, and AI prompts. Use these docs directly for outbound; no analysis required for templates.

**Source:** docs/README.md, all files under docs/templates/, docs/analysis/

---

## Part 1: Directory Structure and Usage

| Subdir | Contents | When to Use |
|--------|----------|-------------|
| **templates/** | 13 send-as-is checklists, worksheets, frameworks | Attach to emails or send as links |
| **analysis/** | Step-by-step instructions + scripts + AI prompts | When you need to produce custom analysis (teardown, attribution) |

---

## Part 2: Templates — No Analysis Required

### IT Director / Modern Workplace (Campaigns 03, 04)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| Systems Ownership Checklist | `templates/01 Systems Ownership Checklist.md` | 5-min check: who owns each system | 03 IT Director Ownership |
| Drift Audit Template | `templates/02 Drift Audit Template.md` | Document system, owner, dependencies, status | 04 IT Director Drift |
| Orphan System Red Flag Checklist | `templates/12 Orphan System Red Flag Checklist.md` | Red flags for drift signals | 03, 04 |

**Hook:** "Most waste comes from 'nobody owns this system anymore.'"

---

### Data & Analytics / Decision Latency (Campaign 05)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| Decision Latency Worksheet | `templates/03 Decision Latency Worksheet.md` | 5 questions: list top decisions, answer time, where delay sits | 05 Director Decision Latency |
| KPI Latency Snapshot | `templates/07 KPI Latency Snapshot.md` | 5-question snapshot for operational KPIs | 10 C-level KPI |

**Hook:** "How long does it take to answer basic performance questions?"

---

### Marketing VP / Marketing Services (Campaign 06)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| Spend Reallocation Framework | `templates/04 Spend Reallocation Framework.md` | 4 questions: attribution, conversion, spend vs outcome, cadence | 06 Marketing VP Spend |
| Channel Scoring Framework | `templates/11 Channel Scoring Framework.md` | Score channels by performance | 01, 02 |
| UTM Parameter Template | `templates/13 UTM Parameter Template.md` | Add campaign/source/medium to links | 01, 02 |

---

### Finance Director (Campaign 07)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| System Ownership Map | `templates/05 System Ownership Map.md` | Critical systems, who owns, review cadence | 07 Finance Director Ownership |

**Note:** Finance Director × Modern Workplace = 100% win rate (6/6).

---

### IT Director Backlog (Campaign 08)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| Backlog Prioritization Matrix | `templates/06 Backlog Prioritization Matrix.md` | Effort vs impact, partner vs in-house | 08 IT Director Backlog |

---

### Marketing Creative (Campaigns 01, 09)

| Template | Doc | Use For | Campaign |
|----------|-----|---------|----------|
| Conversion Leak Checklist | `templates/08 Conversion Leak Checklist.md` | 5 items: CTA, form, trust, thank-you, mobile | 01, 09 |
| Trust Signal Placement Checklist | `templates/09 Trust Signal Placement Checklist.md` | Where to put social proof | 01 |
| Landing Page CTA Audit Criteria | `templates/10 Landing Page CTA Audit Criteria.md` | CTA audit criteria | 01, 09 |

---

## Part 3: Analysis Required — Instructions + Scripts + AI Prompts

### Message #1 & #9 — Conversion Teardown / 3 Fixes One-Pager

**Instructions:** `analysis/Conversion Teardown Instructions.md`

**What it does:** Analyze prospect's landing page for conversion leaks; produce 3 fixes with before/after.

**Step-by-step:**
1. Get asset (visit URL, screenshot)
2. Run through checklist (8 items: value prop, CTA, form length, trust signals, mobile, speed, headline match)
3. Identify 3 biggest leaks
4. Write one-pager: QUICK TAKE + 3 FIXES (Current / Change / Why)
5. Attach or paste into email

**Script (semi-automated):**
```bash
python3 scripts/run_conversion_teardown.py "https://example.com/landing-page"
```
Script extracts structure (forms, CTAs, headings); you add the 3 fixes narrative.

**AI Prompt:** Copy from doc; paste URL or HTML; get structured output.

---

### Message #2 — Attribution Snapshot

**Instructions:** `analysis/Attribution Snapshot Instructions.md`

**What it does:** Infer where attribution breaks (no analytics access) from website, ads, public info.

**Step-by-step:**
1. Map traffic sources (paid search, paid social, organic, webinars, email)
2. Check: Do ads link to dedicated landing pages or homepage?
3. Use checklist: Last-click only, no UTM, homepage as destination, form without source field, no cross-channel view
4. Write snapshot: OBSERVED + LIKELY GAPS + ONE CHANGE THAT WOULD SURFACE IT
5. Attach as PDF or paste

**Script:**
```bash
python3 scripts/run_attribution_check.py "https://example.com"
```
Looks for UTM params, forms, landing URL count. You add narrative.

**AI Prompt:** Copy from doc; paste URL; get structured output.

---

## Part 4: Template Content Summary (Key Elements)

### 01 Systems Ownership Checklist
- Table: System / Owner / Last reviewed / Documented
- Red flags: No owner 6+ months, multiple "owners," no login 90+ days, outdated docs, unclear integrations, no runbook
- Action: If 2+ red flags → schedule 30-min review

### 02 Drift Audit Template
- Per-system: name, purpose, users, owner, backup, escalation
- Dependencies, review cadence
- Status: Active/maintained | Active/no owner | Candidate for retirement | Replace
- Output: List orphan systems, no-cadence systems, retirement candidates; assign next steps

### 03 Decision Latency Worksheet
- Step 1: Top 5 operational decisions + answer time
- Step 2: Where delay sits (data gathering, manual work, waiting, tool/access)
- Step 3: Prioritize 1–2 highest impact
- Step 4: One change to cut answer time 50%+

### 04 Spend Reallocation Framework
- Q1: Attribution by channel (Yes/Partial/No)
- Q2: Conversion by stage (Visit→Lead, Lead→MQL, etc.)
- Q3: Spend vs outcome (cost per lead/MQL/opp)
- Q4: Decision cadence (weekly/monthly/quarterly/rarely)
- Summary: Score each area; identify action

### 08 Conversion Leak Checklist
- Above-the-fold CTA
- Form length and fields
- Trust signals
- Thank-you page and handoff
- Mobile and load
- Quick action: If 2+ unchecked, fix first

---

## Part 5: Campaign → Template Mapping

| Campaign | Primary Templates | Secondary |
|----------|-------------------|-----------|
| 01 Marketing Creative | Conversion Leak Checklist, Trust Signal | Landing Page CTA, UTM |
| 02 Attribution | Channel Scoring, UTM | — |
| 03 IT Director Ownership | Systems Ownership, Orphan Red Flags | Drift Audit |
| 04 IT Director Drift | Drift Audit | Systems Ownership |
| 05 Decision Latency | Decision Latency Worksheet | — |
| 06 Marketing VP Spend | Spend Reallocation | Channel Scoring |
| 07 Finance Director | System Ownership Map | — |
| 08 IT Director Backlog | Backlog Prioritization Matrix | — |
| 09 Marketing Manager | Conversion Leak, 3 Fixes (analysis) | — |
| 10 C-level KPI | KPI Latency Snapshot | Decision Latency |

---

## Part 6: Value-First Message Flow

1. **Day 1:** Send template or analysis output. No ask.
2. **If reply:** Offer brief call — low pressure.
3. **Segments:** Messages 1–2, 6, 9 → Marketing; 3–4, 8 → IT Director; 5, 10 → Data/Ops; 7 → Finance Director.
4. **Inbound alignment:** Mirror "looking for," "partner," "guidance," "migrate," "build."

---

## Part 7: Regeneration and Dependencies

| Output | Script | Input |
|--------|--------|-------|
| Conversion teardown structure | `run_conversion_teardown.py` | URL |
| Attribution check structure | `run_attribution_check.py` | URL |

Templates themselves are static. Analysis outputs are custom per prospect.

---

## Part 8: Quick Reference — "Which Doc for Whom"

| If targeting... | Use template | Or run analysis |
|-----------------|--------------|-----------------|
| Marketing Director + Creative | 08 Conversion Leak, 09 Trust Signal | 01 Conversion Teardown, 09 3 Fixes |
| Marketing Director + Attribution | 11 Channel Scoring, 13 UTM | 02 Attribution Snapshot |
| IT Director + Ownership/Drift | 01 Systems Ownership, 02 Drift Audit, 12 Orphan Red Flags | — |
| IT Director + Backlog | 06 Backlog Prioritization | — |
| Director + Decision Latency | 03 Decision Latency Worksheet, 07 KPI Latency | — |
| Marketing VP + Spend | 04 Spend Reallocation | — |
| Finance Director + Modern Workplace | 05 System Ownership Map | — |

---

**Start here:** [docs/README.md](README.md)
