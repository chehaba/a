# Company × Service × Buyer Title — Pattern Analysis

**Focus:** WHO (company type, buyer title) buys WHAT (service). Channel-agnostic.

---

## Top Patterns (by win rate, n≥2)

| Company Type | Service | Buyer Title | n | Win Rate | Inbound Asks | Topics |
|--------------|---------|-------------|---|----------|---------------|--------|
| Healthcare | Modern Workplace | Finance / Director | 6 | 100% | — | migration, implementation, integration |
| Commercial | Infrastructure | IT/Tech / IC | 3 | 100% | — | — |
| Financial Services | Modern Workplace | Other / Manager | 3 | 100% | — | migration, implementation, integration |
| Manufacturing | Modern Workplace | Executive / VP | 2 | 100% | — | migration, implementation, integration |
| Energy / Utilities | Modern Workplace | Other / Director | 2 | 100% | — | migration, implementation, integration |
| Agriculture | Data & Analytics | Other / Director | 2 | 100% | — | implementation |
| Education | Infrastructure | Marketing / Director | 2 | 100% | — | — |
| Government | Custom Dev | IT/Tech / Director | 2 | 100% | — | — |
| Healthcare | Modern Workplace | Product/Program / Manager | 2 | 100% | — | migration, implementation, integration |
| Hospitality | Custom Dev | Executive / IC | 2 | 100% | — | — |
| Commercial | Modern Workplace | Executive / IC | 2 | 100% | SharePoint General, SharePoint Migration, Power Automate/Flows | migration, implementation, integration |
| Commercial | Modern Workplace | IT/Tech / C-Suite | 2 | 100% | SharePoint General, SharePoint Migration, Power Automate/Flows | migration, implementation, integration |
| Commercial | Custom Dev | Other / Director | 2 | 100% | — | — |
| Financial Services | Modern Workplace | Other / C-Suite | 2 | 100% | — | migration, implementation, integration |
| Government | Custom Dev | Other / IC | 2 | 100% | — | — |
| Technology | Modern Workplace | Other / IC | 2 | 100% | — | migration, implementation, integration |
| Education | Modern Workplace | Other / IC | 5 | 80% | — | migration, implementation, integration |
| Non-Profit | Modern Workplace | Other / Manager | 4 | 75% | — | migration, implementation, integration |
| Technology | Creative | Marketing / Director | 3 | 67% | — | — |
| Technology | Custom Dev | Other / C-Suite | 3 | 67% | — | — |
| Commercial | CRM | Other / C-Suite | 3 | 67% | Dynamics/CRM | migration, implementation, managed service |
| Commercial | Modern Workplace | Other / IC | 4 | 50% | SharePoint General, SharePoint Migration, Power Automate/Flows | migration, implementation, integration |
| Technology | Creative | Other / Manager | 4 | 50% | — | — |
| Technology | Custom Dev | IT/Tech / IC | 2 | 50% | — | — |
| Financial Services | Modern Workplace | Executive / VP | 2 | 50% | — | migration, implementation, integration |
| Healthcare | Modern Workplace | IT/Tech / Manager | 2 | 50% | — | migration, implementation, integration |
| Healthcare | Infrastructure | IT/Tech / Manager | 2 | 50% | — | — |
| Healthcare | Infrastructure | Other / Manager | 2 | 50% | — | — |
| Healthcare | Modern Workplace | Other / Manager | 2 | 50% | — | migration, implementation, integration |
| Healthcare | Modern Workplace | IT/Tech / Director | 2 | 50% | — | migration, implementation, integration |
| Technology | Custom Dev | Marketing / Manager | 2 | 50% | — | — |
| Commercial | Marketing Services | Marketing / Director | 2 | 50% | — | — |
| Commercial | Infrastructure | IT/Tech / C-Suite | 2 | 50% | — | — |
| Commercial | Modern Workplace | IT/Tech / IC | 2 | 50% | SharePoint General, SharePoint Migration, Power Automate/Flows | migration, implementation, integration |
| Cities, Towns, Municipalities | Modern Workplace | IT/Tech / Manager | 2 | 50% | — | migration, implementation, integration |
| Construction | Modern Workplace | Other / IC | 2 | 50% | — | migration, implementation, integration |
| Education | Marketing Services | Marketing / Director | 2 | 50% | — | — |
| Education | Marketing Services | Marketing / VP | 2 | 50% | — | — |
| Manufacturing | Marketing Services | Marketing / Director | 2 | 50% | — | — |
| Manufacturing | Infrastructure | IT/Tech / Manager | 2 | 50% | — | — |

---

## Datasets (data/patterns/)

| File | Description |
|------|-------------|
| company_service_title.json | Full patterns with inbound_asks, case_study_topics, service_notes |
| company_type_service.json | Company Type × Service win rates |
| inbound_language_by_segment.json | What inbound leads say they want, by segment |
| case_study_topics_by_service.json | Project themes from case study filenames |

**Regenerate:** `python3 scripts/company_service_title_analysis.py`