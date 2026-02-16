# Outbound — Deep Synthesis

**Purpose:** Evidence-based outbound messaging: persona, channel, offer, copy variants. Match message to segment using validated win rates.

**Source:** Messaging Framework.md, Segment Packs Outbound.md, SDR Starter Guide.md, Value First Message Templates.md, value-first-campaigns/

---

## Part 1: Statistical Foundation (Oops.csv, 562 opportunities)

### Persona Win Rates (Function × Seniority)

| Persona | n | Win% | Lift | Frame |
|---------|---|------|------|-------|
| Marketing Director | 21 | 52.4% | +17 | Strategy, pipeline, conversion |
| Other VP | 26 | 46.2% | +11 | Outcomes, ownership, decision speed |
| IT/Tech Director | 48 | 45.8% | +10 | Ownership, drift, reliability |
| Marketing VP | 16 | 43.8% | +8 | Same as Director |
| IT/Tech Manager | 23 | 26.1% | -9 | Execution, unblockers, less strategy |
| IT/Tech IC | 16 | 25.0% | -10 | Tactical, specific ask |
| Other Manager | 128 | 21.9% | -14 | Execution, proof, low-friction CTA |

**Pattern:** Director/VP outperform; Manager/IC underperform → different framing.

---

### Service Win Rates

| Service | Win% | Best Frame |
|---------|------|------------|
| CRM | 45.2% | Pipeline accuracy, conversion, churn |
| Creative | 42.9% | Conversion leaks, attribution |
| Modern Workplace | 42.0% | Reliability, drift, ownership |
| Marketing Services | 40.8% | Spend allocation, decision cadence |
| Infrastructure | 40.0% | Reliability, ownership, scalability |
| Custom Dev | 24.3% | Ready-to-run team, backlog reduction |
| Data & Analytics | 18.3% | Decision latency, not "analytics" |

---

### Industry Win Rates

| Industry | Win% | Prioritize |
|----------|------|------------|
| Non-Profit | 83.3% | High |
| Government | 58.3% | High |
| Healthcare | 47.9% | High |
| Energy, Utilities, Waste | 47.4% | High |
| Business Services | 46.3% | High |
| Software | 20.3% | Low (unless sub-segmented) |
| Transportation | 10.0% | Avoid |
| Organizations | 13.3% | Avoid |

---

### Channel Fit (LinkedIn Only)

| Function × Service | n | Win% | Use LinkedIn? |
|-------------------|---|------|---------------|
| Marketing × Creative | 11 | 54.5% | **Yes** |
| Marketing × Marketing Services | 11 | 27.3% | Test only |
| Other × Custom Dev | 30 | 6.7% | **No** |
| Other × Data & Analytics | 12 | 8.3% | **No** |

---

## Part 2: Segment → Channel → Message Matrix

| Segment | Channel | Primary Offer | Financial Lever |
|---------|---------|---------------|-----------------|
| Marketing Director/VP × Creative | LinkedIn | Conversion teardown | Increase revenue (conversion) |
| Marketing Director/VP × Marketing Services | Email | Attribution + reallocation | Reduce cost (spend efficiency) |
| IT Director × Modern Workplace | Email, then LinkedIn | Ownership + drift review | Reduce cost, protect revenue |
| IT Director × Infrastructure | Email | Reliability + governance | Protect revenue, reduce cost |
| IT Director × Data & Analytics | Email | Decision latency audit | Increase revenue, reduce cost |
| Finance/C-level × Data & Analytics | Email | KPI latency + owner alerts | Reduce cost, capital efficiency |
| Manager/IC (any) | Email | Tactical, low-friction CTA | Execution unblocker |

---

## Part 3: Financial Expression Templates (Director/VP)

Every pitch must tie to one of four levers: increase revenue, protect revenue, reduce cost, increase capital efficiency.

| Service | Template |
|---------|----------|
| Creative | "This investment will **increase revenue** by tightening conversion from existing traffic and fixing leaks..." |
| Marketing Services | "This investment will **reduce cost** and **increase revenue** by improving spend allocation and attribution clarity..." |
| Modern Workplace / Infrastructure | "This investment will **reduce cost** and **protect revenue** by putting owners + cadence around cloud/app drift..." |
| Data & Analytics | "This investment will **increase revenue** and **reduce cost** by reducing decision latency (time-to-answer)..." |
| Custom Dev | "This investment will **reduce cost** and **increase revenue capacity** by bringing a ready-to-run team for backlog reduction..." |
| CRM | "This investment will **increase revenue** and **protect revenue** by improving pipeline accuracy and sales discipline..." |
| AI / Automation | "This investment will **reduce cost** and **increase revenue capacity** by automating manual processes..." |

**Replace "this investment" with service phrase:** "this SharePoint migration," "this Power BI deployment," "this Dynamics implementation," etc.

---

## Part 4: Copy Variants by Segment

### Segment A: LinkedIn — Marketing × Creative

**Variant 1 — Conversion leak**
- Hook: We usually spot 2–3 conversion leaks in 10 minutes.
- Body: Most teams have traffic but leave pipeline on the table. We help tighten conversion from landing page through nurture—without adding headcount.
- CTA: Want me to do a quick teardown and send 3 fixes?

**Variant 2 — Attribution clarity**
- Hook: We help teams see what's working vs not—and where spend leaks.
- Body: Simple reporting + decision cadence so you reallocate faster. Creative performance benchmark in one call.
- CTA: Want a creative performance benchmark (ads + landing pages)?

---

### Segment B: Email + LinkedIn — IT Director

**Variant 1 — Ownership + drift**
- Hook: Most waste comes from "nobody owns this system anymore."
- Body: We help put owners + rules + cadence around cloud/app drift. Reduces multi-stakeholder chaos.
- CTA: Worth a 15-min check if you have any orphan systems or drift right now?

**Variant 2 — Time compression**
- Hook: We help reduce backlog by bringing in a ready-to-run team.
- Body: 2-week scoping sprint, fixed output: plan + effort bands. No long discovery cycles.
- CTA: Want a 30-minute systems ownership + drift review?

---

### Segment C: Email — Data & Analytics (Director+)

**Variant 1 — Decision latency**
- Hook: How long does it take to answer basic performance questions?
- Body: We reduce KPI reporting time and create owner-based alerts. Fix the few reports that drive the biggest decisions.
- CTA: Want a quick "decision latency" audit—where answers get stuck and why?

**Variant 2 — Operational control**
- Hook: We fix the few reports that drive the biggest decisions.
- Body: Power BI / reporting healthcheck with 5 fixes prioritized by ROI. Alerts on deviations + owners + action loops.
- CTA: Want an executive KPI latency audit?

---

### Segment D: Finance Director × Modern Workplace (100% win)

- Hook: Director of Finance has 100% win rate (6/6) on Modern Workplace.
- Angle: Reliability, continuity, audit trail, cost predictability.
- Body: We help put owners + cadence around critical systems. Fewer surprises, clearer spend control.
- CTA: Worth a 15-min review of your key system ownership and drift?

---

## Part 5: Don't-Use Rules (Statistically Validated)

| Rule | Data |
|------|------|
| Don't run LinkedIn for Custom Dev to "Other" roles | 6.7% win (n=30) |
| Don't run LinkedIn for Data & Analytics | 8.3% win (n=12) |
| Don't lead with "we do analytics/dashboards" | 18.3% overall Data & Analytics win |
| Don't target Manager/IC as primary unless execution-only | -9 to -14 pp lift |
| Don't over-pitch multi-opp accounts | 24.4% win vs 40%+ single |
| Don't prioritize Software without sub-segmenting | 20.3% win (n=133) |
| Don't prioritize Transportation, Organizations | 10–13% win |

---

## Part 6: Value-First Messages (No Meeting Ask)

10 messages that offer free value upfront. No ask on first touch.

| # | Segment | Free Value |
|---|---------|------------|
| 1 | Marketing Director × Creative | Conversion teardown (3 fixes) |
| 2 | Marketing Director × Creative | Attribution snapshot |
| 3 | IT Director × Modern Workplace | Systems Ownership Checklist |
| 4 | IT Director × Infrastructure | Drift Audit Template |
| 5 | Director × Data & Analytics | Decision Latency Worksheet |
| 6 | Marketing VP × Marketing Services | Spend Reallocation Framework |
| 7 | Finance Director × Modern Workplace | System Ownership Map |
| 8 | IT Director × Custom Dev | Backlog Prioritization Matrix |
| 9 | Marketing Manager × Creative | 3 Fixes One-Pager |
| 10 | C-level / VP × General | KPI Latency Snapshot |

**Templates:** docs/templates/. **Analysis:** docs/analysis/ (+ scripts for 1, 2, 9).

---

## Part 7: Value-First Campaigns (31-Day Cadences)

**Location:** value-first-campaigns/[Campaign Name]/Day N.md

**Campaigns:**
- 05 Director Decision Latency
- 06 Marketing VP Spend
- (Others per generate_cadence_templates.py)

**Structure per day:** Persona, Campaign, Day, Channel; Subject; Body; FREE VALUE; ATTACH; CTA.

**Rule:** Day 1 = no ask. Subsequent days = soft CTA. Attach template on CTA days.

---

## Part 8: SDR Starter Guide — 3 Campaigns

### Campaign 1: Marketing + Creative (LinkedIn)
- Who: Marketing Directors and VPs
- Message: Conversion leaks or attribution benchmark
- CTA: Reply or book 15-min teardown

### Campaign 2: IT Directors (Email first, then LinkedIn)
- Who: IT Directors, Directors of IT, CIOs
- Message: "Nobody owns this" / ownership + drift
- CTA: Book 15–30 min review

### Campaign 3: Data & Analytics (Email only)
- Who: Directors and VPs in Ops, Finance, IT (not analysts)
- Don't say: "We do analytics and dashboards"
- Do say: "We reduce how long it takes to get answers"
- CTA: Book quick audit

---

## Part 9: Industry-Specific Hooks

| Industry | Hook Angle |
|----------|------------|
| Healthcare | Compliance, reliability, patient data workflows |
| Non-Profit | Cost containment, donor/revenue protection |
| Government | Compliance, continuity, audit trail |
| Business Services | Operational efficiency, client delivery |
| Energy/Utilities | Reliability, asset management, regulatory |
| Manufacturing | Production continuity, supply chain visibility |
| Software | Pipeline, conversion (Marketing only); avoid generic IT |
| Finance | Decision latency, KPI cadence, risk visibility |

---

## Part 10: Inbound Alignment (Mirror Their Language)

| They say | Use in copy |
|----------|-------------|
| "looking for" (144) | "I know you're looking for..." |
| "migrate" (89) | "Migration mandate" / "need to move off" |
| "build" (59) | "Build" / "help you build" |
| "partner" (51) | "Partner" not "vendor" |
| "guidance" (15) | "Guidance" / "need guidance" |

**Pain hooks:** struggling, urgent, broken, end of life, messy/cluttered, information overload, lean team.

---

## Part 11: Quick Lookup — "Who Gets What"

| If targeting... | Channel | Offer | Lead with... |
|-----------------|---------|-------|---------------|
| Marketing Director + Creative | LinkedIn | Teardown / Benchmark | Conversion leaks or attribution |
| Marketing Director + Marketing Services | Email | Attribution audit | Spend leaks, reallocation |
| IT Director + Modern Workplace | Email first | Ownership + drift | "Nobody owns this" |
| IT Director + Data & Analytics | Email | Decision latency | Time-to-answer |
| Finance Director + Modern Workplace | Email | Ownership review | Reliability, control |
| Manager/IC (any) | Email | Tactical fix | Execution unblocker, 3 fixes |
| Non-Profit, Healthcare, Gov | Any | Same offers + compliance angle | Industry hook first |

---

## Part 12: Testing Protocol

1. One variable per test: Change hook OR offer; hold persona, channel, industry constant.
2. Sample size: 80–150 per variant per segment.
3. Success ladder: Reply rate → meeting set rate → opp created rate.
4. Duration: 7–10 days per test.
5. Winner: Keep higher reply rate; kill loser; expand only segments that work.

---

**Data sources:** Oops.csv, Inbound.xlsx. **Regenerate:** persona_normalization.py, run_analysis.py.
