# Reports — Deep Synthesis

**Purpose:** Analysis outputs, targeting matrices, lead lists, and frameworks. Use for outreach planning, messaging, and lead prioritization.

**Source:** All files under reports/, reports/consolidated/

---

## Part 1: Report Inventory and Purpose

| Report | Purpose | Data Source |
|--------|---------|-------------|
| **Cloud-Migration-Target-Analysis-Deep-Synthesis.md** | Niches, value props, 100 companies for cloud migrations | Reports, data, affirma_what_we_do |
| **Company Type Target Matrix.md** | Company Type × Ask → Service; service phrases | Inbound.xlsx |
| **Inbound Analysis Report.md** | Why qualified leads come in; category distribution | Inbound.xlsx |
| **Inbound What They Want.md** | Granular Ask, Title×Ask, Industry×Ask | Inbound.xlsx (deep parse) |
| **Messaging Framework Summary and Conclusion.md** | Consolidated messaging conclusions | Multiple |
| **Custom Dev Segmentation Analysis.md** | Titles, industries, sources for Custom Dev | Oops.csv |
| **Vendor Channel Persona Service Analysis Report.md** | Channel win rates, source recommendations | vendor analysis |
| **Company Service Title Patterns.md** | Company × Service × Title win patterns | Oops + Inbound + case studies |
| **Case Study Cadence Mapping.md** | Pain → case study → cadence | assets/ |
| **Case Study Value Prop Mapping.md** | Full case study list by service (323 assets) | assets/ |
| **Open Leads Best to Target.md** | Tier 1–2 leads for Modern Workplace | Open Leads export |
| **Texas CRM List Modern Workplace Targeting.md** | Texas contacts, title normalization | CRM export |
| **ATX Leads Best to Target.md** | Austin leads for MW and Marketing | atx leads |
| **Analysis Report.md** | Opportunity segmentation, win rates | Oops.csv |
| **Deep Parse Report.md** | CRM/account/opportunity structure | Multiple exports |

---

## Part 2: Consolidated Reports (reports/consolidated/)

| File | Content | Use When |
|------|---------|----------|
| README.md | Index and usage notes | Finding the right report |
| Reference.md | Ask → Service → Pain Point | Before writing copy |
| Inbound Report.md | What leads want, by ask/category/title/industry | Inbound optimization |
| Leads to Target Modern Workplace.md | Lead list with tiers, source tags | MW outreach prioritization |
| Targeting Matrix.md | Company type × service × title, channel | Segment outbound |
| Case Study Playbook.md | Pain → case study → cadence | Attach proof |
| Segment Performance.md | Value prop mapping + company patterns | Deep segment dive |

---

## Part 3: Targeting Logic — Report Flow

```
1. Identify prospect
   └─> Company Type Target Matrix / Reference.md
       (Company type → Service → Phrase)

2. Choose messaging
   └─> Messaging Framework Summary / Outbound
       (Persona → Channel → Offer)

3. Prioritize leads
   └─> Open Leads Best to Target / Texas CRM / ATX Leads
       (Tier 1–3 by title fit)

4. Attach proof
   └─> Case Study Playbook / Case Study Value Prop Mapping
       (Pain → Case Study)

5. Segment strategy
   └─> Vendor Channel / Company Service Title / Analysis Report
       (Win rates, channels, industries)
```

---

## Part 4: Key Matrices (Quick Reference)

### Company Type × Top Asks → Service

| Company Type | Top Asks | Services | Say This |
|--------------|----------|----------|----------|
| Government | SharePoint, Power BI, Google→M365 | Modern Workplace, Data & Analytics | "this SharePoint migration" / "this Power BI deployment" |
| Healthcare | SharePoint, Compliance, Dashboard | Modern Workplace, Data & Analytics | "this SharePoint migration" |
| Non-Profit | Dynamics, SharePoint, Migration | CRM, Modern Workplace | "this Dynamics implementation" / "this SharePoint migration" |
| MSP | BPO/Helpdesk, Power BI | Infrastructure/BPO, Data & Analytics | "this helpdesk outsourcing" |
| Financial Services | SharePoint, Dynamics | Modern Workplace, CRM | "this SharePoint migration" |
| Education, Manufacturing | Dynamics, Power BI | CRM, Data & Analytics | "this Dynamics implementation" |

---

### Ask → Service → Phrase

| Ask | Service | Phrase |
|-----|---------|--------|
| SharePoint (any) | Modern Workplace | "this SharePoint migration" / "this intranet build" |
| Power BI, Dashboards | Data & Analytics | "this Power BI deployment" |
| Dynamics, CRM | CRM | "this Dynamics implementation" |
| HubSpot, SEO | Marketing Services | "this HubSpot setup" |
| AI, Copilot | AI / Automation | "this AI rollout" |
| BPO, Helpdesk | Infrastructure / BPO | "this helpdesk outsourcing" |
| Google→M365, Tenant | Infrastructure | "this migration" |

---

## Part 5: Lead List Sources and Tiers

### Open Leads (409 total)
- **Tier 1:** IT Director+, infrastructure/cloud ownership. 9 named contacts.
- **Tier 2:** CTO/VP, mixed Marketing+Tech.
- **Campaign:** 03 Ownership, 04 Drift. Email first, then LinkedIn.

### Texas CRM (1,336 contacts, 100 shown)
- **Tier 1:** IT/Tech VP, Director. 10 contacts. Email first, LinkedIn Day 3/7.
- **Tier 2:** IT Manager, cloud-adjacent. 6 contacts.
- **Tier 3:** Champions only (IC). Need Director intro.
- **Skip:** Marketing, Sales, BD, Healthcare non-IT, Retail, HR, Finance (non-IT).

### ATX Leads (Austin-focused)
- **Modern Workplace:** 16 contacts. IT Director+, infrastructure.
- **Marketing Services:** 28 contacts. Marketing Director+, Brand, Creative.
- **Local angle:** "Austin-based consulting firm" for coffee/call.

---

## Part 6: Channel Recommendations (from Vendor Analysis)

| Channel | Win Rate | Action |
|---------|----------|--------|
| Account Management Campaign | 63% | **RUN** — double down |
| Customer Expansion | 47% | **RUN** |
| Inbound/Retargeting | 44% | **RUN** |
| Personal Network | 50% | **TEST** |
| SEO | 45% | **TEST** |
| LinkedIn | 19% | Segment-specific only (Marketing × Creative) |
| PPC | 43% | Nurture; don't scale cold |
| Partners | 0% | Fix or stop |

---

## Part 7: Regeneration Commands

| Report | Command |
|--------|---------|
| Inbound What They Want | `python3 scripts/deep_parse_inbound.py` |
| Inbound Analysis | `python3 scripts/analyze_inbound.py` |
| Company Type Target Matrix | `python3 scripts/company_target_matrix.py` |
| Company Service Title Patterns | `python3 scripts/company_service_title_analysis.py` |
| Analysis Report | `python3 scripts/run_analysis.py` |
| ATX Leads | `python3 scripts/analyze_atx_leads.py` |
| Case Study Cadence | `python3 scripts/parse_case_studies.py` |

---

## Part 8: Cross-References

| If you need... | See |
|----------------|-----|
| Full Messaging Framework | outbound/Messaging Framework.md |
| Segment Packs + copy variants | outbound/Segment Packs Outbound.md |
| SDR quick start | outbound/SDR Starter Guide.md |
| Templates for attachments | docs/templates/ |
| Cloud migration targets | reports/Cloud-Migration-Target-Analysis-Deep-Synthesis.md |
| Data sources | data/ |

---

**Start here:** [reports/consolidated/README.md](consolidated/README.md)
