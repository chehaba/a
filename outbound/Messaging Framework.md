# Outbound Messaging Framework — Statistical Basis

**Data source:** Oops.csv (562 opportunities, 35.4% win rate)  
**Inbound source:** data/Inbound/Inbound.xlsx (550 qualified leads) — [Inbound Analysis Report](../reports/Inbound%20Analysis%20Report.md)  
**Purpose:** Match message to persona, service, channel, and industry using validated performance data.

---

## 1. Statistical Foundation (Quick Reference)

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

### Channel Fit (LinkedIn Only)

| Function × Service | n | Win% | Use LinkedIn? |
|-------------------|---|------|----------------|
| Marketing × Creative | 11 | 54.5% | **Yes** |
| Marketing × Marketing Services | 11 | 27.3% | Test only |
| Other × Custom Dev | 30 | 6.7% | **No** |
| Other × Data & Analytics | 12 | 8.3% | **No** |

---

## 2. Segment → Channel → Message Matrix

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

## 3. Financial Expression Templates (Director/VP)

Use these when speaking to Director+ or C-level. Budget owners need one of four levers.

### Creative
> This investment will **increase revenue** by tightening conversion from existing traffic and fixing leaks in landing page → nurture, resulting in higher pipeline yield without adding headcount.

### Marketing Services
> This investment will **reduce cost** and **increase revenue** by improving spend allocation and attribution clarity, resulting in faster reallocation and less wasted budget.

### Modern Workplace / Infrastructure
> This investment will **reduce cost** and **protect revenue** by putting owners + cadence around cloud/app drift, resulting in lower downtime risk and more controlled infrastructure spend.

### Data & Analytics (reframed)
> This investment will **increase revenue** and **reduce cost** by reducing decision latency (time-to-answer for key questions), resulting in faster corrective action and less performance leakage.

### Custom Dev
> This investment will **reduce cost** and **increase revenue capacity** by bringing a ready-to-run team for backlog reduction, resulting in faster time to ship without hiring.

### CRM
> This investment will **increase revenue** and **protect revenue** by improving pipeline accuracy and sales discipline, resulting in higher conversion and reduced churn.

### AI / Automation
> This investment will **reduce cost** and **increase revenue capacity** by automating manual processes, resulting in improved margins without proportional headcount growth.

### 3b. Service-Specific Phrasing (Use Instead of "This Investment")

**Choose the phrase that matches the service you're selling.** See [Company Type Target Matrix](../reports/Company%20Type%20Target%20Matrix.md).

| Service | Say This |
|---------|----------|
| Modern Workplace (SharePoint, Intranet, M365) | "This SharePoint migration" / "This intranet build" |
| Data & Analytics | "This Power BI deployment" |
| CRM | "This Dynamics implementation" |
| Marketing Services | "This HubSpot setup" |
| AI / Automation | "This AI rollout" |
| Infrastructure / BPO | "This helpdesk outsourcing" / "This migration" |

**Example:** Instead of "This investment will reduce cost..." → "**This SharePoint migration** will reduce cost and protect revenue by putting owners + cadence around drift..."

---

## 4. Persona-Based Framing Rules

### Director / VP / C-level (win better)
- Lead with outcome, not capability.
- Use financial lever in first 1–2 sentences.
- CTA: strategic (audit, review, benchmark).
- Example: "Worth a 15-min review to see where conversion leaks."

### Manager / IC (underperform; different frame)
- Lead with execution unblocker, not strategy.
- Avoid "we help you think differently."
- CTA: low-friction, specific, short.
- Example: "Want 3 quick fixes we can implement this week?"

---

## 5. Company Type → Who to Target With What

*(From inbound: Company Type × Ask × Service. See [Company Type Target Matrix](../reports/Company%20Type%20Target%20Matrix.md).)*

| Company Type | Primary Service to Message | Phrase |
|--------------|----------------------------|--------|
| Government | Modern Workplace, Data & Analytics | "this SharePoint migration" / "this Power BI deployment" |
| Healthcare | Modern Workplace, Data & Analytics | "this SharePoint migration" |
| Non-Profit | CRM, Modern Workplace | "this Dynamics implementation" / "this SharePoint migration" |
| MSP | Infrastructure/BPO, Data & Analytics | "this helpdesk outsourcing" |
| Construction, Legal | Modern Workplace | "this SharePoint migration" |
| Education, Manufacturing | CRM, Data & Analytics | "this Dynamics implementation" |
| Financial Services | Modern Workplace, CRM | "this SharePoint migration" / "this Dynamics implementation" |

**To improve accuracy:** Add Email column to your CRM export. Domain-based inference (.gov, .edu, healthcare.com, etc.) will classify company type when description doesn't mention it.

---

## 6. Industry-Specific Hooks

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

## 7. Message Components by Segment

### Segment A: LinkedIn → Marketing × Creative

**Variant 1 — Conversion leak**
- **Hook:** We usually spot 2–3 conversion leaks in 10 minutes.
- **Body:** Most teams have traffic but leave pipeline on the table. We help tighten conversion from landing page through nurture—without adding headcount.
- **Financial:** Increase revenue by fixing conversion → higher pipeline yield.
- **CTA:** Want me to do a quick teardown and send 3 fixes?

**Variant 2 — Attribution clarity**
- **Hook:** We help teams see what's working vs not—and where spend leaks.
- **Body:** Simple reporting + decision cadence so you reallocate faster. Creative performance benchmark in one call.
- **Financial:** Reduce cost (spend efficiency) + increase revenue (reallocation).
- **CTA:** Want a creative performance benchmark (ads + landing pages)?

---

### Segment B: Email + LinkedIn → IT Director × Modern Workplace / Infrastructure

**Variant 1 — Ownership + drift**
- **Hook:** Most waste comes from "nobody owns this system anymore."
- **Body:** We help put owners + rules + cadence around cloud/app drift. Reduces multi-stakeholder chaos.
- **Financial:** Reduce cost, protect revenue (downtime risk).
- **CTA:** Worth a 15-min check if you have any orphan systems or drift right now?

**Variant 2 — Time compression**
- **Hook:** We help reduce backlog by bringing in a ready-to-run team.
- **Body:** 2-week scoping sprint, fixed output: plan + effort bands. No long discovery cycles.
- **Financial:** Increase revenue capacity (faster delivery), reduce cost (no ramp).
- **CTA:** Want a 30-minute systems ownership + drift review?

---

### Segment C: Email → Data & Analytics (Director+)

**Variant 1 — Decision latency**
- **Hook:** How long does it take to answer basic performance questions?
- **Body:** We reduce KPI reporting time and create owner-based alerts. Fix the few reports that drive the biggest decisions.
- **Financial:** Increase revenue, reduce cost (decision accuracy, wasted spend).
- **CTA:** Want a quick "decision latency" audit—where answers get stuck and why?

**Variant 2 — Operational control**
- **Hook:** We fix the few reports that drive the biggest decisions.
- **Body:** Power BI / reporting healthcheck with 5 fixes prioritized by ROI. Alerts on deviations + owners + action loops.
- **Financial:** Reduce cost (reporting time), increase revenue (faster action).
- **CTA:** Want an executive KPI latency audit?

---

### Segment D: Director of Finance × Modern Workplace (highest-scoring)

**Hook:** Director of Finance has 100% win rate (6/6) on Modern Workplace.
- **Angle:** Reliability, continuity, audit trail, cost predictability.
- **Body:** We help put owners + cadence around critical systems. Fewer surprises, clearer spend control.
- **CTA:** Worth a 15-min review of your key system ownership and drift?

---

## 8. Don't-Use Rules (Statistically Validated)

| Rule | Data |
|------|------|
| Don't run LinkedIn for Custom Dev to "Other" roles | 6.7% win (n=30) |
| Don't run LinkedIn for Data & Analytics (current packaging) | 8.3% win (n=12) |
| Don't lead with "we do analytics/dashboards" for Data & Analytics | 18.3% overall win |
| Don't target Manager/IC as primary outbound unless frame is execution-only | -9 to -14 pp lift |
| Don't over-pitch multi-opp accounts; reduce perceived scope | 24.4% win vs 40%+ single |
| Don't prioritize Software without sub-segmenting by title | 20.3% win (n=133) |
| Don't prioritize Transportation, Organizations | 10–13% win |

---

## 9. Testing Protocol

1. **One variable per test:** Change hook OR offer; hold persona, channel, industry constant.
2. **Sample size:** 80–150 per variant (per segment).
3. **Success ladder:** Reply rate → meeting set rate → opp created rate.
4. **Duration:** 7–10 days per test.
5. **Winner:** Keep higher reply rate; kill loser; expand only segments that work.

---

## 10. Quick Lookup: "Who Gets What"

| If targeting... | Use channel | Use offer | Lead with... |
|-----------------|-------------|-----------|--------------|
| Marketing Director + Creative | LinkedIn | Teardown / Benchmark | Conversion leaks or attribution |
| Marketing Director + Marketing Services | Email | Attribution audit | Spend leaks, reallocation |
| IT Director + Modern Workplace | Email first | Ownership + drift | "Nobody owns this" |
| IT Director + Data & Analytics | Email | Decision latency | Time-to-answer |
| Finance Director + Modern Workplace | Email | Ownership review | Reliability, control |
| Manager/IC (any) | Email | Tactical fix | Execution unblocker, 3 fixes |
| Non-Profit, Healthcare, Gov | Any | Same offers, add compliance/reliability angle | Industry hook first |

---

## 11. Inbound Insights (Apply to All Messaging)

**Source:** 550 qualified inbound leads. See [Inbound Analysis Report](../reports/Inbound%20Analysis%20Report.md) and [Inbound What They Want](../reports/Inbound%20What%20They%20Want.md) (deep parse: industry × ask, pain language, size bands).

### Why they come in (top categories)
- **SharePoint** (25%+) — General, migration, intranet, restructure
- **Dynamics/CRM** (10%) — Implementation, GP→BC, CRM setup
- **Power BI** (9%) — Dashboards, Tableau/SSRS migration
- **BPO/Helpdesk** (7%) — L1/L2, call center, MSP outsourcing
- **Migration** — Exchange, tenant, Google, on-prem, file server
- **Support** — Ongoing, maintenance, EOL upgrade

### Language to mirror
| They say | Use in copy |
|----------|-------------|
| "looking for" (144) | "I know you're looking for..." |
| "migrate" (89) | "Migration mandate" / "need to move off" |
| "build" (59) | "Build" / "help you build" |
| "partner" (51) | "Partner" not "vendor" |
| "guidance" (15) | "Guidance" / "need guidance" |

### Pain hooks (from inbound)
- "Struggling" / "urgent" / "broken" (high frequency)
- "End of life" / "EOL upgrade" / "messy/cluttered"
- "Information overload with the M365 stack"
- "Migration mandate" / "need to move off [legacy]"
- "Looking for a partner to guide us"
- "Lean team" / "no internal IT"

### Alignment
Outbound messaging for IT Director, Modern Workplace, Infrastructure should echo these inbound themes (SharePoint, migration, Power Platform, support) to match what converts when they find you via PPC/SEO.

---

## 12. Data Sources

- Persona normalization: `scripts/persona_normalization.py`
- Full analysis: `scripts/run_analysis.py`
- Inbound analysis: `reports/Inbound Analysis Report.md`
- Inbound deep parse: `reports/Inbound What They Want.md` (run `scripts/deep_parse_inbound.py`)
- Company type target matrix: `reports/Company Type Target Matrix.md` (run `scripts/company_target_matrix.py`) — Company Type × Ask × Service; service-specific phrases to replace "this investment"
- Segment packs: `Segment Packs Outbound.md`
- Financial framework: System Prompt.pdf
