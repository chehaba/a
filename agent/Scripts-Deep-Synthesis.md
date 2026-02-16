# Scripts — Deep Synthesis

**Purpose:** Analysis and automation scripts for prospecting data. Run from repo root. Each script produces structured output for reports or downstream use.

**Source:** All .py files under scripts/, grep of function definitions, docstrings.

---

## Part 1: Script Inventory and Purpose

| Script | Input | Output | Purpose |
|--------|-------|--------|---------|
| run_analysis.py | Oops.csv | reports/Analysis Report.md | Opportunity segmentation, win rates, segment attractiveness |
| persona_normalization.py | Oops.csv | outbound/Segment Packs | Persona win rates, LinkedIn fit, copy variants |
| deep_parse_inbound.py | Inbound.xlsx | reports/Inbound What They Want.md | Granular Ask, Title×Ask, Industry×Ask, pain language |
| analyze_inbound.py | Inbound.xlsx | reports/Inbound Analysis Report.md | Category distribution, theme frequency |
| company_target_matrix.py | Inbound.xlsx (+ Email) | reports/Company Type Target Matrix.md | Company Type × Ask × Service, service phrases |
| company_service_title_analysis.py | Oops + Inbound + case studies | data/patterns/company_service_title.json | Company × Service × Title patterns |
| analyze_atx_leads.py | Open Leads + Directors lists | reports/ATX Leads Best to Target.md | Austin leads for MW and Marketing |
| run_conversion_teardown.py | URL | Structured checklist | Landing page conversion analysis |
| run_attribution_check.py | URL | Short report | UTM, forms, landing URL check |
| scrape_austin_chamber.py | — | directory.csv, directory.json | Austin Chamber member scrape |
| scrape_affirma_services.py | — | affirma_what_we_do.md | Affirma.com service pages scrape |
| parse_case_studies.py | assets/*.pptx | Case study list | Extract client, service, pains from PPTX |
| parse_all_case_studies.py | assets/ | Full parse | Comprehensive case study extraction |
| organize_assets_by_service.py | assets/ | Service folders | Organize case studies by service |
| organize_other_deeper.py | assets/Other/ | Subfolders | Organize Other by subcategory |
| generate_cadence_templates.py | Campaign config | value-first-campaigns/ | 31-day cadence files per campaign |
| parse_vendor_analysis.py | vendor data | — | Vendor channel analysis |
| run_conversion_teardown.py | URL | — | Conversion teardown |
| run_attribution_check.py | URL | — | Attribution check |
| segment_score.py | Segment data | — | Segment attractiveness scoring |

---

## Part 2: Core Analysis Scripts — Usage and Logic

### run_analysis.py

**Usage:** `python3 scripts/run_analysis.py`

**Logic:**
- Loads Oops.csv, filters Won/Lost
- agg_by_dim(): Aggregate by Service, Industry, Source Campaign
- segment_attractiveness(): Score = w1(Revenue) + w2(Win Rate) + w3(Urgency) + w4(Strategic Fit)
- industry_service_matrix(): Industry × Service win rates
- Outputs Analysis Report.md with tables and takeaways

**Key outputs:** Service/Industry/Source win rates; top segments; multi-opp warning.

---

### persona_normalization.py

**Usage:** `python3 scripts/persona_normalization.py`

**Logic:**
- classify_seniority(title): C-level, VP, Director, Manager, IC
- classify_function(title): Marketing, IT/Tech, Finance, Other
- Aggregates by Function × Seniority, filters LinkedIn source
- Wilson CI for win-rate confidence intervals
- Outputs Segment Packs with persona win rates, LinkedIn fit, copy variants

**Key outputs:** Marketing Director 52.4%, IT Director 45.8%; LinkedIn RUN for Marketing×Creative only.

---

### deep_parse_inbound.py

**Usage:** `python3 scripts/deep_parse_inbound.py`

**Logic:**
- CATEGORY_PATTERNS: 20+ regex patterns for granular Ask (SharePoint Migration, Intranet Build, Power BI, etc.)
- get_primary_category(text): First match wins
- TITLE_PATTERNS: Director, Manager, Consultant, Owner, CTO, etc.
- extract_industry(text): Government, Healthcare, Non-Profit, etc.
- extract_pain_flags(text): struggling, urgent, broken, end of life
- Cross-tabs: Ask distribution, Title×Ask, Industry×Ask, Source×Ask

**Key outputs:** SharePoint 25%+, Top 22 asks, pain language, employee size bands.

---

### company_target_matrix.py

**Usage:**
```bash
python3 scripts/company_target_matrix.py                    # default: data/Inbound/Inbound.xlsx
python3 scripts/company_target_matrix.py path/to/leads.xlsx  # custom file
```

**Logic:**
- domain_to_company_type(domain): .gov→Government, .edu→Education, *health*→Healthcare, etc.
- get_ask(text): Reuses deep_parse category logic
- ASK_TO_SERVICE: Maps Ask → Affirma Service
- Service-specific phrase: "this SharePoint migration" not "this investment"
- Outputs Company Type × Top Asks → Service table

**Requirement:** Email column in export enables domain inference. Without it, uses Industry from description.

---

### company_service_title_analysis.py

**Usage:** `python3 scripts/company_service_title_analysis.py`

**Logic:**
- Loads Oops.csv, Inbound.xlsx, case_study_topics_by_service.json
- Normalizes industry → company type, title → Function × Seniority
- Cross-tabulates Company Type × Service × Buyer Title
- Enriches with inbound_asks, case_study_topics, service_notes
- Outputs company_service_title.json; feeds Company Service Title Patterns report

---

### analyze_atx_leads.py

**Usage:** `python3 scripts/analyze_atx_leads.py`

**Logic:**
- mw_score(title, company): Modern Workplace fit (IT Director+, infrastructure, cloud)
- mkt_score(title, company): Marketing fit (Marketing Director+, Brand, Creative)
- is_gatekeeper(title): Exclude BD, Sales, pure Marketing (no Tech)
- Industries with better MW win rates from Oops.csv
- Outputs ATX Leads Best to Target with Tier 1 contacts

**Input:** Open Leads + Directors lists (data/Inbound/atx leads/).

---

## Part 3: Scraping and Asset Scripts

### scrape_austin_chamber.py

**Usage:**
```bash
python3 scripts/scrape_austin_chamber.py --categories 328   # Health Care
python3 scripts/scrape_austin_chamber.py --categories 323   # IT & Technology
python3 scripts/scrape_austin_chamber.py --categories 328 323
python3 scripts/scrape_austin_chamber.py --no-filter   # Full directory
```

**Logic:** Fetches API, parses orgs, filters by category_ids, writes CSV and JSON.

---

### scrape_affirma_services.py

**Usage:** `python3 scripts/scrape_affirma_services.py`

**Logic:** Fetches affirma.com service pages from navigation, extracts text, builds affirma_what_we_do.md.

---

### parse_case_studies.py

**Usage:** `python3 scripts/parse_case_studies.py`

**Logic:** Walks assets/, extracts text from PPTX, identifies client and service from filename, parses for pains. Feeds Case Study Cadence Mapping.

---

### organize_assets_by_service.py

**Usage:** `python3 scripts/organize_assets_by_service.py`

**Logic:** get_service(path): Infers from filename (SharePoint→Modern Workplace, Salesforce→CRM, etc.). Moves/copies to service folders.

---

### organize_other_deeper.py

**Usage:** `python3 scripts/organize_other_deeper.py`

**Logic:** Subcategory rules (pattern, subdir_name). Classifies files in Other/ into Government, Financial Services, Microsoft Customer Stories, etc.

---

## Part 4: Analysis Scripts (Prospect-Facing)

### run_conversion_teardown.py

**Usage:** `python3 scripts/run_conversion_teardown.py "https://example.com/landing-page"`

**Logic:** fetch_url(), extracts forms, CTAs, headings, counts fields. Outputs structured checklist. User adds 3 fixes narrative.

---

### run_attribution_check.py

**Usage:** `python3 scripts/run_attribution_check.py "https://example.com"`

**Logic:** fetch_url(), looks for UTM in links, form structure, landing URL count. User adds narrative.

---

## Part 5: Cadence Generation

### generate_cadence_templates.py

**Usage:** `python3 scripts/generate_cadence_templates.py`

**Logic:**
- Campaign id → folder name mapping (05 → Director Decision Latency, etc.)
- 31 value items per campaign
- Maps (value_type, day) → docs/templates/ filename
- build_content(): Generates Day N.md with subject, body, attach, CTA
- Outputs value-first-campaigns/*/Day *.md

---

## Part 6: Dependency Graph

```
Oops.csv ─┬─ run_analysis.py
          ├─ persona_normalization.py
          ├─ company_service_title_analysis.py
          └─ parse_vendor_analysis.py

Inbound.xlsx ─┬─ deep_parse_inbound.py
              ├─ analyze_inbound.py
              └─ company_target_matrix.py

austin-chamber/ ← scrape_austin_chamber.py
affirma_what_we_do.md ← scrape_affirma_services.py
assets/ ─┬─ parse_case_studies.py
         ├─ organize_assets_by_service.py
         └─ organize_other_deeper.py

data/patterns/case_study_topics_by_service.json ← parse scripts
```

---

## Part 7: Regeneration Order

When data changes, run in this order:

1. **Inbound changed:** deep_parse_inbound.py → company_target_matrix.py
2. **Opportunities changed:** run_analysis.py → persona_normalization.py → company_service_title_analysis.py
3. **Austin Chamber:** scrape_austin_chamber.py
4. **Affirma.com:** scrape_affirma_services.py
5. **Assets reorganized:** organize_assets_by_service.py → organize_other_deeper.py
6. **Cadence refresh:** generate_cadence_templates.py

---

## Part 8: Quick Reference — "I Need X, Run Y"

| Need | Script |
|------|--------|
| Win rates, segment attractiveness | run_analysis.py |
| Persona win rates, LinkedIn fit | persona_normalization.py |
| What inbound leads want (granular) | deep_parse_inbound.py |
| Company Type × Ask × Service | company_target_matrix.py |
| Company × Service × Title patterns | company_service_title_analysis.py |
| Austin MW and Marketing leads | analyze_atx_leads.py |
| Conversion teardown structure | run_conversion_teardown.py "URL" |
| Attribution check structure | run_attribution_check.py "URL" |
| Austin Chamber directory | scrape_austin_chamber.py --categories 328 |
| Affirma services scrape | scrape_affirma_services.py |
| Organize case studies | organize_assets_by_service.py |
| 31-day cadence files | generate_cadence_templates.py |

---

**All scripts:** Run from repo root. Paths relative to BASE = script parent's parent.
