# Agent Skills

**Purpose:** Executable skills the agent can run from Cursor. No guessing—use these to fetch real data.

---

## Skill 1: Detect Tech Stack from Website

**When:** You need to know what technology a company uses (SharePoint, WordPress, M365, etc.). Do not guess.

**Command:**
```bash
python3 scripts/detect_tech_stack.py "https://example.com"
```

**With JSON output (for piping):**
```bash
python3 scripts/detect_tech_stack.py "https://example.com" --json
```

**Returns:** Observed technologies from HTML (meta tags, script src, link href). Evidence-based only.

---

## Skill 2: Scrape Austin Business Registry

**When:** You need fresh leads from Austin Chamber of Commerce member directory.

**Command:**
```bash
python3 scripts/scrape_austin_chamber.py --categories 328 323
```

**Categories:** 328 = Health Care, 323 = IT & Technology. Add 326 (Finance), 330 (Manufacturing) as needed.

**Full directory (no filter):**
```bash
python3 scripts/scrape_austin_chamber.py --no-filter
```

**Output:** `data/austin-chamber/directory.json`, `directory.csv`

---

## Skill 3: Export Austin Leads to Document

**When:** You need a printable markdown document of Austin registry leads.

**Command:**
```bash
python3 scripts/export_austin_leads.py
```

**Re-scrape then export:**
```bash
python3 scripts/export_austin_leads.py --refresh
```

**Custom categories when refreshing:**
```bash
python3 scripts/export_austin_leads.py --refresh --categories 328 323
```

**Output:** `reports/Austin Registry Leads.md`

---

## Skill 4: Enrich Leads with Tech Stack

**When:** You need to know each company's tech stack (from their website HTML) and print a combined lead document.

**Command:**
```bash
python3 scripts/enrich_leads_with_tech.py
```

**Quick test (5 URLs):**
```bash
python3 scripts/enrich_leads_with_tech.py --limit 5
```

**All URLs (slow):**
```bash
python3 scripts/enrich_leads_with_tech.py --no-limit
```

**Output:** `reports/Austin Leads With Tech Stack.md`

---

## Usage in Cursor

Run these from the terminal in Cursor. The agent should:

1. Use **Skill 2** to get leads when Austin registry data is stale or missing.
2. Use **Skill 1** on specific URLs when you need one company's stack.
3. Use **Skill 4** when you need many companies with detected tech in one document.
4. Use **Skill 3** for a simple lead list (no tech enrichment).
