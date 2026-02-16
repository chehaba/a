# Data — Organization

Raw data for prospecting analysis, segmentation, and outbound messaging.

---

## Structure

| Directory           | Contents                                                         |
| ------------------- | ---------------------------------------------------------------- |
| **opportunities/**  | Won/Lost opportunities, pipeline snapshots, enriched Oops.csv    |
| **accounts/**       | Account base exports (All Account)                               |
| **leads/**          | Leads, campaign analysis, source/job title counts                |
| **inbound/**        | Qualified inbound leads (Inbound.xlsx) — messaging insights      |
| **austin-chamber/** | Austin Chamber directory scrapes (directory.csv, directory.json) |
| **reference/**      | PDFs, misc reference docs                                        |

---

## Key Files

| File                           | Used By                                                             |
| ------------------------------ | ------------------------------------------------------------------- |
| `opportunities/Oops.csv`       | persona_normalization.py, run_analysis.py                           |
| `inbound/Inbound.xlsx`         | deep_parse_inbound.py, analyze_inbound.py, company_target_matrix.py |
| `austin-chamber/directory.csv` | scrape_austin_chamber.py output                                     |

---

## Regenerate

```bash
# Austin Chamber directory
python3 scripts/scrape_austin_chamber.py --categories 328
```
