# Data — Deep Synthesis

**Purpose:** Raw data for prospecting analysis, segmentation, and outbound messaging. Structure, key files, usage, and regeneration.

**Source:** data/README.md, data/patterns/*.json, data/austin-chamber/, data/affirma-services/, data/opportunities/

---

## Part 1: Directory Structure

| Directory | Contents | Primary Use |
|-----------|----------|-------------|
| **opportunities/** | Oops.csv — Won/Lost opportunities, enriched | Win-rate analysis, persona normalization, segment scoring |
| **patterns/** | company_service_title.json, company_type_service.json, inbound_language_by_segment.json, case_study_topics_by_service.json | Targeting matrices, segment patterns |
| **austin-chamber/** | directory.csv, directory.json — Scraped Austin Chamber members | Austin/Texas lead source; Health Care (328), IT (323) |
| **affirma-services/** | affirma_what_we_do.md — Scraped service pages (65) | Service taxonomy, capability reference |
| **inbound/** | Inbound.xlsx — Qualified inbound leads | Ask distribution, pain language, company type inference |
| **accounts/** | All Account exports | Account base (referenced in reports) |
| **leads/** | Campaign analysis, source/job title counts | Lead analysis |
| **reference/** | PDFs, misc | Reference docs |

---

## Part 2: Key Files — Schema and Usage

### Oops.csv (data/opportunities/Oops.csv)

**Purpose:** Won + Lost opportunities for segmentation, win-rate analysis.

**Key columns (inferred):**
- Status: Won / Lost
- Primary_Service: Modern Workplace, Custom Dev, Marketing Services, Data & Analytics, Infrastructure, Creative, CRM
- Industry: Non-Profit, Healthcare, Government, Software, etc.
- Source_Campaign: Account Management, PPC, SEO, LinkedIn, etc.
- Job_Title: Raw title (normalized by scripts to Function × Seniority)

**Used by:**
- `scripts/run_analysis.py` — Segmentation, Industry × Service, Source × Win
- `scripts/persona_normalization.py` — Persona win rates, LinkedIn fit
- `scripts/company_service_title_analysis.py` — Company × Service × Title patterns

**Key stats:** 562 opportunities, 35.4% win rate, 199 Won, 363 Lost.

---

### Inbound.xlsx (data/Inbound/Inbound.xlsx)

**Purpose:** Qualified inbound lead descriptions — what they want, language they use.

**Key columns (inferred):**
- Description: Free text (parsed for Ask, Title, Industry, Pain)
- Source Campaign: PPC, SEO, etc.
- No. of Employees: Size band
- Email: Optional — enables domain-based company type inference

**Used by:**
- `scripts/deep_parse_inbound.py` — Granular Ask, Title × Ask, Industry × Ask
- `scripts/analyze_inbound.py` — Category distribution, theme frequency
- `scripts/company_target_matrix.py` — Company Type × Ask × Service (requires Email for domain inference)

**Key stats:** 550 qualified leads; SharePoint 25%+, Migration 71 refs, "looking for" 144, "migrate" 89.

---

### directory.json / directory.csv (data/austin-chamber/)

**Purpose:** Austin Chamber of Commerce member directory (scraped).

**Schema:**
- id, title, slug, tier (Chairman's Circle, Advocate, Catalyst, Build)
- description, street1, street2, city, state, zip, phone
- webUrl, linkedin
- categories, category_ids (328 = Health Care, 323 = IT & Technology)

**Used by:** Manual lead list building; ATX leads analysis.

**Regenerate:**
```bash
python3 scripts/scrape_austin_chamber.py --categories 328   # Health Care
python3 scripts/scrape_austin_chamber.py --categories 323   # IT & Technology
python3 scripts/scrape_austin_chamber.py --categories 328 323  # Both
```

**Key stats:** 101 Health Care members (default scrape); categories expandable.

---

### affirma_what_we_do.md (data/affirma-services/)

**Purpose:** Scraped service pages from affirma.com — full capability taxonomy.

**Structure:** Category → Subcategory → Key Offerings table; full page content per URL.

**Key categories:**
- AI (Agent Dev, Generative AI, Process Automation, ML, Content Creation)
- Application Software (Web, Mobile, Cloud Apps, Modernization)
- Data & Analytics (Engineering, Visualization, Marketing Analytics, Predictive)
- Cloud (Migrations, Strategy, DevOps)
- BPO (Help Desk, Customer Service)
- Content Services, Design, Digital Marketing, Platforms (AWS, Azure, M365, Power BI, Dynamics, HubSpot, Salesforce, etc.)
- Search Marketing (PPC, SEO)

**Regenerate:** `python3 scripts/scrape_affirma_services.py`

---

## Part 3: data/patterns/ — Derived Datasets

### company_service_title.json

**Purpose:** Company Type × Service × Buyer Title patterns with win rates, inbound asks, case study topics.

**Schema (per row):**
- company_type, service, buyer_title
- n, won, win_rate
- inbound_asks (list), inbound_snippets
- case_study_topics, service_notes

**Regenerate:** `python3 scripts/company_service_title_analysis.py`

**Use:** Targeting Matrix, Company Service Title Patterns report; who wins with what.

---

### company_type_service.json

**Purpose:** Company Type × Service win rates (aggregate).

**Schema:** company_type, service, n, won, win_rate

**Top patterns (win_rate ≥ 0.8):**
- Financial Services × Marketing Services: 100%
- Non-Profit × Custom Dev: 100%
- Non-Profit × Modern Workplace: 83.3%
- Government × Custom Dev: 80%

**Use:** Prioritize company types by service.

---

### inbound_language_by_segment.json

**Purpose:** What inbound leads say they want, by Company Type × Service.

**Schema:** company_type, service, inbound_asks (list), n

**Top volume:**
- Commercial × Data & Analytics × Power BI: 42
- Commercial × Marketing × HubSpot: 20
- Commercial × Modern Workplace × SharePoint/Migration/Power: 6

**Use:** Tailor messaging by segment.

---

### case_study_topics_by_service.json

**Purpose:** Project themes from case study filenames (migration, implementation, etc.).

**Schema:** Service → list of {file, topic_hints}

**Use:** Match case study to prospect pain; Pain → Case Study mapping.

---

## Part 4: Data Flow — Scripts and Reports

```
Oops.csv ─┬─ run_analysis.py ──> reports/Analysis Report.md
          ├─ persona_normalization.py ──> outbound/Segment Packs
          ├─ company_service_title_analysis.py ──> data/patterns/company_service_title.json
          └─ parse_vendor_analysis.py ──> (vendor model)

Inbound.xlsx ─┬─ deep_parse_inbound.py ──> reports/Inbound What They Want.md
              ├─ analyze_inbound.py ──> reports/Inbound Analysis Report.md
              └─ company_target_matrix.py ──> reports/Company Type Target Matrix.md

austin-chamber/ ─ scrape_austin_chamber.py ──> directory.json, directory.csv
affirma.com ─ scrape_affirma_services.py ──> data/affirma-services/affirma_what_we_do.md
assets/ ─ parse_case_studies.py, organize_assets_by_service.py ──> case_study_topics_by_service.json
```

---

## Part 5: Gaps and Recommendations

| Gap | Recommendation |
|-----|----------------|
| Email column missing in Inbound export | Add to CRM export; enables domain-based company type (.gov, .edu, healthcare) |
| Industry often blank in Oops | Use description fallback; document inferred vs explicit |
| austin-chamber only Health Care by default | Re-run with categories 323 (IT), 326 (Finance), 330 (Manufacturing) for broader lists |
| patterns/ are derived | Re-run scripts when Oops.csv or Inbound.xlsx updates |

---

## Part 6: File Sizes and Scope

| File | Approx Size | Rows / Records |
|------|-------------|----------------|
| Oops.csv | — | 562 opportunities |
| Inbound.xlsx | — | 550 qualified leads |
| directory.json | — | 101+ (Health Care default) |
| affirma_what_we_do.md | ~160K chars | 65 pages scraped |
| company_service_title.json | — | 80+ patterns |
| company_type_service.json | — | 60+ combinations |

---

## Part 7: Quick Reference — "I Need X, Use Y"

| Need | Data Source | Script |
|------|-------------|--------|
| Win rates by Service, Industry, Source | Oops.csv | run_analysis.py |
| Persona win rates, LinkedIn fit | Oops.csv | persona_normalization.py |
| What inbound leads want (Ask, Industry, Title) | Inbound.xlsx | deep_parse_inbound.py |
| Company Type × Ask × Service matrix | Inbound.xlsx (+ Email) | company_target_matrix.py |
| Company × Service × Title patterns | Oops + Inbound + case studies | company_service_title_analysis.py |
| Austin healthcare companies | austin-chamber/directory.json | scrape_austin_chamber.py |
| Affirma service taxonomy | affirma_what_we_do.md | scrape_affirma_services.py |

---

**Regenerate commands:** See data/README.md and per-script docstrings.
