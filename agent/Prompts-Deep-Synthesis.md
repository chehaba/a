# Prompts — Deep Synthesis

**Purpose:** System prompts for AI agents. Guide Parse → Find → Interpret → Construct workflow for targeting and messaging.

**Source:** Cloud Migration Targeting System Prompt.md, Messaging Prompt System Prompts.md

---

## Part 1: Prompt Inventory

| Prompt | Purpose | Triggers |
|--------|---------|----------|
| **Cloud Migration Targeting System Prompt** | Target companies for cloud migration; parse repo, filter for Microsoft workload | "Find companies to target for cloud migration" |
| **Messaging Prompt System Prompts** | Create/refine messaging motions; Parse → Find → Interpret → Construct | "Create messaging motion for [ICP/industry/service]" |

---

## Part 2: Cloud Migration Targeting — Workflow

### 1. Parse the Repository

**Assets to read first:**

| Asset | Path | Extract |
|-------|------|---------|
| Market Analysis Tables | cloud-migration-modernization/Market Analysis Tables.md | Named companies, legacy targets, barriers |
| Targeting Strategy | cloud-migration-modernization/Targeting Strategy.md | ICP, scope, messaging angles |
| Enterprise Legacy On-Prem | outbound/Enterprise Legacy On-Prem Sales Motion.md | Role-based messaging |
| Messaging Framework | outbound/Messaging Framework.md | Persona templates |
| Opportunity data | data/opportunities/Oops.csv | Win rates |
| Inbound | data/Inbound/ | Ask patterns |
| ATX best leads | reports/ATX Leads Best to Target.md | Austin contacts |
| Company Target Matrix | reports/Company Type Target Matrix.md | Company type → service → phrase |
| Case studies | assets/case-studies/ | Client names, services |

**Scripts:** company_target_matrix.py, deep_parse_inbound.py, analyze_atx_leads.py

### 2. Find Relevant Information

- Named companies from vendor lists (SAP, AWS, Salesforce, Microsoft)
- Industry fit: Healthcare, Government, Manufacturing, Financial Services
- Persona fit: IT Director, VP IT, CIO, CTO
- Service mapping: Modern Workplace, Infrastructure — not mainframes, core ERP
- Trigger events: AI initiatives, end-of-life, compliance, M&A

### 3. Interpret

- **Scope filter:** Microsoft collaboration stack only. Exclude mainframe, SAP RISE-only, Oracle-only.
- **Prioritize:** Companies on Dynamics, Copilot, Azure = easier extension.
- **Pain language:** Data silos, AI-ready architecture, TCO, compliance.
- **Campaign alignment:** 03 Ownership, 04 Drift, 08 Backlog, Enterprise Legacy On-Prem.

### 4. Construct Output

- Target list: Company, industry, signal, priority tier
- Messaging: Role-based (Champion, Influencer, DM). Service-specific phrasing.
- Sources cited
- Regeneration commands

### Critical Constraints

- Do NOT suggest mainframe or Oracle DB migrations as primary Affirma opportunities
- Do NOT use generic "this investment" when service phrase is known
- Do NOT ignore Enterprise Legacy On-Prem for CIO/CTO
- DO cross-reference vendor lists with CRM
- DO filter for Microsoft-adjacent workloads

---

## Part 3: Messaging Motion — Workflow

### 1. Parse

- Identify data sources: CRM exports, inbound forms
- Extract: Status, Source Campaign, Description, Title, Industry, Size, Email
- Handle missing: Use description fallback; document inferred vs explicit

### 2. Find

- Ask/Category extraction: Regex/keyword for SharePoint, Power BI, Dynamics, BPO
- Company type: From email domain (.gov, .edu) or description
- Persona: Map title to Function × Seniority
- Cross-tabulate: Company Type × Ask, Title × Ask, Source × Ask

### 3. Interpret

- Connect Ask → Service
- Identify financial levers (revenue, cost, protect, capacity)
- Spot pain language (struggling, urgent, end of life)
- Validate with win rates

### 4. Construct

- Service-specific phrasing
- Role-based messaging (Champion, Influencer, DM, Stakeholder)
- ICP definition
- Cadence by role

### Output Rules

- Plain English, short bullets, no jargon
- Evidence-based; cite source
- Actionable phrases, subject lines, CTAs
- Structured (tables, matrices)
- Regenerable (paths, scripts)

### Messaging Construction Checklist

- [ ] ICP defined
- [ ] Buying committee mapped
- [ ] Pain points per role
- [ ] Ask → Service mapping explicit
- [ ] Service-specific phrasing (no generic "this investment")
- [ ] Financial lever per service
- [ ] Cadence by role
- [ ] Data sources and regen commands documented
- [ ] Cross-reference to Messaging Framework, Company Type Target Matrix

---

## Part 4: Affirma Messaging Reference (Embedded in Messaging Prompt)

**Tagline:** Intelligent Technology. Stronger Outcomes.

**Positioning:**
- Consulting partner built to turn technology spend into clear business results
- Breadth of big integrator + speed of specialist
- One team across Modern Workplace, Data & Analytics, CRM, Infrastructure
- Faster cycle times; alignment to outcomes; no permanent headcount bloat

**One line:** Affirma gives you big-integrator depth and specialist responsiveness in one team, so you get faster delivery and clearer outcomes without adding permanent headcount.

---

## Part 5: When Data Is Missing

| Missing | Fallback | Label |
|---------|----------|-------|
| No Email | Industry from description | "Add Email for domain inference" |
| No Title | Infer from description | "Inferred" |
| No Win Rates | Inbound volume + Company Type × Ask | "Directional" |
| Small N | Report counts | "Exploratory" |

---

## Part 6: Anti-Patterns

- Do not invent data
- Do not use generic "this investment" when service phrase known
- Do not ignore company type
- Do not produce long prose (prefer bullets, tables)
- Do not omit regeneration commands

---

## Part 7: Example Triggers and Expected Agent Behavior

**"Find companies to target for cloud migration in [region/industry]."**

Agent should: Parse market tables + targeting strategy; load Oops + inbound; cross-reference vendor lists; filter Microsoft workload + industry; output ranked list with messaging; cite sources; document regen commands.

**"Create messaging motion for [ICP / industry / service]."**

Agent should: Parse available data; Find patterns (Ask, Company Type, Title×Ask); Interpret (Ask→Service, pain, financial levers); Construct (role-based messaging, cadence, ICP, phrases); Document sources; Cross-reference frameworks.

---

## Part 8: Repository Structure (for Agent Context)

```
/
├── cloud-migration-modernization/   # Market tables, targeting
├── data/
│   ├── Inbound/
│   ├── opportunities/
│   ├── patterns/
│   └── affirma-services/
├── outbound/                        # Messaging Framework, campaigns
├── prompts/                         # These prompts
├── reports/                         # ATX, matrices, analyses
├── scripts/                         # Analysis scripts
└── assets/case-studies/             # Proof points
```

---

**Use these prompts** when invoking AI agents for targeting or messaging construction.
