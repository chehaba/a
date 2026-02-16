# Prospecting — Segmentation & Outbound

Sales prospecting analysis, messaging framework, and value-first outbound assets.

---

## Structure

```
├── data/              Raw data (Excel, CSV, PDF)
│   ├── opportunities/  Won/Lost opps, pipeline, Oops.csv
│   ├── accounts/      Account base exports
│   ├── leads/         Leads, campaign analysis
│   ├── inbound/       Qualified inbound leads (Inbound.xlsx)
│   ├── austin-chamber/ Austin Chamber directory scrapes
│   └── reference/     PDFs, misc reference docs
├── assets/            Case studies (PowerPoint), reference materials
├── scripts/           Analysis and helper scripts
├── reports/           Analysis outputs (segmentation, deep parse, company targeting)
├── outbound/          Messaging framework, SDR guide, segment packs, sales motions
├── prompts/           System prompts for AI agents (messaging construction)
└── docs/              Value-first templates and analysis instructions
    ├── templates/     Static docs (ownership checklist, drift audit, etc.)
    └── analysis/      Instructions + AI prompts for conversion/attribution
```
# Repository Structure

## Quick navigation

### Data
| Path | Contents |
|------|----------|
| `data/opportunities/` | Oops.csv, pipeline exports |
| `data/inbound/` | Inbound.xlsx |
| `data/patterns/` | Company × Service × Title (channel-agnostic) |
| `data/austin-chamber/` | Austin Chamber directory scrape |
| `data/outbound_only/` | Outbound-filtered datasets (optional branch) |

### Assets — Case studies by service
| Path | Contents |
|------|----------|
| `assets/case-studies/Modern Workplace/` | SharePoint, M365, Teams, intranet |
| `assets/case-studies/CRM/` | Salesforce, Dynamics |
| `assets/case-studies/Data Analytics/` | Power BI, BI |
| `assets/case-studies/Marketing/` | HubSpot, Pardot, demand gen |
| `assets/case-studies/Custom Dev/` | Apps, portals, mobile |
| `assets/case-studies/AI Automation/` | Copilot, agents |
| `assets/case-studies/Infrastructure/` | MDM, Intune |
| `assets/case-studies/Creative/` | Video, webinar, design |
| `assets/case-studies/Other/` | Mixed, proposals |

### Reports
| Path | Contents |
|------|----------|
| `reports/Company Service Title Patterns.md` | Company × Service × Buyer Title (no channel) |
| `reports/Case Study Value Prop Mapping.md` | Case studies → value props |
| `reports/Case Study Cadence Mapping.md` | Case studies → cadences |
| `reports/Vendor Channel Persona Service Analysis Report.md` | Channel/vendor analysis |
| `reports/Inbound What They Want.md` | Inbound ask/title patterns |
| `reports/Company Type Target Matrix.md` | Company type × service |

### Scripts
| Script | Purpose |
|--------|---------|
| `scripts/company_service_title_analysis.py` | Company × Service × Title (patterns, no channel) |
| `scripts/organize_assets_by_service.py` | Organize PPTXs by service |
| `scripts/parse_all_case_studies.py` | Case study → value prop mapping |
| `scripts/company_target_matrix.py` | Company type × ask × service |
| `scripts/persona_normalization.py` | Title → Function × Seniority |
| `scripts/run_analysis.py` | Segmentation analysis |

### Outbound
| Path | Contents |
|------|----------|
| `outbound/` | Messaging framework, cadences, templates |
| `outbound/value-first-campaigns/` | 31-day cadences by persona |
---

## Quick Start

**Run segmentation analysis:**

```bash
python3 scripts/run_analysis.py
```

**Run persona normalization + target lists:**

```bash
python3 scripts/persona_normalization.py
```

**Deep parse data files:**

```bash
python3 scripts/deep_parse.py
```

**Conversion teardown (prospect URL):**

```bash
python3 scripts/run_conversion_teardown.py "https://prospect-site.com/landing-page"
```

**Attribution check (prospect URL):**

```bash
python3 scripts/run_attribution_check.py "https://prospect-site.com"
```

**Inbound deep parse:**

```bash
python3 scripts/deep_parse_inbound.py
```

**Company type target matrix:**

```bash
python3 scripts/company_target_matrix.py
```

---

## Key Documents

| Doc                                                                                                                    | Purpose                                             |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [outbound/Messaging Framework.md](outbound/Messaging%20Framework.md)                                                   | Statistical basis for outbound messaging            |
| [outbound/SDR Starter Guide.md](outbound/SDR%20Starter%20Guide.md)                                                     | Simple SDR implementation guide                     |
| [outbound/Segment Packs Outbound.md](outbound/Segment%20Packs%20Outbound.md)                                           | Target lists and copy variants                      |
| [outbound/Value First Message Templates.md](outbound/Value%20First%20Message%20Templates.md)                           | 10 value-first messages (no meeting ask)            |
| [outbound/value-first-campaigns/](outbound/value-first-campaigns/)                                                     | 31-day cadences (10 campaigns × 31 templates)       |
| [reports/Analysis Report.md](reports/Analysis%20Report.md)                                                             | Opportunity segmentation by service/industry/source |
| [reports/Inbound Analysis Report.md](reports/Inbound%20Analysis%20Report.md)                                           | Why qualified inbound leads come in                 |
| [reports/Inbound What They Want.md](reports/Inbound%20What%20They%20Want.md)                                           | Deep parse: Company Type × Ask, pain language       |
| [reports/Company Type Target Matrix.md](reports/Company%20Type%20Target%20Matrix.md)                                   | Company type → service → phrase                     |
| [reports/Messaging Framework Summary and Conclusion.md](reports/Messaging%20Framework%20Summary%20and%20Conclusion.md) | Consolidated messaging conclusions                  |
| [reports/Deep Parse Report.md](reports/Deep%20Parse%20Report.md)                                                       | Deep parse of data files                            |
| [outbound/Enterprise Legacy On-Prem Sales Motion.md](outbound/Enterprise%20Legacy%20On-Prem%20Sales%20Motion.md)       | Enterprise sales motion (Champion, DM, etc.)        |
| [docs/README.md](docs/README.md)                                                                                       | Value-first templates and analysis instructions     |

---

## Data

| Location                 | Contents                                                                                      |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| **data/opportunities/**  | Oops.csv (Won + Lost), All Opportunities, Pipeline, Consolidated_Opportunities, My Open Leads |
| **data/inbound/**        | Inbound.xlsx (550 qualified leads)                                                            |
| **data/accounts/**       | All Account (15K+)                                                                            |
| **data/leads/**          | All Leads, Count of Leads/Source Campaign, Campaign Outbound Analysis                         |
| **data/austin-chamber/** | Austin Chamber directory scrapes (directory.csv, directory.json)                              |

---

## Quick navigation

### Data
| Path | Contents |
|------|----------|
| `data/opportunities/` | Oops.csv, pipeline exports |
| `data/inbound/` | Inbound.xlsx |
| `data/patterns/` | Company × Service × Title (channel-agnostic) |
| `data/austin-chamber/` | Austin Chamber directory scrape |
| `data/outbound_only/` | Outbound-filtered datasets (optional branch) |

### Assets — Case studies by service
| Path | Contents |
|------|----------|
| `assets/case-studies/Modern Workplace/` | SharePoint, M365, Teams, intranet |
| `assets/case-studies/CRM/` | Salesforce, Dynamics |
| `assets/case-studies/Data Analytics/` | Power BI, BI |
| `assets/case-studies/Marketing/` | HubSpot, Pardot, demand gen |
| `assets/case-studies/Custom Dev/` | Apps, portals, mobile |
| `assets/case-studies/AI Automation/` | Copilot, agents |
| `assets/case-studies/Infrastructure/` | MDM, Intune |
| `assets/case-studies/Creative/` | Video, webinar, design |
| `assets/case-studies/Other/` | Mixed, proposals |

### Reports
| Path | Contents |
|------|----------|
| `reports/Company Service Title Patterns.md` | Company × Service × Buyer Title (no channel) |
| `reports/Case Study Value Prop Mapping.md` | Case studies → value props |
| `reports/Case Study Cadence Mapping.md` | Case studies → cadences |
| `reports/Vendor Channel Persona Service Analysis Report.md` | Channel/vendor analysis |
| `reports/Inbound What They Want.md` | Inbound ask/title patterns |
| `reports/Company Type Target Matrix.md` | Company type × service |

### Scripts
| Script | Purpose |
|--------|---------|
| `scripts/company_service_title_analysis.py` | Company × Service × Title (patterns, no channel) |
| `scripts/organize_assets_by_service.py` | Organize PPTXs by service |
| `scripts/parse_all_case_studies.py` | Case study → value prop mapping |
| `scripts/company_target_matrix.py` | Company type × ask × service |
| `scripts/persona_normalization.py` | Title → Function × Seniority |
| `scripts/run_analysis.py` | Segmentation analysis |

### Outbound
| Path | Contents |
|------|----------|
| `outbound/` | Messaging framework, cadences, templates |
| `outbound/value-first-campaigns/` | 31-day cadences by persona |

---

# Cloud Migration Target Analysis — Deep Synthesis

**Date:** 2026-02-15  
**Purpose:** Methodical analysis of reports, case studies, Affirma services, and data to identify niches, value propositions, and 100 companies to target for cloud migrations.

**Sources:** All files under `reports/`, `data/affirma-services/affirma_what_we_do.md`, `data/patterns/*.json`, `data/austin-chamber/`, Case Study Value Prop Mapping.

---

## Part 1: Report Synthesis — What the Data Tells Us

### Win Rate Hierarchy (Opportunity Analysis)

| Segment | Win Rate | n | Action |
|---------|----------|---|--------|
| Non-Profit (any service) | 83.3% | 12 | **Highest priority** |
| Government | 58.3% | 12 | **High priority** |
| Healthcare | 47.9% | 48 | **High priority** |
| Energy/Utilities/Waste | 47.4% | 19 | **High priority** |
| Business Services | 46.3% | 54 | **High priority** |
| Software | 20.3% | 133 | Deprioritize unless sub-segmented |
| Transportation | 10.0% | — | Avoid |
| Organizations | 13.3% | — | Avoid |

### Service × Win Rate (Modern Workplace = Cloud Migration Core)

| Service | Win% | Volume | Best For Cloud Migration |
|---------|------|--------|--------------------------|
| CRM | 45.2% | 31 | Dynamics/BC migration (GP→BC) |
| Creative | 42.9% | 35 | Post-migration intranet/creative |
| **Modern Workplace** | **42.0%** | **176** | **Primary — SharePoint, M365, intranet** |
| Marketing Services | 40.8% | 76 | HubSpot/Pardot migration |
| Infrastructure | 40.0% | 50 | MDM, Exchange, tenant consolidation |
| Custom Dev | 24.3% | 111 | Portals, apps post-migration |
| Data & Analytics | 18.3% | 60 | Power BI, dashboards (reposition) |

### Channel Reality Check

- **Account Management Campaign:** 63% win — best. Double down on existing customers.
- **Personal Network:** 50% — warm intros convert.
- **SEO:** 45% — qualified intent.
- **LinkedIn cold:** 19% — only for Marketing × Creative, Marketing Services. **Do not scale for IT/Cloud.**
- **Partners:** 0% — fix or stop.

### Inbound Demand (550 leads) — What They Actually Want

1. **SharePoint** — 25%+ (intranet, migration, build, restructure)
2. **Migration** — 71 references (Exchange, SharePoint, M365 tenant, Google Workspace, on-prem)
3. **Power Platform** — Power BI (9%), Dynamics (10%), Power Automate
4. **Support** — Ongoing, EOL upgrade, "end of life"
5. **Guidance** — "Information overload," "need a partner"

**Language to mirror:** "looking for," "migrate," "build," "partner," "assistance," "guidance" — not "we sell."

---

## Part 2: Affirma Capabilities — What We Actually Do (affirma_what_we_do.md)

### Cloud Migration Skills (Platforms → Microsoft 365, Cloud)

| Capability | Description | Fit for Targeting |
|------------|-------------|-------------------|
| **Google Workspace → M365** | Mail, calendar, storage, permissions, UX | Strong — many orgs still on Google |
| **SharePoint migration** | On-prem → SPO, file server → SPO, tenant consolidation | Strong — 24% of inbound |
| **Tenant-to-tenant** | M&A, restructuring, data/identity continuity | Strong |
| **Exchange migration** | Intermedia, on-prem → M365 | Strong |
| **MDM/Intune** | Device management, modernize | Adjacent |
| **Application modernization** | Legacy → cloud-native | Adjacent |

### Case Study Proof Points (Cloud / Modern Workplace)

| Client | Industry | Proof |
|--------|----------|-------|
| Kaiser Permanente | Healthcare | SharePoint migration |
| Children's Hospital | Healthcare | SharePoint |
| Colorado Mountain College | Education | SharePoint migration |
| Ferguson | Manufacturing | SharePoint migration |
| Peoples Bank | Financial Services | SharePoint, Teams |
| County of San Bernardino | Government | SharePoint migration |
| Seattle Art Museum | Government | SharePoint |
| Roku | Tech | M365 migration |
| Valve | Tech | SharePoint Online migration |
| Zillow | Tech | O365 implementation |

### Financial Expression (Procurement Must-Have)

> "**This SharePoint migration** will reduce cost and protect revenue by putting owners + cadence around drift, resulting in lower downtime risk."

Replace "this investment" with service phrase. Every pitch must tie to: increase revenue, protect revenue, reduce cost, increase capital efficiency.

---

## Part 3: Niches and Value Propositions (Data-Derived)

### Niche 1: Healthcare — SharePoint + Compliance

**Data:** Healthcare × Modern Workplace 55.6% win (15/27). Inbound: SharePoint, Compliance, Dashboard, Power BI.

**Value prop:** "We help healthcare organizations migrate SharePoint, build intranets, and meet HIPAA/Purview requirements without breaking what's working."

**Case studies:** Kaiser Permanente, Children's Hospital, Marin General Hospital, UW Valley Medical Center.

**Trigger language:** "compliance," "HIPAA," "Purview," "clinical documentation," "EMR."

---

### Niche 2: Government — SharePoint + Power BI

**Data:** Government 58.3% win. Top asks: SharePoint, Power BI, Google→M365.

**Value prop:** "We help government agencies migrate from legacy SharePoint or Google Workspace to M365 with governance and Power BI for decision visibility."

**Case studies:** City of Seattle (Dynamics), WA State Parks, County of San Bernardino, City of Hillsboro.

**Trigger language:** "migration mandate," "legacy upgrade," "CMMC," ".gov."

---

### Niche 3: Non-Profit — Dynamics + SharePoint

**Data:** Non-Profit 83.3% win. Top asks: Dynamics/CRM, SharePoint, Migration.

**Value prop:** "We help non-profits implement Dynamics and migrate SharePoint so they can focus on mission, not spreadsheets."

**Case studies:** Mary's Place, Cystic Fibrosis Foundation, Degrees of Change, YMCA.

**Trigger language:** "lean team," "limited IT," "mission focus," ".org."

---

### Niche 4: Financial Services — M365 Governance + SharePoint

**Data:** Financial Services × Modern Workplace 47.6% win. Finance Director × Modern Workplace 100% (6 opps).

**Value prop:** "We help financial institutions consolidate M365 tenants, migrate SharePoint, and implement governance for compliance and cost control."

**Case studies:** Chevron Credit Union, Peoples Bank, Hawaii Bank, Solarity Credit Union.

**Trigger language:** "governance," "consolidation," "compliance," "audit."

---

### Niche 5: Manufacturing / Industrial — SharePoint + Field Apps

**Data:** Manufacturing × Modern Workplace 46.7% win. Construction 40.9%.

**Value prop:** "We help manufacturing and construction firms migrate SharePoint, build intranets, and deploy field-service apps without overbuilding."

**Case studies:** Ferguson, Snap On, CaptiveAire, Avista, Hermanson.

**Trigger language:** "file server," "legacy," "field service," "restructure."

---

### Niche 6: Education — SharePoint Migration

**Data:** Education × Modern Workplace 36.4% win. Education × Infrastructure 50%.

**Value prop:** "We help schools and universities migrate from on-prem SharePoint or file servers to M365 with minimal disruption to faculty and staff."

**Case studies:** Colorado Mountain College, Seattle Pacific Univ, Thales Academy.

**Trigger language:** "migration," "classic to modern," "faculty adoption."

---

## Part 4: 100 Companies to Target for Cloud Migrations

**Criteria:** Mid-market to enterprise; industries that convert (Healthcare, Government, Non-Profit, Financial Services, Manufacturing, Education); likely cloud migration triggers (legacy, sprawl, M&A, compliance).

**Sources:** Austin Chamber directory (Health Care), reports (Open Leads, Texas CRM, ATX Leads), industry patterns.

---

### Healthcare (35 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 1 | Ascension Seton | Austin, TX | Large system; SharePoint/compliance likely |
| 2 | Baylor Scott & White Health | Austin/Dallas, TX | Major system; migration volume |
| 3 | St. David's HealthCare | Austin, TX | Multi-facility; intranet/collab needs |
| 4 | Texas Oncology | Austin, TX | Clinical workflows; compliance |
| 5 | Dell Children's Medical Center | Austin, TX | Pediatric; EHR/collab |
| 6 | Heart Hospital of Austin | Austin, TX | Specialized; IT modernization |
| 7 | Texas Children's Hospital Austin | Austin, TX | New presence; build-out |
| 8 | Austin Regional Clinic | Austin, TX | Multi-site; shared systems |
| 9 | Hanger, Inc. | Austin, TX | Public company; enterprise IT |
| 10 | Curative | Austin, TX | Health tech; scalable infra |
| 11 | Carbon Health | Austin, TX | Digital health; rapid scale |
| 12 | Luminex Corporation | Austin, TX | Life sciences; data/collab |
| 13 | AbbVie (Austin presence) | Austin, TX | Pharma; M365 governance |
| 14 | Abbott (Austin presence) | Austin, TX | Med device; global standards |
| 15 | Suvida Healthcare | Austin, TX | Senior care; growth mode |
| 16 | Babson Diagnostics | Austin, TX | Diagnostics; lab systems |
| 17 | Goldfinch Health | Austin, TX | Health tech; cloud-native |
| 18 | SonderMind | Austin, TX | Behavioral health; scale |
| 19 | One Medical (Austin) | Austin, TX | Primary care; tech-forward |
| 20 | Meadows Behavioral Health | Austin, TX | Behavioral; multi-site |
| 21 | Marbridge Foundation | Austin, TX | Disability services; non-profit adj |
| 22 | Samaritan Center | Austin, TX | Counseling; community |
| 23 | The YMCA of Austin | Austin, TX | Non-profit; membership systems |
| 24 | Integrative Creative Therapy | Austin, TX | Healthcare adj |
| 25 | SenoPro | Austin, TX | Medical device; data |
| 26 | Cedar Park Regional Medical Center | Cedar Park, TX | Regional hospital |
| 27 | Seton Healthcare Family | Austin, TX | Multi-hospital system |
| 28 | North Austin Medical Center | Austin, TX | HCA facility |
| 29 | Round Rock Medical Center | Round Rock, TX | Regional |
| 30 | South Austin Hospital | Austin, TX | Acute care |
| 31 | St. David's Medical Center | Austin, TX | Flagship facility |
| 32 | Austin Radiological Association | Austin, TX | Multi-site imaging |
| 33 | Capitol Anesthesiology Association | Austin, TX | Large group |
| 34 | Texas Spine & Joint Hospital | Austin, TX | Specialty |
| 35 | Arise Medical | Austin, TX | Urgent care chain |

---

### Financial Services / Credit Unions / Banks (15 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 36 | Experian | Costa Mesa, TX presence | Already in CRM; expansion |
| 37 | Austin Capital Bank | Austin, TX | Regional; M365 governance |
| 38 | Amplify Credit Union | Austin, TX | CU; member systems |
| 39 | University Federal Credit Union | Austin, TX | CU; growth |
| 40 | Velocity Credit Union | Austin, TX | CU; digital |
| 41 | Randolph-Brooks FCU | San Antonio, TX | Large CU; TX presence |
| 42 | Firstmark Credit Union | San Antonio, TX | CU; IT modernization |
| 43 | UFCU (University FCU) | Austin, TX | Education-adj; SharePoint |
| 44 | JPMorgan Chase (Austin ops) | Austin, TX | Major; regional IT |
| 45 | Frost Bank | San Antonio, TX | Regional bank; compliance |
| 46 | Broadway Bank | San Antonio, TX | Regional; IT |
| 47 | Veritex Community Bank | Dallas, TX | Growth; mergers |
| 48 | Spirit of Texas Bank | Conroe, TX | Regional; cloud |
| 49 | Independent Bank | McKinney, TX | Texas-based; branches |
| 50 | Cadence Bank | Houston, TX | Regional; M&A history |

---

### Government / Municipal / Education (20 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 51 | City of Austin | Austin, TX | Major municipality; M365 |
| 52 | Travis County | Austin, TX | County gov; SharePoint |
| 53 | Texas Education Agency | Austin, TX | State; large scale |
| 54 | Austin Independent School District | Austin, TX | K-12; migration |
| 55 | Round Rock ISD | Round Rock, TX | Large district |
| 56 | Pflugerville ISD | Pflugerville, TX | Growth district |
| 57 | Leander ISD | Leander, TX | Fast-growing |
| 58 | University of Texas System | Austin, TX | Multi-campus; SharePoint |
| 59 | Texas State University | San Marcos, TX | Large; IT sprawl |
| 60 | Austin Community College | Austin, TX | Community college |
| 61 | Hays County | San Marcos, TX | County; growth |
| 62 | Williamson County | Georgetown, TX | County; IT |
| 63 | City of Round Rock | Round Rock, TX | Municipality |
| 64 | City of Cedar Park | Cedar Park, TX | Municipality |
| 65 | City of Georgetown | Georgetown, TX | Municipality |
| 66 | City of San Marcos | San Marcos, TX | University town |
| 67 | Texas Comptroller | Austin, TX | State agency |
| 68 | Texas Department of Transportation | Austin, TX | Large agency |
| 69 | Lower Colorado River Authority | Austin, TX | Utility; gov-adj |
| 70 | Texas Municipal League | Austin, TX | Member orgs; reach |

---

### Manufacturing / Industrial / Construction (15 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 71 | Dell Technologies | Round Rock, TX | Enterprise; existing relationship |
| 72 | Samsung Austin Semiconductor | Austin, TX | Manufacturing; IT scale |
| 73 | NXP Semiconductor | Austin, TX | Chip; global IT |
| 74 | Applied Materials | Austin, TX | Semiconductor; enterprise |
| 75 | Flex Ltd. | Austin, TX | Manufacturing; global |
| 76 | Cirrus Logic | Austin, TX | Semiconductor; growth |
| 77 | SolarWinds | Austin, TX | Software; infra |
| 78 | National Instruments (NI) | Austin, TX | Industrial; data |
| 79 | Indeed | Austin, TX | Tech; large employer |
| 80 | Whole Foods (Amazon) | Austin, TX | Retail; enterprise IT |
| 81 | H-E-B | San Antonio, TX | Retail; TX pride; IT scale |
| 82 | Blue Bell Creameries | Brenham, TX | Manufacturing; legacy |
| 83 | Trico Products | Austin, TX | Manufacturing |
| 84 | Bury + Partners | Austin, TX | Engineering; AEC |
| 85 | Pape-Dawson Engineers | San Antonio, TX | Civil eng; growth |

---

### Non-Profit / Associations (10 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 86 | Austin Community Foundation | Austin, TX | Non-profit; grants |
| 87 | United Way for Greater Austin | Austin, TX | Non-profit; CRM/SharePoint |
| 88 | Caritas of Austin | Austin, TX | Social services |
| 89 | Meals on Wheels Central Texas | Austin, TX | Non-profit; operations |
| 90 | Foundation Communities | Austin, TX | Housing non-profit |
| 91 | Texas Tribune | Austin, TX | Non-profit media |
| 92 | KLRU (PBS Austin) | Austin, TX | Media; content |
| 93 | Austin Habitat for Humanity | Austin, TX | Non-profit; construction |
| 94 | SAFE Alliance | Austin, TX | Social services |
| 95 | Workers Defense Project | Austin, TX | Advocacy; operations |

---

### Professional Services / Tech (5 companies)

| # | Company | Location | Why Target |
|---|---------|----------|------------|
| 96 | KPMG (Austin) | Austin, TX | Professional services |
| 97 | Deloitte (Austin) | Austin, TX | Consulting; M365 |
| 98 | Accenture (Austin) | Austin, TX | Large; delivery centers |
| 99 | EY (Austin) | Austin, TX | Professional services |
| 100 | Infosys (Austin) | Austin, TX | Tech services; scale |

---

## Part 5: Outreach Recommendations

### Messaging by Segment

| Segment | Hook | CTA | Phrase |
|---------|------|-----|--------|
| Healthcare | "Compliance and drift often go hand-in-hand with legacy SharePoint." | "Worth a 15-min check on orphan systems or permissions drift?" | "this SharePoint migration" |
| Government | "Most waste comes from 'nobody owns this system anymore.'" | "Worth a 15-min check if you have any orphan systems or drift?" | "this SharePoint migration" / "this Power BI deployment" |
| Non-Profit | "Lean teams need systems that don't create more work." | "Quick audit of where your SharePoint or M365 might be drifting?" | "this Dynamics implementation" / "this SharePoint migration" |
| Financial | "Governance and consolidation reduce risk and cost." | "15-min review of tenant consolidation or M365 governance?" | "this SharePoint migration" / "M365 consolidation" |

### Channel

- **Email first** — IT Director wins on email, not LinkedIn-only.
- **LinkedIn Day 3, 7** — Follow-up only for IT/Infrastructure.
- **Austin angle** — "Austin-based consulting firm" for local coffee/call.

### Next Steps

1. **Export Contact Level:** Get IT Director, Director of IT, VP Information Systems, CTO at each company.
2. **Domain Check:** Add Email → run `company_target_matrix.py` for company type inference.
3. **Account Management:** Prioritize existing Affirma customers for expansion (63% win).
4. **PPC Conversion:** 177 qualified leads; improve follow-up, don't cut spend.
5. **Non-Profit + Government Lists:** Build dedicated lists (strongest levers).

---

**Regenerate:** Re-run `scripts/company_target_matrix.py`, `scripts/analyze_inbound.py` when new data arrives.



