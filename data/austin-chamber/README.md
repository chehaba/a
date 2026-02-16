# Austin Chamber of Commerce — Member Directory (Scraped)

**Source:** https://www.austinchamber.com/directory?categories=328  
**API:** `https://www.austinchamber.com/api/v1/directory`  
**Category 328:** Health Care

---

## Files

| File | Description |
|------|--------------|
| `directory.csv` | 101 Health Care member organizations (CSV) |
| `directory.json` | Same data in JSON |

---

## Columns

| Column | Description |
|--------|-------------|
| id | Chamber org ID |
| title | Organization name |
| slug | URL slug |
| tier | Chairman's Circle, Advocate, Catalyst, Build |
| description | Org description (some have HTML) |
| street1, street2, city, state, zip | Address |
| phone | Phone |
| webUrl | Website |
| linkedin | LinkedIn URL |
| categories | Category labels |
| category_ids | Category IDs (328 = Health Care) |

---

## Regenerate

```bash
# Health Care only (default)
python3 scripts/scrape_austin_chamber.py --categories 328

# IT & Technology (323)
python3 scripts/scrape_austin_chamber.py --categories 323

# Multiple categories
python3 scripts/scrape_austin_chamber.py --categories 328 323

# Full directory (no filter)
python3 scripts/scrape_austin_chamber.py --no-filter

# Test run (20 pages)
python3 scripts/scrape_austin_chamber.py --categories 328 --max-pages 20
```

---

## Category IDs (from site)

| ID | Category |
|----|----------|
| 328 | Health Care |
| 323 | Computers, IT & Technology |
| 326 | Finance & Insurance |
| 330 | Industrial & Manufacturing |
| 301 | Restaurants, Food & Beverages |
| 305 | Advertising & Media |
